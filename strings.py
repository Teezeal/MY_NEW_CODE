


Color = "blue, green, yellow"
print(Color)

###String Concatination###

First_name = "Tobi"
Last_name = "Taiwo"
print(First_name + " " + Last_name)

### String Interpolation ###

x = 10
print(f"The valuie of x is {x}")

name = input("Tell us you name: ")
what_year_were_born = int(input("Tell us your birth yeear "))
recent_year = 2022

age = recent_year - what_year_were_born 

print(f"welcome, {name}. We can see that you are {age} years old. ")

### Indexing and String Slicing ### 

b = "I am just good you know"
#print(b[2])
#print(b[7])
#print(b[5:9])
print(b[0:4] + " " + b[10:14])

##Username Generator###

User_first_name = input("What is your first name ")
User_last_name = input("What is your last name")
print(f"First name: {User_first_name}. Last Name: {User_last_name}")
user_name = (User_last_name[:4] + "" + User_first_name[-3:])
print(user_name)

##Method###


my_name = "Tobi"
print(my_name.upper())

Yo = "I am a boy"
#print(Yo.find("a"))
# print(Yo.rfind("a"))
# print(Yo.rfind("k"))
print(Yo.count("a"))

brand = "Toby"
print(brand.replace("T", "33"))

x = "I am a good boy"
print(x.split())

x = "I am, a good boy"
print(x.split(","))

