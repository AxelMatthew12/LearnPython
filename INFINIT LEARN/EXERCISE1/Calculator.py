class PlusOption:
    def execute(self):
        print("Input your number: ")
        input1= input("1st: ")
        input2= input("2nd: ")

        input1 = int(input1)
        input2 = int(input2)

        totalinput = (input1 + input2)
        print("Your result is: "+ str(totalinput))

        print("Are u satisfied?, wanna go again ? (Y/N)")
        inputoption= input("Answer: ")
        if inputoption=="Y":
            command=PlusOption()
            command.execute()
        elif inputoption=="N":
            print("Wanna return to Main Calculator? (Y/N)")
            inputoption2= input("Answer: ")
            if inputoption2 =="Y":
                command=mini_calculator()
                command.execute()
            elif inputoption2 =="N":
                command=exit
                print("ThankYour for Using this Apps :)")

class MinusOption:
    def execute(self):
        print("Input your Number: ")
        input1= input("1st: ")
        input2= input("2nd: ")

        input1 = int(input1)
        input2 = int(input2)

        totalinput= input1-input2
        print("Your result is: "+ str(totalinput))
        
        print("Are u satisfied, wanna try again ? (Y/N)")
        inputoption= input("Answer: ")
        if inputoption=="Y":
            command= MinusOption()
            command.execute()
        elif inputoption=="N":
            print("Wanna back to Calculator? (Y/N)")
            inputoption1=input("Answer: ")
            if inputoption1 =="Y":
                command=mini_calculator()
                command.execute()
            elif inputoption1 =="N":
                command=exit
                print("Thankyou for using the Apps :) ")

class Multiplication:
    def execute(self):
        print("Enter your number: ")
        input1= input("1st: ")
        input2= input("2nd: ")

        input1 = int(input1)
        input2 = int(input2)

        totalinput = input1 * input2
        print("Your Result: "+ str(totalinput))
        print("Are u satisfied, wanna try again ? (Y/N)")
        inputoption= input("Answer: ")
        if inputoption=="Y":
            command= Multiplication()
            command.execute()
        elif inputoption=="N":
            print("Wanna back to Calculator? (Y/N)")
            inputoption1=input("Answer: ")
            if inputoption1 =="Y":
                command=mini_calculator()
                command.execute()
            elif inputoption1 =="N":
                command=exit
                print("Thankyou for using the Apps :) ")


class Distribution:
    def execute(self):
        print("Enter your number: ")
        input1= input("1st: ")
        input2= input("2nd: ")

        input1 = int(input1)
        input2 = int(input2)

        totalinput = input1 / input2
        print("Your Result:  "+ totalinput)
        print("Are u satisfied, wanna try again ? (Y/N)")
        inputoption= input("Answer: ")
        if inputoption=="Y":
            command= Distribution()
            command.execute()
        elif inputoption=="N":
            print("Wanna back to Calculator? (Y/N)")
            inputoption1=input("Answer: ")
            if inputoption1 =="Y":
                command=mini_calculator()
                command.execute()
            elif inputoption1 =="N":
                command=exit
                print("Thankyou for using the Apps :) ")


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
        
