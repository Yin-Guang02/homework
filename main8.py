class Robot:
    def __init__(self, name):
        self.name = name

    def introduce_self(self):
        print(f"Hello! My name is {self.name}. I am ready to help Harsh!")

robot1 = Robot("Tom")
robot2 = Robot("Jerry")

robot1.introduce_self()
robot2.introduce_self()