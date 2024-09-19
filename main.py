print("========================================")
print("IMPLEMENTASI MTK BY MUHAMMAD AINUL FUADY")
print("========================================")


def hitung_kecepatan():
    print("hitung kecepatan!")
    jarak = float(input("masukan jarak: "))
    waktu = float(input("masukan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan, "\n")


def luas_segitiga():
    print("hitung segitiga!")
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * (alas * tinggi)
    print("luas segitiga adalah: ", luas)


def luas_balok():
    print("hitung luas balok!")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
    print("luas balok adalah: ", luas)


def luas_bola():
    print("hitung luas bola!")
    r = float(input("masukan jari-jari: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 4 * 3.14 * (r**2)
    print("luas bola adalah: ", luas)


while True:
    userInput = int(input(
        "pilih rumus yang akan di pakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3.luas_balok\n4.luas bola\n\n0.keluar program\n\npilih nomer berapa: "))
    if (userInput == 1):
        hitung_kecepatan()
    elif (userInput == 2):
        luas_segitiga()
    elif (userInput == 3):
        luas_balok()
    elif (userInput == 4):
        luas_bola()
    else:
        break
