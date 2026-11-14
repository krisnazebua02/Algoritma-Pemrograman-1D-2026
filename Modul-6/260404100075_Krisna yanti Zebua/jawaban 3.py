# Fungsi untuk mengevaluasi kelayakan PC
def evaluasi_pc(status, ram):
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


# Membuat list untuk menyimpan data PC
inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

# Input data PC
for i in range(jumlah):
    print("Data PC ke-", i + 1)

    nama = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    # Menyimpan data ke dalam multidimensional list
    inventaris.append([nama, status, ram])


# Evaluasi dan mencetak hasil
print("=== HASIL EVALUASI INVENTARIS PC ===")

for pc in inventaris:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]

    try:
        hasil = evaluasi_pc(status, int(ram))

    except ValueError:
        hasil = "Format RAM Kacau"

    # Manipulasi string untuk format output
    hasil_cetak = '{ "PC": "' + nama + '", "Status": "' + hasil + '" }'

    print(hasil_cetak)