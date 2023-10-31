import sys
import os
# Get the current directory of the file
current_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate to the parent directory
parent_directory = os.path.dirname(current_directory)

# Define the relative path to the 'RefactorCode' folder
relative_path = 'refactorcode'

# Construct the absolute path to the 'RefactorCode' folder
absolute_path = os.path.join(parent_directory, relative_path)

# Append the absolute path to sys.path
sys.path.append(absolute_path)
from assignment import DoublyLinkedList, twenties, create_linked_list, Node

def test_node():
    dL = DoublyLinkedList()
    
    for i in range(4):
         dL.add_last(Node(i))

    print(dL)
    assert str(dL) == f"(0, (1, (2, (3, ('Trailer', None)))))"

def test_size():
    dL = create_linked_list()
    print(dL.size())
    assert dL.size() == 4

def test_empty():
    dL = create_linked_list()
    dL2 = DoublyLinkedList()
    print(dL.is_empty())

    dL2 = DoublyLinkedList()
    print(dL2.is_empty())


    assert dL.is_empty() == False
    assert dL2.is_empty() == True
    del dL2




def test_get_element():
    dL = create_linked_list()
    #Test your implementation here
    print(dL.get_first())
    print(dL.get_last())

    assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"
    assert str(dL.get_last()) == f"(3, ('Trailer', None))"


def test_previous():
    dL = create_linked_list()
#Test your implementation here
    print(dL.get_last().get_previous())
    print(dL.get_first().get_next())

    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"


def test_add_before_after():
    dL = create_linked_list()
    #Test your implementation here
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())

    print(dL)
    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"



def test_add_first_last():
    dL = create_linked_list()
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())
    #Test your implementation here
    dL.add_first(Node(7))
    dL.add_last(Node(-1))
    print(dL)
    assert str(dL) == "(7, (0, (42, (1, (2, (34, (3, (-1, ('Trailer', None)))))))))"


def test_remove():
    dL = create_linked_list()
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())
    #Test your implementation here
    dL.add_first(Node(7))
    dL.add_last(Node(-1))
    #Test your implementation here
    dL.remove(dL.get_first())
    print(dL.get_first())

    assert dL.get_first().get_element() == 0


def test_map():
    dL = create_linked_list()
    dL = create_linked_list()
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())
    #Test your implementation here
    dL.add_first(Node(7))
    dL.add_last(Node(-1))
    dL.remove(dL.get_first())
    #Test your implementation here
    dL.map(lambda x: x**2)

    print(dL)

    assert str(dL) == "(0, (1764, (1, (4, (1156, (9, (1, ('Trailer', None))))))))"

#Dont know what dn is and dont want to figure it out
# def test_iterator():
#     dL = create_linked_list()
#     for node in dL: 
#         print(node.get_element() == dn.__next__().get_element())
#         print(dn)


def test_twenties():
    doubleDigits = twenties()

    doubleDigits.map(lambda x: x+10)

    print(doubleDigits)
    assert str(doubleDigits) =="(30, (31, (32, (33, (34, (35, (36, (37, (38, (39, ('Trailer', None)))))))))))"
