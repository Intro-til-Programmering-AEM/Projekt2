from menu_helpers import *
from systems import *
from turtles import *
import sys

system = None
N = None
custom = False
print("Welcome to the Lindenmayer system playground! :D")
while True:
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is not None:
        if option == 1:
            print("What kind of system would you like to use?")
            kind_choice = menu(["Predefined", "Custom"])
            if kind_choice == 1:
                print("Which system would you like to see?")
                system_choice = menu(system_options)
                if system_choice is not None:
                    System = list(names.keys())[system_choice-1]
                    system = names[System]
                    custom = False
            else:
                system = custom_system_menu()
                if system is not None:
                    custom = True
                    print(system)
        elif option == 2:
            print("Please choose the desired number of iterations:")
            n_choice = input_nonNeg_int("N = ")
            if n_choice is not None:
                N = n_choice
        elif option == 3:
            if system is not None and N is not None:
                turtlePlot(turtleGraph(iterate(system, N), system if custom else None))
            else:
                print("Please choose your desired L-system and number of iterations first")
        elif option == 4:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()

