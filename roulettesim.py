import random

def random_numbers():
    # generating random numbers
    return random.randint(0, 36)  
    
def matching(user, winnums, money):
    # matching user's and random numbers
    # calculating number of tries and financial result
    count = 0
    while user != winnums:
        winnums = random.randint(0, 36) 
        print(winnums)
        count += 1
    if user == winnums:
        print("Win")    
        print("Number of tries:", count)
        print("Money flow:", (money * 35) - (count * money))
        
def user_numbers():
    # user's numbers
    user = int(input("Enter one number form 1 to 35:"))
    money = int(input("Enter value of 1 bet in dollars:"))
    winnums = random_numbers()
    matching(user, winnums, money)
    
user_numbers()