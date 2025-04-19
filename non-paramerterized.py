# Non-Perameterized Functions
def greet():
    # function definition/statement
    print(f"Hello! we're learning Python....")

# functions calling
# greet()
# print("Aptech learning")
# greet()


count = 0

def count_increment():
    global count
    count+=1
    # count = count + 1


def reset_count():
    global count
    count = 0

def print_count():
    print(f"Count value is {count}")


# count_increment()
# count_increment()
# print_count()
# count_increment()
# print_count()
# reset_count()
# print_count()


from datetime import date

def current_date():
    today = date.today()
    print(f"Today's date {today}")

# current_date()


def add_numbers():
    num1 = 10
    num2 = 10
    result = num1 + num2
    print(result)

add_numbers()