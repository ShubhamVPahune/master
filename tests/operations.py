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
    """Doc string for sqr generator"""
    n=0
    while n<10:
        sq = n*n
        n+=1
        yield sq



class SQUARE:
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
