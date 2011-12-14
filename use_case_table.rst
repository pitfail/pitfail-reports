
=============  ===================================================  ===================  =====
Actor          Description                                          Short Name            UC#
=============  ===================================================  ===================  =====
WebPlayer      Purchases a security from the market at the price    Buy                  UC-1
               the *stock price source* indicates is the market
               price for that security.
WebPlayer      Sells a held security at the price indicated by the  Sell                 UC-2
               *stock price source*.
WebPlayer      Indicates that they wish to begin participating in   Join League          UC-3
               a particular league. Does not remove them from any
               league. Also note that leaveing a league is omitted
               to prevent people from gaming the system by
               joining a league, doing poorly, and leaving to
               essentially have a "clean record".
WebPlayer      Examine the contrents of his or her portfolio,       View Portfolio       UC-4
               displaying information regarding their current
               assets and liabilities as well as how they have
               been progressing over time
WebPlayer      Examines details of a particular security.           Get Security         UC-5
                                                                    Details
WebPlayer      Checks league statistics. Provide a clear view of    View League Stats    UC-6
               the leaderboard as well as changes over time.
TwitterPlayer  Purchases a security from the market at the price    Buy via Twitter      UC-7
               the *stock price source* indicates is the market
               price for that security.
TwitterPlayer  Sells a held security at the price indicated by the  Sell via Twitter     UC-8
               *stock price source*.
TwitterPlayer  Query portfolio value & other details.               Portfolio Info       UC-9
TwitterPlayer  Changes his or her current (default) league.         Change Default       UC-10
               The default league is the league which UC-1(Buy)     League
               and UC-2(Sell) requests are sent to when a league
               is not specified in the command string.
Coordinator    Creates a league.                                    Make League          UC-11
Coordinator    Modifies a league's settings. A coordinator will     League Settings      UC-12
               need to manage a league via changing settings
               regarding the league.
Coordinator    Add an additional Coordinator to a league.           Add Coordinator      UC-13
Coordinator    Remove a coordinator from the league.                Remove Coordinator   UC-14
Coordinator    Delete a league.                                     Delete League        UC-15
Coordinator    Accept or decline requests to join a league.         Manage League        UC-16
Coordinator    Invite players to a league.                          Invite to League     UC-17
WebPlayer      Authenticates with the system.                       Authentication       UC-18
WebPlayer,     Has their initial account (portfolio tracking)       Create User          UC-19
TwitterPlayer  created.
WebPlayer      Vote on trade.                                       Vote                 UC-20
TwitterPlayer  Vote on trade via a Twitter repost.                  Vote by Tweet        UC-21
WebPlayer      Create derivative.                                   Derivative Designer  UC-22
WebPlayer      Accept offer of a derivative.                        Accept derivative    UC-23

=============  ===================================================  ===================  =====
