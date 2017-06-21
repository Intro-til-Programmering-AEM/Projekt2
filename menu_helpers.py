#Menu haandtering projekt 2

# Creates a menu
# Takes a userinput
# Returns the selected option
# Asks for input again if it does not correspont with a menu option
def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_int_constrained("Select an option: ",
                                 lambda x: x > 0 and x <= len(options),
                                 "Please input a number corresponding to the option you want to select.")


def input_int_constrained(request, test, error):
    while True:
        try:
            x = int(input_wrapper(request))
            if test(x):
                return x
            else:
                raise ValueError
        except ValueError:
            print(error)
        except EOFError:
            return None

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
    print("""
Please note the following:
    1) Cancelling at any point will return you to the main menu.
    2) Since an empty input is used to cancel, use a single space to indicate an empty string.
    3) All characters in your strings will be counted,
        so if you include e.g. a comma or a space,
        that will also be counted as a symbol.
    4) Each character will be counted only once.


First you will be able to define your constants.
Please note:
    1) There are two constants you will be not able to define yourself: L and R.
    2) You will always have those two constants available,
        and they will each represent a turn by 45°.
    3) The same symbol cannot be used as both a variable and a constant.
    """)
    # Puts 'L' and 'R' in a predefined list. Used to deny the user possibility
    # of overwriting them later
    predefined = ['L', 'R']
    # The user chooses constants. Can't be the predefined constants.
    constant_string = input_legal_string("containing all your constants", lambda c: c not in predefined)
    if constant_string is None:
        return None
    else:
        # Put chosen constants into a list
        constants = list(set(constant_string))
    print("""

You must now define your variables.
Please note: the same symbol cannot be used as both a variable and a constant.
""")
    # The user chooses variables. Can't be predefined constants or constants.
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constants+predefined, "Symbols cannot be both constants and variables!")
    if variable_string is None:
        return None
    else:
        # Put chosen variables into a list
        variables = list(set(variable_string))
    # Put both variables and constants into symbols
    symbols = constants+variables
    print("""

Now choose the symbols (can be both constants and variables)
that will be drawn as line segments when plotting the system.
""")
    # The user chooses which constants and/or variables that represent line segments
    # Only chosen constants and variables can represent line segments.
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    else:
        # Put line symbols into a list
        line_symbols = list(set(line_string))
    print("\n\nNow choose the initial string. This symbol must also be chosen from the constants and variables.\n")
    # The user chooses the initial string. Only chosen constants, variables and
    # predefined constants may be in the initial string
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+predefined)
    if initial_string is None:
        return None
    # Create an empty list to be filled out with replacements for the variables
    rules = []
    # The replacements must be constants, variables or predefined constants
    print("""

Please choose the strings that you want to replace each variable with.
We encourage you to create rules with more than one symbol
and include L and R if you want the curve to bend.
""")
    for c in variables:
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
                print("Remember, L and R are constants that you cannot define yourself, and they represent 45° turns.")
        # Return x if none of the above problems were encountered
        else:
            return x


