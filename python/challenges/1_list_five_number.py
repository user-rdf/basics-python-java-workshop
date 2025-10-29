# 1. Buat list berisi 5 angka
numbers = [10, 25, 7, 40, 15]
print("List awal:", numbers)

# 2. TODO: Tampilkan angka pertama dan terakhir
print("Angka pertama:", numbers[0])
print("Angka terakhir:" ,numbers[4])

# 3. TODO: Tambahkan angka baru (apapun) ke akhir list
numbers.append(60)
print("List setelah ditambah:", numbers)

# 4. TODO: Urutkan list secara descending
reverse_list=numbers[::-1] #atau bisa menggunakan numbers.reverse()

# 5. Tampilkan hasil akhir
print("List urut descending:", reverse_list)
