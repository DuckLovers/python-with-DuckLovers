import random

print("Selamat datang di Batu Gunting Kertas")

# Mekanisme
while True:
    # Score
    score_pemain = 0
    score_bot    = 0

    while score_pemain != 3 and score_bot != 3:
        print(f"===Score=== \nPemain \t= {score_pemain} \nBot \t= {score_bot}")

    # Batu Gunting Kertas Input
        pemain = str(input("Batu/Gunting/Kertas \n=>")).lower()
        if pemain != "batu" and pemain != "kertas" and pemain != "gunting":
            print("===Input tidak di kenali===")
            continue

    # Batu Gunting Kertas Bot (1 = Batu ; 2 = Gunting ; 3 = Kertas)
        bot    = random.randint(1,3)
        if bot == 1:
            print("Bot memakai Batu")
            if pemain == "batu":
                print("=Seri=") 
            elif pemain == "gunting":
                print("=Kalah=")
                score_bot += 1
            elif pemain == "kertas":
                print("=Menang=")
                score_pemain += 1
        if bot == 2:
            print("Bot memakai Gunting")
            if pemain == "batu":
                print("=Menang=")
                score_pemain += 1 
            elif pemain == "gunting":
                print("=Seri=")
            elif pemain == "kertas":
                print("=Kalah=")
                score_bot += 1
        if bot == 3:
            print("Bot memakai Kertas")
            if pemain == "batu":
                print("=Kalah=") 
                score_bot += 1
            elif pemain == "gunting":
                print("=Menang=")
                score_pemain += 1
            elif pemain == "kertas":
                print("=Seri=")
    # Score akhir
    if score_pemain > score_bot:
        print("===Selamat anda menang===\n")
    else:
        print("=======Anda Kalah========\n")

    # Menu
    while True:
        akhir = str(input('Ketik "Lanjut" jika ingin melanjutkan \njika ingin berhenti tekan Q \n=>')).lower()
        if akhir != "lanjut" and akhir != "q":
            print("Input tidak di kenali")
        elif akhir == "lanjut":
            break
        elif akhir == "q":
            print("===Terima Kasih Telah Bermain===")
            quit() 
