class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")
        print("")
    def resultados(self):
        if self.nota >= 7:
            print("QUE NALGON!")
        else:
            print("No sirves pa nada!")
print("")
estudiante1 = Estudiante("Gayred", 5)
estudiante1.imprimir()
estudiante1.resultados()
print("")
estudiante2 = Estudiante("Fabigod", 7)
estudiante2.imprimir()
estudiante2.resultados()
print("")