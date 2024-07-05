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


@dataclass
class SingleLinkedNode[T](Node[T]):
    """
    Represents a single linked node in a linked list.

    Attributes:
        _next (Node[T] | None): The reference to the next node in the linked list.
    """

    _next: Node[T] | None = None

    @property
    def next(self) -> Node[T] | None:
        """
        Get the reference to the next node in the linked list.

        Returns:
            Node[T] | None: The reference to the next node, or None if there is no next node.
        """
        return self._next

    @next.setter
    def next(self, next: Node[T] | None) -> None:
        """
        Setter for the next attribute.

        Args:
            next (Node[T] | None): The reference to the next node, or None if there is no next node.
        """
        self._next = next


@dataclass
class DoubleLinkedNode[T](SingleLinkedNode[T]):
    """
    Represents a double linked node in a linked list.

    Attributes:
        _previous (Node[T] | None): The reference to the previous node in the linked list.
    """

    _previous: Node[T] | None = None

    @property
    def previous(self) -> Node[T] | None:
        """
        Get the reference to the previous node in the linked list.

        Returns:
            Node[T] | None: The reference to the previous node, or None if there is no previous node.
        """
        return self._previous

    @previous.setter
    def previous(self, previous: Node[T] | None) -> None:
        """
        Setter for the previous attribute.

        Args:
            previous (Node[T] | None): The reference to the previous node, or None if there is no previous node.
        """
        self._previous = previous
