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

.. [ADTs] http://gleichmann.wordpress.com/2011/02/05/functional-scala-algebraic-datatypes-sum-and-product-types/
.. [American] http://www.investopedia.com/ask/answers/06/americanvseuropean.asp#axzz1gFsL9Mp8
.. [Anemic] http://stackoverflow.com/questions/258534/anemic-domain-model-pros-cons
.. [Applicative1] http://en.wikibooks.org/wiki/Haskell/Applicative_Functors
.. [Controllers] http://www.aptprocess.com/whitepapers/DomainModelling.pdf
.. [CurryHoward] http://en.wikibooks.org/wiki/Haskell/The_Curry-Howard_isomorphism
.. [Currying] http://www.haskell.org/haskellwiki/Currying

.. raw:: latex
    
    \clearpage

.. [Data] http://en.wikibooks.org/wiki/Haskell/Type_declarations
.. [DSL] http://c2.com/cgi/wiki?DomainSpecificLanguage
    Ed.  Eric  McLaughlin  and  Mary  O'Brien. Sebastopol: O'Reilly, 2006.
.. [Erasure] http://docs.oracle.com/javase/tutorial/java/generics/erasure.html
.. [H2] http://www.h2database.com/html/main.html
.. [HList1] http://apocalisp.wordpress.com/2010/06/08/type-level-programming-in-scala/
.. [HList] http://apocalisp.wordpress.com/2010/06/08/type-level-programming-in-scala/
.. [HTTP] http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

.. raw:: latex
    
    \clearpage

.. [Implicits] http://lampwww.epfl.ch/~odersky/talks/wg2.8-boston06.pdf
.. [Inversion] http://martinfowler.com/bliki/InversionOfControl.html
.. [Iry1] http://james-iry.blogspot.com/2010/08/why-scalas-and-haskells-types-will-save.html
.. [Iry2] http://james-iry.blogspot.com/2009/08/getting-to-bottom-of-nothing-at-all.html
.. [JDBC] http://en.wikipedia.org/wiki/Java_Database_Connectivity
.. [Jetty1] http://jetty.codehaus.org/jetty/
.. [Kiselyov] Oleg Kiselyov and Ralf Lämmel and Keean Schupke. "Strongly typed heterogeneous collections". Haskell 2004: Proceedings of the ACM Sigplan workshop on Haskell.
.. [Lambda] http://www.scala-lang.org/node/133

.. raw:: latex
    
    \clearpage

.. [Lift1] http://liftweb.net/
.. [Lift2] http://exploring.liftweb.net/master/index-6.html
.. [Loop] http://stackoverflow.com/questions/5024148/how-to-iterate-through-a-heterogeneous-recursive-value-in-haskell
.. [Makers] http://en.wikipedia.org/wiki/Market_maker
.. [Marsic] Marsic, Ivan. *Software Engineering*. Piscataway: Rutgers University, 2011. PDF. Miles,  Russ  and  Kim  Hamilton.  *Learning  UML  2.0*.
.. [ML] http://www.standardml.org/Basis/option.html
.. [Monads1] http://lamp.epfl.ch/~emir/bqbase/2005/01/20/monad.html
.. [MVC] http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
.. [Option1] http://www.scala-lang.org/api/current/scala/Option.html

.. raw:: latex
    
    \clearpage

.. [Option2] http://james-iry.blogspot.com/2010/08/why-scalas-and-haskells-types-will-save.html
.. [Pollak] http://markmail.org/message/cco7biz2g3jeilg6
.. [Scalaz] http://code.google.com/p/scalaz/
.. [SCOM] Luis Fernández and Rosalía Peña. "A Sensitive Metric of Class Cohesion". Information Theories and Applications.
.. [SICP1] http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-20.html#%_sec_3.1.1
.. [SideEffects] http://c2.com/cgi/wiki?SideEffect
.. [Squeryl1] http://squeryl.org/

.. raw:: latex
    
    \clearpage

.. [Squeryl2] https://github.com/max-l/Squeryl/blob/master/src/main/scala/org/squeryl/internals/PosoMetaData.scala
.. [Stop] http://www.investopedia.com/terms/s/stoporder.asp#axzz1g4pXxPbD
.. [Traits] http://www.scala-lang.org/node/126
.. [Typing] http://www.haskell.org/haskellwiki/Typing
.. [Unit] http://en.wikipedia.org/wiki/Unit_type
.. [View] http://www.assembla.com/wiki/show/liftweb/View_First
.. [XML] http://www.scala-lang.org/node/131

