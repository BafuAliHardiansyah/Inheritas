class Bunga(object):
    def __init__(self,w,m):
        self.warna= w
        self.mekar= m
    def cetakData(self):
        print("warna\t:", self.warna)
        print("mekar\t:", self.mekar)

# mendefinisikan kelas turunan(subclass)
class BungaAnggrek (Bunga):
    def __init__(self,w,m,h):
        self.warna= w
        self.mekar= m
        self.harga= h

    def cetakData(self):
        print("warna\t:", self.warna)
        print("mekar\t:", self.mekar)
        print("harga\t:",self.harga)
def main():
    # membuat objek Bunga anggrek
    bungaAnggrek1 = BungaAnggrek("3 macam" , "3 bulan", "20k")

    #menggunakan objek
    bungaAnggrek1.cetakData()
    

if __name__ == "__main__":
   main()
        
