# ### String Con

First_name = "John"
Last_name = "Doe"
print(First_name + " " + Last_name)

# ### String Interpolation ###

x = 10
print(F"The value of x {10}")

Name = input("Tell us your name: ")
what_year_were_born = int(input("Tell us your birth yeear "))
recent_year = 2022

age = recent_year - what_year_were_born 

print(f"welcome, {Name}. We can see that you are {age} years old. ")

# ### Indexing and Strings Slicing ###

Yo = "I Love the pussy juicy"
print(Yo[:6] + " " + Yo[11:16])

# ### Username Generator ###

User_first_name = input("First Name:")
User_last_name = input("Last Name:")
print(f"first name: {User_first_name} last name: {User_last_name}") 
user_name = (User_first_name[:4] + User_last_name[-4:])
print(user_name) 

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for numbers in num:
    print(numbers)



num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for numbers in num:
    print(numbers*2)

name = "Waris"
email = f"""
Hello {name}, 
How are you doing today ?
Hope you had a good time smoking?

"""
print(email)


### Logical Operator ###

print(10 > 5 and 1 < 3 and "A" == "A")  # all expression must be true when using "and" logical Operator
print(10 > 5 or 1 > 3 or "A" == "A")  # at least one expression must be true 
print(not("James" == "Maria"))

    #### Assignment Operator ###

number = 3
number += 2  # any arithmetic operation can be use * - and the likes 
print(number)

# ### If Statements ###

number = 0
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(number)
else:
    print(f"{number} is negative")


# Ternary If Statement ###   #it should only be used if you have one IF and Else

number = 10
message = "positive" if number > 0 else "0 or negative"
print(message)

# Set Union / Intersection / Differences

lettersA = {"A", "B", "C", "D", "E"}
lettersB = {"A", "F", "G", "S", "C"}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"Union {union}")
print(f"Intersection {intersection}")
print(f"Differnce {difference}")

### Dictionaaries ###
person = {
    "name" : "Jamal",
    "age" : 20,
    "address" : "USA"
}
print(person["name"])
print(person["age"])
print(person["address"])
print(person.values())
print(person.keys())
person["age"] = 45
print(person)



a ="prosper"
print(a[::-1])

a = [1, 1, 1, 2, 2, 2, 3, 3, 3,]
b = set(a)
print(b)


a = []
print(type(a))\
