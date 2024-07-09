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

        Parameters:
        - head: The new head node of the linked list.

        Returns:
        - None

        Raises:
        - AttributeError: If the head attribute is immutable.
        """
        raise AttributeError("Immutable attribute.")

    def insert(self, node: SingleLinkedNode[T]) -> None:
        """
        Inserts a node at the head of the linked list.

        Parameters:
        - node: The node to be inserted.

        Returns:
        - None
        """
        node.next = self.head
        self._head = node

    def remove(self, data: T) -> SingleLinkedNode[T] | None:
        """
        Removes the first occurrence of a node with the specified data from the linked list.

        Parameters:
        - data: The data to be removed.

        Returns:
        - SingleLinkedNode[T] | None: The removed node, or None if the data was not found.
        """
        current, previous, removed = self.head, None, None

        while current is not None:
            if current.data == data:
                removed = current
                try:
                    previous.next = removed.next
                except AttributeError:
                    # NOTE: previous is None.
                    self._head = removed.next
                finally:
                    break

            previous = current
            current = current.next

        return removed
