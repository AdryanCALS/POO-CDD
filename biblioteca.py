from pickle import FALSE

class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.dormindo = False
        self.comendo = False
        self.falando = False
        
    def comer(self):
        if self.dormindo == True:
            print(f"{self.nome} está dormindo e nao pode comer!")
        elif self.falando == True:
            print(f"{self.nome} está falando e nao pode comer!")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo!")
        else:
            self.comendo = True
            print(f"{self.nome} foi comer agora")
            
    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo!")
        elif self.falando == True:
            print(f"{self.nome} está falando e nao pode dormir!")
        elif self.comendo == True:
            print(f"{self.nome} não pode estar dormindo pois está comendo")
        else:
            self.dormindo = True
            print(f"{self.nome} foi dormir agora")
            
    def falar(self):
        if self.dormindo == True:
            print(f"{self.nome} nao pode estar falando pois está dormindo")
        elif self.falando == True:
            print(f"{self.nome} já está falando!")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois já está comendo!")
        else:
            self.falando = True
            print(f"{self.nome} está falando agora")
                