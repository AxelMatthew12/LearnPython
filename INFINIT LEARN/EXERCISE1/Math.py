from Calculator import mini_calculator

class Manual:
    def execute(self):
        print("||     Manual Math Solve program     ||")
        print("||   1. Use The mini Calculator      ||")
        print("||   2. Use us for Solve mathwork    ||")
        print("=======================================")
        ManualMsg = input("Input : ")

        try:
            ManualMsg = int(ManualMsg)
        except ValueError:
            ManualMsg = None

        if ManualMsg == 1:
            mini_calculator()
            # Tambahkan logika untuk mini calculator di sini
        elif ManualMsg == 2:
            print("Solve mathwork selected")
            # Tambahkan logika untuk solve mathwork di sini
        else:
            print("Invalid option")

def main():
    print("=========== WELCOME ===========")
    print("         -------------         ")
    print("||   1.USE VOICE COMMAND     ||")
    print("||   2.USE MANUAL COMMAND    ||")
    print("===============================")
    MsgOne = input("Input : ")

    # Mengonversi input dari string menjadi integer
    try:
        MsgOne = int(MsgOne)
    except ValueError:
        MsgOne = None

    if MsgOne == 1:
        print("Your option is 1")
        # Tambahkan logika untuk Voice Command di sini
    elif MsgOne == 2:
        command = Manual()
        command.execute()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
