class Instrumento:

    def __init__(self, nombre, armonia, melodia, afinacion):
        self.nombre = nombre
        self.armonia = armonia
        self.melodia = melodia
        self.afinacion = afinacion

    def percusion(self, diametro, frecvibra):
        self.diametro = diametro
        self.frecvibra = frecvibra

        if diametro < 0 or frecvibra < 0:
            raise ValueError('No hay diametros ni frecuencias negativas')
        return f'{self.nombre} tiene un diametro de {diametro} cm y una frecuencia de vibracion de {frecvibra} Hz'

    def cuerdas(self, n_cuerdas, a_c_1):
        self.n_cuerdas = n_cuerdas
        self.a_c_1 = a_c_1


        if n_cuerdas < 0:
            raise ValueError('No hay cuerdas negativas')
        return f'{self.nombre} tiene {n_cuerdas} cuerdas y estan afinadas en {a_c_1} respectivamente'

    def cantidad(self, numero):
        if numero < 0:
            raise ValueError('No existen cantidades negativas')
        else:
            return f'{self.nombre} cuenta con {numero} ejemplares'


tambor = Instrumento('Tambor', 'I', 'Jazz', 'F')
guitarra = Instrumento('Guitarra', 'IV', 'Blues', 'B')

# print(tambor.percusion('30 cm', '40 Hz'))
# print(guitarra.cuerdas('6', 'C', 'AM', 'D', 'F', 'G', 'DM'))
# print(guitarra.cantidad(5))

    # def descripcion(self):
    #     print(self.nombre, "tiene una armonia", self.armonia, "una melodia", self.melodia, "y esta afinado en", self.afinacion)