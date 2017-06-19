from menu_helpers import *
from systems import *
from turtles import *
import sys

System = None
N = None
print("Welcome to the Lindenmayer system playground! :D")
while True:
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        if option == 1:
            print("Which system would you like to see?")
            system_choice = menu(system_options)
            if system_choice is not None:
                System = list(names.keys())[system_choice-1]
            print("Please choose the desired number of iterations:")
            n_choice = input_nonNeg_int("N = ")
            if n_choice is not None:
                N = n_choice
        elif option == 2:
            if System is not None and N is not None:
                turtlePlot(turtleGraph(LindIter(System, N)))
            else:
                print("Please choose your desired L-system and number of iterations first")
        elif option == 3:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()

