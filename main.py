# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Repository import repo
import DTO

def delete_all_tables():
    repo.hats.delete_table()
    repo.suppliers.delete_table()
    repo.orders.delete_table()

def configurate():
    with open("example_input/config.txt") as conf:
        lines = conf.readlines()
        nums_line = lines[0]
        data_nums = nums_line.rstrip("\n").split(",")
        hat_num = data_nums[0]
        supplier_num = data_nums[1]
        lines = lines[1:]
        for i in range(int(hat_num)):
            hat = lines[0]
            hat_data = hat.rstrip("\n").split(",")
            to_insert = DTO.Hat(*hat_data)
            repo.hats.insert(to_insert)
            lines = lines[1:]
        for i in range(int(supplier_num)):
            supplier = lines[0]
            supplier_data = supplier.rstrip("\n").split(",")
            to_insert = DTO.Supplier(*supplier_data)
            repo.suppliers.insert(to_insert)
            lines = lines[1:]

def get_orders():
    order_list = []
    with open("example_input/orders.txt") as ordering:
        lines = ordering.readlines()
        orders_num = len(lines)
        for i in range(orders_num):
            request = lines[0]
            order_data = request.rstrip("\n").split(",")
            first_matched_hat = repo.hats.find_first(order_data[1])
            my_supplier = repo.suppliers.find_supplier(first_matched_hat[2])
            to_insert = DTO.Order(i+1, order_data[0], first_matched_hat[0])
            data_line = ""+order_data[1]+","+my_supplier[0]+","+order_data[0]
            order_list.append(data_line)
            repo.orders.insert(to_insert)
            repo.hats.dispose_hat(first_matched_hat)
            lines = lines[1:]
    textfile = open("true_output.txt", "w")
    for line in order_list:
        textfile.write(line + "\n")
    textfile.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    delete_all_tables()
    configurate()
    get_orders()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
