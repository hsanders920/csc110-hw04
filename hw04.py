# ------------------------------------------------------
#        Name: Hannah Sanders
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys
#define secret word (can be anything)
secret_word = "food"


# Task 1
def check_text():
    """ This function prompts the user to input a sentence and checks to see w
    whether the secret word or the word dog is within the sentence. If not, then the
    user is prompted again until they guess correctly"""
    
    stop= False #flag for while loop
    
    while not stop:
        sent = (input("sentence: ")).lower()
        if secret_word in sent:
            stop = True
            print("You used the secret word!")
        elif "dog" in sent:
            stop = True
            print("You used the word \"dog\" or the word \"Dog\"!")
        else:
             print("Try again")
             # boolean is not changed so function continues
            
        
    

        

   
    


# Task 2
def check_greater():
    """ This function prompts the user to provide an integer.
    as long as both inputs are the same, the loop will continue.
    If the inputs are different, then the values of the two integers are compared.
    If int1>int2 then it prints " First is Greater" and if int2>int1, it prints
    "Second is Greater" """
    
    int1 = int(input("give me a first integer:"))
    int2 = int(input("give me a second integer:"))

    while int1==int2: #only if both are equal then the loop is entered
        print("Try again") 
        int1 = int(input("give me a first integer:"))
        int2 = int(input("give me a second integer:"))
        
    if int1>int2:
        print("First is Greater")
        
    elif int2>int1:
        print("Second is Greater")





# Task 3
def get_special_numbers():
    """ This function checks each number between 1 and 40. If the number is
    odd (or num%2 is 1), a multiple of 3( or num % 3 is 0) and, not a
    multiple of 5 (if num%5 is not zero), then the number prints"""
    for num in range (1,41):
        if (num%2==1):
            if (num%3 ==0):
                if (num%5 != 0):
                    print (num)
    


# Task 4.a
def my_for_loop():
    '''This function creates a list of vowels and constontants. It then
    prompts the user for a string. If the string is between 2-5 charecters
    and has no spaces between charecters, then each charecter is checked to
    see whether it is a vowel or a constonant. If these conditions are not met
    then "bad word" is printed and the function is returned'''
    vowels= ["a","e","i","o","u"]
    #creates a list of vowels
    constontants= ["b","c","d","f","g", "h", "j", "k","l","m","n","p","q","r","s","t","v","w","x","z"]
    #creates a list of constonants 

    while True:
        string = input("Give me a string:")
        x = len(string)
        if not 2<=x<=5:
            print("bad word")
            return ()
        

        elif " " in string:
            print("bad word")
            return ()
           
        break # if this point is reached then function can continue on
    
    for char in string:
        if char in vowels:
            print( char, "is a vowel")
        else: # if not a vowel, then a constonant
            print(char, "is a consonant")
    
        

# Task 4.b
def my_while_loop():

    """ This function prompts the user to input either "a", "b", or 'c"
    if a is chosen, then the menu is repeated. If b is chosen then
    "goodbye" is printed and the function is returned, if c is chosen then the
    program exits"""

    let = input("Choose one option: a, b, or c:")
    while True:
        if let == 'a':
            let = input("Choose one option: a, b, or c:")
            
        elif let == 'b':
            print ("Goodbye")
            break
        
        elif let == 'c':
            exit ()
        else:
            print("try again")
            let = input("Choose one option: a, b, or c:")
           
            
            
    

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

