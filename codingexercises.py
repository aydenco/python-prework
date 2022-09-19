# Question 1
def hello_name(user_name):
    """Say hello to each user"""
    print("Hello, " + user_name + "!")

# Test
hello_name("Ayden")

# Question 2
def first_odds():
    """Print every odd number between 1 and 100"""
    numbers= range(0,100)
    for num in numbers:
        if num < 100:
            if num % 2 == 1:
                print(num)

# Test
first_odds()

# Question 3
def max_num_in_list(a_list):
    """Return last number in list"""    
    print(a_list[-1])

# Test
ex_list = [1, 2, 3, 4, 5]

max_num_in_list(ex_list)

# Question 4
def is_leap_year(a_year):
    """Determine if given year is a leap year"""
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 100 != 0 and a_year % 400 == 0:
        return True
    else:
        return False

# Test
print(is_leap_year(2020))
print(is_leap_year(2022))

# Question 5
def is_consecutive(a_list):
    """Determine if a list of numbers is consecutive"""
    # I am completely stumped on this one.