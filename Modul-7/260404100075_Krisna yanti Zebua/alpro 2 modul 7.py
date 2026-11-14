
playlist = {}

while True:
    print("\n1. Buat Playlist\n2. Tambah Lagu\n3. Tampilkan\n4. Cari Lagu\n5. Hapus Lagu\n6. Hapus Playlist\n7. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        playlist[nama] = {}

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            playlist[nama][judul] = input("Penyanyi: ")
        else:
            print("Playlist tidak ditemukan!")

    elif pilih == "3":
        for nama, lagu in playlist.items():
            print("\n", nama, ":", lagu)

    elif pilih == "4":
        judul = input("Cari lagu: ")
        hasil = False
        for nama, lagu in playlist.items():
            if judul in lagu:
                print(judul, "-", lagu[judul], "|", nama)
                hasil = True
        if not hasil:
            print("Lagu tidak ditemukan!")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
            else:
                print("Lagu tidak ditemukan!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilih == "6":
        nama = input("Nama playlist: ")
        if nama in playlist:
            del playlist[nama]
        else:
            print("Playlist tidak ditemukan!")

    elif pilih == "7":
        break

    else:
        print("Pilihan tidak valid!")
