
.. role:: ref

.. role:: label

.. raw:: latex

	\begin{titlepage}
	\centering
	\singlespacing

	\vspace*{2in}

	\begin{center}
		\Huge PitFail Report 3 \\
		\Large An Online Financial Engineering Game
	\end{center}

	\vspace*{2in}

	\large
	December 12, 2011 \\

	\vspace*{0.5in}

	Software Engineering I, Group 3 \\
	\href{https://github.com/pitfail/pitfail-reports/wiki}{https://github.com/pitfail/pitfail-reports/wiki} \\

	\vspace*{0.5in}

	Michael Koval, Cody Schafer, \\
	Owen Healy, Brian Goodacre \\
	Roma Mehta, Sonu Iqbal \\
	Avanti Kulkarni \\
	\end{titlepage}
    
.. sectnum::

.. contents:: Table of Contents

.. raw:: latex

	\pagebreak

Individual Contributions
########################
//TODO

.. raw:: latex

	\begin{center}
	\small

.. csv-table::
	:header: "Responsibility", "Michal Koval", "Cody Schafer", "Owen Healy", "Brian Good-acre", "Roma Mehta", "Sonu Iqbal", "Avanti Kulkarni"
	:widths: 15, 6, 6, 6, 6, 6, 6, 6

	Customer Reqs. (6),                ,     ,     ,     ,     ,     , 100%
	Glossary of Terms (4),          %,  10%,  10%,  10%,  10%,  10%,  10%
	Functional Reqs.,                  ,     ,     ,     ,     ,     ,
	? Stakeholders (2),                , 100%,     ,     ,     ,     ,
	? Actors (2),                      , 100%,     ,     ,     ,     ,
	? Goals (4),                    %,  50%,     ,     ,     ,     ,
	? Casual UC (5),                   , 100%,     ,     ,     ,     ,
	? Dressed UC (11),              %,  20%,     ,  40%,     ,     ,
	? UC Diagram (4),                  , 100%,     ,     ,     ,     ,
	? UC Tracability,              %,     ,     ,     ,     ,
	Seq. Diagrams (9),                 ,     ,     ,     ,     , 100%,
	Nonfunc. Reqs. (6),                ,     ,     ,     ,     , 100%,
	Domain Analysis,                   ,     ,     ,     ,     ,     ,
	? Concepts (12),                   ,     , 100%,     ,     ,     ,
	? Associations (4),                ,     , 100%,     ,     ,     ,
	? Attributes (3),                  ,     , 100%,     ,     ,     ,
	Contracts (6),                     ,     ,     ,     , 100%,     ,
	User Interface (8),            %,     ,     ,     ,     ,     ,
	Plan of Work (3),                  ,     ,     , 100%,     ,     ,
	References (1),                 14%,  14%,  14%,  14%,  14%,  15%,  14%

.. raw:: latex

	\end{center}

General Information
###################

.. include:: general.rst

Glossary
########

.. include:: glossary.rst

Summary of Changes
##################

.. include:: changes.rst
	
Architecture
############

.. include:: architecture.rst

Domain Model
############

.. include:: domain.rst

Perturbations and Interactions
##############################

.. _interactions:

.. include:: interactions.rst

System Architecutre and System Design
#####################################

.. include:: templating.rst

.. include:: intform.rst

.. include:: spser.rst

.. include:: cohesion.rst

Customer Statement of Requirements
##################################

.. include:: reqs.rst

Functional Requirements Specification
#####################################

.. include:: func_reqs.rst

Nonfunctional Requirements
##########################

.. include:: nonfunc.rst

User Interface Design and Implementation
########################################

Effort Estimation using Use Case Points
#######################################
..TODO

Class Diagram and Interface Specification
#########################################
..TODO

Object Constraint Language (OCL) Contracts 
##########################################
..TODO

History of Work & Current Status of Implemenation 
#################################################

.. include:: status.rst

Conclusions and Future Work
###########################

.. include:: conclusions.rst

References
##########

.. [ADTs] Marie Gleichman. "Functional Scala: Algebraic Datatypes – Sum and Product Types" http://gleichmann.wordpress.com/2011/02/05/functional-scala-algebraic-datatypes-sum-and-product-types/
.. [American] Investopedia. "How do you tell whether an option is American or European style?" http://www.investopedia.com/ask/answers/06/americanvseuropean.asp#axzz1gFsL9Mp8
.. [Anemic] StackOverflow "Anemic Domain Model: Pros/Cons" http://stackoverflow.com/questions/258534/anemic-domain-model-pros-cons
.. [Applicative1] Haskell Wikibook - Applicative Functors. http://en.wikibooks.org/wiki/Haskell/Applicative_Functors
.. [Ask] Investopedia - Ask price http://www.investopedia.com/terms/a/ask.asp
.. [Bid] Investopedia - Bid price http://www.investopedia.com/terms/b/bidprice.asp#axzz1gTt8rHSo
.. [Browse] Mark Harrah's Browse Plugin https://github.com/harrah/browse
.. [CAMC] Steven Counsell, Stephen Swift. "The Interpretation and Utility of Three Cohesion Metrics for Object-Oriented Design". ACM Trans. Softw. Eng. Methodol. 15, 2 (April 2006), 123-149. DOI=10.1145/1131421.1131422 http://doi.acm.org/10.1145/1131421.1131422 
.. [CC] Challa Bonja and Eyob Kidanmariam. 2006. Metrics for class cohesion and similarity between methods. In Proceedings of the 44th annual Southeast regional conference (ACM-SE 44). ACM, New York, NY, USA, 91-95. DOI=10.1145/1185448.1185469 http://doi.acm.org/10.1145/1185448.1185469 
.. [Controllers] Paul Oldfield. "Domain Modelling" http://www.aptprocess.com/whitepapers/DomainModelling.pdf
.. [CurryHoward] Haskell Wikibook - The Curry-Howard Isomorphism. http://en.wikibooks.org/wiki/Haskell/The_Curry-Howard_isomorphism
.. [Currying] HaskellWiki - Currying. http://www.haskell.org/haskellwiki/Currying

.. raw:: latex
    
    \clearpage

.. [Data] Haskell Wikibook - Type Declarations. http://en.wikibooks.org/wiki/Haskell/Type_declarations
.. [DRY] Ward's Wiki - Don't Repeat Yourself. http://c2.com/cgi/wiki?DontRepeatYourself
.. [DSL] Ward's Wiki - Domain Specific Language. http://c2.com/cgi/wiki?DomainSpecificLanguage
    Ed.  Eric  McLaughlin  and  Mary  O'Brien. Sebastopol: O'Reilly, 2006.
.. [Erasure] Oracle. "Type Erasure". The Java Tutorials. http://docs.oracle.com/javase/tutorial/java/generics/erasure.html
.. [H2] H2 Database Engine. http://www.h2database.com/html/main.html
.. [HList] Mark Harrah. "Type Level Programming in Scala". http://apocalisp.wordpress.com/2010/06/08/type-level-programming-in-scala/
.. [HTTP] Wikipedia. "Hypertext Transfer Protocol". http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

.. raw:: latex
    
    \clearpage

.. [Implicits] Martin Odersky. "Poor Man's Type Classes". http://lampwww.epfl.ch/~odersky/talks/wg2.8-boston06.pdf
.. [Inversion] Martin Fowler. "Inversion of Control". http://martinfowler.com/bliki/InversionOfControl.html
.. [Iry1] James Iry. "Why Scala's Option and Haskell's Maybe types will save you from null". http://james-iry.blogspot.com/2010/08/why-scalas-and-haskells-types-will-save.html
.. [Iry2] James Iry. "Getting to the bottom of nothing at all". http://james-iry.blogspot.com/2009/08/getting-to-bottom-of-nothing-at-all.html
.. [JDBC] Wikipedia. "Java Database Connectivity". http://en.wikipedia.org/wiki/Java_Database_Connectivity
.. [Jetty1] Jetty Web Server. http://jetty.codehaus.org/jetty/
.. [Kiselyov] Oleg Kiselyov and Ralf Lämmel and Keean Schupke. "Strongly typed heterogeneous collections". Haskell 2004: Proceedings of the ACM Sigplan workshop on Haskell.
.. [Lambda] "A Tour Of Scala: Anonymous Function Syntax". http://www.scala-lang.org/node/133

.. raw:: latex
    
    \clearpage

.. [Lift1] Lift Web Framework. http://liftweb.net/
.. [Lift2] Lift Forms. http://exploring.liftweb.net/master/index-6.html
.. [Limit] Investopedia - Limit Order http://www.investopedia.com/terms/l/limitorder.asp
.. [Loop] StackOverflow. "How to iterate through a heterogeneous recursive value in Haskell". http://stackoverflow.com/questions/5024148/how-to-iterate-through-a-heterogeneous-recursive-value-in-haskell
.. [LSCC] J Al Dallal, Lionel C. Briand. "A Precise Method-Method Interaction-Based Cohesion Metric for Object-Oriented Classes". ACM Transactions on Software 2010.
.. [Makers] Wikipedia. "Market Maker". http://en.wikipedia.org/wiki/Market_maker
.. [Marsic] Marsic, Ivan. *Software Engineering*. Piscataway: Rutgers University, 2011. PDF. 
.. [ML] The Standard ML Basis Library - The Option Structure. http://www.standardml.org/Basis/option.html
.. [Monads1] Burak Emir. "Monads in Scala". http://lamp.epfl.ch/~emir/bqbase/2005/01/20/monad.html
.. [MVC] Wikipedia. "MVC". http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
.. [Option1] Scala Standard Library - Option. http://www.scala-lang.org/api/current/scala/Option.html

.. raw:: latex
    
    \clearpage

.. [Pollak] David Pollak. "Separating Presentation Logic from scala files". http://markmail.org/message/cco7biz2g3jeilg6
.. [Scalaz] Scalaz Libarry. http://code.google.com/p/scalaz/
.. [SCOM] Luis Fernández and Rosalía Peña. "A Sensitive Metric of Class Cohesion". Information Theories and Applications.
.. [SICP1] Harold Abelson, Gerald Sussman, Julie Sussman. "The Structure and Interpretation of Computer Programs". http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-20.html#%_sec_3.1.1
.. [SideEffects] Ward's Wiki - Side Effect. http://c2.com/cgi/wiki?SideEffect
.. [Squeryl1] Squeryl. http://squeryl.org/

.. raw:: latex
    
    \clearpage

.. [Squeryl2] Squeryl source code, showing where it fails at inner classes. https://github.com/max-l/Squeryl/blob/master/src/main/scala/org/squeryl/internals/PosoMetaData.scala
.. [Stop] Investopedia - Stop Order. http://www.investopedia.com/terms/s/stoporder.asp#axzz1g4pXxPbD
.. [Struct] Steven Schmidt. "Scala Goodness: Structural Typing". http://codemonkeyism.com/scala-goodness-structural-typing/
.. [Traits] "A Tour Of Scala: Traits". http://www.scala-lang.org/node/126
.. [Typing] Haskell Wiki - Typing. http://www.haskell.org/haskellwiki/Typing
.. [UML] Miles,  Russ  and  Kim  Hamilton.  *Learning  UML  2.0*.
.. [Unit] Wikipedia - "Unit Type". http://en.wikipedia.org/wiki/Unit_type
.. [View] Lift - "View First". http://www.assembla.com/wiki/show/liftweb/View_First
.. [XML] "A Tour of Scala: XML Processing". http://www.scala-lang.org/node/131

.. raw:: latex
    
    \clearpage

.. [Android]"Developers Guide". http://developer.android.com/guide/index.html

