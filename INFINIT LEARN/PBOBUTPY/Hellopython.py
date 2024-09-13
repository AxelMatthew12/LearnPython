import random


def get_user_choice():

    user_input = input("Pilih (Batu, gunting , Kertas):")
    while user_input not in["Batu","gunting","Kertas"]:
        print("Pilihan tidak valid. Coba lagi !. ")
        user_input = input("Pilih (Batu,gunting, Kertas): ")
    return user_input
def get_comp_choice():
    return random.choice(["Batu","gunting", "Kertas"])

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "SERI!"
    elif(user_choice == "Batu" and comp_choice == "scissors") or \
        (user_choice == "gunting" and comp_choice == "Kertas") or \
        (user_choice == "Kertas" and comp_choice == "Batu"):
        return  "Kamu menang!"
    else:
        return "Komputer Menang"

def play_game():
    print("Selamat datang di permainan Batu,Gunting,Kertas!")

    while True:
        user_choice = get_user_choice()
        comp_choice = get_comp_choice()

        print((f"Kamu memilih: {user_choice}"))
        print(f"Komputer memilih: {comp_choice}")

        result = determine_winner(user_choice, comp_choice)
        print(result)

        play_again = input("ingin bermain lagi? (yes/no):").lower()
        if play_again != "yes":
            break

    print("Terima Kasih sudah bermain! ")

if __name__ == "__main__":
    play_game()

