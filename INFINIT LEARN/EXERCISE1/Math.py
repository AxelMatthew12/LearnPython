# Misalkan mini_calculator ada di file bernama Calculator.py
from Calculator import mini_calculator

def program_penyelesaian_matematika_manual():
    print("||     Program Penyelesaian Matematika Manual     ||")
    print("||   1. Gunakan Kalkulator Mini                  ||")
    print("||   2. Gunakan Kami untuk Menyelesaikan Tugas   ||")
    print("===================================================")
    pesan_manual = input("Input : ")

    try:
        pesan_manual = int(pesan_manual)
    except ValueError:
        pesan_manual = None

    if pesan_manual == 1:
        mini_calculator()
        # Tambahkan logika untuk kalkulator mini di sini
    elif pesan_manual == 2:
        print("Penyelesaian tugas matematika dipilih")
        # Tambahkan logika untuk penyelesaian tugas di sini
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
        # Tambahkan logika untuk Perintah Suara di sini
    elif pesan_utama == 2:
        program_penyelesaian_matematika_manual()
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
