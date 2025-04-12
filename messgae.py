# def msg(name:str,age): # type annotation in python
#     text = f"""Hello {name}, your current age is {age}."""
#     print(text)


# inp_name = input("Enter your name: ")
# inp_age =  input("Enter your age: ")

# msg(inp_name,inp_age) # positional
# msg(age=inp_age,name=inp_name) # keyword args

def is_present(ali="present", ahmed="prenst", amjad="present"):
    print("ali is",ali,"ahmed is",ahmed,"amjad is",amjad)


# posinational args
is_present("present", "present", "absent")

# kwargs
is_present(amjad="absent")