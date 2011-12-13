
Improving Lift Forms
--------------------

Limitations of standard lift forms
..................................

Lift provides some abstractions for getting data out of a submitted
form [Lift2]_. It is done in a callback-manner::
    
    var ticker: String
    var shares: String
    
    bind("param", html,
        "ticker" -> SHtml.text(ticker, { t => ticker = t }),
        "shares" -> SHtml.text(shares, { s => shares = s })
    )

That is, when the form is submitted, the callbacks are called, and they are
passed the data that was submitted.

There are a few reasons we wanted to improve on this system:

* Because callbacks are called individually, you have to use side-effects to
  build up the complete structure of the data. We like to avoid side-effects
  when possible [SideEffects]_.
  
* Because callbacks are called individually, you have to wait until all have
  been called to do checks that synthesize multiple values.
  
* Lift forms deal almost entirely with Strings. This is awkward in a statically
  typed language. We'd rather worked with typed fields.
  
To address these concerns we wrote ``intform``, which is a wrapper around lift
forms (website/intform/).

Typed form fields
.................

Every field in ``intform`` has a type (website/intform/intform.scala ref_727).
This is the type of the value that is produced when the form is submitted. So
for example a StringField produces a String, a UserField (where you type in a
user's name) produces a User, a DollarsField a Dollars, and so on. The Field
class has a ``process()`` method (website/intform/intform.scala ref_997) that
produces a value of the correct type.

Once you have introduced typed fields you have to deal with the fact that you
might not be able to produce a value of the type you want. Say you have a
``DollarsField`` and the user types in "onehua,s.chuetnouhscrasc.hua". You
can't convert that to a number. So the ``process()`` method has to have the
type::

    def process(): Option[A]
    
where ``A`` is the type that the field produces (see the section on `Option
Types`_).

Aggregating multiple fields together
....................................

Say you have two ``IntFields`` and a class::

    case class Point(x: Int, y: Int)
    
and you want to use these to build a ``PointField``. We use the same method we
used in `Serializing objects without using reflection`_: we treat ``Point`` as
a product type, which be built from a heterogeneous list of fields
(website/intform/branches.scala ref_575).

.. raw:: latex

    \clearpage

Hiding side-effects
...................

When an ``intform`` is submitted a callback is called with the submitted data
(example website/view/CommentPage.scala ref_524). At first this seems no
different than what Lift forms do. The improvement is that while in Lift forms
you have multiple, separate callbacks that are passed the individual fields, in
``intform`` you get the entire data as a single object, so you do not have to
deal with *interaction* between the callbacks. Consider (psuedocode)::

    var x: Int
    var y: Int
    
    IntField() { newX =>
        x = newX
    }
    IntField() { newY =>
        y = newY
    }

Now say you want to add a check that ``x < y``. Where do you add it? If you add
it here::

    var x: Int
    var y: Int
    
    IntField() { newX =>
        x = newX
    }
    IntField() { newY =>
        y = newY
        if (y >= x) throw BadInput
    }

you are assuming that the ``x`` callback happens before the ``y`` callback --
but this is not at all obvious from the code. On the other hand, if your
callback takes all data together::

    PointField() { p =>
        if (p.y >= p.x) throw BadInput
    }
    
now you are not relying on the order of any side-effects.


