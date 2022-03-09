# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# TFarmer,3.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TFarmer,3.6.2022,Modified code to complete assignment 8
    """
    # -- Constructor --
    # product info
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # product name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    # product price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        self.__product_price = float(value)

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + " , " + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> (boolean
        status)

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TFarmer,3.6.2022,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
            print("Data has been saved to " + strFileName)
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep="\n")
        return success_status

    @staticmethod
    def read_data_from_file(file_name):
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(" , ")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__, type(e), sep="\n")
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Interface to allow current file data to be viewed, in addition
     to obtaining product name and price data from the user:

    methods:
        ##save_data_to_file(file_name, list_of_product_objects):

        ##read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TFarmer,3.6.2022,Modified code to complete assignment 8
    """
    @staticmethod
    def print_menu_items():
        print("""
        Menu Options:
        1. Show Current Data
        2. Add A New Product
        3. Save Data To File
        4. Exit The Program
        """)
        print()

    @staticmethod
    def input_menu_options():
        choice = str(input("Please select an option: [1-4] - "))
        print()
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows):
        print("***** Current Products: *****")
        for row in list_of_rows:
            print(row.product_name + " | " + str(row.product_price))
        print("*****************************")

    @staticmethod
    def add_product_data():
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        print()
        prodInfo = Product(product_name=name, product_price=price)
        print(name + " - added to your product list.")
        return prodInfo

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    IO.print_menu_items()
    choice = IO.input_menu_options()
    if choice.strip() == "1":
        IO.print_current_list_items(lstOfProductObjects)
    elif choice.strip() == "2":
        lstOfProductObjects.append(IO.add_product_data())
    elif choice.strip() == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
    elif choice.strip() == "4":
        break

# Main Body of Script  ---------------------------------------------------- #