print ("Hello world, from python")
print("This is first time")
my_integer = 4
variable_type = type(my_integer)
print(variable_type)
distance_in_meter = 8.4
print(distance_in_meter)
name = 'John'
print(name)
greeting = 'Hello'
print(greeting+'John') 
first = 'There was '
string_part = '1' # 1 is surrounded by quotes, making it a string
int_part = 1 # 1 is standing alone, making it an integer
print(first + string_part)
#print(first + int_part)
print(first + str(int_part))
print(int(4.567))
print(float(5))
print(bool(1))
print(bool('false'))
my_list = ['apple', 'pear', 'orange', 50, 4]
print(my_list)
my_list = ['apple', 'pear', 'orange', 50, 14]
print(my_list[0]) # Lists and tuples are both referenced using square brackets.
print(my_list[2])
my_list = ['apple', 'pear', 'orange', 50, 14]
print(my_list[0:1]) # Prints apple
print(my_list[0:2]) # Prints apple, pear
print(my_list[-1:]) # The last item in the array
print(my_list[:-1]) # Everything except the last item
print(my_list[0:5:2])
print('my_list has ' + str(len(my_list)) + ' entries')
print(my_list[0:len(my_list):2])
user_details = {
"name": "Nico",
"surname": "Loubser",
"age": 68,
"house_number": 68,
"street_name": "Mitchell street"
}
details_list = ["Nico", "Loubser", 68, 68, "Mitchell street"]
print(user_details['name'])
print(user_details.get('name'))
# Initialise 2 variables
age = 100
limit_age = 120
# Do logical comparisons.
print(age == limit_age)
print(age > limit_age)
print(age < limit_age)
set_one = [1, 2, 3, 4, 5]
set_two = set_one
if set_one is not set_two:
    print('Both variables are pointing to the same list object')
else:
    print('Both variables are not pointing to the same listobject')
fruit = ['applee', 'pear', 'orange', 'kiwi']
if 'apple' in fruit:
    print('Apple is in the list')
else:
    print('End jims alga')
number = (1+2)*10
print(number)
print((True or False) and False)
price = 30
money_in_wallet = 25
change_left = 0
if money_in_wallet < price:
    print('You do not have enough money')
elif price == money_in_wallet:
    print('You have the exact amount')
elif money_in_wallet > price:
    change_left = money_in_wallet - price
print('You have ' + str(change_left) + ' left')
number = 0
while number < 10:
    print(number)
    number += 1
students = ('Justin', 'Ron', 'Andy', 'Jonathan')
for name in students:
    print(name)
for name in students:
    if name == 'Ron':
        print('Found Ron')    
map_of_values = {'name': 'Andy', 'surname': 'Bieber', 'marital_status': 'married', 'country': 'Great Britain'}
for key, value in map_of_values.items():
    print(key + ' ' + value)
# The list we will be iterating over.
numbers = [1, 2, 3, 4, 5]
# Function that will be called in the loop
def multiply(amount):
    return amount * 10
# The loop is wrapped in square brackets, and that list is returned to the variable
# called 'results'.
results = [multiply(value) for value in numbers]
# This will contain a new list, where each value in the old list will be multiplied by 10.
print(results)
# people = [ {'name': 'ron', 'position':'middle'},
# {'name':'nico', 'position':'bottom'}, {'name':'andy',
# 'position':'top'} ]
# # One example using continue.
# for person in people:
#     for details_key, details_value in person.items():
#         if person['position'] == 'bottom':
#             continue
#         print details_value
# # One example using break.
# for person in people:
#     for details_key, details_value in person.items():
#         if person['position'] == 'bottom':
#             break
#         print details_value

def name_and_surname(name, surname):
    return 'Your name is ' + name + ' and surname is ' +surname
print(name_and_surname('Nico', 'Loubser'))

import datetime
def calculate_age(year_born) -> int:
    current_year = datetime.datetime.now().year
# This function returns a value. Y
    return (current_year - year_born)
#Here we are calling the function. It returns the age and stores it in the variable
# called 'age'
age = calculate_age(2000)
# Print age to screen
print(age)

def log_error(error, return_data=True):
    if return_data:
        return error
    else:
        print(error)
# Equivalent calls, prints directly to screen
log_error('error message 1')
log_error('error message 2', True)
"""
Returns its variable to the code calling the function, where
you can do more operations on it or in this case, just print it
"""
error = log_error('error message 3', False)
print(error)

