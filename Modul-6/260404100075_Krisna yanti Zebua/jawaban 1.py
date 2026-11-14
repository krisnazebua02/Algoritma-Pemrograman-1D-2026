# Membuat list untuk menyimpan nama calon anggota
anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

# Menampilkan daftar nama anggota
print("Daftar Calon Anggota:")
print(anggota)

# Memeriksa validitas nama anggota
print("Hasil Pemeriksaan Nama:")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

# Menghapus nama yang dicurigai sebagai penyusup
penyusup = input("\nMasukkan nama yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama", penyusup, "tidak ditemukan dalam daftar.")

# Menampilkan daftar akhir
print("Daftar Anggota Setelah Penghapusan:")
print(anggota)

