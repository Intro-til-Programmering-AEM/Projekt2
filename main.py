from menu_helpers import *
from systems import *
from turtles import *
from warning import *
import sys
import matplotlib.image as img
import matplotlib.pyplot as plt

System = None
N = None
print("Welcome to the Lindenmayer system playground! :D")
while True:
    # Main menu
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        if option == 1:
            print("Which system would you like to see?")
            system_choice = menu(system_options)
            if system_choice is not None:
                # Makes a list of the rightside of system_choice
                System = list(names.keys())[system_choice-1]
                # Calls the systemnames to system
                system = names[System]
            print("Please choose the desired number of iterations:")
            while True:
                n_choice = input_nonNeg_int("N = ")
                if n_choice is not None:
                    N = n_choice
                    # Warning message if N is too high
                    if shouldWarn(system,N)==True:
                        print("N is very high! Are you sure you want to continue with this number of iterations?")
                        # Shows funny image
                        plt.imshow(img.imread('meme.jpg'))
                        plt.show()
                        # yes/no menu
                        warn_choice=menu(warn_options)
                        # Continiues anyway
                        if warn_choice==1:
                            print("Good luck with that!")
                            break
                        # New number of iterations
                        else:
                            print("Please choose another N-value")
                    # Returns to main menu if enter is pressed
                    else:
                        break
                    # Returns to main menu if enter is pressed
                else:
                    break
        elif option == 2:
            if System is not None and N is not None:
                # Plots
                turtlePlot(turtleGraph(LindIter(System, N)))
            else:
                print("Please choose your desired L-system and number of iterations first")
        elif option == 3:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()

