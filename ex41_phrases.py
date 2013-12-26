class: creates a new blueprint
object: creates the most basic object from a blueprint, and any instance of an
object
instance: what a spawned object is called
def: how you define functions inside a class
self: inside functions in a class, a variable for the instance/object being
accessed
inheritance: the concept that one class can inherit traits from another
composition: concept that a class can be composed of other classes as parts
attribute: a property classes have that are from composition, usually variables
is-a: a phrase to say that something inherits form another
has-a: a phrase to say that something is composed of other things or has a
trait

class X(Y)
    makes a class named X that is-a Y
class X(object): def__init__(self, J)
    class X has-a__init__that takes self and J parameters
class X(object):def M(self,J)
    class X has-a function named M that takes self and J parameters
foo = X()
    set foo to an instance of class X
foo.M(J)
    from foo get the M function, and call it with parameters self, J
foo.K = Q
    from foo get the K attribute and set it to Q


