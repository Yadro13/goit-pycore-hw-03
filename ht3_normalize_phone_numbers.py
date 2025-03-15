import re

pattern = r"\D" # everything except for digits

# Normalize phone number to the standard international format started from + and with numbers only
def normalize_phone(phone_number: str) -> str:
    
    phone = re.sub(pattern, "", phone_number) # Remove all symbols except for digits
    
    # Check if number is too short - NOT OK
    if len(phone) < 10: 
        print(f"Wrong phone number: {phone_number} because has only {len(phone)} digits")
        return
    
    # Check if number is 10 digits and starts not from 0 - NOT OK
    elif (len(phone) == 10) and (phone[0] != '0'): 
        print(f"Wrong mobile operator code: {phone[:3]}")
        return
    
    # Check if number is 10 digits and starts from 0 - OK!
    elif (len(phone) == 10) and (phone[0] == '0'):
        phone = "+38" + phone # Adding "+38" to start with
    
    # Check if number is 12 digits and starts from 3 - OK!
    elif (len(phone) == 12) and (phone[0] == '3'):
        phone = "+" + phone # Adding "+"" to start with

    # Check if number is 12 digits and starts not from 3 - NOT OK!
    elif (len(phone) == 12) and (phone[0] != '3'):
        print(f"Sorry, this phone: {phone} is not from Ukraine, it's forbidden!")
        return

    else:
        print(f"Wrong phone number: \"{phone_number}\" - incorrect format")
        return
    
    return phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Test additional cases
good_phone = normalize_phone(" 123-32-34")
if good_phone:
    print(good_phone)

good_phone = normalize_phone(" (666) 123-32-34")
if good_phone:
    print(good_phone)

good_phone = normalize_phone(" + 48 (097) 123-32-34")
if good_phone:
    print(good_phone)

good_phone = normalize_phone("    sdf234550)1,,,678423-32-34")
if good_phone:
    print(good_phone)

good_phone = normalize_phone("    12345678910")
if good_phone:
    print(good_phone)
        
        
