Several of the most common usage scenarios for the PitFail website are
evaluated below. In particular, note that common scenarios (e.g. buying a
stock) are much easier to perform than rare scenarios (e.g. creating a new
league):

====================================  ======  ==========
Usage Scenario                        Clicks  Keystrokes
====================================  ======  ==========
purchase a stock                      3       7
create a derivative                   4       27
act on a pending derivative offer*    1       1
bid on a derivative auction*          4       5
close a derivative auction*           1       1
sell a stock                          3       2
create a new league                   n/a     n/a
modify an existing league             n/a     n/a
invite a user to a league             n/a     n/a
====================================  ======  ==========

Features that are not currently implemented are shown as empty rows and actions
that have been added since the original mockups are marked with asterisks. Both
these new usage scenarios and existing usage scenarios that were modified are
analyzed in detail below. This includes buying and selling stocks because of
the lack of league support in the current version of PitFail.

Purchase a Stock
................

Assume the user wishes to purchase 10 shares of Google stock. The user must:

- **Navigation:** total of one click, as follows

 1. Click on "login".

- **Data Entry:** total of two clicks and seven keystrokes, as follows

 1. Click on the "enter a ticker symbol" text field.
 2. Press the keys "G", "O", "O", and "G".
 3. Press "enter" to load the quote.
 4. Press the keys "1" and "0" to specify 10 shares.
 5. Click the "buy" button to confirm the purchase.

Note that the user could press "enter" instead of clicking the "buy" button.

Creating a Derivative
.....................

Assume the user wishes to offer a call option to Bucky that includes 10 shares
of Google stock and expires on December 25, 2011. This option costs $1000 to
begin active and one can buy the shares for $10,000 if and only if the market
rate for Google stock is greater than $1000 per share. The user must:

- **Navigation:** total of one click, as follows

 1. Click on "login".

- **Data Entry:** total of 3 clicks and 27 keystrokes, as follows

 1. Click on the "enter a ticker symbol" text field.
 2. Press the keys "G", "O", "O", and "G".
 3. Press the "enter" key to load the quote.
 4. Press the keys "1" and "0" to specify 10 shares.
 5. Click the "add" button to begin creating a derivative.
 6. Press the "B", "u", "c", "k", and "y" keys to enter the recipient's name.
 7. Press "tab" to move to the "premium" field.
 8. Press the keys "1", "0", "0", and "0" to enter $1000.
 9. Press "tab" to move to the "expiration date" field.
 10. Press the "1", "2", "/", "2", and "5" keys to select December 25th of the current year.
 11. Press "tab" to move to the "strike price" field.
 12. Press the "1", "0", "0", "0", and "0" keys to enter $10000.
 13. Click on the "Propose Contract" button to complete the transaction.

Sell a Stock
............

Assume the user wishes to sell 10 shares of Google stock from his or her Global
League. The user must:

- **Navigation:** total of one clicks, as follows

 1. Click on "login".

- **Data Entry:** total of two clicks and two keystrokes, as follows

 1. Click on the text input in the row corresponding to Google.
 2. Press the keys "1" and "0" to specify 10 shares.
 3. Click the "sell" button to confirm the purchase.

Note that the user could press "enter" instead of clicking the "sell" button.


Act on Derivative Offer
.......................

Assume the user wishes to accept a derivative that was directly offered to him
or her:

- **Navigation:** total of one click, as follows

 1. Click on "login".

- **Data Entry:** total of one click, as follows

 1. Click on the "accept" button next to the correct derivative.

Bid on Derivative
.................

Assume the user wishes to bid $50,000 on a derivative that is being sold in a
public auction:

- **Navigation:** total of two clicks, as follows

 1. Click on "login".
 2. Click on the correct derivative link in the sidebar.

- **Data Entry:** total of two clicks and five keystrokes, as follows

 1. Click on the "your bid" field.
 2. Press the keys "5", "0", "0", 0", and "0".
 3. Click the "Cast Bid" button.

Close Derivative Auction
........................

Assume the user wishes to close an auction that he or she posted:

- **Navigation:** total of one click, as follows

 1. Click on "login".

- **Data Entry:** total of one click, as follows

 1. Click on the "close" button next to the correct auction.
