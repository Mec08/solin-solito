from personajes import personajes

class personaje():
    def __init__(self,nombre,raza,vida,poder,clase):
        self.nombre=nombre
        self.vida=vida
        self.raza=raza
        self.poder=poder
        self.clase=clase

    def elegirPersonaje(self):
        print("Elije su Raza\n")
        Raza=int(input("1) Humano \n2) Orco"))
        if Raza==1:
            Raza="Humanos"
            print("\nElije su clase: \n1) Guerrrero \n2) Mago \n3) Arquero")
            Clase=int(input("\n->"))
            if Clase==1:
                Clase="Guerrero"
                self.crearPersonaje(Raza,Clase)
            elif Clase==2:
                Clase="Mago"
                self.crearPersonaje(Raza,Clase)
            elif Clase==3:
                Clase="Arquero"
                self.crearPersonaje(Raza,Clase)
            else:
                print("opción no valida")
        if Raza==2:
            Raza="Orcos"
            print("\nElije su clase: \n1) Luchador \n2) Chaman \n3) Jinete")
            Clase=int(input("\n->"))
            if Clase==1:
                Clase="Luchador"
                self.crearPersonaje(Raza,Clase)
            elif Clase==2:
                Clase="Chaman"
                self.crearPersonaje(Raza,Clase)
            elif Clase==3:
                Clase="Jinete"
                self.crearPersonaje(Raza,Clase)
            else:
                print("opción no valida")

    def crearPersonaje(self, raza_selec,clase_selec):
        vida=personajes["Raza"][raza_selec]["Clase"][clase_selec]["Vida"]
        poder=personajes["Raza"][raza_selec]["Clase"][clase_selec]["Poder"]
        nombre=input("\ningresa el nombre de tu personaje")
        new_pj=personaje(nombre=nombre,raza=raza_selec,vida=vida,poder=poder,clase=clase_selec)
        datos={"nombre":new_pj.nombre,
                "raza":new_pj.raza,
                "clase":new_pj.clase,
                "vida":new_pj.vida,
                "poder":new_pj.poder}
        print("el personaje a sido creado con el nombre: {}".format(datos["nombre"]))

class iniciar(personaje):
    def __init__(self):
        self.elegirPersonaje()

iniciar()

        
        
        
        
