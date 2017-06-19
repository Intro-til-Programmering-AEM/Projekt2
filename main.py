from menu_helpers import *
from systems import *
from turtles import *
from warning import *
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
            while True:
                n_choice = input_nonNeg_int("N = ")
                if n_choice is not None:
                    N = n_choice
                    if shouldWarn==True:
                        print("N is very high! Are you sure you want to continue with this number of iterations?")
                        warn_choice=menu(warn_options)
                        if warn_choice==1:
                            break
                        else:
                            print("Good luck with that!")
                    else:
                        break
        elif option == 2:
            if System is not None and N is not None:
                turtlePlot(turtleGraph(LindIter(System, N)))
            else:
                print("Please choose your desired L-system and number of iterations first")
        elif option == 3:
            print("Thank you for using the Lindenmayer system playground")
            # Exit properly
            sys.exit()

