class Node:
    def __init__(self, customerid, name, date, amount):
        self.customerid = customerid
        self.name = name
        self.date = date
        self.amount = amount
        self.next = None

class CustomerDetails:
    def __init__(self):
        self.head = None

    def add_customer(self, customerid, name, date, amount):
        new_node = Node(customerid, name, date, amount)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            if current.amount > amount:
                new_node.next = current
                self.head = new_node
            else:
                while current.next is not None and current.next.amount < amount:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def view_all_customers(self):
        current = self.head
        while current is not None:
            print("Customer Id:", current.customerid)
            print("Customer Name:", current.name)
            print("Purchase date:", current.date)
            print("Bill amount:", current.amount)
            print()
            current = current.next

    def total_purchase_amount(self, year):
        total = 0
        current = self.head
        while current is not None:
            if current.date.endswith(year):
                total += current.amount
            current = current.next
        print("Total purchase amount for year", year, "is", total)

    def view_customer_details(self, name):
        current = self.head
        found = False
        while current is not None and not found:
            if current.name == name:
                print("Customer Id:", current.customerid)
                print("Purchase date:", current.date)
                print("Bill amount:", current.amount)
                found = True
            else:
                current = current.next
        if not found:
            print("Customer", name, "not found")

if __name__ == "__main__":
    customer_data = CustomerDetails()
    while True:
        print("1. Add Customer Data")
        print("2. View All Customer Data in Sorted Order based on Bill Amount")
        print("3. View Total Purchase Amount for a Specific Year")
        print("4. View Details of a Specific Customer based on Name")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            customerid = int(input("Enter Customer Id: "))
            name = input("Enter Customer Name: ")
            date = input("Enter Purchase Date (dd/mm/yy): ")
            amount = float(input("Enter Bill Amount: "))
            customer_data.add_customer(customerid, name, date, amount)
        elif choice == 2:
            customer_data.view_all_customers()
        elif choice == 3:
            year = input("Enter Year (yy): ")
            customer_data.total_purchase_amount(year)
        elif choice == 4:
            name = input("Enter Customer Name: ")
            customer_data.view_customer_details(name)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")
