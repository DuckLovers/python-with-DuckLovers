# Kalkulator

print("Selamat Datang di Kalkulator Sederhana")
x = 1
while x > 0: 
    operasi = input("Masukkan operasi       = ")
    if (operasi == "exit"):
        break
    elif operasi != "+" and operasi != "-" and operasi != "*" and operasi != "/" and operasi != "%" and operasi != "%" and operasi != "//" and operasi != "**":
        print("===Input tidak dikenali===")
        continue    

    angka1  = input("Masukkan angka pertama = ") 
    if (angka1 == "exit"):
        break
    elif not angka1.isdecimal():
        print("===Input tidak dikenali===")
        continue
           
    angka2  = input("Masukkan angka kedua   = ")
    if (angka2 == "exit"):
        break
    elif not angka2.isdecimal():
        print("===Input tidak dikenali===")
        continue

    elif operasi == "+":
            hasil = (int(angka1) + int(angka2))
            
    elif operasi == "-":
            hasil = (int(angka1) - int(angka2))
            
    elif operasi == "*":
            hasil = (int(angka1) * int(angka2))
            
    elif operasi == "/":
            hasil = (int(angka1) / int(angka2))
            
    elif operasi == "%":
            hasil = (int(angka1) % int(angka2))
            
    elif operasi == "//":
            hasil = (int(angka1) //int(angka2))
            
    elif operasi == "**":
            hasil = (int(angka1) **int(angka2))

    print(f"Hasil = {hasil}")      

print("Sampai Jumpa")

"""
Catatan
    Break = memaksa loop berhenti
    Continue = memaksa loop mengulang dari awal
"""