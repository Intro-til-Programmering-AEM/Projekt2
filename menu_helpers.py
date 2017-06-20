#Menu haandtering projekt 2

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)

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

# Denne funktion ser om der er et input fra brugeren og laver en EOFError, hvis input er tomt.
# Den returnerer en string
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
    predefined = ['L', 'R']
    constant_string = input_legal_string("containing all your constants", lambda c: c not in predefined)
    if constant_string is None:
        return None
    else:
        constants = list(set(constant_string))
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constants+predefined, "Symbols cannot be both constants and variables.")
    if variable_string is None:
        return None
    else:
        variables = list(set(variable_string))
    symbols = constants+variables
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    else:
        line_symbols = list(set(line_string))
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+predefined)
    if initial_string is None:
        return None
    rules = []
    for c in variable_string:
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
