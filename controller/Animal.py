"""This class will be abstract class"""
from abc import ABC, abstractmethod
import datetime

class Animal(ABC):
    """Class Animal defines the characteristics of Animal.
    Animal Will have:
        Type: Herbivorous, carnivorous;
        Color: White,gray, red, black;
        isDomestic: True, False"""
    @abstractmethod
    def __type__(self):
        pass

    @abstractmethod
    def __species__(self):
        pass

    @abstractmethod
    def __age__(self):
        pass

    @abstractmethod
    def __color__(self):
        pass

    @abstractmethod
    def __is_domestic__(self):
        pass

    @abstractmethod
    def __move__(self):
        pass

    @abstractmethod
    def __sound__(self):
        pass

    @abstractmethod
    def __eat__(self):
        pass



class practice_4th_Feb():
    def __init__(self):
        self.object_create_date = datetime.datetime(2024, 2, 3).date()
        self.current_date = datetime.date.today()

    def print_some_text(self):
        self.difference = self.calculate_date_difference()

        print(f"Class was created on {self.object_create_date}")
        print(f"todays date {self.current_date}")        
        print(f"approximately {self.difference} ago.\n\n")

    def calculate_date_difference(self):
        if isinstance(self.object_create_date, datetime.date) and isinstance(self.current_date, datetime.date):
            self.difference = self.current_date - self.object_create_date
            return self.difference
        else:
            print(f"type of self.object_create_date ={type(self.object_create_date)}")
            print(f"type of self.current_date ={type(self.current_date)}")
            raise TypeError("Both object_create_date and current_date should be datetime objects.")


class practice_5th_Feb():

    @staticmethod
    def get_next_date(input_date):
        """Format of date should be 01Jul2024"""
        date = input_date[0:2]
        month = input_date[2:5]
        year = int(input_date[5:])
        months = ["Jan","Feb","Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        if month in ["Jan","Mar", "May", "Jul", "Sep", "Nov", "Dec"]:
            last_date=31
        elif month == "Feb":
            if year%4 == 0:
                last_date=29
            else:
                last_date=28
        else:
            last_date=30

        next_date = int(date)+1
        if next_date > last_date:
            if month == "Dec":
                next_date = 1
                month = months[0]
                year = year + 1
            else:
                next_date = 1
                month_index = months.index(month)
                month = months[month_index+1]

        new_date = f"{next_date}{month}{year}"
        print(new_date)

    def print_anything(self, anyString:str):
        if not anyString:
            anyString = "Anything"

        print(anyString)


if __name__ == '__main__':
    pr = practice_4th_Feb()
    pr.print_some_text()
    print(f"pr id = {id(pr)}")
    five=5
    str = 's'

    print(f"five id = {id('2')}")
    print(f"five id = {id('s')}")
    print(f"str id = {id('2')}")
    print(f"str id = {id('s')}")
    pr5 = practice_5th_Feb()
    pr5.print_anything("29Feb2022")
    practice_5th_Feb.get_next_date("29Feb2022")
else:
    print(f"not called directly. Executed when imported.")
