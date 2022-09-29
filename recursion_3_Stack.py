class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def size(self):
        return len(self.stack)

    #
    def pop(self):
        if self.size() == 0:
            return self.count
        else:
            self.count += 1
            self.stack.pop()


def len_with_pop_only(array: list) -> int:
    if len(array) == 0:
        return 0
    main_stack = Stack()
    main_stack = array.copy()
    return main_stack.pop()

print(len_with_pop_only([1,2,34]))


# l1 = [1,2,3,4,5,6,7,8]
# l2 = Stack()
# print(l1, l2)
#
# l2 = l1.copy()
# print(l1, l2)
#
# l1.clear()
# print(l1, l2)
