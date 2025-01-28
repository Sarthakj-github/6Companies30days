'''
For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.
Implement the DataStream class:
DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and false otherwise. If there are less than k integers, the condition does not hold true, so returns false.
'''

class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.n=0

    def consec(self, num: int) -> bool:
        if num!=self.value:
            self.n=0
        else:
            self.n+=1
        if self.n==self.k:
            self.n-=1
            return True
        return False
