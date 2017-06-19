#Menu haandtering projekt 2

main_options = ["Choose the type of Lindenmayer system and the number of iterations", "Generate plots", "Quit"]
system_options = ["Kochs curve", "Sierpinski triangle"]
warn_options= ["Yes", "No"]


# Denne funktion tager et brugerinput (options) og sender det videre, hvis det er valid.
# Hvis ikke så kommer der en fejlmeddelelse
def input_option(options):
    while(True):
        try:
            # Get number that may be a legal option
            x = int(input_wrapper("Select an option: "))
            # Check if it's legal
            if x <= len(options) and x > 0:
                return x
            # if the options is not legal, an appropriate message is printed
            else:
                print("Not an option, please try again.")
        # if no option is selected, return None
        except EOFError:
            return None
        # if a wrong type of options is selected, pass and repeat while-statement
        except ValueError:
            print("Please input a number corresponding to the option you want to select.")
            pass

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)

# Denne funktion ser om der er et input fra brugeren og laver en EOFError, hvis input er tomt.
# Den returnerer en string
def input_wrapper(request):
    x = input(request)
    if x == "":
        raise EOFError
    return x

def input_nonNeg_int(request):
    try:
        x = int(input_wrapper(request))
        if x >= 0:
            return x
        else:
            raise ValueError
    except ValueError:
        print("Please input a non-negative integer")
    except EOFError:
        return None