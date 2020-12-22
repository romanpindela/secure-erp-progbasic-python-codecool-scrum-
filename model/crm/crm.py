""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util
from view import terminal


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]
id_index = 0
name_index = 1
email_index = 2
subscribed_index = 3
labels = {"ask_name":"type in customer name", "ask_email": "type in customer email",
            "subscribed":"please indicate if customer is subscribed y/n", "customer_id": "please type in customer id"}



# def get_customers():
#     customers = data_manager.read_table_from_file(DATAFILE)
#     customers.insert(0,HEADERS)
#     print(customers)
#     return customers

#
# def add_customer():
#
#     customers = get_customers()
#     customer_name = str(input(labels["ask_name"])) #wywalić do terminala view
#     customer_email = str(input(labels["ask_email"]))#wywalić do terminala view
#     customer_sub_input = input(labels["subscribed"]).upper()#wywalić do terminala view
#     if customer_sub_input == "Y":#wywalić do terminala view
#         customer_subscribed = 1#wywalić do terminala view
#     else:
#         customer_subscribed = 0#wywalić do terminala view
#     customer_id = util.generate_id()
#     new_customer = [customer_id,customer_name,customer_email,str(customer_subscribed)]
#     customers.append(new_customer)
#     list_customers_added = data_manager.write_table_to_file(DATAFILE,customers)
#     return list_customers_added
#
# def update_customer():
#
#     customers = get_customers()
#
#     customer_id_asked = input(labels["customer_id"])#wywalić do terminala view
#     customer_index = get_customer_from_id(customers,customer_id_asked)
#     if customer_index is not None:
#         customer_new_name = str(input(labels["ask_name"]))#wywalić do terminala view
#         customer_new_email = str(input(labels["ask_email"]))#wywalić do terminala view
#         customer_new_sub_input = input(labels["subscribed"]).upper()#wywalić do terminala view
#         if customer_new_sub_input == "Y":#wywalić do terminala view
#             customer_new_subscribed = 1#wywalić do terminala view
#         else:
#             customer_new_subscribed = 0#wywalić do terminala view
#
#         customer_updated = [customer_id_asked, customer_new_name, customer_new_email,str(customer_new_subscribed)]
#         customers[customer_index[0]] = customer_updated
#         list_customers_updated = data_manager.write_table_to_file(DATAFILE,customers)
#         return list_customers_updated
#     else:
#         add_customer()

# def delete_customer():
#     customers = get_customers()
#     customer_id_asked = input(labels["customer_id"])#wywalić do terminala view
#     customer_index = get_customer_from_id(customers,customer_id_asked)
#     if customer_index is not None:
#         customer_to_remove = customers[customer_index[0]]
#         customers.remove(customer_to_remove)
#         data_manager.write_table_to_file(DATAFILE,customers)
#     else:
#         print("no such id")


# def get_subscribed_emails():
#     customers = get_customers()
#     customers_subscribed = []
#     for customer in customers:
#         if customer[subscribed_index] == "1":
#             customers_subscribed.append(customer)
#         else:
#             continue
#     subscribed_customers_emails = []
#     for customer in customers_subscribed:
#         subscribed_customers_emails.append(customer[email_index])
#
#     return subscribed_customers_emails

# def get_customer_from_id(list_of_customers,customer_id):
#
#     for sub_i, sublist in enumerate(list_of_customers):
#         try:
#             return (sub_i, sublist.index(customer_id))
#         except ValueError:
#             continue
#     return None



