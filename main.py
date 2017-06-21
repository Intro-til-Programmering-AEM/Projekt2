import sys

import matplotlib.image as img
import matplotlib.pyplot as plt

from menu_helpers import menu, input_int_constrained, define_custom_system
from systems import iterate, names
from turtles import turtleGraph, turtlePlot
from warning import shouldWarn


main_options = ["Choose your Lindenmayer system", "Number of iterations", "Generate plots", "Quit"]
system_options = (["Koch's curve", "Sierpinski's triangle"])


print("Welcome to the Lindenmayer system playground! :D\n")
# Shows "splash screen" image of example fractal
# that can be generated using the program
plt.imshow(img.imread('drage.jpg'))
plt.axis('off')
plt.show()

system = None
N = None
custom = False

while True:
    if system is not None:
        print("You have chosen the system "+str(name)+"\n")
    if N is not None:
        print("The system will be run for "+str(N)+" iterations\n")
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        # Main menu - System
        if option == 1:
            print("What kind of system would you like to use?")
            kind_choice = menu(["Predefined", "Custom"])
            # System menu - Predefined
            if kind_choice == 1:
                print("Which system would you like to see?")
                system_choice = menu(system_options)
                # Only redefine global variables if a system was chosen
                if system_choice is not None:
                    # Indices are 0-based but menus are 1-based,
                    # so subtract 1 from the system_choice
                    system = list(names.values())[system_choice-1]
                    # Get the nice name from the choices the user saw
                    name = system_options[system_choice-1]
                    # A predefined system is in use
                    custom = False
            # System menu - Custom
            elif kind_choice==2:
                # Walks user through defining a custom system
                new_system = define_custom_system()
                # If cancelled, the original system is kept as is
                if new_system is not None:
                    system = new_system
                    custom = True
                    name = "A custom L-system"
            # Only other option is None, pass to the main menu
            else:
                pass
        # Main menu - Iterations
        elif option==2:
            if system is None:
                print("Please note: You are currently trying to select the number of iterations before chosing the system. This means that the program cannot warn you if the system will take too long to iterate")
            print("Please choose the desired number of iterations:")
            while True:
                n_choice = input_int_constrained("N = ", lambda x: x >= 0, "Please input a non-negative integer")
                if n_choice is not None:
                    N = n_choice
                    if system is not None and shouldWarn(system,N):
                        print("N is very high! Are you sure you want to continue with this number of iterations?")
                        warn_choice=menu(["Yes", "No"])
                        # First choice is Yes
                        if warn_choice==1:
                            print("Good luck with that!")
                            break
                        # Otherwise, give them a new chance to choose N
                        else:
                            print("Please choose another N-value")
                    # Returns to main menu if enter is pressed
                    else:
                        break
                # Returns to main menu if enter is pressed
                else:
                    break
        #Main menu - Plotting
        elif option == 3:
            # Can only plot if it is known which system to iterate and for how long
            if system is not None and N is not None:
                # turtleGraph can work with custom systems using an optional argument,
                # so passing None is the same as not passing said argument
                turtlePlot(turtleGraph(iterate(system, N), system if custom else None), name)
            else:
                print("Please choose both your desired L-system and number of iterations first.")
        #Main menu - Exit
        elif option == 4:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()
