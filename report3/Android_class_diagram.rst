Android Client class Diagram 
===============================

.. figure:: figures/class-diagrams/android
    :width: 60%

The class Diagram for Android Client consists of five classes.

1. HomeScreen - Creates the homescreen for the user on the android clients when he logs in. The user can
  then navigate to all the other features via this class.

2. BuyDetail - Gives user all the information about a particular stock as choser by him from the HomeScreen and
  gives an option of buying that stock.

3. PollingService -  Creates a background service to get stock updates from server. It is trigerred from the Homescreen Class.

4. PortfolioDetail - Provides the portfolio detail of any portfolio which belongs to the user

5. NewTeam - This class creates a new Team/Portfolio for the user where he can invite new users.

6. LeaderBoard - Displays the default Leader Board for the PitFail System

