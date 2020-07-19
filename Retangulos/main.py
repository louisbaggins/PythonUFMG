class Ponto2D:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
        

class Retangulo:
    def __init__(self, esq_sup, dir_inf):
        self.__esq_sup = esq_sup
        self.__dir_inf = dir_inf
        
    @property
    def esq_sup(self):
        return self.__esq_sup
        
    @property
    def dir_inf(self):
        return self.__dir_inf
    
    def calcularArea(self):
        return self.height * self.width
    @property
    def height(self):
        return self.__esq_sup.y - self.__dir_inf.y
    @property
    def width(self):    
        return self.__dir_inf.x - self.__esq_sup.x

    def calcularIntersecao(self, rec):
        if self.__dir_inf.y > rec.__esq_sup.y or self.__esq_sup.x > rec.__dir_inf.x:
            return None
        elif self.__esq_sup.y < rec.__dir_inf.y or self.__dir_inf.x < rec.__esq_sup.x:
            return None
        else:
         return self.calculateIntersectArea(rec)

    def calculateIntersectArea(self, rec):
        y = 0.0
        x = 0.0

        if self.__esq_sup.y > rec.__esq_sup.y:
            y = rec.__esq_sup.y - max(rec.__dir_inf.y, self.__dir_inf.y)
        else:
            y = self.__esq_sup.y - max(rec.__dir_inf.y, self.__dir_inf.y)
        
        if self.__dir_inf.x > rec.__dir_inf.x:
            x = rec.__dir_inf.x - max(rec.__esq_sup.x, self.__esq_sup.x)
        else:
            x = self.__dir_inf.x - max(rec.__esq_sup.x, self.__esq_sup.x)

        return x*y
  
    #Adicione o seu codigo aqui


# esq_sup = Ponto2D(1, 4)
# dir_inf = Ponto2D(5, 0)

# print(esq_sup.x)
# print(esq_sup.y)

# print(dir_inf.x)
# print(dir_inf.y)
# result = Retangulo(esq_sup, dir_inf)
# print (result.calcularArea())




def main():
#  r1_esq_sup = Ponto2D(-6.5, 5.0)
#  r1_dir_inf = Ponto2D(-2.0, 2.5)
#  ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
#  area1 = ret1.calcularArea() 
#  print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
 
#  r2_esq_sup = Ponto2D(2.0, 7.0)
#  r2_dir_inf = Ponto2D(5.0, 4.0)
#  ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
#  area2 = ret2.calcularArea()
#  print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
 

#  r1_esq_sup = Ponto2D(1.0, 4.0)
#  r1_dir_inf = Ponto2D(5.0, 0.0)
#  ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
#  area1 = ret1.calcularArea() 
#  print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
 
#  r2_esq_sup = Ponto2D(4.0, 3.0)
#  r2_dir_inf = Ponto2D(8.0, 0.0)
#  ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
#  area2 = ret2.calcularArea()
#  print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
#  intersecao = ret1.calcularIntersecao(ret2)
#  print(intersecao)

 r1_esq_sup = Ponto2D(-6.5, 5.0)
 r1_dir_inf = Ponto2D(-2.0, 2.5)
 ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
 area1 = ret1.calcularArea() 
 print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
 
 r2_esq_sup = Ponto2D(2.0, 7.0)
 r2_dir_inf = Ponto2D(5.0, 4.0)
 ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
 area2 = ret2.calcularArea()
 print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
 intersecao = ret1.calcularIntersecao(ret2)
 print(intersecao)


if __name__ == "__main__":
    main()