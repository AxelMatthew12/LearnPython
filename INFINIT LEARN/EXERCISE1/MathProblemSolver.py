# MathProblemSolver.py

class AskaboutFormula:
    def execute(self):
        print("|| 1. ")

class AskaboutProblem:
    def execute(self):
        print("Hello world 1")

class MathSolver:
    def execute(self):
        print("||========== Welcome ==========||")
        print("|| 1. Bertanya terkait rumus ? ||")
        print("|| 2. Bertanya mengenai soal ? ||")
        print("|| 3. Back to Main             ||")
        print("||=============================||")
        input_option = input("Answer: ")

        try:
            input_option = int(input_option)
        except ValueError:
            input_option = None

        if input_option == 1:
            command = AskaboutFormula()
            command.execute()
        elif input_option == 2:
            command = AskaboutProblem()
            command.execute()
        elif input_option == 3:
            from Math import main  # Impor di dalam fungsi untuk menghindari impor melingkar
            main()
        else:
            print("Pilihan tidak valid")
