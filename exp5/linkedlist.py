# Define the Node class with four fields
class Node:
    def __init__(self, data1, data2, data3, data4):
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the end of the list and sort the list
    def append(self, data1, data2, data3, data4):
        new_node = Node(data1, data2, data3, data4)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            prev_node = None
            while current_node is not None and current_node.data1 <= data1:
                prev_node = current_node
                current_node = current_node.next

            if prev_node is None:
                new_node.next = self.head
                self.head = new_node
            else:
                prev_node.next = new_node
                new_node.next = current_node

    # Insert a new node at the beginning of the list and sort the list
    def prepend(self, data1, data2, data3, data4):
        new_node = Node(data1, data2, data3, data4)

        if self.head is None or self.head.data1 > data1:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            prev_node = None
            while current_node is not None and current_node.data1 <= data1:
                prev_node = current_node
                current_node = current_node.next

            prev_node.next = new_node
            new_node.next = current_node

    # Delete the first occurrence of a node with the given data and sort the list
    def delete(self, data1, data2, data3, data4):
        if self.head is None:
            return

        if self.head.data1 == data1 and self.head.data2 == data2 and self.head.data3 == data3 and self.head.data4 == data4:
            self.head = self.head.next
            return

        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data1 == data1 and current_node.data2 == data2 and current_node.data3 == data3 and current_node.data4 == data4:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data1, current_node.data2, current_node.data3, current_node.data4)
            current_node = current_node.next

# Define a function to prompt the user for a menu selection
def get_menu_selection():
    print("Menu:")
    print("1. Add a node to the end of the list")
    print("2. Add a node to the beginning of the list")
    print("3. Delete a node from the list")
    print("4. Print the list")
    print("5. Exit")


my_list = LinkedList()
while True:
    selection = get_menu_selection()

    if selection == 1:
        data1 = input("Enter data1 for the new node: ")
        data2 = input("Enter data2 for the new node: ")
        data3 = input("Enter data3 for the new node: ")
        data4 = input("Enter data4 for the new node: ")
        my_list.append(data1, data2, data3, data4)
        print("Node added to the end of the list.")
    elif selection == 2:
        data1 = input("Enter data1 for the new node: ")
        data2 = input("Enter data2 for the new node: ")
        data3 = input("Enter data3 for the new node: ")
        data4 = input("Enter data4 for the new node: ")
    elif selection == 3:
        my_list.delete