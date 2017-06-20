import sys

import matplotlib.image as img
import matplotlib.pyplot as plt

from menu_helpers import menu, input_nonNeg_int, custom_system_menu
from systems import iterate, names
from turtles import turtleGraph, turtlePlot
from warning import shouldWarn


main_options = ["Choose your Lindenmayer system", "Set the number of iterations", "Generate plots", "Quit"]

system = None
N = None
custom = False
print("Welcome to the Lindenmayer system playground! :D")
while True:
    # Main menu
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        if option == 1:
            print("What kind of system would you like to use?")
            kind_choice = menu(["Predefined", "Custom"])
            if kind_choice == 1:
                print("Which system would you like to see?")
                system_choice = menu(["Koch's curve", "Sierpinski's triangle"])
                if system_choice is not None:
                    system = list(names.values())[system_choice-1]
                    custom = False
            else:
                system = custom_system_menu()
                if system is not None:
                    custom = True
        elif option == 2:
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
                        warn_choice=menu(["Yes", "No"])
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
        elif option == 3:
            if system is not None and N is not None:
                # Plots
                turtlePlot(turtleGraph(iterate(system, N), system if custom else None))
            else:
                print("Please choose your desired L-system and number of iterations first")
        elif option == 4:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()
