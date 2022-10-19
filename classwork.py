from time import time


x = (4 - 5) / 2
print(x)

# Exercise 1.2

#Q1

A_minute = 60

Minutes = 42

x = A_minute*Minutes

print(x)

Result_in_seconds = x + 42

print(Result_in_seconds)


A_mile = 1.6
Result_in_miles = 10 / 1.6

print(Result_in_miles)


# convert t = 42:42 to minutes and seconds
m = 42 + (42 / 60)
print(m)
s = (42 * 60) + 42
print(s)
h = m / 60
print(h)

In_terms_of_miles_and_minutes = Result_in_miles / m
print(In_terms_of_miles_and_minutes)

in_terms_of_miles_and_seconds = Result_in_miles / s
print(in_terms_of_miles_and_seconds)

in_terms_of_hours = Result_in_miles / h
print(in_terms_of_hours)


# Exercise 2.2

# Q1

r = 5
pi = 3.142

Volume_of_a_sphere = 4/3 * 3.142 * r**3
print(Volume_of_a_sphere)

#Q2

Book_price = 24.95
discount = Book_price * (40/100)
print(discount)

discount_price = Book_price - discount
print(discount_price)

shipping = 3 + (0.75 * (60-1))
print(shipping)

wholesale = discount_price * 60 + shipping
print(wholesale)

#Q3

start_time = (6*60 + 52) *60
easy_pace = (8*60 + 15) *2
tempo_pace = (7*60 + 12) *3

run_time = easy_pace+tempo_pace

home_time = start_time+run_time

break_fast_hour = home_time//3600
break_fast_min = (home_time%3600) // 60
break_fast_sec = (home_time%3600) % 60

print(f"{break_fast_hour}:{break_fast_min}:{break_fast_sec}am")


