class penjumlahan :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        
    def lakukanOperasi(self) :
        print("nilai x : ", self.x)
        print("nilai y : ", self.y)
        print("Hasil penjumlahan : ", self.x+self.y)
        
        
class perkalian :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        
    def lakukanOperasi(self) :
        print("nilai x : ", self.x)
        print("nilai y : ", self.y)
        print("Hasil penjumlahan : ", self.x*self.y)
        
class pembagian :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        
    def lakukanOperasi(self) :
        print("nilai x : ", self.x)
        print("nilai y : ", self.y)
        print("Hasil penjumlahan : ", self.x/self.y)     
        
        
def judul():
    print("CALCULATOR SANGAT SEDERHANA\n\n")