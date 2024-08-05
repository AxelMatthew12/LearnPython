
from Calculator import mini_calculator

def program_penyelesaian_matematika_manual():
    print("||     Program Penyelesaian Matematika Manual    ||")
    print("||   1. Use our Mini Calkulator                  ||")
    print("||   2. Use us for Asking math problem           ||")
    print("===================================================")
    pesan_manual = input("Input : ")

    try:
        pesan_manual = int(pesan_manual)
    except ValueError:
        pesan_manual = None

    if pesan_manual == 1:
        mini_calculator()

    elif pesan_manual == 2:
        print("Penyelesaian tugas matematika dipilih")
        
    else:
        print("Pilihan tidak valid")

def main():
    print("=========== SELAMAT DATANG ===========")
    print("          -------------               ")
    print("||   1. GUNAKAN PERINTAH SUARA      ||")
    print("||   2. GUNAKAN PERINTAH MANUAL     ||")
    print("======================================")
    pesan_utama = input("Input : ")

    try:
        pesan_utama = int(pesan_utama)
    except ValueError:
        pesan_utama = None

    if pesan_utama == 1:
        print("Pilihan Anda adalah 1")
        
    elif pesan_utama == 2:
        program_penyelesaian_matematika_manual()
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
