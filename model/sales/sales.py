""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util
import time

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

index_id = HEADERS.index("Id")
index_customer = HEADERS.index("Customer")
index_product = HEADERS.index("Product")
index_price = HEADERS.index("Price")
index_date = HEADERS.index("Date")



sales_table = []
csv_separator = ';'

def __load_sales_from_file() -> list:
    sales_table = data_manager.read_table_from_file(DATAFILE, csv_separator)
    sales_table.insert(0, HEADERS)
    return sales_table


def __write_sales_to_file(sales_table):
    sales_table.pop(0)
    data_manager.write_table_to_file(DATAFILE, sales_table, csv_separator)


def list_transactions() -> bool or list:
    try:
        sales_table = __load_sales_from_file()
        return sales_table
    except:
        return False


def add_transaction(new_transaction: list) -> bool:
    try:
        sales_table = __load_sales_from_file()
        sales_table.append(new_transaction)
        __write_sales_to_file(sales_table)
        return True
    except:
        return False


def does_transaction_exist(transaction_id: str) -> bool:
    sales_table = __load_sales_from_file()
    index_id = HEADERS.index("Id")

    for transaction in sales_table:
        if transaction_id == transaction[index_id]:
            return True
    return False # transaction doesn't exist


def update_transaction(transaction_to_update: str) -> bool:
    try:
        sales_table = __load_sales_from_file()

        for transaction in sales_table:
            if transaction_to_update[index_id] == transaction[index_id]:
                transaction[index_customer] = transaction_to_update[index_customer]
                transaction[index_product] = transaction_to_update[index_product]
                transaction[index_price] = transaction_to_update[index_price]
                transaction[index_date] = transaction_to_update[index_date]

                __write_sales_to_file(sales_table)
                return True
    except:
        return False


def delete_transaction(transaction_id_to_delete: str) -> bool:
    try:
        sales_table = __load_sales_from_file()

        for transaction_index_to_delete in range(0, len(sales_table)):
            if sales_table[transaction_index_to_delete][index_id] == transaction_id_to_delete:
                sales_table.pop(transaction_index_to_delete)
                __write_sales_to_file(sales_table)
                return True
    except:
        return False

def get_biggest_revenue_transaction() -> list:
    try:
        sales_table = __load_sales_from_file()
        header_row = sales_table[0]
        sales_table.pop(0)

        biggest_revenue_transaction_price = float(sales_table[0][index_price])
        biggest_revenue_transaction = []
        for transaction in sales_table:
            if float(transaction[index_price]) >= float(biggest_revenue_transaction_price):
                biggest_revenue_transaction_price = float(transaction[index_price])
                biggest_revenue_transaction = transaction

        biggest_revenue_transaction_table = []
        biggest_revenue_transaction_table.append(header_row)
        biggest_revenue_transaction_table.append(biggest_revenue_transaction)
        return biggest_revenue_transaction_table
    except:
        return False


def get_biggest_revenue_product():
    try:
        sales_table = __load_sales_from_file()
        header_row = sales_table[0]
        sales_table.pop(0)

        # 1st get set of products in transactions
        list_of_products = []
        for transaction in sales_table:
            list_of_products.append(transaction[index_product])
        products = set(list_of_products)

        # 2nd check overall value transaction for each product type
        products_sum = []
        for product in tuple(products):
            product_sum_of_transaction = 0
            for transaction in sales_table:
                if transaction[index_product] == product:
                    product_sum_of_transaction += float(transaction[index_price])
            products_sum.append([product, product_sum_of_transaction])

        name = 0
        sum = 1
        first_product_group = 0
        biggest_revenue_product = products_sum[first_product_group]
        for product_sum in products_sum:
            if product_sum[sum] >= biggest_revenue_product[sum]:
                biggest_revenue_product = product_sum

        #adapt output format to str (instead of float)
        biggest_revenue_product[sum] = str(biggest_revenue_product[sum])

        biggest_revenue_product_table = []
        biggest_revenue_product_table.append(["Product","Sum of transaction"])
        biggest_revenue_product_table.append(biggest_revenue_product)

        return biggest_revenue_product_table

    except:
        return False


def __get_transactions_between_dates(sales_table: list, _min_date:str, _max_date:str) -> list:
    transactions_table = []
    min_date = time.strptime(_min_date, "%Y-%m-%d")
    max_date = time.strptime(_max_date, "%Y-%m-%d")

    for transaction in sales_table:
        transaction_date = time.strptime(transaction[index_date], "%Y-%m-%d")
        if transaction_date >= min_date and transaction_date <= max_date:
            transactions_table.append(transaction)
    return transactions_table

def count_transactions_between(min_date: str, max_date: str) -> list:
    try:
        sales_table = __load_sales_from_file()
        header_row = sales_table[0]
        sales_table.pop(0)

        transaction_table = __get_transactions_between_dates(sales_table, min_date, max_date)

        transactions_number_table = []
        transactions_number_table.append(['Transactions between dates:', 'Transactions number' ])
        transactions_number_table.append([f"{min_date} - {max_date}", str(len(transaction_table))])

        return transactions_number_table
    except:
        return False


def sum_transactions_between(min_date: str, max_date: str) -> list:
    try:
        sales_table = __load_sales_from_file()
        header_row = sales_table[0]
        sales_table.pop(0)

        transaction_table = __get_transactions_between_dates(sales_table, min_date, max_date)

        sum_of_transactions = 0
        for transaction in transaction_table:
            sum_of_transactions += float(transaction[index_price])

        transactions_number_table = []
        transactions_number_table.append(['Transactions between dates:', 'Transactions sum' ])
        transactions_number_table.append([f"{min_date} - {max_date}", str(round(sum_of_transactions,2))])

        return transactions_number_table
    except:
        return False

