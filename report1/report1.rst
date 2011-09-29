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
  An instance of the *game* having particular rules associated with it. A
  *coordinator* may create a league for *players* to join.

Player
  See `Actors and Goals`_

Coordinator
  See `Actors and Goals`_

Game
  The trading of securities given a particular set of rules with the object to
  increase the value of one's portfolio.

Functional Requirements Specification
=====================================

Stakeholders
------------

- *Advertisers* who purchase ads on the website
- *Spectators* interested in finance who do not wish to invest in the real market
- *Teachers* of economics courses and their *students*

Actors and Goals
----------------
- A *Player* is one who participates by buying and selling securities.

  - Wants to increase the value of their portfolio, thereby proving compitency
    at security trading.

- A *Web Player* is a *player* who is interacting with the *game* via the web
  browser interface. This actor contains all use cases of the *player*. It also
  shares the goal of the *player*.
- A *Twitter Player* is a *player* who is interacting with the *game* via the
  twitter interface. This actor contains all use cases of the *player*. It also
  shares the goal of the *player*.
- A *Coordinator* is responsible for administering a *league*.

  - Wants to effectively administer the tournament to provide either a learning
    experience to the *players*, or, alternately, an enjoyable experience to
    the players.
  - Desires a construct in which to effectively challenge others interested in
    security trading.

- *Yahoo* is the source for all real market data which determines the actual
  effect of purchasing and selling securities.

Use Cases
---------

The system is designed such that customization and setup by a *player* is
minimized. As such, league joining is uneeded by new players. In fact, to be a
new *twitter player*, one can simply send a *commanding tweet* and the Pitfail
system will automatically initialize the required backing data.

Account creation is ommited from the use case listing because account creation
is always acomplished implicitly. Third party services are used for
authorization, and all other setup is accomplished with defaults that may be
changed at another point it time by the *player* as requested (UC-7).

=============  ===================================================  =======
Actor              Description                                        UC#
=============  ===================================================  =======
Player         Purchases a security.                                 UC-1
Player         Sells a held security.                                UC-2
Player         Joins a leage                                         UC-3
WebPlayer      Queries the value of his or her portfolio.            UC-4
WebPlayer      Examines details of a particular asset.               UC-5
WebPlayer      Checks league statistics.                             UC-6
WebPlayer      Changes some settings regarding their Player          UC-7
WebPlayer      Changes some settings regarding a portfolio/league    UC-8
               they are a member of.
TwitterPlayer  Requests to brag about their portfolio.               UC-9
TwitterPlayer  Changes his or her current (default) league.          UC-10
Coordinator    Creates a league.                                     UC-11
Coordinator    Modifies a league's settings.                         UC-12
Coordinator    Add an additional Coordinator to a league.            UC-13
Coordinator    Delete a league.                                      UC-14
Coordinator    Accept or decline requests to join a league.          UC-15
Coordinator    Invite players to a league.                           UC-16
=============  ===================================================  =======

Nonfunctional Requirements
==========================

1.Usability:
------------

The website should be easy to navigate irrespective of the type of user. 
It should have an appealing user interface which is pleasant to the eyes.
A through consideration should be given for its aesthetic design in order 
to make it easily navigable and to have a good readability. The key focus
 should be on making the user interface as interactive as possible. 

2.Performance:
------------

In order to have a great performance, the website should be as lightweight
as possible by keeping minimum hardware demands. For it to be efficient, 
any task initiated by the user should be completed in a timely manner. 
The web server should be able to serve multiple requests and when a large
number of users are logged in. 

3.Reliability:
------------

In case of Internet failure, the user’s portfolios should be brought
back to a consistent state when user logs in the system again after 
the failed internet connection. The system should keep a backup of 
user’s data in case of server failure. A proper care should be taken 
to handle a situation where a particular stock source is not available (i.e. Yahoo).

4.Security:
------------

The system should be secure enough such that user’s privacy is maintained.  
The system should have a login process irrespective of the application i.e via 
Website, Mobile or twitter interface.
 
5.Supportability/Extensibility:
------------

It should be feasible to extend any server components and include improved 
versions of modules which can be installed only by administrators. For future 
purposes of handling the load, it should be easier to include more number of 
servers to achieve load balancing. The system should be platform independent 
so that it is easy to move to newer technologies or the next versions of web server. 

6.Maintainability:
------------

The system should be easy to maintain for the administrator. The administrator
 should be provided with an interface to interact with the entire system to 
make changes and to recover from any failure manually as well. The interface 
should give the administrator enough capability to perform future maintenance.

7.Testability:
------------

The system should be flexible enough to allow creating test databases and fake 
players so that feature test does not need to manipulate the actual database. 
This would ensure that it has great testability which can be used to build a 
more robust 

8.Consistency:
------------

It should be ensured that the application is consistent throughout irrespective 
of what interface the player is using i.e whether website, mobile application or 
twitter interface. Functionality might be limited on these different interfaces 
but it should not difficult for the user to shift from one application to another 
to access the system. Buzz words used should be same throughout and on all the 
interfaces to avoid confusion.

9.Documentation:
------------

The website should have enough material in the form of tutorial which can help 
the user to understand the rules and policies of the Stock fantasy league game 
and how it works.



Domain Analysis
===============

Domain Model
------------

A sparse overview of the Domain Model looks like

.. figure:: domain-analysis/Overview.pdf
    :width: 100%

We can zoom in on the various parts to add attributes and assocations:

The Model is the backend persistent storage:

.. figure:: domain-analysis/Model.pdf
    :width: 50%

The Price Fetcher:

.. figure:: domain-analysis/PriceFetching.pdf
    :width: 50%

The Web trading frontend:

.. figure:: domain-analysis/WebTrading.pdf
    :width: 50%

The Twitter trading frontend:

.. figure:: domain-analysis/TwitterTrading.pdf
    :width: 50%

And the login process:

.. figure:: domain-analysis/Login.pdf
    :width: 50%

Concept Definitions
...................

The concepts from the model are:

**User**

*Defition*: A human being playing the PitFail game.

**Web Browser**

*Definition*: The User's browser, running on the User's computer.

*Responsibilities*:

 - Take input from User
 - Send requests to Web Server
 - Receive responses from Web Server
 - Render page content

**Web Server**

*Definition*: HTTP web server, running on PitFail's server.

*Responsibilities*

 - Receive requests for Web Browser
 - Delegate requests to Web Framework
 - Receive responses from Web Framework
 - Send Responses to Web Browser

**Web Framework**

*Definition*: Web framework APIs.

*Responsibilities*

 - Recieve requests from Web Server
 - Convert requests to structured data and delegate to appropriate handlers
 - Receive rendered pages in the form of structured data and convert to markup
 - Send responses to Web Server

**Page Renderer**

*Definition*: Creates a presentation aimed at the User in the form of
structured data.

*Responsibilities*:

 - Decide what information should be rendered
 - Convert prices/balance sheets/news to human-readable form
 - Send rendered pages to the Web Framework

**OAuthConsumer**

*Definition*: Takes the role of the "consumer" in the OAuth protocol.

*Responsibilities*:

 - Receive requests from Web Framework
 - Send requests for authentication to twitter.com
 - Receive + store session secrets from twitter.com
 - Inform Login Manager of new logins
   
**Stock Trader**

*Definition*: Is in change of the logic of making trades.

*Responsibilities*:

 - Receive requests from Web Framework
 - Interpret requests and translate them into operations on the Model
 - Decide of a request makes sense and is legal for the current user
 - Inform the Page Renderer of recent actions so that they may be report to the user
 - Manipulate the Model to reflect the result of trades

**Price Fetcher**

*Definition*: Gets real-world stock prices.

*Responsibilities*:

 - Receive requests for price information from various components
 - Request new price information from yahoo.com
 - Receive price information from yahoo.com
 - Maintain a cache of recent price quotes
   
**Login Manager**

*Definition*: Handles the current user login.

*Responsibilities*:

 - Receive new login information from OAuthConsumer
 - Store current login information for the session
 - Query the Model to check for existing user information
 - Update the Model to reflect new user information

**Twitter Listener**

*Definition*: Provides an interface for users to play PitFail via Twitter.

*Responsibilities*:

 - Maintains a connection with twitter.com and listens for tweets
 - Delegates tweets to the Interpreter
 - Receives responses from the interpreter and sends them as tweets

**Interpreter**

*Definition*: Interprets text-based trading commands.

*Responsibilities*:

 - Receive text commands from Twitter Listener and Facebook Listener
 - Delegate commands to the Parser and receive a structured representation
 - Send structured commands to the Stock Trader and receive a response
 - Convert response to text and send back to the corresponding Listener
   
**Parser**

*Definition*: Converts human-entered text to structured trading commands.

*Responsibilities*:

 - Receive text commands from the Interpreter
 - Convert commands to structured from

**Model**

*Definition*: Handles persistent data.

*Responsibilities*:

 - Create and maintain a database handle
 - Convert high-level model operations to database queries

Attribute Definitions
.....................

Because it is primarily web-based, the PitFail program is mostly stateless.
Persistent data is almost entirely stored in a database, the schema for which
is described later.

A few attributes related to sessions and volatile information are stored within
the program itself. These are described here.

=============  ===============  =======================================================
Concept        Attribute        Meaning
=============  ===============  =======================================================
Model          datase handle    Allows communication with the database.
Database       tables           Relational tables. Schema described elsewhere.
Price Fetcher  cached prices    Stores recently retrieved prices to avoid DOSing yahoo
OAuthConsumer  session secrets  OAuth authentication secrets
OAuthConsumer  auth status      Whether authenticated, and if so as whom
Login Manager  current login    Currently logged in user
=============  ===============  =======================================================

Association Definitions
.......................

=================  ==================  ================  ===================================================
Subject            Verb                Object            Meaning
=================  ==================  ================  ===================================================
Browser            sends request to    Web Server        The user has followed a link or performed at action

Login Manager      informs             Page Renderer     Reports login status so it can be displayed on page
Login Manager      manipulates         Model             When a new user logs in, remember them in database
Model              informs             Login Manager     Tells is this a new user and who are they
OAuth Consumer     informs             Login Manager     Tells about new authentications

Model              sends query         JODBC             Sends SQL to be performed on the database
JODBC              returns srct. data  Model             Results of query

Stock Trader       requests            Price Fetcher     Requests price data for a ticker symbol
Price Fetcher      informs             Stock Trader      Returns requested data
Price Fetcher      requests            yahoo.com         Requests price for ticker
yahoo.com          informs             Price Fetcher     Tells price for ticker
                                                    
Stock Trader       manipulates         Model             To perform a trade
Model              informs             Stock Trader      Current status of portfolios

Interpreter        sends text          Parser            Human-written command to be parsed
Parser             sends structure     Interpreter       Interpretation (or failure)
Interpreter        sends operation     Stock Trader      Trade to be performed
Stock Trader       sends status        Interpreter       did it perform correctly

twitter.com        sends tweets        Twitter Listener  Live stream of user's tweets
Twitter Listener   sends tweets        twitter.com       Response to users

Web Framework      delegates request   Stock Trader      User performed a trade in browser
Stock Trader       informs             Page Renderer     Reports status of trade back to user
Page Renderer      informs             Web Framework     How to render the new page
Model              informs             Page Renderer     Current status of portfolios
=================  ==================  ================  ===================================================

System Operation Contracts
--------------------------

.. We don't have one of these, as far as I know
.. Mathematical Model
.. ------------------

User Interface Design
=====================
Pitfail's website satisfies the requirements that the other interfaces cannot:
enabling social interaction, providing a rich user interface, and coordinating
leagues. Providing a rich set of features above what is available via Twitter
is crucial for drawing existing users to the website. On balance, the website
must have a simple interface that welcomes new users and guides the new user
through the registration process. This starkly contrasts with many exiting
trading simulations, such as the Stock Market Game's seven page registration
procedure that requires a large amount of personal information.

Preliminary Design
------------------
Simplifying the registration procedure starts with the welcome page. Instead of
welcomes the logged-out user with a registration page, Pitfail presents him or
her with a simple four-step guide to purchasing his or her first stock.
Existing users can bypass this guided registration process at any time by
following the "login" link that is in the top-right corner of ever page. This
intentionally mimics the login method on popular websites such as Facebook,
Google, and Reddit.

If the prospective user chooses to create an account, he or she is guided
through a four step process to buy his or her first stock:

.. figure:: ui-mockups/ui-welcome1
	:scale: 50%

	When logged out, the website displays a welcome message and a simple
	four-step process for getting started. The user begins by entering a
	stock symbol that he or she wants to buy.

.. figure:: ui-mockups/ui-welcome2
	:scale: 50%

	After entering a valid ticker symbol the user proceeds to the second
	step and chooses an amount of stock to buy. This purchase is added to
	the user's global league portfolio once his or her account is created.

.. figure:: ui-mockups/ui-welcome3
	:scale: 50%

	Finally, the user is presented with an option to login using his or an
	existing OpenID account. Facebook and Google login buttons are provided
	for users that aren't familiar with OpenID.

Once authenticated with OpenID the user's account has been created and the
stock has been purchased. Note that the user is not prompted for any personal
information when creating his or her account. Whether registering a new account
or logging in, the user is now redirected to his or her Global league
portfolio.

Once logged in the user is redirected to his or her portfolio page in the
Global League. The portfolio page is the heart of the Pitfail website and
serves as a portal to the rest of the website and is split into three sections:
(1) controls to buy/sell securities, (2) league controls, and (3) an overview
of the securities in the current portfolio:

.. figure:: ui-mockups/ui-portfolio
	:scale: 50%

Users that are members of more than one league manage their league portfolios
completely independently: buying and selling securities only applies to the
portfolio that he or she is currently viewing. Such users can see which
portfolio they are managing and switch between portfolios using the tabs
attached to the top of the table of securities.

Much like when completing the guided account creation process, users can
purchase shares of a stock at market price by entering a ticker symbol in the
large search box near the top of the page. This displays a stock quote for the
requested company and displays the fields necessary to purchase the stock:

.. figure:: ui-mockups/ui-buy
	:scale: 50%

The user completes the purchase by entering a number of shares or dollar amount
into the text field and clicking the "buy" button. Similarly, the user can sell
shares at market price by using the same input technique in the table row that
corresponds to the stock that he or she wishes to sell (not pictured due to
space constraints).


User Effort Estimation
----------------------

Plan of Work
============

References
==========

