class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top = -1

    def push(self, val):
        self.stack.append(val)
        self.top += 1
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.top == -1:
            return None
        val = self.stack.pop()
        self.top -= 1
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top_value(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def min_value(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Minimum")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        stack.push(val)
        print("Value pushed to stack")

    elif choice == 2:
        val = stack.pop()
        if val is None:
            print("Stack is empty")
        else:
            print("Popped value:", val)

    elif choice == 3:
        val = stack.top_value()
        if val is None:
            print("Stack is empty")
        else:
            print("Top value:", val)

    elif choice == 4:
        val = stack.min_value()
        if val is None:
            print("Stack is empty")
        else:
            print("Minimum value:", val)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
