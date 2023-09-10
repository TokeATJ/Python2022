# Toke Atijosan MEOWW#

from cat2 import Cat

def main():
    #Complete the main() method below
    #1. Ask the user to enter the name of the cat
    #2. Create a Cat object using the name provided by the user
    #3. Ask how the user would like to intreact with the cat.
    #   The user can enter 'play' or 'feed'. 
    #   DO NOT use words other than 'play' or 'feed' for input.
    #4. Call the corresponding methods from the Cat class
    #5. Ask if the user would like to continue. If yes, repeat from #3
    #   The user can enter 'y' or 'n'. 
    #   Both uppercase or lowercase y/n should be acceptable.
    
    name = input("Please enter the name of your cat: ")
    cat = Cat(name)
    answer = 'y'
    Y = ["Y", "y"]
    N = ["N", "n"]
    while True:
        if answer in Y:
            task = input("How would you like to interact with " + name + " ? Enter 'play' or 'feed': ")
            if task == "play":
                cat.play()
            elif task == "feed":
                cat.eat()
            else:
                print("INVALID INPUT")
        elif answer in N:
            print ("Goodbye!")
            break
        else:
            print("INVALID INPUT")
        answer = input("Would you like to continue? y/n: ")
            


# Do NOT change any of the lines below
if __name__ == "__main__":
    main()
