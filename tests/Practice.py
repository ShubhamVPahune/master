# from controller.Animal import practice_4th_Feb

class Practice():
    """
    Instance Variable: 
        It is basically a class variable without a static modifier and is usually shared by all class instances. 
        Across different objects, these variables can have different values. 
        They are tied to a particular object instance of the class, therefore, 
        the contents of an instance variable are totally independent of one object instance to others.


    Class Variable: 
        It is basically a static variable that can be declared anywhere at class level with static. 
        Across different objects, these variables can have only one value. 
        These variables are not tied to any particular object of the class, 
        therefore, can share across all objects of the class.
    """

    lastname = "PAHUNE"
    def __init__(self, name) -> None:
        """
        self in Python class
            Self represents the instance of the class. 
            By using the “self”  we can access the attributes 
            and methods of the class in Python. 
            It binds the attributes with the given arguments. 
            The reason you need to use self. is because 
            Python does not use the @ syntax to refer to instance attributes. 
            Python decided to do methods in a way that makes the 
            instance to which the method belongs be passed automatically, 
            but not received automatically: 
            the first parameter of methods is the instance the method is called on.

        What is the use of self in Python?
            When working with classes in Python, 
            the term “self” refers to the instance of the class that is currently being used. 
            It is customary to use “self” as the first parameter in instance methods of a class. 
            Whenever you call a method of an object created from a class, 
            the object is automatically passed as the first argument using the “self” parameter. 
            This enables you to modify the object’s properties and execute tasks unique to that particular instance.
        """
        
        self.name = name

    @classmethod
    def return_lastname(cls):
        """The @classmethod decorator is a built-in function decorator that is an 
        expression that gets evaluated after your function is defined. 
        The result of that evaluation shadows your function definition. 
        A class method receives the class as an implicit first argument, 
        just like an instance method receives the instance """

        return cls.lastname
    
    @staticmethod
    def print_info():
        """A static method does not receive an implicit first argument. 
        A static method is also a method that is bound to the class 
        and not the object of the class. This method can’t access or 
        modify the class state. It is present in a class because it 
        makes sense for the method to be present in class."""

        print("This is the usage of static method")

    @staticmethod
    def test_lambda_function():
        """Lambda Functions:
                A lambda function is a small anonymous function.

                A lambda function can take any number of arguments, 
                but can only have one expression."""
        average= lambda a,b,c: (a+b+c)/3
        print(f"average = {average(3,3,3)}")  

if __name__ == '__main__':
    # pr = practice_4th_Feb()
    # pr.print_some_text()
    # print(f"pr id = {id(pr)}")
    # five=5
    # str = 's'

    # print(f"five id = {id('2')}")
    # print(f"five id = {id('s')}")
    # print(f"str id = {id('2')}")
    # print(f"str id = {id('s')}")

    # pr = Practice("shubham")
    # pr2 = Practice("shital")
    # print(f"pr firsname = {pr.name}")
    # print(f"pr lastname = {pr.lastname}")

    # print(f"pr2 firsname = {pr2.name}")
    # print(f"pr2 lastname = {pr2.lastname}")
    # print("\n---------------\n")
    # Practice.lastname = "pahune"
    # print(f"pr2 firsname = {pr2.name}")
    # print(f"pr2 lastname = {pr2.lastname}")
    # print(f"pr firsname = {pr.name}")
    # print(f"pr lastname = {pr.lastname}")
    # print("\n---------------\n")
    # Practice.lastname = "PAHUNE"
    # # pr2.lastname = "PAHUNE2"
    # print(f" used class method . and here is the return value = {Practice.return_lastname()}")

    print("\n---------------\n")
    # Practice.print_info()

      

else:
    print(f"not called directly. Executed when imported.")