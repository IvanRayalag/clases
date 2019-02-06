#crear una clase personal () personas. py que tenga como atributos 
#nombre, edad y profesion 
# al instanciar la clase tiene que saludar igual que el dino dicinedo sus atributos 

class  persona:
    def __init__(self, nombre, edad, profesion= "ingeniero"):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        print("Hola me llamo", nombre , "tengo" , edad , "soy", profesion)

juancho = persona ("juan", 35)
moncho = persona ("ramon", 20)
