import random 

# Generates required sorted amount of random numbers within provided range
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    numbers = [] # Init empty list to store numbers

    if (min >= 1) and (max <= 1000) and (min <= quantity <= max): # check entry parameters
        while len(numbers) < quantity: # Add random numbers to the list until it's full
            random_number = random.randrange(min, max + 1) # Generate random number in the range
            if random_number not in numbers: 
                numbers.append(random_number) # If not in list, add number to the list
        numbers.sort() # sort the list
    
    return numbers

# Test 5 different cases:
print(get_numbers_ticket(1,49,6))
print(get_numbers_ticket(1,36,5))
print(get_numbers_ticket(1,36,-1))
print(get_numbers_ticket(0,36,5))
print(get_numbers_ticket(1,1001,5))