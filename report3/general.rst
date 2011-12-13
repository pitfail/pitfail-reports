
References to the code
======================

References into the code are given with a filename and an id such as ref_254,
which appears in the code as a comment. line numbers can change but these
should be constant.

Some general points about the code
==================================

Here we attempt to pre-clarify some aspects that might be confusing or
unexpected in the report that follows. Some of this is due to our choice of
programming languages; some of it is peculiar to our own code.

Lambda expressions
------------------

Scala has, and we often use, lambda expressions (example
website/view/CommentPage.scala ref_524)::

    val postSubmit = Submit(postForm, "Post") { case text =>
        currentUser.userPostComment(ev, text)
    }
    
The expression in curly braces::

    { case text => currentUser.userPostComment(ev, text) }

is a lambda expression [Lambda]_ (anynomous function). It becomes a function
that can be treated like a value, and is passed to the Submit object, to be
called when the form is submitted.

Some consequences of this:

1. Many of our functions do not have names. Their role is evident by the
   context.

2. Inversion of control [Inversion]_ is easy and so we use it often.
   
Traits
------

A ``trait`` in scala is similar to a Java interface, except that it can have
concrete code in it as well [Traits]_. Traits in scala can be used to

1. Split functionality into multiple units (See for example `Organization of
   the Model into traits`_).
   
2. Provide a common interface to several classes (like how you'd use a Java
   interface).
   
3. Group together a set of disjoint cases, similar to an enum [ADTs]_ (example
   website/view/StockSeller.scala ref_104).

Option Types
------------

Many of our functions return a type like ``Option[Int]``. (example
model/auctions.scala ref_188) ``Option`` is a Scala type (based on the ML type
by the same name [ML]_) that can be either present or absent [Option1]_
[Option2]_. So for example::

    def sumOption(l: List[Int]): Option[Int] =
        if (l.isEmpty) Some(l.sum)
        else None

Monads
------

Some of our code is monadic [Monads1]_ (example model/stocks.scala ref_745,
website/jsapi/jsapi.scala ref_618, model/magic.scala ref_650).

Applicative Functors
--------------------

Some of our code uses applicative functors [Applicative1]_ provided by the
Scalaz [Scalaz]_ library (example model/magic.scala ref_853).

Typesafe numbers
----------------

In the report there are many references to the types ``Dollars``, ``Shares``,
``Price`` and ``Scale``. These are our own classes, defined in model/model.scala
ref_868. They represent numbers, where the number represents a dollar value, a
shares value, a price, or a unitless number (scale).

The purpose of these classes is to check at compile time that we are using the
correct units. You can do (example model/stocks.scala ref_325)::

    val cost = price * shares
    
and get the right type. But if you accidentally do:

    val cost = price / shares
    
you will get a compile-time error.

We did this after making too many math mistakes. It was a huge improvement.

HLists
------

Some of our code uses HLists (examples model/spser.scala ref_718,
website/intform/branches.scala ref_575) (and other heterogeneous
collections) [HList]_. Our use of these is described more thoroughly in the
sections that use them.

