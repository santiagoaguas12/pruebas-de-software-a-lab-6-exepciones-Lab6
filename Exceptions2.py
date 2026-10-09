class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError:
            print("Error: Invalid input types.")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("Error: Index out of range.")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print("Error: Key not found.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("Error: File not found.")

    def access_attribute(self, obj):
        try:
            print(obj.nonexistent_attribute)
        except AttributeError:
            print("Error: Attribute not found.")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
        except MyException as e:
            print("Custom error:", e)


class MyException(Exception):
    pass

if __name__ == "__main__":

    demo = ExceptionsDemo()

    demo.divide(10, 0)   
    demo.divide("10", 2)  

    demo.access_list([1,2,3], 5)   
    demo.access_list(1, 0)   

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")  
    demo.access_dict("not_a_dict", "b")  

    demo.read_file("text_2.txt") 
    demo.read_file("text.txt") 

    demo.access_attribute(object())  

    try:
        demo.check_positive(-5)
    except MyException as e:
        print(" Custom error:", e)
