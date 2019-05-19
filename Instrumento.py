class Instrumento:

    def __init__(self, nombre, armonia, melodia, afinacion):
        self.nombre = nombre
        self.armonia = armonia
        self.melodia = melodia
        self.afinacion = afinacion

    def percusion(self, diametro, frecvibra):
        self.diametro = diametro
        self.frecvibra = frecvibra
        return f'{self.nombre} tiene un diametro de {diametro} y una frecuencia de vibracion de {frecvibra}'

    def cuerdas(self, n_cuerdas, a_c_1, a_c_2, a_c_3, a_c_4, a_c_5, a_c_6):
        self.n_cuerdas = n_cuerdas
        self.a_c_1 = a_c_1
        self.a_c_2 = a_c_2
        self.a_c_3 = a_c_3
        self.a_c_4 = a_c_4
        self.a_c_5 = a_c_5
        self.a_c_6 = a_c_6
        return f'{self.nombre} tiene {n_cuerdas} cuerdas y estan afinadas en {a_c_1}, {a_c_2}, {a_c_3}, {a_c_4}, {a_c_5}, {a_c_6} respectivamente'


tambor = Instrumento('Tambor', 'I', 'Jazz', 'F')
guitarra = Instrumento('Guitarra', 'IV', 'Blues', 'B')

print(tambor.percusion('30 cm','40 Hz'))
print(guitarra.cuerdas('6','C','AM','D','F','G','DM'))

    # def descripcion(self):
    #     print(self.nombre, "tiene una armonia", self.armonia, "una melodia", self.melodia, "y esta afinado en", self.afinacion)