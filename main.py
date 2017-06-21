import sys

import matplotlib.image as img
import matplotlib.pyplot as plt

from menu_helpers import menu, input_int_constrained, custom_system_menu
from systems import iterate, names
from turtles import turtleGraph, turtlePlot
from warning import shouldWarn


main_options = ["Choose your Lindenmayer system", "Number of iterations", "Generate plots", "Quit"]

system = None
N = None
custom = False
print("Welcome to the Lindenmayer system playground! :D\n")
# Shows image
plt.imshow(img.imread('drage.jpg'))
plt.show()
while True:
    # Main menu option 1 - System
    if system is not None:
        print("You have chosen the system "+str(name)+"\n")
    if N is not None:
        print("The system will be run for "+str(N)+" iterations\n")
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        if option == 1:
            print("What kind of system would you like to use?")
            kind_choice = menu(["Predefined", "Custom"])
            # Opens predefined menu
            if kind_choice == 1:
                print("Which system would you like to see?")
                system_choice = menu(["Koch's curve", "Sierpinski's triangle"])
                if system_choice is not None:
                    system = list(names.values())[system_choice-1]
                    name=list(names.keys())[system_choice-1]
                    custom = False
            # Opens custom menu
            elif kind_choice==2:
                system = custom_system_menu()
                if system is not None:
                    custom = True
                    name = "Custom"
            # Passes to main menu
            else:
                pass
            print("Please choose the desired number of iterations:")
        # Main menu option 2 - Iterations
        elif option==2:
            if system is None:
                # Warning
                print("Please note: You are currently trying to select the number of iterations before chosing the system. This means that the program cannot warn you if the system will take too long to iterate")
            while True:
                n_choice = input_int_constrained("N = ", lambda x: x >= 0, "Please input a non-negative integer")
                if n_choice is not None:
                    N = n_choice
                    # Warning message if N is too high
                    if system is not None and shouldWarn(system,N):
                        print("N is very high! Are you sure you want to continue with this number of iterations?")
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
        #Main menu option 3 - Plotting
        elif option == 3:
            if system is not None and N is not None:
                # Plots
                turtlePlot(turtleGraph(iterate(system, N), system if custom else None),name)
            else:
                print("Please choose both your desired L-system and number of iterations first")
        #Main menu option 3 - Exit
        elif option == 4:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()
