#!/usr/bin/python3
class Node:
    """Node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (not isinstance(value, Node) or value is not None):
            raise TypeError("next_node must be a Node Object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """A list of Nodes that are linked singly"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the SLL"""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

        def __str__(self):
            """Define how print(SinglyLinkedLits()) would be"""
            node_values = []
            tmp = self.__head
            while tmp is not None:
                tmp = tmp.next_node
            return ("\n".join(node_values)
