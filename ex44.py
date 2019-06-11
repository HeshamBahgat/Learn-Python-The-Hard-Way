class Parent():
    def order_must_do(self):
        print("Home work")


class Mother():
    def order_have_do(self):
        print("take out the trash")


class Son(Parent, Mother):
    def I_dont_understand(self):
        super(Son, Mother, Parent)
        print("After super")


he = Son()

he.order_must_do()
he.order_have_do()

#---------------------------------------------------------------

class Other(object):

    def override(self):
        print("OTHER OVERIDE()")

    def implicit(self):
        print("OTHER IMPLICIT()")

    def altered(self):
        print("OTHER ALTERED()")

class Child(object):

    def __init__(self):
        self.other = Other()
    def imilicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE OTHER ALTERED()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

SON = Child()
SON.implicit()
SON.override()
SON.altered()
