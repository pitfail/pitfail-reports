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

League
  An instance of the Game having particular rules associated with it. A
  Coordinator may create a league for Players to join.

term2
  definition 2

Functional Requirements Specification
=====================================

Stakeholders
------------

1. Ad Space purchasers.
2. People with an interest in the fincancial markets who lack the means or
   willingness to interact with the Real Market directly.
3. Teachers of economics courses (and the students of those teachers).

Actors and Goals
----------------

Actors
~~~~~~
1. Player, participates by buying and selling items and managing a portfolio
2. Coordinator, controls/runs a league

Goals
~~~~~

Use Cases
---------

===========  ===================================================  =====
Actor            Description                                       UC#
===========  ===================================================  =====
Player       Purchases a security.                                   1
Player       Sells a held security.                                  2
Player       Querys the value of his portfolio.                      3
Player       Examines details of a particular asset.                 4
Player       Checks league statistics.                               5
Player       Changes their current league.                           6
Coordinator  Creates a league.                                       7
Coordinator  Modifys the settings for a league.                      8
Coordinator  Add an additional Coordinator to a league.              9
Coordinator  Delete a tournament.                                   10
Coordinator  Admit players to a league (accept/reject requests).    11
Coordinator  Invite players to a league.                            12
===========  ===================================================  =====


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

