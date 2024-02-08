class Object_chaining:
    def __init__(self, data):
        self.__obj = data

    def __repr__(self):
        return f"{self.__obj}"

    def get_data(self):
        return self.__obj
    

    def str_to_list(self, delimeter:str=","):
        try:
            self.__obj = self.__obj.split(delimeter)
            return self
        except TypeError as err:
            print(err)

    def list_to_str(self, delimeter:str=","):
        try:
            self.__obj = f"{delimeter}".join(self.__obj)
            return self
        except TypeError as err:
            print(err)
    
    def convert_numbers_to_its_square(self):
        is_string = isinstance(self.__obj, str)
        if is_string:
            self.str_to_list()
                    
        sqr_list = []
        for item in self.__obj:
            sqr = str(int(item)*int(item))
            sqr_list.append(sqr)

        if is_string:
            self.__obj = f",".join(sqr_list)
        else:
            self.__obj = sqr_list

        return self

if __name__=="__main__":
    string = "1,2,3,4,5,6"
    t_s = Object_chaining(data=string)
    print(t_s)
    print(t_s.str_to_list())
    print(t_s.list_to_str().str_to_list())
    print(t_s.convert_numbers_to_its_square())
    print(t_s.list_to_str().convert_numbers_to_its_square())
    print(t_s.str_to_list().list_to_str().convert_numbers_to_its_square())