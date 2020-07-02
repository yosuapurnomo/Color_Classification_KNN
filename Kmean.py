# from builtins import print

import numpy as np
import pandas as pd


class kmean:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.df = pd.read_excel('warna.xlsx', header=0, index_col=0)
        print(self.df)
        # Average Merah
        self.R_merah = self.df['R'][self.df['Warna'] == 'merah'].mean()
        self.G_merah = self.df['G'][self.df['Warna'] == 'merah'].mean()
        self.B_merah = self.df['B'][self.df['Warna'] == 'merah'].mean()
        # Avarega Hijau
        self.R_hijau = self.df['R'][self.df['Warna'] == 'hijau'].mean()
        self.G_hijau = self.df['G'][self.df['Warna'] == 'hijau'].mean()
        self.B_hijau = self.df['B'][self.df['Warna'] == 'hijau'].mean()
        # Average Biru
        self.R_biru = self.df['R'][self.df['Warna'] == 'biru'].mean()
        self.G_biru = self.df['G'][self.df['Warna'] == 'biru'].mean()
        self.B_biru = self.df['B'][self.df['Warna'] == 'biru'].mean()
        # Average kuning
        self.R_kuning = self.df['R'][self.df['Warna'] == 'kuning'].mean()
        self.G_kuning = self.df['G'][self.df['Warna'] == 'kuning'].mean()
        self.B_kuning = self.df['B'][self.df['Warna'] == 'kuning'].mean()
        # Average Biru
        self.R_putih = self.df['R'][self.df['Warna'] == 'putih'].mean()
        self.G_putih = self.df['G'][self.df['Warna'] == 'putih'].mean()
        self.B_putih = self.df['B'][self.df['Warna'] == 'putih'].mean()

        self.Hasil = 0

    def check(self):
        warna = ""
        for i in range(len(self.df)):
            if [self.df.loc[i][0], self.df.loc[i][1], self.df.loc[i][2]] == [self.r, self.g, self.b]:
                print("Data sudah ada diDataSet")
                warna = self.df.loc[i][3]
                break
        else:
            print("Data Belum ada diDataset")
            warna = self.testing()
            new_rows = {'R':self.r, 'G':self.g, 'B':self.b, 'Warna':warna}
            self.df = self.df.append(new_rows, ignore_index=True)
            self.df.to_excel('warna.xlsx')
        return warna

    def testing(self):
        may_merah = (abs((self.r - self.R_merah)) + abs((self.g - self.G_merah)) + abs((self.b - self.B_merah)))
        may_hijau = (abs(self.r - self.R_hijau) + abs((self.g - self.G_hijau)) + abs((self.b - self.B_hijau)))
        may_biru = (abs(self.r - self.R_biru) + abs((self.g - self.G_biru)) + abs((self.b - self.B_biru)))
        may_kuning = (abs(self.r - self.R_kuning) + abs((self.g - self.G_kuning)) + abs((self.b - self.B_kuning)))
        may_putih = (abs(self.r - self.R_putih) + abs((self.g - self.G_putih)) + abs((self.b - self.B_putih)))

        self.Hasil = np.array([round(may_merah, 2), round(may_hijau, 2),
                               round(may_biru, 2), round(may_kuning, 2),
                               round(may_putih, 2)]).argmin() + 1
        print("\nHasil Perhitungan K-Mean : \nMerah : ", may_merah,
              "     Hijau : ", may_hijau,
              "     Biru : ", may_biru,
              "     Kuning : ", may_kuning,
              "     Putih : ", may_putih, "\n")

        print(self.Hasil)
        warna = self.Finis()
        return warna

    def Finis(self):
        # 1 = Merah     2 = Hijau      3 = Biru     4 = Kuning      5 = Putih
        if (self.Hasil == 1):
            warna = "Merah"
        elif (self.Hasil == 2):
            warna = "Hijau"
        elif (self.Hasil == 3):
            warna = "Biru"
        elif (self.Hasil == 4):
            warna = "Kuning"
        elif (self.Hasil == 5):
            warna = "Putih"
        return warna

