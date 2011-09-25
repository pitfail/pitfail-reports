
Attribute Definitions
~~~~~~~~~~~~~~~~~~~~~

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

