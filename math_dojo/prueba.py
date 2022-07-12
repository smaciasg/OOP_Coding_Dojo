class MatematicasDojo:

    def __init__(self):
        self.resultado = 0

    def add(self, num, *numrs):
        self.resultado += num
        for i in numrs:
            self.resultado += i
        return self
    
    def sustrac(self, num, *numrs):
        self.resultado -= num
        for i in numrs:
            self.resultado -= i
        return self

