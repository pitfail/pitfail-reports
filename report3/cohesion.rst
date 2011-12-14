
Applying OO cohesion metrics to our code
========================================

A Scala compiler plugin was used to automatically find which methods reference
which attributes. This information is used to calculate the cohesion metrics
SCOM [SCOM]_, CC [CC]_, LSCC [LSCC]_, and CAMC [CAMC_] (the last one uses
method signature types and does not look at attributes).

The file ``metrics-summary.txt`` shows the method-attribute matrix for each
class.

A summary of the metrics for all the classes are:

.. csv-table::
    :file: metrics/metrics.csv

Decisions that were made about how to calculate the metrics
-----------------------------------------------------------

Fernandez and Peña do not say explicitly whether in the following situtaion
method foo() references attribute x [SCOM]_::

    class A {
        var x: Int = _
        def foo() = bar()
        def bar() = x
    }

Because Scala wraps almost *all* attributes in accessor methods, even
internally, these metrics would make little sense unless foo() is considered to
reference bar().

Another question is, What is an atttribute? The following decisions were made:

============  ==========  ===========================================
Member        attribute?  Why?
============  ==========  ===========================================
var           yes         Exact analog of a Java instance variable
concrete val  no          Cannot change
abstract val  yes         Value depends on where it is made concrete
def           no          This is a method
============  ==========  ===========================================

Problems with OO cohesion metrics for Scala code
------------------------------------------------

The biggest problem with these metrics is that in Scala it is common (and good
practice) to have classes with no methods at all; that act merely as a container
for multiple fields [ADTs]_.

Another problem is that it is common (and also good practice) to abstract
methods out into ``traits`` which contain no fields. Hence a large number of Scala
classes contain only fields and no methods, or only methods and no fields.

CAMC suffers from the fact that Scala types tend to be more complicated than
types in other OO languages, so it is harder for two types to be equal.

These three facts result in the following histograms:

.. figure:: metrics/SCOM.pdf
    :width: 80%
    
.. figure:: metrics/CC.pdf
    :width: 80%
    
.. figure:: metrics/LSCC.pdf
    :width: 80%
    
.. figure:: metrics/CAMC.pdf
    :width: 80%

Most classes either fall to 0 or 1, with only a few in the middle. Further more
it is not clear that those that fall to 0 (classes with no methods) are really
bad -- they would be bad Java classes but they are good Scala classes.

It is good to see the above histograms before looking at the below trellis
graphic, because otherwise the trellis graphic makes the metrics look more
appropriate than they really are:

.. figure:: metrics/trellis.pdf
    :width: 95%

Most of the metrics corellate well with each other, except CAMC, which is all
over the place.

Evaluating the cohesion of functional code
==========================================

We do not know how to give a metric nor or we sure that a numerical metric is
the right approach, but we have some ideas on what makes functional code more
or less cohesive.

Why OO metrics do not work well for functional code
---------------------------------------------------

OO metrics do not work well with functional code because they do not give good
answers for the following pattern::

    case class Point(x: Double, y: Double)
    
    def dist(p1: Point, p2: Point): Double = ...
    
That is, defining classes that only hold fields, and then defining methods
outside of those classes. This is common in functional programming [Data]_.
Scala does incorporate OO, but this pattern is still too common (in our
experience) to make OO metrics useful, which would consider the fields of
``Point`` to be unconnected [SCOM]_.

Another pattern that OO metrics have trouble with is::

    def diff(f: Double=>Double) = { (x: Double) =>
        (f(x + 1e-5) - f(x)) / 1e-5
    }

There is a context being created, in which the variable ``f`` is visible,
almost as if you defined a class like::

    class Diff {
        val f: Double=>Double
        
        def apply(x: Int) = (f(x + 1e-5) - f(x)) / 1e-5
    }
    
(For many good examples on this pattern see  [SICP1]_).

OO metrics act as if the only creator of context is a class [SCOM]_, but in
functional programming this is often not true, as above.

Thinking in terms of statements and proofs
------------------------------------------

The Curry-Howard Isomorphism relates types and data in a programming language
to logical statements [CurryHoward]_:

* A *type* corresponds to a statement.
  
* A *value* corresponds to a proof of the statement of its type.

A function with input type ``A`` and output type ``B`` has a type written ``A
=> B`` which is taken to mean "A implies B" [CurryHoward]_. So the actual
function (ie the value)::

    def foo(a: A): B = ...
    
can be thought of as the proof that ``A`` implies ``B``. So ``A`` is the
hopethesis in the proof, and ``B`` is the conclusion.

This gives us a way to describe (not quite define, unfortunately) an idea which
we will use to describe cohesion. Say we have a function defined like::

    def foo(x: String, y: Int): Int = y * 2
    
This has type::
    
    (String, Int) => Int
    
(the product type ``(String, Int)`` is analogous to "and" [CurryHoward]_).

So our hypothesis is "``String`` and ``Int``", but in the proof we only use
``Int``. So we have made an unnecessary assumption. And you can see just by
looking that the ``x`` argument to ``foo`` is superfluous.

So, this gives us a way to say whether a function has superfluous arguments.
But that was already obvious, because you don't usually write functions with
unneeded arguments anyway: you have to make a conscious effort to put in the
``x`` argument, and if it's really unnecessary you wouldn't add it in the first
place.

But there is another place where hypotheses come from: enclosing scopes.
Consider the curried form [Currying]_ of ``foo``::

    def foo(x: String) = {
    
        def bar(y: Int) = y * 2
        
        bar _
    }
    
Inside ``foo`` we define a function ``bar``, and then return that function.

What is not so obvious, and easy to miss in actual code, is that ``bar`` could
refer to ``x`` if it so desires::

    def foo(x: String) = {
    
        def bar(y: Int) = x
        
        bar _
    }
    
but it doesn't. This means the assumptions ("``String``") introduced by the
enclosing context are not needed in the proof of bar.

There are other ways that unneeded hypotheses can sneak in. Consider::

    case class Point(x: Int, y: Int)
    
    def projectX(p: Point): Int = p.x
    
``Point`` is a product type (See `Product Types`_), but ``projectX`` uses only
one field of the product. A more cohesive design would be::

    trait HasX { val x: Int }
    case class Point(x: Int, y: Int) extends HasX
    
    def projectX(h: HasX) = h.x
    
Or, directly using Scala's structural types [Struct]_::

    case class Point(x: Int, y: Int)
    
    def projectX(p: {val x: Int}) = p.x

Evaluating cohesion
-------------------

Say we want to evaluate the cohesion of the previous code::

    def foo(x: String) = {
    
        def bar(y: Int) = y * 2
        
        bar _
    }

We would say that the scope created by ``foo`` has extra things in it that do
not belong there, because they make no use of that scope in their code. A more
cohesive version is::

    def bar(y: Int) = y * 2
    
In this sample of code from PitFail (model/auctions.scala ref_823)::

    trait PortfolioWithAuctions {
        self: Portfolio =>
        
        def auctionOffers: Seq[AuctionOffer] = schema.auctionOffers where
            ('offerer ~=~ this) toList
            
        def userCastBid(auction: AuctionOffer, price: Dollars) = editDB {
            if (price <= auction.goingPrice)
                throw BidTooSmall(auction.goingPrice)
            
            (
                  AuctionBid(offer=auction, by=this, price=price).insert
                & Bid(this, auction, price).report
            )
        }
    }

we see that ``userCastBid`` has ``auctionOffers`` in scope, but never uses it.
We could break it up like::

    trait PortfolioWithAuctions
        extends PortfolioWithAuctionOffers
        with    PortfolioWithBids

    trait PortfolioWithAuctionOffers {
        self: Portfolio =>
        
        def auctionOffers: Seq[AuctionOffer] = schema.auctionOffers where
            ('offerer ~=~ this) toList
            
    }
    
    trait PortfolioWithBids {
        self: Portfolio =>
        
        def userCastBid(auction: AuctionOffer, price: Dollars) = editDB {
            if (price <= auction.goingPrice)
                throw BidTooSmall(auction.goingPrice)
            
            (
                  AuctionBid(offer=auction, by=this, price=price).insert
                & Bid(this, auction, price).report
            )
        }
    }
    
so ``userCastBid`` is now more restrictively typed.
    
Can you assume too little?
--------------------------
    
We talked about assuming too much, but is it possible to assume too little?
    
It is possible, if there are holes in your code [CurryHoward]_ such as
exceptions, infinite loops [Iry1]_ or incomplete case expressions
[CurryHoward]_. These are regarded in functional programming as a Bad Thing
[Iry2]_ and people already avoid them.
    
