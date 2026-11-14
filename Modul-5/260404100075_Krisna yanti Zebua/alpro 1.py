def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Masukkan hari ke-N: "))

if hari > 0:
    print("Jumlah pelanggan pada hari ke-", hari, "adalah", fibonacci(n), "orang")
else:
    print("Input harus berupa bilangan bulat positif!")

# fibonacci(hari)