class PlusOption:
    def execute(self):
        print("Hello world")

class MinusOption:
    def execute(self):
        print("Hello world")

class Multiplication:
    def execute(self):
        print("Hello world")

class Distribution:
    def execute(self):
        print("Hello world")

def mini_calculator():
    print("\t|| CALCULATOR ||")
    print("\t||============||")
    print("\t||   CHOOSE   ||")
    print("\t||     +      ||")
    print("\t||     -      ||")
    print("\t||     *      ||")
    print("\t||     /      ||")
    print("\t||============||")
    
    choice = input("\t:")
    
    if choice == "+":
        command = PlusOption()
        command.execute()
    elif choice == "-":
        command = MinusOption()
        command.execute()
    elif choice == "*":
        command = Multiplication()
        command.execute()
    elif choice == "/":
        command = Distribution()
        command.execute()
        
