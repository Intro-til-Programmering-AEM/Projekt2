# Displays a menu,
# then asks user to select an option
# until a valid option is chosen,
# which is then returned
# Returns the selected option
def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    # Accepts only integers within the range of possible options
    return input_int_constrained("Select an option: ",
                                 lambda x: x > 0 and x <= len(options),
                                 "Please input a number corresponding to the option you want to select.")

# Repeatedly requests an integer from the user,
# which must follow some sort of constraint,
# until an acceptable integer is chosen,
# and then returns it,
# printing a custom error message otherwise.
# Inputs: a string `request` which is used as the request for the user;
# a function `test` that must take an integer and return a boolean value,
# which must return True for integers iff they are to be considered acceptable;
# and a string `error` which will be printed if the user input cannot be parsed
# as an acceptable integer.
# Errors: returns None if user input is empty or EOF,
# which indicates a cancel.
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

# Takes an input from the user
# with the request text `request`,
# raising `EOFError` if the input was empty
# (even if it was not directly EOF)
def input_wrapper(request):
    x = input(request)
    if x == "":
        raise EOFError
    return x

# Queries for user input to build a custom L-system.
# Will return None if cancelled, which can happen at any time during the process.
# Please note that, while this function certainly has script-like aspects to it
# (printing, requesting user input, doing interactive error handling)
# it functions as an independent unit from the main menu,
# constructing a system tuple,
# and could theoretically be used in any piece of software
# that is compatible with the system description tuples
# used in this program.
# In addition, since there are no "naked" statements present
# in the module scope itself,
# and the module thus does nothing when imported even if `__name__ == "__main__"`,
# it is not formally a script.
def define_custom_system():
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
    # This list is used later to deny the user possibility of overwriting 'L' and 'R'
    predefined = ['L', 'R']
    # The user can't choose the predefined constants.
    constant_string = input_legal_string("containing all your constants", lambda c: c not in predefined)
    # Handle cancelling
    if constant_string is None:
        return None
    else:
        # Turns the string into a set to eliminate any symbols that appear more than once
        # and then into a list to be used in the rest of the code
        constants = list(set(constant_string))
    print("""

You must now define your variables.
Please note: the same symbol cannot be used as both a variable and a constant.
""")
    # The iser can't choose any of their constants (including L and R) as variables
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constants+predefined, "Symbols cannot be both constants and variables!")
    if variable_string is None:
        return None
    else:
        variables = list(set(variable_string))
    symbols = constants+variables
    print("""

Now choose the symbols (can be both constants and variables)
that will be drawn as line segments when plotting the system.
""")
    # Only user-chosen constants and variables can represent line segments
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    else:
        line_symbols = list(set(line_string))
    print("\n\nNow choose the initial string. This symbol must also be chosen from the constants and variables.\n")
    # The initial string can contain all legal symbols ('L', 'R', and user-chosen symbols)
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+predefined)
    if initial_string is None:
        return None
    # Create an empty list to be filled out with replacement rule tuples
    rules = []
    print("""

Please choose the strings that you want to replace each variable with.
We encourage you to create rules with more than one symbol
and include L and R if you want the curve to bend.
""")
    for c in variables:
        # Same restriction as on the initial string
        rule_string = input_legal_string("which "+str(c)+" should be replaced with", lambda c: c in symbols+predefined)
        if rule_string is None:
            return None
        # Fill out the rules list with a tuple of the left hand side and desired right hand side
        # Slow in theory, but insignificant compared to the time spent waiting for the user
        rules.append((c, rule_string))
    # All the information of this new-born system is returned in the same
    # format as the predefined systems,
    # transforming the list of rule tuples into a dictionary
    return (constants+predefined, initial_string, dict(rules), line_symbols)

# Repeatedly requests an string from the user,
# which must follow some sort of constraint,
# until an acceptable string is chosen,
# and then returns it,
# printing a custom error message otherwise.
# Inputs: a string of a sentence `request`
# which is modified to be grammatical,
# and then used as the request for the user;
# a function `test` that must take a string and return a boolean value,
# which must return True for string iff they are to be considered acceptable;
# and a string `error` which will be printed if the user is not an acceptable string.
# Errors: returns None if user input is empty or EOF,
# which indicates a cancel.
def input_legal_string(request, test, error = "String must only contain legal symbols."):
    while True:
        try:
            x = input_wrapper("Please input a string "+request+": ")
        except EOFError:
            return None
        # Deliberately return the empty string if input is a single space
        if x == " ":
            return ""
        # Print an error message if an unacceptable input is given
        if not all(test(c) for c in x):
            print(error)
        # An error is printed if neither L and R are allowed but any of them is present
            if all(not test(c) for c in "LR") and any(c in "LR" for c in x):
                print("Remember, L and R are constants that you cannot define yourself, and they represent 45° turns.")
        # Return x if none of the above problems were encountered
        else:
            return x

