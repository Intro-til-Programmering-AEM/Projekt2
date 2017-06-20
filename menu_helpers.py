#Menu haandtering projekt 2

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

def input_symbol_string(request, allow_lr = False):
    while True:
        try:
            x = input_wrapper("Please input a string "+request+": ")
        except EOFError:
            return None
        if x is None:
            return None
        if x == " ":
            x = ""
        if any(c in x for c in "LR") and not allow_lr:
            print("String cannot contain L or R as these have predefined meaning, please try again.")
        else:
            return x

def input_legal_string(request, test, error = "String must only contain legal symbols."):
    allow_lr = all(test(x) for x in "LR")
    while True:
        x = input_symbol_string(request, allow_lr)
        if x is None:
            return None
        elif not all(test(c) for c in x):
            print(error)
        else:
            return x

def custom_system_menu():
    print("First you will define your constants and variables.")
    print("There are two constants you will be able to define:")
    print("L and R. You will always have those two available.")
    print("They will each represent a turn by 45°.")
    print("Then you will choose which symbols will eventually represent a line segment.")
    print("Then, the initial string for your system.")
    print("And then, finally, you will choose the replacement rules for each variable.")
    print("Cancelling at any point will return you to the main menu.")
    print("Since an empty input is used to cancel, use a single space to indicate an empty string.")
    print("All characters in your strings will be counted, so if you include e.g. a comma or a space, it will be counted as a symbol.")
    constant_string = input_symbol_string("containing all your constants")
    if constant_string is None:
        return None
    variable_string = input_legal_string("containing all your variables", lambda c: c not in constant_string, "Symbols cannot be both constants and variables.")
    if variable_string is None:
        return None
    symbols = constant_string+variable_string
    line_string = input_legal_string("containing all the symbols that should represent line segments", lambda c: c in symbols)
    if line_string is None:
        return None
    initial_string = input_legal_string("that your system will be iterated from", lambda c: c in symbols+"LR")
    if initial_string is None:
        return None
    rules = []
    for c in variable_string:
        rule_string = input_legal_string("which "+str(c)+" should be replaced with", lambda c: c in symbols+"LR")
        if rule_string is None:
            return None
        rules.append((c, rule_string))
    return ([c for c in constant_string+"LR"], initial_string, dict(rules), [c for c in line_string])
