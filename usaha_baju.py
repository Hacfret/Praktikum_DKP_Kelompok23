#Kelompok 23
#
#Farah Gesty Amandari - 21120121140112 - Shift 2
#Muhamad Ibnu Fadhil - 21120121120023 - Shift 2
#Zidane Romandhon Putra - 21120121140115 - Shift 2

from metode import *
print("Selamat datang di Tugas program Kelompok 23\n")
def listBaju(): #fungsi list baju no return
    print("""
     -------------------------------------
    Simulasi harga total modal pakaian
    Persiapkan uang modal!
    Daftar list pakaian dan harga-nya :
    1 : Kaos Polo\t - Rp. 50.000
    2 : Kemeja\t\t - Rp. 80.000
    3 : Baju Batik\t - Rp. 65.000
    4 : Celana\t\t - Rp. 70.000
    5 : Rok\t\t - Rp. 55.000
    0 : Batal
    ------------------------------------
    """)


def opsiBaju(opsi): #fungsi opsi baju dengan return berparameter
    switcher={
        1: "Kaos polo \t - Rp. 50.000",
        2: "Kemeja \t - Rp. 80.000",
        3: "Baju Batik \t - Rp. 65.000",
        4: "Celana \t - Rp. 70.000",
        5: "Rok \t - Rp. 55.000",
        0: "Program selesai",
        }
    return switcher.get(opsi, "Kode tersebut salah")


def hargaBaju(opsi): #fungsi harga baju dengan return berparameter
    if opsi == int(1):
        harga = int(50000)
        return harga
    elif opsi == 2:
        harga = int(80000)
        return harga
    elif opsi == 3:
        harga = int(65000)
        return harga
    elif opsi == 4:
        harga = int(70000)
        return harga
    elif opsi == 5:
        harga = int(55000)
        return harga
    else:
        print("Opsi anda salah! ")


def totalModal():
    global total 
    total = 0
    while True:
        listBaju()
        a = int(input("Masukkan kode baju : "))
        print(opsiBaju(a))
        list = [opsiBaju(a)]
        q = int(input("Masukkan kuantitas baju : "))
        totalAwal = hargaBaju(a) * q
        total = total + totalAwal
        print("Total harga modal baju : ", total)
        lanjut = int((input("Apakah anda masih ingin menambahkan baju lagi? : (1. Iya/ 0. Tidak) : ")))
        if lanjut != 1:
            print("Total harga modal baju : " , total)
            break

    return total


def diskon(totalByr):
    if totalByr > 200000:
            totalByr = totalByr * 0.95 #diskon 5%
    elif totalByr > 500000:
            totalByr = totalByr * 0.90 #diskon 10%
    elif totalByr > 1000000:
            totalByr = totalByr * 0.20 #diskon 20%
    else:
            totalByr = totalByr
    return totalByr



panggil = metode(totalModal())
print("total harga dengan diskon : " , diskon(total))
panggil.trims()
panggil.selesai(5)
input("ENTER untuk selesai")
