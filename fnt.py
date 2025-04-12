
# default parameter, agrument with defualt value, keyword arg
# name, age
def full_name(first,last,middle=""):
    if middle:
        name = f"{first} {middle} {last}"
    else:
        name = f"{first} {last}"
    
    print(name.title())
    # return name.title()


#
full_name("M","jinnah","ali") # posinal-args
full_name(first="M",middle="ali",last="jinnah") #kw-args
















# positional args
def fisrt_come_first_serve(one,two,three,four): # order matters
    return one, two, three, four


#tuple unpacking
# default order changed
user_x, user_y, user_z, user_zero = fisrt_come_first_serve(four="ali",three="ahmed",two="amjad",one="bilal") # value->str

print(user_x)
print(user_y)
print(user_z)
print(user_zero)
