PitFail's overall user interface closely resembles the interface depicted in
its mockups: most of the changes were merely cosmetic. Most of the functional
changes are because the current implementation of PitFail is missing features
that were included in the mockup: e.g. companies, leagues, and social
interaction. These changes are grouped into general categories, described in
detail, and justified in the following sections.

Welcome Page for New User
-------------------------
PitFail was originally described as having a "guided registration" process
where the user registers as part of purchasing his or her first stock. While
the user can still explore the stock purchasing interface before logging in,
the current implementation of PitFail does not support this "zero effort"
registration because of a technical limitation. As such, guided messages no
longer are displayed next to each step in the purchasing pipeline:

.. raw:: latex

    \begin{figure}[H]
        \centering
        \includegraphics[height=1.5in]{ui/ui-welcome2}
        \includegraphics[height=1.5in]{ui/actual-welcome}
    \end{figure}

Note that the list of steps is not visible and the current step is not
indicated with an arrow. Some form of guided registration will be implemented
in the next version of PitFail. Thankfully, this doesn't change user effort:
the user simply must login *before* selecting a stock instead of *after*
selecting a stock.

Portfolio Management
--------------------

Perhaps the largest change from the original mockups to the current
implementation is the user's portfolio. This was planned to be displayed as a
single large table containing the all of the user's assets: a combination of
cash, stocks, and derivatives. This design made it difficult to visually
differentiate between types of assets and to locate an asset of interest.

Instead, the portfolio displayed as a "T"-chart, splitting assets and
liabilities into two separate columns. The assets column is further subdivided
by the type of asset: cash, stocks, and derivatives. These subdivisions allow
the user to quickly locate an asset of interest, for example, when selling a
stock. Each column is summarized with a "total" row that estimates the current
value of his or her portfolio by approximating the value of derivatives as if
they were immediately executed. While none of these changes dramatically alter
user effort relative to the mockup, reformatting the portfolio as a "T"-chart
and adding this additional information makes it much easier for a user to view
his or her current assets at a glance:

.. raw:: latex

    \begin{figure}[H]
        \centering
        \includegraphics[width=3in]{ui/ui-portfolio}
        \includegraphics[width=3in]{ui/actual-portfolio}
    \end{figure}

Besides the changes to the table of assets, there are clearly several features
missing from the implementation: (1) historic portfolio performance, (2)
multiple portfolios, and (3) league navigation. These missing interface
elements will be restored after companies, leagues, and logging of historic
prices are implemented in the next iteration of PitFail.

Buying Stocks
-------------
Purchasing stocks is one of the fundamental activities on PitFail. The
interface for buying stocks is very similar to the interface shown in the
original mockups: when the user enters a valid ticker symbol in the large
search bar, a small stock quote expands below the search bar. This quote
includes a few statistics about the stock's daily performance and a graph of
the stock's performance over time.

.. raw:: latex

    \begin{figure}[H]
        \centering
        \includegraphics[width=3in]{ui/ui-buy}
        \includegraphics[width=3in]{ui/actual-buy}
    \end{figure}

Unlike the original mockup, the options for interacting with the stock are not
embedded in the stock quote. Instead, they are displayed in a dedicated section
of the webpage. This extra space is used to display a short description of
stock trading and helps guide new users through the process: something that
will be even more important once options are supported. While the original
mockups allowed the user to enter an amount in either shares or dollars, this
was found to be confusing and was removed in the current version of the user
interface.

Neither of these changes do not considerably effect user effort.

Trading Derivatives
-------------------

If the user clicks the "add to derivative" button instead of the "buy stock"
button, he or she is presented with the derivative offering page. In the
original mockups this was shown as a prose-like description of a derivative
with a number of blanks. Originally intended to guide the user through the
derivative creation process, this was found to be unfeasible with the number of
derivative configuration options supported in PitFail. As such, this was
redesigned to resemble a traditional form: a prose description followed by a
table of input fields.

.. raw:: latex

    \begin{figure}[H]
        \centering
        \includegraphics[width=3in]{ui/ui-derivative}
        \includegraphics[width=3in]{ui/actual-derivative}
    \end{figure}

Once the derivative has been created it can either be offered to a specific
user or to a public auction. If a buyer is specified, that user is prompted to
accept or decline the offer using a special form in his or her portfolio. If
the derivative is offered to a public auction, a link to the auction page is
added to the sidebar and other users have an opportunity to bid. These features
were not included in the mockups, so see the User Effort Estimation section
below for a detailed usability analysis.

Social Features
---------------
PitFail's original mockups included a real-time newsfeed at the bottom of every
page. This news feed was a log of trading history and served as a hub for social
interaction between users. A limited implementation of this newsfeed is
included in the current version of PitFail. Unlike the mockup, the newsfeed is
included in every page's sidebar instead of the footer. This is similar to the
real-time feed that was recently added to Facebook and will be familiar to the
majority of PitFail's users.

.. raw:: latex

    \begin{figure}[H]
        \centering
        \includegraphics[height=2in]{ui/ui-newsfeed}
        \includegraphics[height=2in]{ui/actual-newsfeed}
    \end{figure}

Besides the different location, much of the functionality displayed in the
mockups has not yet been implemented. Notably, this includes: (1) user-specific
newsfeeds, (2) voting, (3) commenting, (4) messages for derivative trades, and
(5) messages for a users going broke. These features will be implemented in the
next version of PitFail and do not effect user effort.

