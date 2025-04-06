import math

class Calculadora:

    def exibir_pi(self):
        """Método sem parâmetros e sem retorno"""
        print(math.pi)
    
    def exibir_em_radianos(self, angulo_graus):
        """Método com parâmetro e sem retorno"""
        angulo_em_radiano = angulo_graus/(180*math.pi)
        print(f"O ângulo em radianos é: {angulo_em_radiano}")

    def retornar_pi(self):
        """Método sem parâmetros e com retorno"""
        return (math.pi)

    def retornar_em_radianos(self,angulo_graus):
        """Método com parâmetro e com retorno"""
        angulo_em_radiano = angulo_graus/(180*math.pi)
        return angulo_em_radiano
    

objeto = Calculadora()
objeto.exibir_pi()
objeto.exibir_em_radianos(180)
pi = objeto.retornar_pi()
print(pi)
angulo_radianos = objeto.retornar_em_radianos(180)
print(f"O valor do ângulo em radianos é: {angulo_radianos}")
