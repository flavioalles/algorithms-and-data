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

        with pytest.raises(AttributeError):
            linked_list.head = a_node

        assert linked_list.head is None

    @pytest.mark.parametrize(
        "data",
        [
            (1, 2),
            (2, 3),
            (3, 4),
            ("4", "5"),
            ("five", "six"),
            ((6, 7), (8, 9)),
            ([8, 9], [10, 11]),
        ],
    )
    def test_insert(self, data):
        T = type(data[0])

        a_node = SingleLinkedNode[T](data[0])

        linked_list = LinkedList[T](a_node)

        assert linked_list.head == a_node

        another_node = SingleLinkedNode[T](data[1])

        linked_list.insert(another_node)

        assert linked_list.head == another_node
        assert linked_list.head.next == a_node
