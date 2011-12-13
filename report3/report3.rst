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
========================
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

Summary of Changes
==================
//TODO
	
Customer Statement of Requirements
==================================
..TODO

Glossary of Terms
=================
..TODO

Functional Requirements Specification
=====================================
..TODO

Nonfunctional Requirements
==========================
..TODO

Effort Estimation using Use Case Points
=======================================
..TODO

Domain Analysis
===============
..TODO

Interaction Diagrams
====================
..TODO

Class Diagram and Interface Specification
=========================================
..TODO

Design Patterns
---------------
..TODO

Object Constraint Language (OCL) Contracts 
------------------------------------------
..TODO

System Architecture and System Design 
=====================================

Android Client Architecture
-------------------------------

The Android client runs on the Android phones (Android version 2.2 and above). The development for the same 
is done using Android Development framework (Android SDK) which is basically Android library written in Java language. 
The Android library allows the developer to create screens, manage flows among the screens and also define connection 
with server (if required). In Pitfail, the connection from Android client can be made to either Yahoo! Finance to get 
the latest stock rates and other information or to the PitFail server, to update the database information about the 
user and also to retrieve user information according to the flow.

Android Frameworks used:

Activities:
An Activity is an application component that provides a screen with which users can interact in order to do something. 
We created activities to perform different tasks like Sell Stock, LeaderBoard, New Team. Each activity is given a window 
in which to draw its user interface.

Services:

A Service is an application component that can perform long-running operations in the background and does not provide a 
user interface. Android provided two types of services. Bounded and Unbounded. We created an Unbound Polling service to receive stock updates
from the server. An Unbound service will continue to run in the background even if the user switches to another application. The Polling service
hits the Jetty server periodically to recieve stock updates on any of the stocks held by user. Our Polling service starts as soon as the User 
starts the PitFail Application on his device. 

Notifications:
Notification is a special feature of the Android smart phones, where the user can receive important updates about the account 
even when the application is not in the front screen. We used this feature to provide notification to the user when the rates 
of the shares held by the user change in the market. This will help the user to receive automatic updates, rather than checking the 
statistics from time to time. The Polling service passes any stock updates as new notifications with a unique ID to the Notification 
Manager. The Notification Manager then displays the stock update message as a New Notification on Android Status Bar. The user can clear 
the Notifications whenever he wants.




Algorithms and Data Structures
==============================
..TODO

User Interface Design and Implementation
========================================
..TODO

History of Work & Current Status of Implemenation 
=================================================

Gantt Chart
-----------
include pdf for the _Plan of Work_

Comparison to Planned Milestones
--------------------------------
The planned milestones from Report 2 differed from reality in that they were overly aggressive and did not take into account that quickness that Pitfail team members could implement certain functions. When creating the planned deadlines in Report 2, team members assumed working two to four hours a day on Pitfail. What happened is that other responsibilities in other classes resulted in stretches of inactivity in Pitfail, thus throwing up the planned deadlines. As the Demo 2 day approached, great amounts of time during the day and night were put into Pitfail in a way that Microsoft Project could not correctly capture a "typical Pitfail working day." The result is a History of Work heavily concentrated around Demo days. If Pitfail were a company, Report 2's Plan of Work would have been a great guiding factor in agile development. Instead, Report 3's History of Work better explains how milestones were achieved. 

The History of Work shows the milestones that were not accomplished as tasks that are corssed out. The various non-accomplished were not accomplished either because their predecessors were not accomplished, the milestones were minor goals if time permitted and time ran out, or the milestones were no longer deemed necassary: 
1. The support for comlplex actions (orders, derivatives) was not implemented because the need for free-form Twitter input seemed unnecessary. The structured Twitter input was easily understandable, but without an upgrade to an unstructured Twitter input recongizer, advanced actions would not be easily understood in the structured Twitter system. Hence, advanced support for Twitter was not implemented. 
2. Challeges was not implemented because the teams and leagues were delievered very close to Demo 2. Implemented challenges would have been a trade-off between itself and debugging and debugging was deemed more important. 
3. Implemented OpenID for Facebook and Google was deemed not necassary since Twitter offered a similar service that was already implemented. 

Key Accomplishments
-------------------
The following are the key accomplishments of the Pitfail project that were implemented split across the platforms they were implemented on and the different use cases that were implemented:

* Multiple Interface
	* Website
	* Android
	* Twitter
	* Facebook
	* Email
* Use Cases 
	* Stocks - Buy/Sell
	* Option for Orders
	* Derivatives 
	* Auctions
	* Portfolio Graphs
	* Auto Trades
	* Comments
	* Voting
	* Teams - cooperative
	* Leagues - competitive
	* Leaderboard

Conclusions and Future Work
===========================
..TODO

References
==========
Marsic, Ivan. *Software Engineering*. Piscataway: Rutgers University, 2011. PDF.
Miles,  Russ  and  Kim  Hamilton.  *Learning  UML  2.0*.  Ed.  Eric  McLaughlin  and  Mary  O'Brien. Sebastopol: O'Reilly, 2006.


http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

http://en.wikipedia.org/wiki/Java_Database_Connectivity
..TODO