
Serializing objects without using reflection
============================================

Why we needed to change
-----------------------

For the first demo, our database backend was written using Squeryl [Squeryl1]_.
There were some pros and cons to using squeryl, but overall we probably would
have kept using it if this were possible.

However, as the model code grew large, we realized we had to reorganize, and
one of the ways we reorganized was to split the code into ``traits`` (See
`Traits`_), and mix them together (See `Organization of the Model into
traits`_). Unfortunately, Squeryl does not support mapping inner classes,
because it does not know how to reconstruct the outer pointer [Squeryl2]_.

It was more important to us to have a better organized model code than to keep
using Squeryl, so we had to change. Initially, we ignored the database backend;
our code had no persistence, but this did not make much of a difference in
testing and we were able to implement all the important operations with no
database. And another benefit of have no database is that we'd keep our code
non-specific to the particular database code we used.

But, in the end, we could not actually present a website that lost all its
information every time it was restarted. So we wrote "spser"
(model/spser.scala).

Product Types
-------------

A product type is a type with members [ADTs]_, e.g. (in Java)::

    class Point {
        public int x;
        public int y;
    }
    
is a product type, where the members are ``x`` and ``y``. Another way of saying
this is that the ``Point`` type is a product of ``int`` and ``int``.

So say you wanted to serialize a class::

    Foo {
        T1 x1;
        T2 x2;
        ...
        TN xN;
    }
    
to a database. Well, if you already have a way to turn the types ``T1...TN``
into database fields, then serializing a ``Foo`` is just a matter of extracting
the members, and converting them to fields (model/spser.scala ref_984).
Deserializing is just a matter of extracting the ``xk`` values, and applying a
constructor::

    (T1, T2, ... TN) => Foo
    
to build a ``Foo`` object (model/spser.scala ref_704).

Generic representation of products
----------------------------------

We use the same representation of products as Mark Harrah's HLists [HList]_,
which in turn is the same representation as Oleg Kiselyov's HList for
Haskell[Kiselyov]_.

A product is either HOne (model/spser.scala ref_220)::
    
    case class HOne() extends HProd
    
ie, a product of 0 types (the name ``HOne`` is a reference to the "unit
type"[Unit]_), or a product of an existing product with one more type added on
(model/spser.scala ref_464)::

    case class HTimes[+H,+T<:HProd](head: H, tail: T) extends HProd
    
Looping over products
---------------------

A common technique when working with Haskell's HLists is to write a typeclass
for the loop operation, and then instance declarations for the base- and
recursive- cases [Loop]_. We use the same technique (as in model/spser.scala
ref_231). Where Haskell has typeclasses Scala has implicit
parameters [Implicits]_. So, for example, to print an ``HProd`` we can do::

    trait Display[A] {
        def display(a: A): Unit
    }

    implicit def displayOne = new Display[HOne] {
        def display(o: HOne) { }
    }
    implicit def displayTimes[H,T<:HProd:Display] = new Display[HTimes[H,T]] {
        def display(p: HTimes[H,T]) { println(p.head) ; hDisplay(p.tail) }
    }

Extracting the fields of a product type
---------------------------------------

Now that we have ``HProd``, we have 2 different ways to represent each product
type. There's the original, "friendly" way::

    case class Point(x: Int, y: Int)
    
and the ``HProd`` "generic" way::

    HProd[Int, HProd[Int, HOne]]
    
When writing code, we want to use the "friendly" way as much as possible,
except in the very backend, where we need to be able to iterate over product
fields and so must use the "generic" way. So we must be able to convert between
them.

If you look at the class::

    case class Point(x: Int, y: Int)

after it has passed through the first few Scala compiler phases, you will see (among
other things; the full output is huge)::

    case class Point extends java.lang.Object with ScalaObject with Product with Serializable {
        <caseaccessor> <paramaccessor> private[this] val x: Int = _;
        <stable> <caseaccessor> <accessor> <paramaccessor> def x: Int = Point.this.x;
        <caseaccessor> <paramaccessor> private[this] val y: Int = _;
        <stable> <caseaccessor> <accessor> <paramaccessor> def y: Int = Point.this.y;
        def this(x: Int, y: Int): Point = {
            Point.super.this();
            ()
        };
        override def productPrefix: java.lang.String = "Point";
        override def productArity: Int = 2;
        override def productElement(x$1: Int): Any = x$1 match {
            case 0 => x
            case 1 => y
            case _ => throw new java.lang.IndexOutOfBoundsException(x$1.toString())
        };
    };

In other words, the Scala compiler provides some minimal support for extracting
elements from product types, in the form of ``productElement``.
``productElement`` is not type-safe, but if we trust the Scala compiler to
generate it correctly, we can do some type coercion and create a type-safe
extractor (model/spser.scala ref_997).

Re-creating a product type from the fields
------------------------------------------

How do we go from ``HTimes[Int,HTimes[Int,HOne]]`` to ``Point``? ``Point`` has
a constructor::

    (Int, Int) => Point
    
which can be used to construct a ``Point`` given the fields. Unfortunately this
is another area where Scala's types are awkward to work with; there is no
type-safe way to generalize over function arity. The solution is a set of
auto-generated functions for every function arity up to some size
(model/spser.scala ref_662).

The advantage to this method of serialization
---------------------------------------------

The biggest advantage to serializing objects using product types is that it
works *within* the language, whereas reflection works outside the language. In
Scala this is especially relevant because Scala uses Java's reflection API's,
which do not know about Scala. The disadvantages to working outside the lanuage
are:

* Less type information. JVM type erasure [Erasure]_ takes away most type
  information.
  
* Less type safety. Because reflection operates a run-time and doesn't have
  static types.
  
* The chance to conflict with language features, such as how Squeryl cannot
  pass the outer pointer to a synthesized object. This one was the killer.
  
Putting this all together
-------------------------

Ideally we would like to add the serialization/deserialization routines to
Squeryl. There is no reason this should not be possible. We tried; given more
time, we might thave succeeded, but the Squeryl code is fairly set on using
reflection to create objects. So we wrote a tiny DSL [DSL]_ for building SQL
queries and attached it to the H2 JDBC library [H2]_ (model/spser.scala
ref_629).

