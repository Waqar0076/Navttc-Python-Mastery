# scope of a function
# global variable.

result_global = 10

def home(num1, num2):
    result_local = num1 + num2    # local variable
    print(f"Local Result inside {result_local}")  # accesable only inside the function
    print(f"Global Result inside {result_global}") # accesable every where

    def room():
        secret_variable = "Top Secert"
        print("global in secret room", result_global)
        print("local in secret room", result_local)
        print("secert in secret room", secret_variable)
    
    print("secert in home", secret_variable)

home(10, 20)   # local variable

print(result_global, "Outside") # global variable
print(result_local, "Outside")