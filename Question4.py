class Stack:
    def __init__(self):
        self.queue = []

    def push(self, data):
        s = len(self.queue)
        self.queue.append(data)
        for i in range(s):
            x = self.queue.pop(0)
            self.queue.append(x)

    def pop(self):
        if not self.queue:
            return "Stack is empty."
        return self.queue.pop(0)

stack = Stack()

while True:
    action = input("What would you like to do? push/pop/quit\n")
    if action == "push":
        data = int(input("Enter the value to push: "))
        stack.push(data)
    elif action == "pop":
        data = stack.pop()
        print("Popped value: ", data)
    elif action == "quit":
        break
    else:
        print("Invalid action.")
