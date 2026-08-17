"""
Q4 (Basic): Create a Counter class that increments and resets a count using methods.
"""

class Counter:

    def __init__(self,start=0):
        self.num=start

    def increment(self):
        self.num += 1

    def reset(self):
        self.num = 0

    def show(self):
        print(f"The value of current count :{self.num}")

    def run(self):
        while True:
            print("1 --> Increament | 2 --> Reset |3 --> Show |4 --> Exit")
            choice = input("Enter :")
            if choice == "1":
                self.increment()
            elif choice == "2":
                self.reset()
            elif choice == "3":
                self.show()
            elif choice == "4":
                break
            else :
                print("Invalid syntax")
            
obj = Counter(12)
obj.run()