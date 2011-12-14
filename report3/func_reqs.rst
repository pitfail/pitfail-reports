
Actors and Goals
================
..  - A *Player* is one who participates by buying and selling securities.

..  - Wants to increase the value of their portfolio, thereby proving competency
..    at security trading.
..  - Competes with other players for higher ranks in leagues.

- A *Web Player* is a *player* who interacts with the *game* via the web
  browser interface. The web interface also provides access to the command based
  interface.

  - Buys and Sell Stocks.
  - View and Modify Portfolio.
  - Create League.
  - Participate in Leagues.
  - Wants to effectively administer the tournament to provide either a learning
    experience to the *players*, or, alternately, an enjoyable experience to
    the *players*.
  - Desires a construct in which to effectively challenge others interested in
    security trading.

- A *Twitter Player* (or *TwitterPlayer*) is an indirect *player* who interacts
  with the *game* via the *Twitter* actor. They are the originator of the
  commands recieved from the *Twitter* actor.

  - Buys and Sells Stocks
  - Examines their portfolio

- A *MobilePlayer* is a *player* who interacts with the *game* via the
  Android interface. This actor contains has limited use cases compared to a Web Player.

  - Buys and Sells Stocks
  - View Portfolio
  - Participate in Leagues

- The *database* is the store for all persistent data on interactions with the
  *system*. It stores data regarding all user portfolios and the association of
  authentications with users.

- A *stock information provider* is a supplier of stock pricing data for the present
  (within the margin of some minutes). They are queried for all data regarding
  actual market numbers. Currently, *Yahoo* is the *stock information provider*
  (via its Yahoo Finance API).

- *Authentication providers* allow us to uniquely identify users and associate
  some stored state with their unique identification.

- *Twitter* is utilized both as a authentication provider (for all *players* as
  well as a portion of the interface to the service. This actor provides a
  stream of text based commands from the indirect actor *Twitter Player*.

Use Cases
=========

.. figure:: use_case_diagram
   :width: 100%

   A diagram of use cases and actors showing interactions and relationships.

Listing of Use Cases
--------------------

1. Buy, Actor: WebPlayer
   Purchases a security from the market at the price listed by the designated market makers.

2. Sell, Actor: WebPlayer
   Sells a held security at the price listed by the *DMMs*.

.. ===========  ===================================================  ===================  =====
.. Actor        Description                                          Short Name            UC#
.. ===========  ===================================================  ===================  =====
.. WebPlayer        Buy                  UC-1
..              
.. WebPlayer    Sells a held security at the price indicated by the  Sell                 UC-2
..              *stock price source*.
.. WebPlayer    Indicates that they wish to begin participating in   Join League          UC-3
..              a particular league. Does not remove them from any
..              league. Also note that leaveing a league is omitted
..              to prevent people from gaming the system by
..              joining a league, doing poorly, and leaving to
..              essentially have a "clean record".
.. WebPlayer    Examine the contrents of his or her portfolio,       View Portfolio       UC-4
..              displaying information regarding their current
..              assets and liabilities as well as how they have
..              been progressing over time
.. WebPlayer    Examines details of a particular security.           Get Security         UC-5
..                                                                   Details
.. WebPlayer    Checks league statistics. Provide a clear view of    View League Stats    UC-6
.. TwitterPlayer  the leaderboard as well as changes over time.
.. WebPlayer      Purchases a security from the market at the price    Buy via Cmd          UC-7
..                the *stock price source* indicates is the market
..                price for that security.
.. WebPlayer      Sells a held security at the price indicated by the  Sell via Cmd         UC-8
..                *stock price source*.
.. WebPlayer      Query portfolio value & other details.               Portfolio Info       UC-9
.. Coordinator    Creates a league.                                    Make League          UC-11
.. Coordinator    Modifies a league's settings. A coordinator will     League Settings      UC-12
..                need to manage a league via changing settings
..                regarding the league.
.. Coordinator    Add an additional Coordinator to a league.           Add Coordinator      UC-13
.. Coordinator    Remove a coordinator from the league.                Remove Coordinator   UC-14
.. Coordinator  Delete a league.                                     Delete League        UC-15
.. Coordinator  Accept or decline requests to join a league.         Manage League        UC-16
.. Coordinator  Invite players to a league.                          Invite to League     UC-17
.. WebPlayer    Authenticates with the system.                       Authentication       UC-18
.. WebPlayer,   Has their initial account (portfolio tracking)       Create User          UC-19
.. CmdPlayer    created.
.. WebPlayer    Vote on trade.                                       Vote                 UC-20
.. CmdPlayer    Vote on trade via a Twitter repost.                  Vote by Tweet        UC-21
.. WebPlayer    Create derivative.                                   Derivative Designer  UC-22
.. WebPlayer    Accept offer of a derivative.                        Accept derivative    UC-23
.. 
.. ===========  ===================================================  ===================  =====

Fully Dressed Use Cases
-----------------------

UC-1: Buy
.........
Related Requirements:
        REQ-1, REQ-2, REQ-6, REQ-7, REQ-8, REQ-9

Initiating Actor:
        Any of: Webplayer, TwitterPlayer, MobilePlayer

Actor's Goal:
        To purchase a security from the market, to add it to his portfolio, and
        see his updated portfolio.

Participating Actors:
        Database, Securities, Stock Price Source, Yahoo!

Preconditions:
        The user should have created an account, be in a league  with settings
        that allows the "BUY", and have enough money to perform the BUY of the
        security.

Postconditions:
        The user needs to be able to see his purchased security in his
        portfolio and track the progress of the security in his portfolio until
        he "SELLS" it.

Flow of Events for Successful Buy:
        1. → The *Player, Webplayer, or TwitterPlayer* determines a *Security*
           and how much of it to "BUY".
        2. ← *System* signals the *Stock Price Source* for the price of the
           security.
        3. ← *Stock Price Source* sends the price of the *Security* to the
           *System.*
        4. ← *System* signals the *Database* for the amount of money the
           *Player* has.
        5. ← *Database* sends the amount of money for the *Player* to the
           System.
        6. ← *System* checks that there is enough money for compelete the
           transcation.
        7. ← *System* signals the *Database* to complete the transcation for a
           *Player*, *Security*, and the quantity.
        8. ← *Database* signals the *System* the transcation is complete.
        9. ← *System* signals to the *Player* "Transcation Completed."

Flow of Events for Unsuccessful Buy:
        1. → The *Player, Webplayer, or TwitterPlayer* determines a *Security*
           and how much of it to "BUY".
        2. ← *System* signals the *Stock Price Source* for the price of the
           security.
        3. ← *Stock Price Source* sends the price of the *Security* to the
           *System.*
        4. ← *System* signals the *Database* for the amount of money the
           *Player* has.
        5. ← *Database* sends the amount of money for the *Player* to the
           System.
        6. ← *System* checks that there is enough money for compelete the
           transcation.
        7. ← There is not enough money. *System* signals to the *Player*
           "Transcation Not Completed: Insufficient Funds."

UC-2: Sell
..........
Related Requirements:
        REQ-1, REQ-2, REQ-6, REQ-7, REQ-8, REQ-9

Initiating Actor:
        Any of: Webplayer, TwitterPlayer, MobilePlayer

Actor's Goal:
        To purchase a security from the market, to add it to his portfolio, and
        see the updated portfolio

Participating Actors:
        Database, Securities, Stock Price Source, Yahoo!

Preconditions:
        - User is logged in
        - Contain in his portfolio at least the quantity of securities his is
          requesting to sell.

Postconditions:
        - The user's portfolio will reflect the quantity of securities sold.

Flow of Events for Successful Sell:
        1. → The *Player* determines a *Security*
           and how much of it to "SELL".
        2. ←  *System* signals the *Stock Price Source* for the price of the
           security.
        3. ←  *Stock Price Source* sends the price of the *Security* to the
           *System.*
        4. ←  *System* signals the *Database* for the amount of the *Security*
           the *Player* has.
        5. ←  *Database* sends the amount of the *Security* the *Player* has to
           the System.
        6. ←  *System* checks that there is enough *Securities* to complete the
           transaction.
        7. ←  *System* signals the *Database* to complete the transcation for a
           *Player*, *Security*, and the quantity.
        8. ←  *Database* signals the *System* the transaction is complete.
        9. ←  *System* signals to the *Player* "Transaction Completed."

Flow of Events for Unsuccessful Sell:
        1. → The *Player* determines a *Security*
           and how much of it to "SELL".
        2. ←  *System* signals the *Stock Price Source* for the price of the
           security.
        3. ←  *Stock Price Source* sends the price of the *Security* to the
           *System.*
        4. ←  *System* signals the *Database* for the amount of the *Security*
           the *Player* has.
        5. ←  *Database* sends the amount of the *Security* the *Player* has to
           the System.
        6. ←  *System* checks that there is enough *Securities* to complete the
           transaction. There is not.
        7. ←  *System* signals to the *Player* "Transaction Not Completed:
           Insufficient Securities."

UC-4: View Portfolio
....................
Related Requrements:
        REQ-1, REQ-2, REQ-6, REQ-10, REQ-11, REQ-14

Initiating Actor:
        Only *WebPlayer*, the similar UC-9 is provided for the *Twitter player*.

Actor's Goal:
        To view information regarding their portfolio. This information
        includes the currently owned securities, minimal statistics regarding
        those securities (as they relate to the current and past value of the
        portfolio), current avaliable capital (and similar minimal information
        regarding its change), and the overall value of the portfolio (also
        with some statistical information regarding changes over time). The
        actor desires this information to make decisions regarding what their
        next interaction with the system should be. They use this info to
        decide to sell stock they have or buy an increased number of shares of
        stock they have).

Participating Actors:
        *Stock information provider*, *Database*

Preconditions:
        None, note that authentication & account creation are handled within
        this use case.

Postconditions:
        None, this is a stateless action. Information is displayed to the user
        but no internal actions are taken.

Flow of Events for Main Success Scenario:
        1. → *Web player* browses to a page which will display his portfolio.
        2. ← *System* checks for authentication and when it does not exsist (a)
           runs the authentication (UC-18). Checks for a associated *user* in
           the system and when there is none runs (b) user creation (UC-19).
        3. ← *System* requests the information about the user's portfolio for
           this particular league from the *Database*.
        4. → *Database* returns the information regarding the portfolio.
        5. ← *System* forms a query regarding all the currently held securities
           within the portfolio and dispatches it to the *stock info provider*.
        6. → *Stock info provider* returns the requested data.
        7. ← *System* forms a web view of the portfolio information and returns
           it to the *web player*

Additional Notes:
        When this use case is running the other contained use cases (UC-18 and
        UC-19), each of these perform their own sequence of interactions with
        the user. In the case of a failure in one of the included use cases,
        the users remains in the control of that included use case until the
        failure is resolved or another use case is initiated.

UC-5: View League Statistics
.............................
Related Requirements:
        REQ-1, REQ-6, REQ-9

Initiating Actor:
        WebPlayer

Actor's Goal:
        To view the performance of his or her portfolio relative to other
        league members. For a teacher, this may also be used to verify that his
        or her students are actively participating in the game.

Participating Actors:
        Database

Preconditions:
	The league that is being viewed exists and the league is either public or the user is a member.

Postconditions:
        None; this is a stateless action.

Flow of Events for Main Success Scenario:
        1. → *Player* requests to view league performance.
        2. ← *System* signals the *Database* for authentication and the league's leaderboard.
        3. ← *Database* authenticates the user's ability to view the statistics and returns the league's leaderboard.
        4. ← *System* returns a leaderboard of all league members.

Flow of Events for league does not exist:
	1. → *Player* requests the league statistics page.
	2. ← *System* signals the *Database* for authentication and the league's leaderboard.
	3. ← *Database* signals the *System* that the league does not exist.
        4. ← *System* returns "page not found" error.

Flow of Events for league is invite-only and the user is not a member:
	1. → *Player* requests the league statistics page.
	2. ← *System* signals the *Database* for authentication and the league's leaderboard.
	3. ← *Database* signals the *System* that the league is invite-only and the *Player* is not a member.
        4. ← *System* returns "access denied" error.

UC-6: Modify League Settings
............................
Related Requirements:
        REQ-1, REQ-14, REQ-20

Initiating Actor:
        Coordinator

Actor's Goal:
        To modify settings for the coordinator's league. This includes modifying
        the league's name, nickname, starting funds, and security settings.

Participating Actors:
        Database

Preconditions:
        - League that is being modified exists
        - Initiating actor is a coordinator of the league that he or she is modifying

Postconditions:
        - League name is still unique
        - League nickname is still unique
        - Starting funds is positive

Flow of Events for Main Success Scenario:
        1. → *Coordinator* requests to view league settings page.
        2. ← *System* signals the *Database* for authentication and the league's settings page.
        3. ← *Database* authenticates the user's ability to modify the league settings and returns the league settings page.
        4. ← *System* returns a league setting page populated with the current settings.
        5. → *Coordinator* submits updated league settings.
        6. ← *System* Validate new league settings
        7. ← *System* sends updated settings to the *database.*
        8. ← *Database* signals the *System* that the settings have been updated.
        9. ← *System* signals the *Coordinator* "Settings have been updated."

Flow of Events for league does not exist:
	1. → *Player* requests the league settings page.
	2. ← *System* signals the *Database* for authentication and the league's settings page.
	3. ← *Database* signals the *System* that the league does not exist.
        4. ← *System* returns "page not found" error.

Flow of Events for user is not a coordinator of the league:
	1. → *Player* requests the league settings page.
	2. ← *System* signals the *Database* for authentication and the league's settings page.
	3. ← *Database* signals the *System* that the league is invite-only and the *Player* is not a member.
        4. ← *System* returns "access denied" error.


Use Case Tracability Matrix
---------------------------
The following is the relationship between the use-cases defined above and the
requirements discussed in the statement of requirements:

- **UC-1:** REQ-1, REQ-2, REQ-6, REQ-7, REQ-8, REQ-9
- **UC-2:** REQ-1, REQ-2, REQ-6, REQ-7, REQ-8, REQ-9
- **UC-3:** REQ-1, REQ-20
- **UC-4:** REQ-1, REQ-2, REQ-6, REQ-10, REQ-11, REQ-14
- **UC-5:** REQ-1, REQ-6, REQ-9
- **UC-6:** REQ-1, REQ-14, REQ-20
- **UC-7:** REQ-3, REQ-6, REQ-7, REQ-8, REQ-9
- **UC-8:** REQ-3, REQ-6, REQ-7, REQ-8, REQ-9
- **UC-9:** REQ-3, REQ-6, REQ-10, REQ-11, REQ-14
- **UC-10:** REQ-3, REQ-20
- **UC-11:** REQ-1, REQ-13, REQ-17
- **UC-12:** REQ-1, REQ-13, REQ-17
- **UC-13:** REQ-1, REQ-13, REQ-17
- **UC-14:** REQ-1, REQ-13, REQ-17
- **UC-15:** REQ-1, REQ-13, REQ-17
- **UC-16:** REQ-1, REQ-13
- **UC-17:** REQ-1, REQ-13
- **UC-18:** REQ-1, REQ-4, REQ-10, REQ-11, REQ-17
- **UC-19:** REQ-1, REQ-4, REQ-5, REQ-10, REQ-11
- **UC-20:** REQ-1, REQ-2, REQ-15, REQ-20
- **UC-21:** REQ-3, REQ-15, REQ-20
- **UC-22:** REQ-1, REQ-18, REQ-19
- **UC-23:** REQ-1, REQ-2, REQ-18, REQ-19
