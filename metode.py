#Kelompok 23
#
#
#Muhamad Ibnu Fadhil - 21120121120023 - Shift 2
#Zidane Romandhon Putra - 21120121140115 - Shift 2

class metode: #print modal
    #init method
    def __init__(self, harga):
        self.harga = harga

    #self parameter
    def trims(self):
        print("Terimakasih sudah menggunakan program kel 23")

    #method dengan parameter
    def selesai(self, waktu):
        print("Program akan selesai dalam :")
        while waktu > 0:
            print(waktu)
            waktu -= 1
