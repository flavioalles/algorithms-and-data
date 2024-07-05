from dataclasses import dataclass
from src.data.nodes import SingleLinkedNode


@dataclass
class LinkedList[T]:
    """
    Represents a linked list.

    Attributes:
        _head (SingleLinkedNode[T] | None): The head of the linked list.
    """

    _head: SingleLinkedNode[T] | None = None

    @property
    def head(self) -> SingleLinkedNode[T] | None:
        """
        Get the head of the linked list.

        Returns:
            SingleLinkedNode[T] | None: The head of the linked list.
        """
        return self._head

    @head.setter
    def head(self, head: SingleLinkedNode[T] | None) -> None:
        """
        Setter for the head attribute.
        """
        self._head = head
