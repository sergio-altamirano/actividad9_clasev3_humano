print("actividad 9 clase humano")
print("sergio Altamirano  mat:22308051281041")
# zona de clases
class Humano1041:
    # zona de atributos dentro de la clase
    edad=0
    genero="no difinido"
    peso=0
    estatura=0
    color_pelo="no definido"
    nacimiento="0"

    #zona de funciones dentro de la clase
    def correr1041(self,n):
        print(f"{n} esta corriendo uff.....")

    def comiendo1041(self,n):
        print(f"{n} esta comiendo")

    def durmiendo1041(self,n):
        print(f"{n} esta durmiendo")

    def jugando1041(self,n):
        print(f"{n} esta jugando")

    def trabajar1041(self,n):
        print(f"{n} esta trabajando")

    # zona de creacion de objetos
sergio=Humano1041()
leslie=Humano1041()
    #zona de usando objeto
print("-----------------------------")
print("Resultados para  sergio")
print("-------------------------------")
sergio.edad=17
sergio.genero="masculino"
sergio.peso=90
sergio.estatura=1.78
sergio.color_pelo="negro"
sergio.nacimiento="27 de junio del 2007"
print(f"edad: {sergio.edad}")
print(f"genero: {sergio.genero}")
print(f"peso: {sergio.peso} kg")
print(f"estatura: {sergio.estatura} metros")
print(f"nacimiento: {sergio.nacimiento}")
print(f"color de pelo: {sergio.color_pelo}")
sergio.correr1041("sergio")
sergio.comiendo1041("sergio")
sergio.durmiendo1041("sergio")
sergio.jugando1041("sergio")
sergio.trabajar1041("sergio")

print("-----------------------------------------------")
print("Resultado de leslie")
leslie.edad=17
leslie.genero="femenino"
leslie.peso=70
leslie.estatura=1.70
leslie.nacimiento="2 de mayo del 2007"

print(f"edad: {leslie.edad}")
print(f"genero: {leslie.genero}")
print(f"peso: {leslie.edad} kg")
print(f"estatura: {leslie.estatura} metros")
print(f"nacimiento: {leslie.nacimiento}")

leslie.correr1041("leslie")
leslie.comiendo1041("leslie")
leslie.durmiendo1041("leslie")
leslie.jugando1041("leslie")