
Investors today are seeking more effective financial tools that not only
motivates them to invest in the stock market and improve their decision making
skills but also an application that is interesting enough to keep using. Our
goal is to build a system that is less focused on simulation than on playing a
game. Existing trading simulations mimic the inconveniences of trading stocks
on real markets; while this might help future traders to practice, it is out of
place for the typical internet user. PitFail's philosophy is that the market
for trading *practice* is already well-handled by games such as Investopedia.
PitFail instead believes that it is more important to teach theory than
mechanics. In contrast with the existing alternatives, PitFail offers number of
differentiating features: while the core program centers around buying and
selling of liquid assets (stocks, options; anything with available market
prices), PitFail aims eventually to users to trade directly with each other in
non-liquid assets such as derivatives. To achieve a low-threshold for getting
in to the game, PitFail may be played using users' existing accounts (such as
Twitter, smart phones or Facebook) with essentially no setup.

PitFail creates a virtual stock world, creating a network of stock investors,
through which they trade real-world stocks without the risk of losing real
money. Unlike existing trading simulations, PitFail does not require the
players to go through a time-consuming registration process. Players can login
to the system using their existing e-mail addresses and the system remembers
the players for their next use. As such, PitFail requires essentially no
commitment and it is easy for players to get started.  Initially, the player is
given a fixed amount of startup funds and uses these funds to buy virtual
stocks.

You could take a trading game different ways -- Investopedia, which is
excruciatingly tied to the real world, or Neopets which is isolated and
pristine -- but the nice thing about capitalism is that we can play with any
rules, so long as they're consistent. But so many (all that I'm aware of) of
the games that have been written so far left out something so important: you
can't enter (enforced) contracts with other players.

It's not a trivial detail -- if you can't enter contracts, you can't turn
intangible ideas into *assets* -- ie, you can't commoditize all the things you
might like to commoditize (well, maybe you can if that's nothing). There's a
good reason they don't do this, of course: to enforce contracts you either need
a legal system (doable -- Wikipedia has one, but a serious impediment still) or
contracts that a computer can enforce. PitFail makes a compromise -- users can
enter into contracts (in the form of derivatives), but the rules are reduced to
a simple set that the system can enforce, yet that can be combined creatively
by the players.

This adds a new aspect to the game -- illiquidity. The PitFail stock exchange
is simulated as a perfectly efficient, perfectly liquid market. This is of
course unrealistic -- in the real world, trading volume is finite, trades are
not made constantly, not all trades are made at the marginal price. Alas, it
would be hard for PitFail to simulated illiquidity in stocks -- unless we have
access to an actual massive population of traders, it would be simply *too*
illiquid to be worth playing.

There are many options for a player to choose from once he/she logs in:

1. Player can join a team (a small group of already registered players). Once
   player joins a team, the player will buy/sell/compete with other players/teams
   using collective portfolio of the team.

2. Player can join a league (a group of already registered players) where the
   members of a league compete with each other using their individual portfolio.

3. Player can play in the "Global League" which includes all players.

When the player trades and builds a portfolio, the system should have access to
real-time stock information and should adjust the value of a player's
investments based on this real time stock info. PitFail retrieves actual stock
prices from a third-party source Yahoo! that monitors stock exchanges and
maintains up-to-date (though delayed) stock prices. If the corresponding actual
stock loses value on a real-world stock exchange, the player's virtual
investment loses value equally.  Likewise, if the corresponding  actual stock
gains value, the player's virtual investment grows equally.

As a game, a crucial part of the application is maintaining player portfolio.
The application  provides every player with portfolio to view his or her
history and modify his or her current investments (i.e. currently owned stocks
and derivatives). In addition to the securities currently owned by the player,
the player is able to view a few summary statistics about their portfolio, such
as a history of net worth over time, and an indication of which assets have
increased in value since their purchase. What the player ultimately cares
about, of course, is net worth in the future -- that's what they are trying to
optimize. We can't tell them that, of course, nor should we, since it's the
whole point of playing the game. We should even be careful in categorizing
assets by change in value -- users will of course purchase assets that perform
oppositely to hedge risk.  Basically, we don't want to decide strategy for the
player; we want to give them information and let them decide strategy.

To add a flavor of a game, players can monitor each other's progress by viewing
a feed of recent activity and browsing leader boards. PitFail also offers
aggregate feeds of recent activity. This allows a group of people to keep
abreast of their friends' or enemies' activities. Remember, this is not real
personal information we're talking about -- we're willing to sacrifice privacy
(if you can call it that) for a competitive spirit. PitFail provides the
players with the ability to comment on other's trades when browsing recent
activity or viewing another user's portfolio. These comments make players feel
involved and part of a larger community. One additional feature PitFail
provides is the ability for players to "upvote" and "downvote" trades based on
their opinion of trade. PitFail can then rank users and assign status symbols
(e.g. badges) to users with the strongest ability to vote predictively. Of
course, predicting is only so good if you can't make good trades yourself --
but it's interesting to see both rankings nonetheless. This type of ranking
appears to be unique to PitFail. Another feature that appears to be unique to
PitFail is that it allows users to design their own securities (i.e futures or
options) , thus creating new financial products. Even without a court system to
enforce complex contracts, custom securities allow PitFail's users to a new
financial environment.

As mentioned, PitFail can be accessed via a website, Twitter, Facebook, or an
Android application. Each of these methods have their own purposes. As financial
trades are compact and atomic and that they can be expressed through small
messages, PitFail provides a Twitter and Facebook interfaces where players can
buy/sell securities by tweeting to a particular account/ writing post on
Facebook account wall .  Twitter and Facebook  provide a familiar interfaces to
use the system. Also, as no registration  is required which makes it easy to
use.  PitFail can also be accessed via a website that offers additional set of
features (In addition to all of the functionality provided by the Twitter
interfaces): like view portfolio, design custom securities, interact socially
with other users and play against or in co-operation (teams/leagues) with other
users. Also, website helps to generate some advertising revenue,
making it desirable to attract users to the PitFail website by offering
features that are not possible via Twitter/Facebook.  Android interface
provides features that are similar to that of the website, with the addition of
notifications to the user when some event occurs within PitFail.

The motivation for implementing teams/leagues comes from the apparent fact that
most (perhaps all) trading games target students and teachers as their
principal user base, suggesting this accounts for most of the people who
actually play these games. While PitFail is mostly seeking a different niche --
the casual online player -- the classroom market is too big to ignore
completely, hence a feature that makes it possible for students to play against
each other in a league.

Below is the list of customer requirements:

1. **REQ-1** Stock Market Simulator Website: Investors are looking for an
   effective tool that allows users to invest and learn without having to
   invest real money and also allows them to interact with other users more
   effectively to make the game really enjoyable.

2. **REQ-2** Android Application: Mobile users who like having native
   applications can use such system with quick access.

3. **REQ-3** Access via Twitter/Facebook: Users who heavily use social networks
   like Facebook/Twitter can connect to PitFail easily.

4. **REQ-4** Simple User Interface: Users are looking for simple interface that
   welcomes new users and guides the new user through portfolio management.

5. **REQ-5** Zero-Configuration Setup: Users should not have to set any
   settings or explicitly create an account to begin playing.

6. **REQ-6** Updated Stock Information: Application should present stock
   symbols, company names, stock history, updated stock values and prices
   amongst other details.

7. **REQ-7** Basic Trading: Users should be able to buy and sell stocks whose
   values change over time.

8. **REQ-8** Large, Liquid, Efficient Market: The simulated "exchange" should
   present the illusion of a large, liquid and efficient market -- stocks are
   traded constantly, at marginal price, and each individual trade is small
   compared to the total trading volume.

9. **REQ-9** Relation to the outside world: The values of stocks should be in
   some way related to the outside world so that users have information to base
   trading decisions on.

10. **REQ-10** Player Portfolio: Each player must have separate portfolio that
    gives him/her option to buy/sell new securities, view currently owned
    securities.

11. **REQ-11** Evaluate Portfolios: Securities owned by each player should be
    periodically evaluated and should be updated to their current value.

12. **REQ-12** Advertisements: The website must contain appropriate and
    interesting advertisements relating to finance and stock

13. **REQ-13** Coordinators for Supervision: Users must be able to create
    their own leagues.

14. **REQ-14** Summary Statistics: The website should provide users with a few
    summary statistics about their portfolio -- aggregate value over time,
    which securities have increased in value. The website shouldn't usurp the
    role of deciding strategy for the player; only the most basic of stats
    should be displayed.

15. **REQ-15** Voting: players should be able to up/down-vote each other's
    trades. Vote tallies should be visible to other users.

16. **REQ-16** Commenting: players should be able to comment (via the website
    -- you can already comment on anything via Twitter) on each other's trades.
    Comments should be visible to all users.

17. **REQ-17** Moderation: There should be at least a minimal degree of comment
    moderation so blatantly offensive comments can be removed.

18. **REQ-18** Designing Derivatives: Players should be able to enter into
    contracts with each other that will be enforced by the PitFail system.

19. **REQ-19** Guided designing of derivatives: The website should guide
    players into common formats for derivatives to make it easier for new
    players to figure out.

20. **REQ-20** Rankings: On the website players should be able to see rankings
    of all players by portfolio value (liquid assets only), and by voting
    score.



