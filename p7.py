class Universidad():
  def __init__(self,Nombre):
    self.Nombre=Nombre

class Carerra():
  def carrera(self,especialidad):
    self.especialidad=especialidad

class Estudiante(Universidad,Carerra):
  def datos(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

    print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")
print("")

persona=Estudiante("SEGA")
print("")

persona.carrera("Hacer nada")
print("")

persona.datos("Sonix", 19)
print("")