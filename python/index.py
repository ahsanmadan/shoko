class Orang:

    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print('')

    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')


class Pelajar (Orang):
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah


class Pekerja (Orang):
    def __init__(self, nama, asal, tempat_kerja):
        Orang.__init__(self, nama, asal)
        self.tempat_kerja = tempat_kerja


deni = Pelajar('Deni', 'Makassar', 'SMA Negeri 1 Makassar')
deni.perkenalan()
print(f'Saya sekolah di {deni.sekolah}')

budi = Pekerja('Budi', 'Pontianak', 'Google')
budi.perkenalan()
print(f'Saya bekerja di {budi.tempat_kerja}')
