asisten_awal = []

while True:
    nama = input("Masukkan nama asisten (ketik cukup untuk berhenti): ")

    if nama.lower() == "cukup":
        break

    asisten_awal.append(nama)

# Mengunci data asisten awal menjadi Tuple
asisten_awal = tuple(asisten_awal)


# Input satu asisten tambahan
tambahan = input("\nMasukkan nama asisten tambahan: ")

# Menggabungkan data ke dalam wadah baru
asisten_akhir = asisten_awal + (tambahan,)


# Input nama-nama hari tugas
hari_tugas = []

while True:
    hari = input("Masukkan hari tugas (ketik cukup untuk berhenti): ")

    if hari.lower() == "cukup":
        break

    hari_tugas.append(hari)

# Mengunci data hari menjadi Tuple
hari_tugas = tuple(hari_tugas)


nama_pengecualian = input("\nMasukkan nama asisten yang dikecualikan: ")
hari_pengecualian = input("Masukkan hari yang dikecualikan: ")


print("\n=== JADWAL SHIFT ASISTEN LABORATORIUM ===")

for nama in asisten_akhir:
    for hari in hari_tugas:

        if nama == nama_pengecualian and hari == hari_pengecualian:
            continue

        print(nama, "-", hari)

print("\nPenjadwalan selesai.")