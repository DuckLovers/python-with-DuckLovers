# Game Tebak Angka 

from random import randint 

nyawa = 3 
angka_rahasia = randint(0,10) 
limit = 0 

print(f"Selamat datang di Game Tebak angka")
while nyawa > limit: 
    print(f"Percobaan anda tersisa {nyawa}")
    jawaban = int(input("Masukkan angka 0-10 = "))
    if jawaban == angka_rahasia:
        print ("Anda Benar")
        break 
    elif nyawa-1 == limit:
        print ("Anda Gagal")
        break
    elif jawaban > angka_rahasia:
        print("Lebih")
        nyawa -= 1
    elif jawaban < angka_rahasia:
        print("Kurang")
        nyawa -= 1




"""# Game Tebak Angka 
from random import randint 
# Mengimpor Library Random untuk membuat angka rahasia secara acak
nyawa = 3 # Jumlah percobaan yang di berikan
angka_rahasia = randint(0,10) # Angka rahasia sebagai jawaban game
limit = 0 # Batas nyawa jika nyawa jadi 0 maka pemain akan gagal

print(f"Selamat datang di Game Tebak angka")
while nyawa > limit: 
# ini menandakan bahwa game akan berjalan 
# jika nyawa lebih besar dari limit
    print(f"Percobaan anda tersisa {nyawa}")
# ini untuk memberitahukan pemain jumlah nyawa yang mereka miliki 
    jawaban = int(input("Masukkan angka 0-10 = "))
# ini untuk menerima angka tebakan dari pemain
    if jawaban == angka_rahasia:
        print ("Anda Benar")
        break
# ini untuk memeriksa apakah angka yang 
# di masukan pemain sama dengan angka rahasia 
    elif nyawa-1 == limit:
        print ("Anda Gagal")
        break
# Jika jawabannya salah maka nyawanya akan di periksa di sini jika 
# nyawanya sudah mencapai limit maka game nya akan selesai 
# dan pemain akan kalah
    elif jawaban > angka_rahasia:
        print("Lebih")
        nyawa -= 1
    elif jawaban < angka_rahasia:
        print("Kurang")
        nyawa -= 1
# ini untuk memberikan bantuan kepada pemain apakah angka yang di masukkan
# itu lebih besar atau kurang dari angka rahasia
"""