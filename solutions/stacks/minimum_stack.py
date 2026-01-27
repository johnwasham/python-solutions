"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.

"""

from collections import deque

class MinStack:
    d = None
    current_min = None

    def __init__(self):
        self.d = deque()

    def push(self, val: int) -> None:
        if self.current_min is None or val < self.current_min:
            self.current_min = val
        self.d.append(MinItem(val, self.current_min))

    def pop(self) -> None:
        if self.d:
            item = self.d.pop()
            if self.d:
                top = self.d[-1]
                self.current_min = top.min
            else:
                self.current_min = None

    def top(self) -> int:
        if self.d:
            top = self.d[-1]
            return top.val
        else:
            return None

    def getMin(self) -> int:
        if self.d:
            return self.current_min
        else:
            return None


class MinItem:
    val = None
    min = None

    def __init__(self, val, min):
        self.val = val
        self.min = min