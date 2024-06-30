class Node:
    """Class for creating a node in linked list"""

    def __init__(self, data):
        # Defining a node with value/data and next section
        self.data = data
        self.next = None


class Linkedlist:
    """Class for creating a linked list and methods for adding data """

    def __init__(self):
        # initiating an empty linked list
        self.head = None

    def append_data(self, value):
        """Adding data to the end of the list"""
        # Creating a new node with the value passed by user
        node = Node(value)
        # If the head is currently empty
        if not self.head:
            # Point the head towards the node created and return the single node linked list
            self.head = node
            return
        # Assign the value of the node to the previous node
        previous_node = self.head
        # Checking if the previous node is the last node
        while previous_node.next:
            # If previous node is not the last node add the value of previous node.next in previous node
            previous_node = previous_node.next
        previous_node.next = node

    def print_linked_list(self):
        """Printing the linked list"""
        # setting the first node to current node
        current_node = self.head
        # Traversing till the end of the list
        while current_node.next:
            # Printing each node in the list
            print(current_node.data, end="-->")
            # Adding the value of the next node to the current node at each iteration
            current_node = current_node.next
        # Using the print statement outside the loop to print the last element of the list
        print(current_node.data)

    def list_length(self):
        """Finding out the length of the linked list"""
        # Setting the length to 1
        length = 1
        # Assigning the value of head to the current node
        current_node = self.head
        # Traversing to the end of the list
        while current_node.next:
            # Incrementing the value of length after each iteration
            length += 1
            current_node = current_node.next
        # Returning the length of the linked list
        return length

    def add_element_at_beginning(self, new_data):
        """Adding a new node at the beginning of the list"""
        # Creating a new node
        new_node = Node(new_data)
        # Setting the current node to point at the first node
        current_node = self.head
        # Pointing the new node to the current node
        new_node.next = current_node
        # Pointing the head to the new node added at the beginning
        self.head = new_node

    def add_element_at_location(self, new_data, location):
        """Adding new node at the location"""
        # creating a new node
        new_node = Node(new_data)
        # Setting the current node to the first node in the list
        current_node = self.head
        # Setting the position counter to 1
        position = 1
        # Traversing till the node before the location
        while location - position != 1:
            current_node = current_node.next
            position += 1
        # Inserting the new node at the position
        new_node.next = current_node.next
        current_node.next = new_node

    def adding_element_at_end(self, new_data):
        """Adding element at the end of the location"""
        # creating a new node
        new_node = Node(new_data)
        # Current node is set to the node at the beginning of the list
        current_node = self.head
        # Traversing till the end of the linked list
        while current_node.next:
            current_node = current_node.next
        # Adding node at the end of the list
        current_node.next = new_node
        new_node.next = None

    def deleting_elements_by_value(self, value):
        """Deleting element from the list by value"""
        # Global parameters to be used in the function
        global next_node, previous_node
        # Adding the value of the head of the Linked list to the current-node
        current_node = self.head
        # Traversing to the end of the list
        while current_node.next:
            # Using the variables to hold the value of current, previous and next node
            previous_node = current_node
            current_node = current_node.next
            next_node = current_node.next
            # Checking if the data at the current node is equal to the value to be deleted
            if current_node.data == value:
                # Deleting the desired node
                previous_node.next = next_node
        # Checking if the last node is the element to be deleted
        if current_node.data == value:
            # Deleting the element if found
            previous_node = None
        else:
            # Printing a message if element not found in the list
            print("Element not in the list")

    def deleting_element_by_position(self, position):
        """Deleting elements from the list by position"""
        # Setting the current node as the first node in the list
        current_node = self.head
        # Setting the location to the first element of the list
        location = 1
        # Assinging the length of the list to a variable
        length_of_list = self.list_length()
        # Checking if the position is not in the list
        if position > length_of_list:
            print("Position not in the list")
        # Checking if the value to remove is the first element in the list
        elif position == 1:
            # Removing the element
            current_node = current_node.next
            self.head = current_node
        else:
            # Traversing to the end of the list
            while current_node.next:
                # Increamenting the value of the location
                location+=1
                # Setting previous node to the current node, current node to the next node and next node as the node after
                previous_node = current_node
                current_node = current_node.next
                next_node = current_node.next
                # Checking if the element is the last element in the list
                if position == length_of_list:
                    # Removing the last element from the list
                    previous_node.next = None
                    break
                # Deleting the element from the location
                elif position == location:
                    previous_node.next = next_node
                    break

def test_cases(*args):
    """Accepts numbers as arguments and tests the functionality of the linked list methods"""
    new_linked_list = Linkedlist()
    print("Appending Elements....")
    for elements in args:
        new_linked_list.append_data(elements)
    print(new_linked_list.print_linked_list())
    print("Checking the length of the list....")
    print(new_linked_list.list_length())
    print("Adding the elements...")
    print("1. At the beginning of the list...")
    new_linked_list.add_element_at_beginning(129)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("2. At the particular location in the list...")
    new_linked_list.add_element_at_location(new_data=232, location=4)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("3. At the end of the list...")
    new_linked_list.adding_element_at_end(new_data=3222)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("Deleting elements from the list....")
    new_linked_list.deleting_elements_by_value(42)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("Deleting elements from the list....")
    new_linked_list.deleting_elements_by_value(3222)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("Deleting elements from the list....")
    new_linked_list.deleting_element_by_position(4)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("Deleting elements from the list....")
    new_linked_list.deleting_element_by_position(3)
    print("The new list is")
    new_linked_list.print_linked_list()
    print("Deleting elements from the list....")
    new_linked_list.deleting_element_by_position(9)
    print("The new list is")
    new_linked_list.print_linked_list()

# CHANGE THE NUMBERS IN THE FUNCTION CALL TO CREATE A LINKED LIST OF YOUR CHOICE
# REMOVE THE COMMENT TO EXECUTE THE CODE BELOW AND TEST THE LINKED LIST FUNCTIONALITY
test_cases(123, 10, 9, 23, 443, 213)

