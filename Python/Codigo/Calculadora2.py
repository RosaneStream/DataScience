#cada metodo recebe um valor diferente
class Calculadora:
    def __init__(self) -> None:
        pass
        
    def soma(self, num_a, num_b):
        return num_a+num_b

    def subtracao(self, num_a, num_b):
        return num_a-num_b

    def multiplicacao(self, num_a, num_b):
        return num_a*num_b

    def divisao(self,num_a, num_b):
        return num_a/num_b

calculadora = Calculadora()
print(calculadora.soma(1,2))
print(calculadora.subtracao(3,4))
print(calculadora.divisao(5,6))
print(calculadora.multiplicacao(7,8))   

