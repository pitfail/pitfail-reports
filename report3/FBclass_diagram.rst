FaceBook class Diagram 
=======================

.. figure:: class-diagrams/FB/class.png
    :width: 60%

The class diagram has only one class as all the Facebook client controller methods are inside one class.
As mentioned earlier, The class mainly includes the methods:
-- FBListener : Listens to the PitFail page wall for new incoming requests.
-- ParseMessage : Parses the user request, checks the request for the syntax and creates tokens to be passed as arguments to server methods.
-- RestFB APIs : these APIs help in retrieving the wall posts and posting the response on wall posts.


