# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready in parent")
    
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim is faster")

# child class
class Penguin(Bird):
    
    def __init__(self):
        super().__init__()
        print("Penguin is ready from inheritag")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Runing now")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
    