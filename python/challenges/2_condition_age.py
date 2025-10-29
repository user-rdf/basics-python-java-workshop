# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
while True:  
    umur = int(input("Masukkan umur pengguna: "))
# 2. TODO Tentukan kategori berdasarkan usia
    if umur < 12:
        print("Anak-anak")
    elif 12 < umur < 17:
        print("Remaja")
    elif 18 < umur < 59:
        print("Dewasa")
    elif umur >= 60:
        print("Lansia")
