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
..TODO

Conclusions and Future Work
===========================
..TODO

References
==========
..TODO