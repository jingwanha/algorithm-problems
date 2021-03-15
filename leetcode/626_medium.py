# https://leetcode.com/problems/design-circular-queue/
from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        self.circular_queue = [None]*k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.circular_queue[self.rear] is None:
            self.circular_queue[self.rear] = value
            self.rear = (self.rear+1) % self.max_len # 최댓값 범위 내에서 인덱스가 유지되도록

            return True

        else: return False

    def deQueue(self) -> bool:
        if self.circular_queue[self.front] is not None:
            self.circular_queue[self.front] = None
            self.front = (self.front+1)%self.max_len
            return True

        else: return False

    def Front(self) -> int:
        if self.circular_queue[self.front] is None: return -1
        else : return self.circular_queue[self.front]

    def Rear(self) -> int:
        if self.circular_queue[self.rear-1] is None : return -1
        else: return self.circular_queue[self.rear-1]

    def isEmpty(self) -> bool:
        if (self.front == self.rear) and self.circular_queue[self.front] is None: return True
        else: return False

    def isFull(self) -> bool:
        if (self.front == self.rear) and self.circular_queue[self.front] is not None: return True
        else: return False

if __name__=='__main__':
    # Your MyCircularQueue object will be instantiated and called as such:
    k = 5
    value = 10

    obj = MyCircularQueue(k)
    param_1 = obj.enQueue(value)
    # param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()

    print (param_1)
    # print(param_2)
    print(param_3)
    print(param_4)
    print(param_5)
    print(param_6)