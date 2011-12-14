
What goals of PitFail are still unmet?
======================================

What are PitFail's goals?


Definite interfaces for interactions between subsystems have yet to be clearly
defined. This lack of a standard interface bettween 'things' leads to
duplication of effort within the codebase. In particular, the model interface
is extremely adhoc. Their exists one abstraction of the model within the
texttrading/ code (refered to there as "backend"). The website/view/  does
database lookups nearly directly. Java servlets are implimented via a set of
compatability methods within the model/ codebase. A unified interface model
interface has the posibility to provide a clear and simple manner for adding
additional components to the codebase, where each of these compenents interacts
with the model in some way.

The external interfaces exposed by the Java servlets (utilized by the Android
and Facebook applications) lack authorization mechanizms and are thus
unsuitable as web service APIs.
