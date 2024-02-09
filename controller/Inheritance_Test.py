class parent_class:
    class_variable = "parent_class"

    def __init__(self) -> None:
        print("init method of parent_class")
        self.var1 = 2
        self.var_parent1 = 0
        self.var_parent2 = 1
        self.var_parent3 = 5
        self.var2 = 4
        self.var3 = 6
        self.__private_var1 = 100  # private variable.

    def __repr__(self) -> str:
        stmnt = "repr method of parent_class"
        return stmnt

    def __str__(self) -> str:
        stmnt = "str method of parent_class"
        return stmnt

    def feature_one(self) -> None:
        print("instance method of parent_class")

    def feature_parent(self) -> None:
        print("feature_parent method of parent_class")

    def feature_two(cls) -> None:
        print("class method of parent_class")

    def print_private_vars(self):
        print(f"__private_var1 = {self.__private_var1}")

    @staticmethod
    def feature_three() -> None:
        print("static method of parent_class")


class child_class():
    class_variable = "child_class"

    def __init__(self) -> None:
        print("init method of child_class")
        super().__init__()
        self.var1 = 8
        self.var2 = 10
        self.var3 = 12

    def __repr__(self) -> str:
        stmnt = "repr method of child_class"
        return stmnt

    def __str__(self) -> str:
        stmnt = "str method of child_class"
        return stmnt

    def instance_method(self) -> None:
        print("instance method of child_class")

    def class_method(cls) -> None:
        print("class method of child_class")
        cls.class_variable = "updated class vairable"

    @staticmethod
    def static_method() -> None:
        print("static method of child_class")


class LearnMRO(child_class,parent_class):
    """Method Resolution Order :
    Method Resolution Order(MRO) it denotes the way a programming language resolves a 
    method or attribute. Python supports classes inheriting from other classes. 
    The class being inherited is called the Parent or Superclass, while the class 
    that inherits is called the Child or Subclass. In python, method resolution order 
    defines the order in which the base classes are searched when executing a method. 
    First, the method or attribute is searched within a class and then it follows 
    the order we specified while inheriting. This order is also called Linearization 
    of a class and set of rules are called MRO(Method Resolution Order). 
    While inheriting from another class, the interpreter needs a way to 
    resolve the methods that are being called via an instance. 
    Thus we need the method resolution order.
    """

    def __init__(self) -> None:
        super().__init__()
        print("In LearnMRO class")

    def print_var1(self):
        print(self.var1)

    def call_instance_method_of_parent(self):
        super().instance_method()

if __name__ == "__main__":

    lmro = LearnMRO()
    lmro.print_var1()
    lmro.call_instance_method_of_parent()





    # child_class_obj = child_class()

    # print(f"child_class_obj.var1 = {child_class_obj.var1}")
    # print(f"child_class_obj.var2 = {child_class_obj.var2}")
    # print(f"child_class_obj.var3 = {child_class_obj.var3}")
    # print(f"child_class_obj.var_parent1 = {child_class_obj.var_parent1}")
    # print(f"child_class_obj.var_parent2 = {child_class_obj.var_parent2}")
    # print(f"child_class_obj.var_parent3 = {child_class_obj.var_parent3}")
    # child_class_obj.print_private_vars()
    # print(f"child_class_obj.__private_var1 = {child_class_obj.__private_var1}") # cannot access private var of parent

    # print(child_class_obj)
    # print(repr(child_class_obj))
    # print("==================================\n")

    # child_class_obj.feature_one()
    # child_class_obj.feature_two()
    # child_class_obj.feature_three()
    # child_class_obj.feature_parent()
    # print("==================================\n")

    # child_class_obj.static_method()
    # child_class_obj.instance_method()
    # print("==================================\n")

    # child_class_obj2 = child_class()
    # print("==================================\n")
    # print(f"child_class_obj class variable = {child_class_obj.class_variable}")
    # print(f"child_class_obj var1 variable = {child_class_obj.var1}")
    # print(f"child_class_obj2 class variable = {child_class_obj2.class_variable}")
    # print(f"child_class_obj2 var1 variable = {child_class_obj2.var1}")
    # print("==================================\n")
    # child_class.class_method(child_class)
    # print("==================================\n")

    # print(f"child_class_obj class variable = {child_class_obj.class_variable}")
    # print(f"child_class_obj var1 variable = {child_class_obj.var1}")
    # print(f"child_class_obj2 class variable = {child_class_obj2.class_variable}")
    # print(f"child_class_obj2 var1 variable = {child_class_obj2.var1}")
