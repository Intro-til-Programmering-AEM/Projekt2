#Menu haandtering projekt 2

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)

# This function aks for a userinput until an input is given and returns it if the input is valid
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
    print("""
Please note the following:
    1) Cancelling at any point will return you to the main menu.
    2) Since an empty input is used to cancel, use a single space to indicate an empty string.
    3) All characters in your strings will be counted, so if you include e.g. a comma or a space, it will be counted as a symbol.
    4) Each character will be counted only once.


First you will be able to define your constants.
Please note:
    1) There are two constants you will be not able to define yourself: L and R.
    2) You will always have those two constants available, and they will each represent a turn by 45°.
    3) The same symbol cannot be assigned as both a variable and a constant!
    """)
    predefined = ['L', 'R']
    constant_string = input_legal_string("containing all your constants", lambda c: c not in predefined)
    if constant_string is None:
        return None
    else:
        constants = list(set(constant_string))
    print("""You must now define your variables.

Please note that the same symbol cannot be assigned as both a variable and a constant!""")
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constants+predefined, "Symbols cannot be both constants and variables.")
    if variable_string is None:
        return None
    else:
        variables = list(set(variable_string))
    symbols = constants+variables
    print("Please choose which constants and variables that should represent linesegments")
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    else:
        line_symbols = list(set(line_string))
    print("Please choose the initial symbol. This symbol must also be chosen from the constants and variables")
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+predefined)
    if initial_string is None:
        return None
    rules = []
    for c in variable_string:
        print("""Please choose wich symbols you want to replace your constants with.

              We encourage you to replace your variable with more than one symbol and include L and R if you want the curve to bent""")
        rule_string = input_legal_string("which "+str(c)+" should be replaced with", lambda c: c in symbols+predefined)
        if rule_string is None:
            return None
        rules.append((c, rule_string))
    return (constants+predefined, initial_string, dict(rules), line_symbols)

def input_legal_string(request, test, error = "String must only contain legal symbols."):
    while True:
        try:
            x = input_wrapper("Please input a string "+request+": ")
        except EOFError:
            return None
        if x == " ":
            # Deliberately return the empty string if input is a single space
            return ""
        if not all(test(c) for c in x):
            print(error)
            if all(not test(c) for c in "LR") and any(c in "LR" for c in x):
                print("Remember, you can't define L and R yourself, and they represent 45° turns.")
        else:
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
