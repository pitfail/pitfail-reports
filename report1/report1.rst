.. raw:: latex

	\begin{titlepage}
	\centering
	\singlespacing

	\vspace*{2in}

	\begin{center}
		\Huge Pitfail Report 1 \\
		\Large An Online Financial Engineering Game
	\end{center}

	\vspace*{2in}

	\large
	September 30, 2011 \\

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
.. raw:: latex

	\begin{center}
	\small

.. csv-table::
	:header: "Responsibility", "Michal Koval", "Cody Schafer", "Owen Healy", "Brian Good-acre", "Roma Mehta", "Sonu Iqbal", "Avanti Kulkarni"
	:widths: 15, 6, 6, 6, 6, 6, 6, 6

	Project Management,    0%, 0%, 0%, 0%, 0%, 0%, 0%
	Customer Statement,    0%, 0%, 0%, 0%, 0%, 0%, 0%
	Glossary of Terms,     0%, 0%, 0%, 0%, 0%, 0%, 0%
	Functional Reqs.,      0%, 0%, 0%, 0%, 0%, 0%, 0%
	Nonfunctional Reqs.,   0%, 0%, 0%, 0%, 0%, 0%, 0%
	Domain Analysis,       0%, 0%, 0%, 0%, 0%, 0%, 0%
	User Interface Design, 0%, 0%, 0%, 0%, 0%, 0%, 0%
	Plan of Work,          0%, 0%, 0%, 0%, 0%, 0%, 0%
	References,            0%, 0%, 0%, 0%, 0%, 0%, 0%

.. raw:: latex

	\end{center}

Glossary of Terms
=================
league
  An instance of the Game having particular rules associated with it. A
  Coordinator may create a league for Players to join.

term2
  definition 2

Functional Requirements Specification
=====================================

Stakeholders
------------
- *Advertisers* who purchase ads on the website
- *Spectators* interested in finance who do not wish to invest in the real market
- *Teachers* of economics courses and their *students*

Actors and Goals
----------------
- TODO

Actors
~~~~~~
- *Player* who participates by buying and selling securities
- *Coordinator* responsible for administering a *league*

Goals
~~~~~

Use Cases
---------

===========  ===================================================  =======
Actor            Description                                        UC#
===========  ===================================================  =======
Player       Purchases a security.                                 UC-1
Player       Sells a held security.                                UC-2
Player       Queries the value of his or her portfolio.            UC-3
Player       Examines details of a particular asset.               UC-4
Player       Checks league statistics.                             UC-5
Player       Changes his or her current league.                    UC-6
Coordinator  Creates a league.                                     UC-7
Coordinator  Modifies a league's settings.                         UC-8
Coordinator  Add an additional Coordinator to a league.            UC-9
Coordinator  Delete a league.                                      UC-10
Coordinator  Accept or decline requests to join a league.          UC-11
Coordinator  Invite players to a league.                           UC-12
===========  ===================================================  =======

Nonfunctional Requirements
==========================

Domain Analysis
===============

Domain Model
------------

System Operation Contracts
--------------------------

Mathematical Model
------------------

User Interface Design
=====================

Preliminary Design
------------------

User Effort Estimation
----------------------

Plan of Work
============

References
==========

