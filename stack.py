class Stack:
    def __init__(self):
        self._data = [None] * 2
        self.size = 0
        self._front = 0

    def push(self, obj):
        if len(self._data) == self.size:
            self. _resizing(len(self._data) * 2)
        self._data[self._front] = obj
        self._front += 1
        self.size += 1

    def pop(self):
        if self._isEmpty():
            raise ValueError("List is empty pop not allowed")
        self._front -= 1
        self._data[self._front] = None
        self.size -= 1

    def _isEmpty(self):
        return self.size == 0

    def _resizing(self, size):
        newList = self._data
        self._data = [None] * size
        for i in range(len(newList)):
            self._data[i] = newList[i]

    def __str__(self):
        return f"Data: {self._data} \nSize: {self.size}"


if __name__ == "__main__":
    lls = Stack()
    lls.push("data1")
    lls.push("data2")
    lls.push("data3")
    lls.push("data4")
    lls.push("data5")
    print(lls)