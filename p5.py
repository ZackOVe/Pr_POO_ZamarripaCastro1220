class Fabrica():
  def __init__(self, llantas, color, precio):
    self._llantas=llantas
    self._color=color
    self._precio=precio

class Moto(Fabrica):
  def cantidad(self):
    print("La cantidad de bateria: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))
    print("")

class Carro(Fabrica):
  def cantidad(self):
    print("La cantidad de bateria: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas,self._color,self._precio))
    print("")

    print("OBJETO = EL AUDIFONO DE DYLAN")
    print("")

moto=Moto(2, "Gris", "$200")
moto.cantidad()
print("")

print("OBJETO = TRABA")
print("")

carro=Carro(4 ,"Negro", "$600")
carro.cantidad()
print("")