# Turn Base Strategy Game

import random 

# Charakter Stat
p_health = 30
p_attack = 10
p_block  = 10
# Enemy A Stat
ea_health = 20
ea_attack = 6
ea_block  = 5
# Enemy B Stat
eb_health = 20
eb_attack = 6
eb_block  = 5

# Mekanisme
print("Selamat Datang di Turn Base Strategy Game")
while True:
    # Reset Sistem
    player_menyerang_a = False
    player_menyerang_b = False
    player_bertahan    = False
    bot_a_menyerang    = 0
    bot_b_menyerang    = 0

    # Status
    print(f"HP kamu\t\t = {p_health}")
    if ea_health > 0:
        print(f"HP Musuh A\t = {ea_health}")
    if eb_health > 0:
        print(f"HP Musuh B\t = {eb_health}")

    # Bot RNG (Random Number Generator) 
    rng_a = random.randint(1,10)
    rng_b = random.randint(1,10)

    # Bot mekanisme (Menyerang == 1 dan Bertahan == 0)
    if ea_health > 0:
        if rng_a % 2 == 0:
            print("Musuh A berniat menyerang")
            bot_a_menyerang = 1
        else:
            print("Musuh A berniat bertahan")
            bot_a_menyerang = 0
    if eb_health > 0:
        if rng_b % 2 == 0:
            print("Musuh B berniat menyerang")
            bot_b_menyerang = 1
        else:
            print("Musuh B berniat bertahan")
            bot_b_menyerang = 0

    # Player input
    perintah = input("Serang/Bertahan\n=>").lower()
    if perintah == "serang":
        if ea_health > 0 and eb_health > 0:    
            serangan = input("Musuh A/B?\n=>").lower()
            if serangan == "a":
                print("Kamu menyerang musuh A")
                player_menyerang_a = True
            else:
                print("Kamu menyerang musuh B")
                player_menyerang_b = True
        elif ea_health > 0:
            print("Kamu menyerang musuh A")
            player_menyerang_a = True
        elif eb_health > 0:
            print("Kamu menyerang musuh B")
            player_menyerang_b = True
    else:
        print("Kamu Bertahan")
        player_bertahan = True

    # Mekanisme Player menyerang

    ## Menyerang Musuh A
    if player_menyerang_a == True:
        if bot_a_menyerang == 0:
            player_damage = p_attack - ea_block
            if player_damage <= 0:
                print("Serangan Berhasil di tahan")
            elif player_damage > 0:
                print(f"Serangan yang di terima musuh A adalah = {player_damage}")
                ea_health -= player_damage     
        else:
            player_damage = p_attack 
            print(f"Serangan yang di terima musuh A adalah = {player_damage}")
            ea_health -= player_damage
        # Memeriksa apakah ada musuh yang mati (HP di bawah 0)
        if ea_health <= 0:
            print("Musuh A berhasil dikalahkan")
            bot_a_menyerang == 0
    
    ## Menyerang Musuh B
    elif player_menyerang_b == True:
        if bot_b_menyerang == 0:
            player_damage = p_attack - eb_block
            print(f"Serangan yang di terima musuh B adalah = {player_damage}")
            eb_health -= player_damage     
        else:
            player_damage = p_attack 
            print(f"Serangan yang di terima musuh B adalah = {player_damage}")
            eb_health -= player_damage
        # Memeriksa apakah ada musuh yang mati (HP di bawah 0)
        if eb_health <= 0: 
            print("Musuh B berhasil dikalahkan")
            bot_b_menyerang == 0

        
    # Mekanisme bot menyerang

    ## Jumlah musuh menyerang
    total_attack = bot_a_menyerang + bot_b_menyerang 

    ## Mekanisme serangan
    if total_attack == 1: # Jika hanya ada 1 bot menyerang
        if player_bertahan: # Jika Player bertahan
            if bot_a_menyerang == 1:
                bot_damage = ea_attack - p_block
                if bot_damage > 0: 
                    print(f"Serangan yang di terima adalah = {bot_damage}")
                    p_health -= bot_damage
                else:
                    print("Serangan berhasil di tahan")
            elif bot_b_menyerang == 1:
                bot_damage = eb_attack - p_block
                if bot_damage > 0: 
                    print(f"Serangan yang di terima adalah = {bot_damage}")
                    p_health -= bot_damage
                else:
                    print("Serangan berhasil di tahan")
        else: # Jika player tidak bertahan
            if bot_a_menyerang == 1:
                bot_damage = ea_attack
                print(f"Serangan yang di terima adalah = {bot_damage}")
                p_health -= bot_damage
            elif bot_b_menyerang == 1:
                bot_damage = eb_attack
                print(f"Serangan yang di terima adalah = {bot_damage}")
                p_health -= bot_damage
    elif total_attack == 2:#Jika ada 2 bot menyerang
        if player_bertahan: # Jika player bertahan
            bot_damage = (ea_attack + eb_attack) - p_block
            if bot_damage > 0:
                print(f"Serangan yang di terima adalah = {bot_damage}")
                p_health -= bot_damage
            else:
                print("Serangan berhasil di tahan")
        else: # Jika player tidak bertahan
            bot_damage = ea_attack + eb_attack
            print(f"Serangan yang di terima adalah = {bot_damage}")
            p_health -= bot_damage

    # Permainan Selesai, jika semua musuh di kalahkan atau HP player <= 0
    if (ea_health <= 0 and eb_health <= 0) or p_health <= 0:
        if (ea_health <= 0 and eb_health <= 0):
            print("=====Selamat Anda Menang=====")
        elif p_health <= 0:
            print("=========Anda Kalah=========")

        quit()
