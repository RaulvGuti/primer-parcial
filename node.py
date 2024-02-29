class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None
        self.previous: Node | None = None

    def return_data(self):
        return self.data
