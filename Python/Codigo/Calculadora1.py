#a classe recebe os mesmos valores para todos os metodos
class Calculadora:
    def __init__(self, num1, num2):
        self.num_a = num1
        self.num_b = num2

    def soma(self):
        return self.num_a+self.num_b
    def subtracao(self):
        return self.num_a-self.num_b
    def multiplicacao(self):
        return self.num_a*self.num_b
    def divisao(self):
        return self.num_a/self.num_b

if __name__ == 'main':
    calculadora = Calculadora(1,2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())   

