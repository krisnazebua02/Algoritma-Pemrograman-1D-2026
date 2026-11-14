
# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Input data
undangan.update(input("Masukkan nama undangan (pisahkan koma): ").split(","))
webinar_A.update(input("Peserta Webinar A: ").split(","))
webinar_B.update(input("Peserta Webinar B: ").split(","))

# Operasi himpunan
print("\nSemua peserta:", webinar_A | webinar_B)
print("Hadir di kedua webinar:", webinar_A & webinar_B)
print("Hadir di salah satu webinar:", webinar_A ^ webinar_B)
print("Undangan tidak hadir:", undangan - (webinar_A | webinar_B))
