# Ex-2.4
# ### Validate Pin ###

# Take a input to test if a string is a valid pin or not.

# A valid pin has:
# 	Exactly 4 or 6 characters.
# 	Only numerical characters (0-9).
# 	No whitespace.



def is_valid_pin(pin):
    # Check if the length is 4 or 6 characters
    if len(pin) == 4 or len(pin) == 6:
        # Check if all characters are numerical
        if pin.isdigit():
            return True
    return False

# Test cases
pin1 = input("Enter a PIN: ")
if is_valid_pin(pin1):
    print("Valid PIN")
else:
    print("Invalid PIN")

    
