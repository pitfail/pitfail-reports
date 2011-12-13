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

Class Diagram and Interface Specification
#########################################

System Architecutre and System Design
#####################################

.. include:: spser.rst

.. include:: cohesion.rst

.. include:: templating.rst

.. include:: intform.rst

Algorithms and Data Structures
##############################

User Interface Design and Implementation
########################################

Summary of Changes
##################
//TODO
	
Customer Statement of Requirements
##################################
..TODO

Functional Requirements Specification
#####################################
..TODO

Nonfunctional Requirements
##########################
..TODO

Effort Estimation using Use Case Points
#######################################
..TODO

Class Diagram and Interface Specification
#########################################
..TODO

Design Patterns
###############
..TODO

Object Constraint Language (OCL) Contracts 
##########################################
..TODO

System Architecture and System Design 
#####################################

Algorithms and Data Structures
##############################
..TODO

User Interface Design and Implementation
########################################
..TODO

History of Work & Current Status of Implemenation 
#################################################

.. include:: status.rst

Conclusions and Future Work
###########################
..TODO

References
##########

.. [ADTs] Marie Gleichman. "Functional Scala: Algebraic Datatypes – Sum and Product Types" http://gleichmann.wordpress.com/2011/02/05/functional-scala-algebraic-datatypes-sum-and-product-types/
.. [American] Investopedia. "How do you tell whether an option is American or European style?" http://www.investopedia.com/ask/answers/06/americanvseuropean.asp#axzz1gFsL9Mp8
.. [Anemic] StackOverflow "Anemic Domain Model: Pros/Cons" http://stackoverflow.com/questions/258534/anemic-domain-model-pros-cons
.. [Applicative1] Haskell Wikibook - Applicative Functors. http://en.wikibooks.org/wiki/Haskell/Applicative_Functors
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
.. [Loop] StackOverflow. "How to iterate through a heterogeneous recursive value in Haskell". http://stackoverflow.com/questions/5024148/how-to-iterate-through-a-heterogeneous-recursive-value-in-haskell
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
.. [Traits] "A Tour Of Scala: Traits". http://www.scala-lang.org/node/126
.. [Typing] Haskell Wiki - Typing. http://www.haskell.org/haskellwiki/Typing
.. [UML] Miles,  Russ  and  Kim  Hamilton.  *Learning  UML  2.0*.
.. [Unit] Wikipedia - "Unit Type". http://en.wikipedia.org/wiki/Unit_type
.. [View] Lift - "View First". http://www.assembla.com/wiki/show/liftweb/View_First
.. [XML] "A Tour of Scala: XML Processing". http://www.scala-lang.org/node/131

