import pytest

from src.data.nodes import Node


class TestNode:

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_read(self, data):
        assert Node[type(data)](data).data == data

    @pytest.mark.parametrize("data", [1, 2, 3, "4", "five", (6, 7), [8, 9]])
    def test_data_write(self, data):
        node = Node[str]("data")

        with pytest.raises(AttributeError):
            node.data = data

        assert node.data == "data"
