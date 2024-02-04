from robot.libraries import BuiltIn



def get_suggestions(webelements:list):
    """get_suggestions"""
    suggestions = []
    for element in webelements:
        # print(type(element))
        print(element.text)
        suggestions.append(element.text)

    return suggestions

def read_all_table_details(table_element):
    """read_all_table_details"""

    # find headers

    header_elements = table_element.find_elements("//th[text()]")
    headers = []
    for header in header_elements:
        headers.append(header.text)

    header_elements = table_element.find_elements("//th[text()]")
    header_elements = table_element.find_elements("//th[text()]")

def sqr_generator():
    """
    Doc string for sqr generator
    A Generator in Python is a function that returns an iterator using the Yield keyword. 
    
    Generator Function in Python
    A generator function in Python is defined like a normal function, 
    but whenever it needs to generate a value, 
    it does so with the yield keyword rather than return. 
    If the body of a def contains yield, 
    the function automatically becomes a Python generator function.
    """
    n=0
    while n<10:
        sq = n*n
        n+=1
        yield sq



class SQUARE:
    """An iterator in Python is an object that is used 
        to iterate over iterable objects like lists, tuples, dicts, and sets.

        The Python iterators object is initialized using the iter() method. 
        It uses the next() method for iteration.

        __iter__(): The iter() method is called for the initialization of an iterator. 
        This returns an iterator object

        __next__(): The next method returns the next value for the iterable. 
        When we use a for loop to traverse any iterable object, internally it uses the iter() 
        method to get an iterator object, which further uses the next() method to iterate over.
         
        This method raises a StopIteration to signal the end of the iteration."""
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <=10:
            val = self.num * self.num
            self.num += 1

            return f"\nnum = {self.num}; val = {val}"
        
        else:
            raise StopIteration
        
    
# defining a decorator
def hello_decorator(func):
    """Decorators are a very powerful and useful tool in Python
      since it allows programmers to modify the behaviour of a function or class. 
      Decorators allow us to wrap another function in order to extend 
      the behaviour of the wrapped function, without permanently modifying it.

      First Class Objects
        In Python, functions are first class objects which means that functions 
        in Python can be used or passed as arguments.

        Properties of first class functions:
            A function is an instance of the Object type.
            You can store the function in a variable.
            You can pass the function as a parameter to another function.
            You can return the function from a function.
            You can store them in data structures such as hash tables, lists, …
    """
	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()
