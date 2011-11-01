.. raw:: latex

	\begin{titlepage}
	\centering
	\singlespacing

	\vspace*{2in}

	\begin{center}
		\Huge PitFail Report 2 \\
		\Large An Online Financial Engineering Game
	\end{center}

	\vspace*{2in}

	\large
	November 4, 2011 \\

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

Interaction Diagrams
====================

Class Diagram and Interface Specification
=========================================
Class Diagram
-------------
Data Types and Operation Signatures
-----------------------------------

System Architecutre and System Design
=====================================
Architectural Styles
--------------------
Identifying Subsystems
----------------------
Mapping Subsystems to Hardware
------------------------------
Persistent Data Storage
-----------------------
Ntework Protocol
----------------
Global Control Flow
-------------------
Hardware Requirements
---------------------

Algorithms and Data Structures
==============================
Algorithms
----------

Data Structures
---------------

User Interface Design and Implementation
========================================



Progress Report and Plan of Work
================================

Progress Report
---------------

All use cases still need more implementation to allow for increased functionality. In 
particular, Leagues and Teams need to be implemented while the actual interactions with the 
stock exchange need to expand to address exceptions usability requirements. 

======  ======================  ============  ================================================
UC#     Use Case Short Name      % Completed   Comments
======  ======================  ============  ================================================
UC-1    Buy                     50%           Functionality needs to be increased and made
                                              uniform across varying interfaces. Smaller 
                                              details like after hours buying, orders, and 
                                              brokerage fees need to be added.
UC-2    Sell                    50%           Functionality needs to be increased and made
                                              uniform across varying interfaces. Smaller 
                                              details like after hours selling, orders, and 
                                              brokerage fees need to be added.
UC-3    Join League             0%            Leagues have not been implemented yet.
UC-4    View Portfolio          75%           Current portfolios can be viewed, but this use 
                                              case will be expanded when a portfolio will need 
                                              to hold more items.
UC-5    Get Security            50%           Needs more functionality, like Buy and Sell.
UC-6    View League Stats       0%            Leagues have not been implemented yet.
UC-7    Buy via Twitter         60%           Users can buy only stocks according to a strict 
                                              input guidelines. There are some bugs that need 
                                              to be fixed.
UC-8    Sell via Twitter        60%           Users can sell only stocks according to a strict 
                                              input guidelines. There are some bugs that need 
                                              to be fixed.
UC-9    Portfolio Info          75%           Users can see other user's portfolios, but 
                                              additional information should be displayed, e.g. 
                                              graphs, creation date, percent increased...
UC-10   Change Default          0%            Leagues have not been implemented yet.
UC-11   Make League             0%            Leagues have not been implemented yet.
UC-12   League Settings         0%            Leagues have not been implemented yet.
UC-13   Add Coordinator         0%            Leagues have not been implemented yet.
UC-14   Remove Coordinator      0%            Leagues have not been implemented yet.
UC-15   Delete League           0%            Leagues have not been implemented yet.
UC-16   Manage League           0%            Leagues have not been implemented yet.
UC-17   Invite to League        0%            Leagues have not been implemented yet.
UC-18   Authentication          75%           Currently done through Twitter, will need to be 
                                              increased for additional logins.
UC-19   Create User             75%           Users can be created only if they have a Twitter 
                                              account.
UC-20   Vote                    0%            Voting has not been implemented yet.
UC-21   Vote by Tweet           0%            Voting has not been implemented yet.
UC-22   Derivative Designer     25%           Partially implemented, but not lacks important 
                                              functionalities and an intuitive design.
UC-23   Accept derivative       75%           Basic functionality is present. Need to expand to
                                              allow counter-offers and to be updated for newer
                                              versions of the implemented derivatives.
======  ======================  ============  ================================================

Plan of Work
------------
.. image:: Plan_of_Work/Plan_of_Work__Report2.pdf

Breakdown of Responsibilities
-----------------------------

=====================  ======================  
Modules                Owner                   
=====================  ======================  
Website                Michael, Owen           
Android                Roma, Sonu              
Facebook               Avanti                  
Twitter                Cody                    
Database               Brian                   
Back-end Functions     Michael, Owen, Brian    
=====================  ======================  

The integration of the system and testing will not require a primary coordinator. 
Since each module relies on only the database and back-end functions and is independent 
of the other modules, the chances of one module affecting the others are low. Each 
auxiliary module developer is responsible for communicating with the database and 
back-end functions developers to ensure their code is using the database and back-end 
functions correctly. During team meetings, the features being employed on each 
auxiliary module will be discussed to ensure that common features are being deployed 
across all systems. Testing will be the responsibility of each module developer. 



References
==========
