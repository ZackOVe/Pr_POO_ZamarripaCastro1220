class Marino():
  def hablar(self):
    print("Hola soy un estudiante de cbtis128 (salvenme)!")
print("")

class Pulpo(Marino):
  def hablar(self):
    print("Hola soy gay (no nnos importa perdedor)!")
print("")

class Foca(Marino):
  def hablar(self,mensaje):
    self.mensaje=mensaje
    print(mensaje)

marino=Marino()
marino.hablar()

pulpo=Pulpo()
pulpo.hablar()

foca=Foca()
foca.hablar("Hola soy racis-!")
print("")