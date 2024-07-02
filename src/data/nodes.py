from dataclasses import dataclass


@dataclass
class Node[T]:
    """
    Represents a node.

    Attributes:
        _data (T): The data stored in the node.
    """

    _data: T

    @property
    def data(self) -> T:
        """
        Get the data stored in the node.

        Returns:
            T: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        """
        Setter for the data attribute.

        Raises:
            AttributeError: This attribute is immutable.
        """
        raise AttributeError("Immutable attribute.")
