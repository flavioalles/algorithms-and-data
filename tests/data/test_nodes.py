import pytest

from src.data.nodes import Node, DoubleLinkedNode, SingleLinkedNode


class TestNode:
    """
    A test class for the Node class.
    """

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_read(self, data):
        assert Node[type(data)](data).data == data

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_write(self, data):
        node = Node[str]("data")

        with pytest.raises(AttributeError):
            node.data = data

        assert node.data == "data"


class TestSingleLinkedNode:
    """
    A test class for the SingleLinkedNode class.
    """

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_read(self, data):
        assert SingleLinkedNode[type(data)](data).data == data

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_write(self, data):
        node = SingleLinkedNode[str]("data")

        with pytest.raises(AttributeError):
            node.data = data

        assert node.data == "data"

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_next_read(self, data):
        a_node = SingleLinkedNode[type(data)](data)
        assert a_node.next is None

        another_node = SingleLinkedNode[type(data)](data, a_node)
        assert another_node.next == a_node

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_next_write(self, data):
        a_node = SingleLinkedNode[type(data)](data)
        assert a_node.next is None

        another_node = SingleLinkedNode[type(data)](data)
        another_node.next = a_node
        assert another_node.next == a_node


class TestDoubleLinkedNode:
    """
    A test class for the DoubleLinkedNode class.
    """

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_read(self, data):
        assert DoubleLinkedNode[type(data)](data).data == data

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_write(self, data):
        node = DoubleLinkedNode[str]("data")

        with pytest.raises(AttributeError):
            node.data = data

        assert node.data == "data"

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_next_read(self, data):
        a_node = DoubleLinkedNode[type(data)](data)
        assert a_node.next is None

        another_node = DoubleLinkedNode[type(data)](data, a_node)
        assert another_node.next == a_node

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_next_write(self, data):
        a_node = DoubleLinkedNode[type(data)](data)
        assert a_node.next is None

        another_node = DoubleLinkedNode[type(data)](data)
        another_node.next = a_node
        assert another_node.next == a_node

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_previous_read(self, data):
        a_node = DoubleLinkedNode[type(data)](data)
        assert a_node.previous is None

        another_node = DoubleLinkedNode[type(data)](data, _previous=a_node)
        assert another_node.previous == a_node

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_previous_write(self, data):
        a_node = DoubleLinkedNode[type(data)](data)
        assert a_node.previous is None

        another_node = DoubleLinkedNode[type(data)](data)
        another_node.previous = a_node
        assert another_node.previous == a_node
