#!/usr/bin/python3

#exo1
print("Success")

#exo2
fruit = "banana"
quantity = 3
pie_crust = "empty"
isOvenOn = False
print(f"You  have {quantity} {fruit} and the pie  crust  is {pie_crust} , is the  oven on? {isOvenOn}")


#exo3
fruit = "apple"
quantity = 5
pie_crust = "empty"

isOvenOn = True

print(f"You  have {quantity} {fruit} and the pie  crust  is {pie_crust} , is the  oven on? {isOvenOn}")

#exo4
def print_hello_please () :
    print("Hello")
print_hello_please ()

def print_hello_with_my_name_please(myName) :
    print("Hello", myName)
print_hello_with_my_name_please("Pierre")

def  calc_my_age_in_two_years(myCurrentAge):
    print("You are", myCurrentAge, "years  old")
    my_age_in_two_years = myCurrentAge + 2
    return  my_age_in_two_years
my_age_in_two_years = calc_my_age_in_two_years (33)
print("In two years , i'll be",my_age_in_two_years, "years  old")

#exo5
fruit = 'apple'
quantity = '5'
pie_crust = "empty"
isOvenOn = False

def prep_my_fruit(quantity, fruit, pie_crust):
    print("you put", quantity, fruit, "on the crust")
    pie_crust = "filled with delicious apples"
    return (pie_crust)

def turn_over_on(isOvenOn):
    isOvenOn = True
    return(isOvenOn)
pie_crust = prep_my_fruit(3, "apple", "empty")
print("my pie is", pie_crust)
print("Is the oved turned on ?", turn_over_on(isOvenOn))
    
