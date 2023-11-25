#lifetime of a Veriable in python 

a=10
# Function definition for 'display'
def display():
    # Declare that we are using the global variable 'a' inside the function
    global a    
    # Print the value of the global variable 'a'
    print("Value of a:", a)    
    # Local variable 's' is defined within the function
    s = 20   
    # Print the value of the local variable 's'
    print("Value of b:", s)
# Call the 'display' function
display()