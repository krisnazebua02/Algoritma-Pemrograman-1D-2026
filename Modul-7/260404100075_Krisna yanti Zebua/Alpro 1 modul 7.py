
todo = {}

while True:
    print("\n1. Tambah\n2. Tampilkan\n3. Selesaikan\n4. Hapus\n5. Hitung\n6. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tugas = input("Nama tugas: ")
        todo[tugas] = "Belum Selesai"

    elif pilih == "2":
        for tugas, status in todo.items():
            print(tugas, ":", status)

    elif pilih == "3":
        tugas = input("Nama tugas: ")
        if tugas in todo:
            todo[tugas] = "Selesai"
        else:
            print("Tugas tidak ditemukan!")

    elif pilih == "4":
        tugas = input("Nama tugas: ")
        if tugas in todo:
            del todo[tugas]
        else:
            print("Tugas tidak ditemukan!")

    elif pilih == "5":
        print("Selesai:", list(todo.values()).count("Selesai"))
        print("Belum selesai:", list(todo.values()).count("Belum Selesai"))

    elif pilih == "6":
        break

    else:
        print("Pilihan tidak valid!")
