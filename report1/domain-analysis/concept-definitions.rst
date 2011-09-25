
Concept Definitions
~~~~~~~~~~~~~~~~~~~

User
----

Defition
........

A human being playing the PitFail game.

Responsibilities
................

Web Browser
-----------

Definition
..........

The User's browser, running on the User's computer.

Responsibilities
................

 - Take input from User
 - Send requests to Web Server
 - Receive responses from Web Server
 - Render page content

Web Server
----------

Definition
..........

HTTP web server, running on PitFail's server.

Responsibilities
................

 - Receive requests for Web Browser
 - Delegate requests to Web Framework
 - Receive responses from Web Framework
 - Send Responses to Web Browser

Web Framework
-------------

Definition
..........

Web framework APIs.

Responsibilities
................

 - Recieve requests from Web Server
 - Convert requests to structured data and delegate to appropriate handlers
 - Receive rendered pages in the form of structured data and convert to markup
 - Send responses to Web Server

Page Renderer
-------------

Definition
..........

Creates a presentation aimed at the User in the form of structured data.

Responsibilities
................

 - Decide what information should be rendered
 - Convert prices/balance sheets/news to human-readable form
 - Send rendered pages to the Web Framework

OAuthConsumer
-------------

Definition
..........

Takes the role of the "consumer" in the OAuth protocol.

Responsibilities
................

 - Receive requests from Web Framework
 - Send requests for authentication to twitter.com
 - Receive + store session secrets from twitter.com
 - Inform Login Manager of new logins
   
Stock Trader
------------

Definition
..........

Is in change of the logic of making trades.

Responsibilities
................

 - Receive requests from Web Framework
 - Interpret requests and translate them into operations on the Model
 - Decide of a request makes sense and is legal for the current user
 - Inform the Page Renderer of recent actions so that they may be report to the user
 - Manipulate the Model to reflect the result of trades

Price Fetcher
-------------

Definition
..........

Gets real-world stock prices.

Responsibilities
................

 - Receive requests for price information from various components
 - Request new price information from yahoo.com
 - Receive price information from yahoo.com
 - Maintain a cache of recent price quotes
   
Login Manager
-------------

Definition
..........

Handles the current user login.

Responsibilities
................

 - Receive new login information from OAuthConsumer
 - Store current login information for the session
 - Query the Model to check for existing user information
 - Update the Model to reflect new user information

Twitter Listener
----------------

Definition
..........

Provides an interface for users to play PitFail via Twitter.

Responsibilities
................

 - Maintains a connection with twitter.com and listens for tweets
 - Delegates tweets to the Interpreter
 - Receives responses from the interpreter and sends them as tweets

Interpreter
-----------

Definition
..........

Interprets text-based trading commands.

Responsibilities
................

 - Receive text commands from Twitter Listener and Facebook Listener
 - Delegate commands to the Parser and receive a structured representation
 - Send structured commands to the Stock Trader and receive a response
 - Convert response to text and send back to the corresponding Listener
   
Parser
------

Definition
..........

Converts human-entered text to structured trading commands.

Responsibilities
................

 - Receive text commands from the Interpreter
 - Convert commands to structured from

Model
-----

Definition
..........

Handles persistent data.

Responsibilities
................

 - Create and maintain a database handle
 - Convert high-level model operations to database queries


