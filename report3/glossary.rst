
Here we attempt to clarify possibly ambiguous words as they are used in
PitFail. We are not defining these words in general; just what they mean in
this document.

Ask Price
    
    The price at which a trader is willing to sell a stock. [Ask]_
    
Asset

    Either a stock or the buyer end of a derivative contract.

Bid Price

    The price a trader is willing to pay for a stock. PitFail has its own
    opinion (independent of Yahoo Finance) of what the bid price of a stock is,
    because PitFail players can trade with one another [Bid]_.
    
Client

    A system that is not running on PitFail's server. An example is a
    webbrowser, the Android phone, or the Facebook connector.
    
Company

    A synonym for Portfolio.
    
Consistency

    Obeying all explicit or implied contracts (e.g., types describe a form of
    consistency).
    
Controller

    The part of MVC that operates on the Model but is not represented by a
    domain concept.
    
Form

    The main mode of interacting with the website frontent. User enters values
    and submits them.
    
Last Traded Price

    The price which Yahoo Finance considers to be the last traded price of a
    stock.
    
Leaderboard

    A list of the highest ranked portfolios in a League.
    
League

    A group of portfolios that compete against each other. `Users, Portfolios,
    and Leagues`_
    
Liability

    The seller end of a derivative contract.
    
Limit Order

    An order to buy or sell a stock at any available price within some bound [Limit]_.
    
Model

    The part of MVC that maintains the state of the system. The Model is where
    concepts from the Domain Model are realized as code.

Player

    A human being interacting with PitFail.
    
PitFail

    The entire trading simulation, including the backend, the various clients,
    and the players playing it.

Portfolio
    
    A portfolio in pitfail is the primary concept in trading; the one that
    makes trades, owns stocks, etc. See `Users, Portfolios, and Leagues`_.
    
Price

    Dollars per share.
    
Scale

    A unitless number.
    
Side-effect

    A result of invoking a function that is hidden by the function's signature. [SideEffects]_
    
Stock

    PitFail recognizes as a stock anything that Yahoo Finance is willing to
    assign a price to.
    
Team

    A synonym for Portfolio, specifically used in the case where more than one
    user is in control of said portfolio.

User

    A user is a single account in the PitFail system. A single user typically
    corresponds to 1 player. See `Users, Portfolios, and Leagues`_.
    
View

    The part of MVC that is visible to the user. The View may include HTML
    files, presentation-specific code, protocols for communicating with the
    user (e.g. HTTP), stylesheets.

