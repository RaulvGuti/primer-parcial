from node import Node


class List:
    def __init__(self):
        self.size = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
            self.head.previous = self.tail
        else:
            new_node.next = self.head
            new_node.previous = self.tail
            self.head.previous = new_node
            self.tail.next = new_node
            self.head = new_node
            self.size += 1

    def eliminar(self, data):
        if self.is_empty():
            return

        current = self.head
        while current.data.grado != data:
            current = current.next
            if current == self.head:
                return

        if current == self.head:
            self.head = current.next
            self.tail.next = self.head
            self.head.previous = self.tail
        elif current == self.tail:
            self.tail = current.previous
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

    def search_data(self, data):
        if self.is_empty():
            return None

        current = self.head
        while current.data != data:
            current = current.next
            if current == self.head:
                return None

        else:
            self.head = current

        return current.data

    def update(self, data_old, data_new):
        if self.is_empty():
            return
        current = self.head
        while current.data != data_old:
            current = current.next
            if current == self.head:
                return
        current.data = data_new

    def transversal(self):
        if self.is_empty():
            print("La lista está vacía.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
