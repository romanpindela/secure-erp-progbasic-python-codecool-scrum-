def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    for option_id in range(1,len(list_options)):
        print(f"({option_id}) {list_options[option_id]}")
        if option_id == len(list_options)-1: # with last option, print also exit option
            print(f"({0}) {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(f"{message}")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    no_of_cols = len(table[0])
    flat_list = [item for items in table for item in items]
    longest_el = max(flat_list, key=len)
    first_line = "/" + ("-" * len(longest_el) * no_of_cols + "-" * no_of_cols) + "\\"
    print(first_line)
    for i, sublist in enumerate(table):
        line = "|" + "|".join(str(item).center(len(longest_el)) for item in sublist) + "|"
        break_line = "|" + "|".join(str("-" * len(longest_el)) for item in sublist) + "|"
        print(line)
        print(break_line)


def get_input(label):
        """Gets single string input from the user.

        Args:
            label: str - the label before the user prompt
        """
        try:
            user_input = input(f"{label}: ")
            return user_input
        except:
            return ""


def get_inputs(labels) -> list:
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    user_inputs = []
    for question in labels:
        user_input = input(f"enter {question}: ")
        user_inputs.append(user_input)
    return user_inputs

def print_error_message(message):
    print(f"Error: {message}")
