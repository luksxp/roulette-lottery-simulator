import random

def wnums():
    # Generating random uniqe numbers
    return sorted(random.sample(range(1, 50), 6))

def matching(wnums, user):
    # Matching random and user's numbers
    count = 0   
    while wnums != user:    
        wnums = sorted(random.sample(range(1, 50), 6))
        print(wnums)
        count += 1
    
    if wnums == user:      
        print("Numbers matched")
        print("Number of tries: ", count)        
        
def user_input():
    # entering numbers
    user = list(map(int, input("Enter 6 numbers:").split()))
    matching(wnums, user)
    
user_input()