
Templating
==========

David Pollak, who developed Lift, believed that it was better not to mix code
and HTML[Pollak]_. This is because code is too powerful -- you may initially
set out to include only View code in the HTML, but it's too easy to
accidentally slip in some functionality that actually belongs in the
Model[Pollak]_.

In lift templates, you write HTML code like::

    <lift:NewsEvent>
        <param:subject/> <param:action/> on <param:when/>
    </lift:NewsEvent>
    
and then bind values to it in the Scala code like::

    class NewsEvent {
        def render(in: NodeSeq) = bind("param", in,
            "subject" -> "joe",
            "action" -> "Bought 100 shares of MSFT",
            "when" -> "Today"
        )
    }

David Pollak may be right, but we found that the drawbacks of using Lift's
templates did not end up being worth the extra help in separating View from
Model, and converted most of our template code to raw Scala code. Some reasons
for this were:

* We have 4 different views attached to our model -- this means that we already
  have a really good idea when when we are putting model code into the view,
  because it gets duplicated among the several Views. Having more than one
  frontend is a great way to enforce good MVC design.
  
* Scala has inline XML literals [XML]_.
  
* Lift templates cannot do 1 really important thing. Consider the following
  made-up template code::
  
      <lift:Dashboard>
        <lift:Portfolio/>
        <lift:Offers/>
      </lift:Dashboard>
  
  This code inserts 3 objects: the containing Dashboard, and inside it a
  Portfolio and a list off incoming Offers. Now the question is: how do you
  make the Portfolio code aware of the enclosing Dashboard code?
  
  In Lift there is no way to do this. Using XML literals this is trivial::
  
        class Dashboard {
            def render =
                <div>
                    {Portfolio(this).render}
                    {Offers(this).render}
                </div>
        }
  
* Transforming XML is not type-safe, so errors are not caught until the page is
  loaded. This wastes a lot of time debugging, and could potentially miss
  errors forever.

Considering these factors, we wrote our HTML using Scala's XML literals
(example website/view/DividendChart.scala ref_44).

