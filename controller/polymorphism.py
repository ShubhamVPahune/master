"""What is Polymorphism: 
    The word polymorphism means having many forms. 
    In programming, polymorphism means the same function name (but different signatures) 
    being used for different types. The key difference is the data types and number 
    of arguments used in function.

    can achieve Polymorphism in python with:
    1] Duck Typing
    2] Operator overloading
    3] Method Overloading
    4] Method Overriding
"""

from multipledispatch import dispatch


class sample1:
    def execute(self):
        print("Achieved polymorphism with Duck Typing from sample1")


class sample2:
    def execute(self):
        print("Achieved polymorphism with Duck Typing from sample2")


class DuckTyping:
    """Duck Typing is a type system used in dynamic languages.
    For example, Python, Perl, Ruby, PHP, Javascript, etc.
    where the type or the class of an object is less important than
    the method it defines. Using Duck Typing, we do not check types at all.
    Instead, we check for the presence of a given method or attribute.

    The name Duck Typing comes from the phrase:

    “If it looks like a duck and quacks like a duck, it’s a duck”
    """

    def try_duck_typing(self, any_obj: any):
        """The object’s type itself is not significant in this
        we do not declare the argument in method prototypes.
        This means that compilers can not do type-checking.
        Therefore, what really matters is if the object has
        particular attributes at run time. Duck typing is hence
        implemented by dynamic languages. But now some of the static
        languages like Haskell also supports it.
        But, Java/C# doesn’t have this ability yet.
        """
        any_obj.execute()


#####################################################################################################


class Student:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self, obj):
        m1 = self.m1 + obj.m1
        m2 = self.m2 + obj.m2

        return Student(m1, m2)


#####################################################################################################
class methodOverloading_way1:
    """Not The Most Efficient Method"""

    def add(self, datatype, *args):
        ans = 0 if datatype == "int" else ""
        for x in args:
            ans = ans + x

        return ans


class methodOverloading_way2:
    """Not the efficient one"""

    def add(self, var1=None, var2=None):
        if var1 and var2:
            return var1 + var2
        elif var1:
            return var1
        else:
            return var2


class methodOverloading_way3:
    """Efficient one

    By Using Multiple Dispatch Decorator

    Multiple Dispatch Decorator Can be installed by:

    'pip install multipledispatch'. We need this installed in order to use it.
    """

    @dispatch(int, int)
    def product(var1, var2):
        return var1 * var2

    @dispatch(int, int, int)
    def product(var1, var2, var3):
        return var1 * var2 * var3

    @dispatch(float, float)
    def product(var1, var2):
        return var1 * var2

    @dispatch(float, float, float)
    def product(var1, var2, var3):
        return var1 * var2 * var3


#####################################################################################################


class testoverriding(methodOverloading_way1, methodOverloading_way2):
    """Method overriding is an ability of any object-oriented programming language
    that allows a subclass or child class to provide a specific implementation of
    a method that is already provided by one of its super-classes or parent classes.
    When a method in a subclass has the same name, same parameters or signature and
      same return type(or sub-type) as a method in its super-class, then the method
      in the subclass is said to override the method in the super-class.
    The version of a method that is executed will be determined by the object t
    hat is used to invoke it. If an object of a parent class is used to invoke the method,
    then the version in the parent class will be executed, but if an object of the
      subclass is used to invoke the method, then the version in the child class will be executed.
      In other words, it is the type of the object being referred to
      (not the type of the reference variable) that determines which
      version of an overridden method will be executed.
    """

    def add(self):
        print("overide add method")
        print("now calling default parent add method")
        print(super().add("int", 4, 2))

        print("now calling specific parent add method.[methodOverloading_way2]")
        print(methodOverloading_way2.add(methodOverloading_way2, 1, 2))


if __name__ == "__main__":

    # Polymorphism using Duck Typing
    # print("Polymorphism using Duck Typing")
    # s1 = sample1()
    # s2 = sample2()
    # duck_type = DuckTyping()
    # duck_type.try_duck_typing(s1)
    # duck_type.try_duck_typing(s2)

    # Polymorphism using Operator Overloading
    # print("Polymorphism using Operator Overloading")
    # s1 = Student(21, 43)
    # s2 = Student(29, 17)
    # s3 = s1 + s2
    # print(s3.m1, s3.m2)

    # Polymorphism using Method Overloading
    # print("Polymorphism using Method Overloading")

    # print("Way 1")
    # way1 = methodOverloading_way1()
    # print(way1.add("int", 2, 3))
    # print(way1.add("int", 2, 3, 4))

    # print("Way 2")
    # way2 = methodOverloading_way2()
    # print(way2.add(2, 3))
    # print(way2.add(5))

    # print("Way 3")
    # way3 = methodOverloading_way3()
    # print(way3.product(2, 3))
    # print(way3.product(2, 3, 2))
    # print(way3.product(2.2, 3.1, 2.5))
    # print(way3.product(2.2, 3.1))

    print("Polymorphism using Method overriding")
    override = testoverriding()
    override.add()
