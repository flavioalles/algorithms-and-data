import pytest

from src.data.lists import LinkedList
from src.data.nodes import SingleLinkedNode


class TestLinkedList:
    """
    A test class for the LinkedList class.
    """

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_head_read(self, data):
        a_node = SingleLinkedNode[type(data)](data)

        assert LinkedList[type(data)](a_node).head == a_node

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_head_write(self, data):
        a_node = SingleLinkedNode[type(data)](data)

        linked_list = LinkedList[type(data)]()

        assert linked_list.head is None

        linked_list.head = a_node

        assert linked_list.head == a_node
