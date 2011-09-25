
Association Definitions
~~~~~~~~~~~~~~~~~~~~~~~

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

