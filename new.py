# a = "prosp"
# if len(a) > 5 :
#     print("yes")
# # elif len(a) == 5:
# #     print("Accurate")
# else:
#     print("No")

# User_first_name = input("First Name:")
# User_last_name = input("Last Name:")
# print(f"first name: {User_first_name} last name: {User_last_name}") 
# username = (User_first_name + "" + User_last_name)
# if len(username) > 10 :
#     print("Too Long")
# elif len(username) ==  7:
#     print("Accepted")
# elif len(username) < 5 :
#      print("Too Short")



# a ="prosper"
# print(a[::-1])


# User_first_name = input("First Name:")
# User_last_name = input("Last Name:")
# print(f"first name: {User_first_name} last name: {User_last_name}") 
# username = (User_first_name + "" + User_last_name)
# if "a" in username :
#     print("invalid")
# elif "c" in username :
#     print("Not Allowed")
# elif "e" in username :
#     print("Error")
# else :
#     print("Username Saved")

# a = []
# print(type(a))
# print(dir(a))

# a = [1,2,3]
# b = ["mango", "apple", "orange"]
# c = [4,"e"]
# a.append(4)
# a.remove(3)
# a.extend(b)
# print(a)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(x[2:9])
# a = [1, 1, 1, 2, 2, 2, 3, 3, 3,]
# b = set(a)
# print(b)

# a = "prosper"
# b =  list(a)
# print(b)

# a = [2, 3, 4, 5, 8]
# # total = sum(a)
# # print(min(a))

# a = [2, 3, 4, 5, 8]
# last_number = a[-1]
# first_number = a[0]
# a.remove(first_number)
# a.remove(last_number)
# print(a)

# my_dict = {
#     "first_name": "Tobi",
#     "last_name": "idamu",
#     "c": 3
# }
# print(my_dict["first_name"])

# a = [2, 4, 8, 15, 22, 55]
# total = sum(a)
# b = len(a)
# print(total // b)


# num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# for numbers in num:
#     print(numbers*2)



# num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# for numbers in num:
#     print(numbers*2)

for i in range(-10, 0) :
    print(i)

i = 0
while i < 10 :
    print(i)
    i += 1



i = 0 
while i in range(3):
    name = input("name :")
    i += 1

for i in range(10):
    if 1 % 2 == 0:
        print(i)

username = input("User Name:")
for letters in username:
    if letters == "a":
        print("True")
    else:
        print("False")

count = 0
while count < 3:
    question = input("Enter Score:")
    count += 1

while count in range(3):
    question = input("Enter Score:")
    count += 1