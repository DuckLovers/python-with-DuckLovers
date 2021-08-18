# Berat Badan Ideal kalkulator

while True:
    gender = input("Masukkan jenis kelamin anda (pria/wanita) =")
    if gender.lower() != "pria" and gender.lower() != "wanita":
        print("Jenis kelamin tidak terdefinisi")
        continue
    tinggi = float(input("Masukkan tinggi badan anda (cm) ="))
    if gender.lower() == "pria":
        hasil = ( (tinggi - 100) - ( (tinggi - 100)*(10 / 100) ) )
        print(f"Berat badan ideal anda adalah {hasil} Kg")
    elif gender.lower() == "wanita":
        hasil = ( (tinggi - 100) - ( (tinggi - 100)*(15 / 100) ) )
        print(f"Berat badan ideal anda adalah {hasil} Kg")
    break