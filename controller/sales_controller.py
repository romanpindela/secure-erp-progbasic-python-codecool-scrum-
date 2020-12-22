from model.sales import sales
from view import terminal as view
from model import util

import datetime


'''
Implement the Sales module with basic and special operations.

(1-4) Provide basic CRUD operations.
(5) Get the transaction that made the biggest revenue.
(6) Get the product that made the biggest revenue altogether.
(7) Count number of transactions between two given dates.
(8) Sum the price of transactions between two given dates.
'''

def list_transactions():
    sales_table = sales.list_transactions()
    view.print_table(sales_table)


def __is_transaction_price_valid(price: str) -> bool:
    try:
        valid_price = float(price)
        return True
    except:
        return False


def __is_transaction_date_format_valid(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def add_transaction():
    new_transaction = []
    new_transaction.append(util.generate_id())
    new_transaction.append(view.get_input("Customer"))
    new_transaction.append(view.get_input("Product"))

    user_input = view.get_input("Price")
    while not __is_transaction_price_valid(user_input):
        view.print_error_message("Error: Invalid input for Price")
        user_input = view.get_input("Price")
    new_transaction.append(user_input)

    user_input = view.get_input("Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Date i.e. 1989-03-21")
    new_transaction.append(user_input)

    if sales.add_transaction(new_transaction):
        view.print_message("New transaction added")
    else:
        view.print_error_message("Error while adding new transaction!")


def __is_transaction_to_update_valid(transaction_id_to_update:str) -> bool:
    does_transaction_to_update_exist = sales.does_transaction_exist(transaction_id_to_update)
    return does_transaction_to_update_exist


def update_transaction():
    user_input = view.get_input("Transaction ID / or 'quit'")
    user_wants_to_quit = False
    while not __is_transaction_to_update_valid(user_input) and not user_wants_to_quit:
        view.print_error_message("Error: Invalid input for Transaction to update")
        user_input = view.get_input("Transaction ID / or 'quit'")
        if user_input == 'quit':
            user_wants_to_quit = True
    transaction_id_to_update = user_input

    new_transaction = []
    new_transaction.append(transaction_id_to_update)
    new_transaction.append(view.get_input("Customer"))
    new_transaction.append(view.get_input("Product"))

    user_input = view.get_input("Price")
    while not __is_transaction_price_valid(user_input):
        view.print_error_message("Error: Invalid input for Price")
        user_input = view.get_input("Price")
    new_transaction.append(user_input)

    user_input = view.get_input("Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Date i.e. 1989-03-21")
    new_transaction.append(user_input)


    if sales.update_transaction(new_transaction):
        view.print_message("Transaction updated")
    else:
        view.print_error_message("Error while updating transaction!")


def __is_transaction_to_delete_valid(transaction_id_to_update:str) -> bool:
    does_transaction_to_update_exist = sales.does_transaction_exist(transaction_id_to_update)
    return does_transaction_to_update_exist


def delete_transaction():
    user_input = view.get_input("Transaction ID / or 'quit'")
    user_wants_to_quit = False
    while not __is_transaction_to_delete_valid(user_input) and not user_wants_to_quit:
        view.print_error_message("Error: Invalid input for Transaction to update")
        user_input = view.get_input("Transaction ID / or 'quit'")
        if user_input == 'quit':
            user_wants_to_quit = True
    transaction_id_to_delete = user_input

    if sales.delete_transaction(transaction_id_to_delete):
        view.print_message("Transaction deleted")
    else:
        view.print_error_message("Error while deleting transaction!")



def get_biggest_revenue_transaction():
    biggest_revenue_transaction = sales.get_biggest_revenue_transaction()
    if not biggest_revenue_transaction == False:
        view.print_table(biggest_revenue_transaction)
    else:
        view.print_error_message('Error while getting biggest revenue')

def get_biggest_revenue_product():
    biggest_revenue_product = sales.get_biggest_revenue_product()
    if not biggest_revenue_product == False:
        view.print_table(biggest_revenue_product)
    else:
        view.print_error_message('Error while getting transactions number between dates')


def count_transactions_between():

    view.print_message("Enter Min and Max date to count number of transactions.")
    user_input = view.get_input("Min Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Min i.e. 1989-03-21")
    min_date = user_input

    user_input = view.get_input("Max Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Max Date i.e. 1989-03-21")
    max_date = user_input

    transactions_number_between = sales.count_transactions_between(min_date, max_date)
    if not transactions_number_between == False:
        view.print_table(transactions_number_between)
    else:
        view.print_error_message('Error while getting transaction number between given dates')


def sum_transactions_between():
    view.print_message("Enter Min and Max date to sum of transactions.")
    user_input = view.get_input("Min Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Min i.e. 1989-03-21")
    min_date = user_input

    user_input = view.get_input("Max Date i.e. 1989-03-21")
    while not __is_transaction_date_format_valid(user_input):
        view.print_error_message("Error: Invalid input for Date")
        user_input = view.get_input("Max Date i.e. 1989-03-21")
    max_date = user_input

    transactions_sum_between = sales.sum_transactions_between(min_date, max_date)
    if not transactions_sum_between == False:
        view.print_table(transactions_sum_between)
    else:
        view.print_error_message('Error while calculating sum of transactions between given dates')


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
