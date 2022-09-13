class Televisao:
    def __init__(self):
        self.ligada= False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada= False
        else:
            self.ligada= True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
    
    def diminui_canal(self):
        if self.ligada:
          self.canal -= 1

if __name__ == 'main':    
    tv = Televisao()
    print('Ligada:{}'.format(tv.ligada))
    tv.power()
    print('Ligada:{}'.format(tv.ligada))
    print('Canal:{}'.format(tv.canal))
    tv.aumenta_canal()
    tv.aumenta_canal()
    print('Canal:{}'.format(tv.canal))
    tv.diminui_canal()
    print('Canal:{}'.format(tv.canal))
