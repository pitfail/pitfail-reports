
Cohesion Metrics for Scala Code
===============================

A Scala compiler plugin was used to automatically find which methods reference
which attributes. This information is used to calculate the cohesion metrics
SCOM, CC, LSCC, and CAMC (the last one uses method signature types and does not
look at attributes).

The file ``metrics-summary.txt`` shows the method-attribute matrix for each
class.

A summary of the metrics for all the classes are:

.. csv-table::
    :file: metrics.csv

Decisions that were made about how to calculate the metrics
-----------------------------------------------------------

Fernandez and Peña ("A Sensitive Metric of Class Cohesion") do not say
explicitly whether in the following situtaion method foo() references attribute
x::

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
practice) to have classes with no methods at all; that at merely as a container
for multiple fields.

Another problem is that it is common (and also good practice) to abstract
methods out into ``traits`` which contain no fields. Hence a large number of Scala
classes contain only fields and no methods, or only methods and no fields.

CAMC suffers from the fact that Scala types tend to be more complicated than
types in other OO languages, so it is harder for two types to be equal.

These three facts result in the following histograms:

.. image:: SCOM.pdf
    :width: 80%
    
.. image:: CC.pdf
    :width: 80%
    
.. image:: LSCC.pdf
    :width: 80%
    
.. image:: CAMC.pdf
    :width: 80%

Most classes either fall to 0 or 1, with only a few in the middle. Further more
it is not clear that those that fall to 0 (classes with no methods) are really
bad -- they would be bad Java classes but they are good Scala classes.

It is good to see the above histograms before looking at the below trellis
graphic, because otherwise the trellis graphic makes the metrics look more
appropriate than they really are:

.. image:: trellis.pdf
    :width: 95%

Most of the metrics corellate well with each other, except CAMC, which is all
over the place.

