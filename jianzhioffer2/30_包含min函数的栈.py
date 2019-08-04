class stack_with_min:
    def __init__(self):
        self.data = []
        self.min_data = []


    def push(self,value):
        self.data.append(value)

        if len(self.min_data) > 0 and  value > self.min_data[-1]:
            self.min_data.append(self.min_data[-1])
        else:
            self.min_data.append(value)

    def pop(self):
        if len(self.data) != 0 and len(self.min_data) != 0:
            self.data.pop()
            self.min_data.pop()

    def min(self):
        if len(self.min_data) == 0:
            print("no data")
        else:
            return (self.min_data[-1])


if __name__ == "__main__":
    stack = stack_with_min()
    stack.push(3)
    print(stack.data, "  ", stack.min())
    stack.push(4)
    print(stack.data, "  ", stack.min())
    stack.push(2)
    print(stack.data, "  ", stack.min())
    stack.push(1)
    print(stack.data, "  ", stack.min())
    stack.pop()
    print(stack.data, "  ", stack.min())
    stack.pop()
    print(stack.data, "  ", stack.min())
    stack.push(0)
    print(stack.data, "  ", stack.min())