#Menu haandtering projekt 2

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)

# This function asks for a userinput until an input is given and returns it if the input is valid
# If the input is not valid an errormessage is printet
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

# This function checks for userinput and makes an EOFError if the input is empty
# The function returns a string
def input_wrapper(request):
    x = input(request)
    if x == "":
        raise EOFError
    return x

# Queries for user input to build a custom L-system.
# Will return None if cancelled, which can happen at any time during the process.
def custom_system_menu():
    print("""First you will define your constants and variables.
There are two constants you will be not able to define yourself: L and R.
You will always have those two available, and they will each represent a turn by 45°.
Then you will choose which symbols will eventually represent a line segment.
Then, the initial string for your system.
Finally, you will choose the replacement rules for each variable.
Cancelling at any point will return you to the main menu.
Since an empty input is used to cancel, use a single space to indicate an empty string.
All characters in your strings will be counted, so if you include e.g. a comma or a space, it will be counted as a symbol.
Each character will be counted only once.""")
    # Put 'L' and 'R' in a predefined list. Used to deny the user possibility
    # of overwriting them later
    predefined = ['L', 'R']
    # The user chooses constants. Can't be the predefined constants.
    constant_string = input_legal_string("containing all your constants", lambda c: c not in predefined)
    if constant_string is None:
        return None
    else:
        # Put chosen constants into a list
        constants = list(set(constant_string))
    # The user chooses variables. Can't be predefined constants or constants.
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constants+predefined, "Symbols cannot be both constants and variables.")
    if variable_string is None:
        return None
    else:
        # Put chosen variables into a list
        variables = list(set(variable_string))
    # Put both variables and constants into symbols
    symbols = constants+variables
    # The user chooses which constants and/or variables that represent line segments
    # Only chosen constants and variables can represent line segments.
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    else:
        # Put line symbols into a list
        line_symbols = list(set(line_string))
    # The user chooses the initial string. Only chosen constants, variables and
    # predefined constants may be in the initial string
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+predefined)
    if initial_string is None:
        return None
    # Create an empty list to be filled out with replacements for the variables
    rules = []
    # The replacements must be constants, variables or predefined constants
    for c in variable_string:
        rule_string = input_legal_string("which "+str(c)+" should be replaced with", lambda c: c in symbols+predefined)
        if rule_string is None:
            return None
        # Fill out the rules string
        rules.append((c, rule_string))
    # All the information of this new-born system is returned in the same
    # format as the predefined systems.
    return (constants+predefined, initial_string, dict(rules), line_symbols)

# This function asks the user to input a string according to a request, which
# lets the user know what kind of string is expected as input.
# It can also tell if a given string is legal - that is, the string must pass
# a test defined in the test-variable. If the test is not passed, an appropriate
# error message will be shown and the user will get to try again.
def input_legal_string(request, test, error = "String must only contain legal symbols."):
    while True:
        # Return None if x is an empty string. Otherwise x is the input of the user
        try:
            x = input_wrapper("Please input a string "+request+": ")
        except EOFError:
            return None
        if x == " ":
            # Deliberately return the empty string if input is a single space
            return ""
        # Print an error message if a non-allowed input is given
        if not all(test(c) for c in x):
            print(error)
        # Check if 'L' and 'R' are allowed, and check if they are in the string
        # An error is printed if L and R are not allowed but present
            if all(not test(c) for c in "LR") and any(c in "LR" for c in x):
                print("Remember, you can't define L and R yourself, and they represent 45° turns.")
        # Return x if none of the above problems were encountered
        else:
            return x

def input_int_constrained(request, test, error):
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

