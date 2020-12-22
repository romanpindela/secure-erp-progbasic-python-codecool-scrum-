from model.crm import crm
from model import data_manager,util
from view import terminal as view

customers = data_manager.read_table_from_file(crm.DATAFILE)

def list_customers():

    customers.insert(0,crm.HEADERS)
    view.print_table(customers)


def add_customer():

    customer_name = str(input(crm.labels["ask_name"])) #wywalić do terminala view
    customer_email = str(input(crm. labels["ask_email"]))#wywalić do terminala view
    customer_sub_input = input(crm. labels["subscribed"]).upper()#wywalić do terminala view
    if customer_sub_input == "Y":#wywalić do terminala view
        customer_subscribed = 1#wywalić do terminala view
    else:
        customer_subscribed = 0#wywalić do terminala view

    customer_id = util.generate_id()

    new_customer = [customer_id,customer_name,customer_email,str(customer_subscribed)]
    customers.append(new_customer)

    list_customers()
    view.print_table(customers)



def update_customer():
    customer_id_asked = input(crm.labels["customer_id"])#wywalić do terminala view
    customer_index = get_customer_from_id(customers,customer_id_asked)
    if customer_index is not None:
        customer_new_name = str(input(crm.labels["ask_name"]))#wywalić do terminala view
        customer_new_email = str(input(crm.labels["ask_email"]))#wywalić do terminala view
        customer_new_sub_input = input(crm.labels["subscribed"]).upper()#wywalić do terminala view
        if customer_new_sub_input == "Y":#wywalić do terminala view
            customer_new_subscribed = 1#wywalić do terminala view
        else:
            customer_new_subscribed = 0#wywalić do terminala view

        customer_updated = [customer_id_asked, customer_new_name, customer_new_email,str(customer_new_subscribed)]
        customers[customer_index[0]] = customer_updated
        #list_customers_updated = data_manager.write_table_to_file(crm.DATAFILE,customers)
        view.print_table(customers)
    else:
        add_customer()



def delete_customer():


    customer_id_asked = input(crm.labels["customer_id"])#wywalić do terminala view
    customer_index = get_customer_from_id(customers,customer_id_asked)
    if customer_index is not None:
        customer_to_remove = customers[customer_index[0]]
        customers.remove(customer_to_remove)
        #ustomers_after_remove = data_manager.write_table_to_file(crm.DATAFILE,customers)
        view.print_table(customers)
    else:
        print("no such id")

def get_subscribed_emails():

    customers_subscribed = []
    for customer in customers:
        if customer[crm.subscribed_index] == "1":
            customers_subscribed.append(customer)
        else:
            continue
    subscribed_customers_emails = []
    for customer in customers_subscribed:
        subscribed_customers_emails.append([customer[crm.email_index]])

    view.print_table(subscribed_customers_emails)

def get_customer_from_id(list_of_customers,customer_id):

    for sub_i, sublist in enumerate(list_of_customers):
        try:
            return (sub_i, sublist.index(customer_id))
        except ValueError:
            continue
    return None

def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)

#list_customers()
#add_customer()
#update_customer()
#delete_customer()
#get_subscribed_emails()
