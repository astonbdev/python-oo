class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial generator from self and start"""
        self.start = start
        self.next = start
    
    def generate(self):
        """Returns current value of next and increments next by 1"""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Sets next to start"""
        self.next = self.start