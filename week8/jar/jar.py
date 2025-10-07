class Jar:
    def __init__(self, capacity=12):
        if (capacity < 0):
            raise ValueError("Invalid capacity")
        else:
            self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
def main():
    jar1 = Jar()
    print(f"jar1 capacity: {jar1.capacity}")
    jar1.deposit(3)
    jar1.withdraw(1)
    print(f"jar1 size: {jar1.size}")
    print(jar1)

    jar2 = Jar(20)
    print(f"jar2 capacity: {jar2.capacity}")
    jar2.deposit(10)
    jar2.withdraw(5)
    print(f"jar2 size: {jar2.size}")
    print(jar2)

if __name__ == "__main__":
    main()