class Car:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

        self.ligado = False
        
    def ligar(self):
        if self.ligado:
           return "Já esta ligado"
        
        self.ligado = True
        return f"{self.modelo} Ligado"
        
        
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"{self.modelo} Desligado"
        
        return f"{self.modelo} Já esta Desligado"
    
    def velocidadeCar(self):
        if self.ligado:
            self.velocidade = self.velocidade + 1
            return f"Velocidade {self.velocidade} k/h"
            
        return f"Ligue o {self.modelo}"
    
    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            return f"Velocidade {self.velocidade} k/h"
            
        return "Não é possivel frear "
    
    def car_info(self):
       return {
           "Cor": self.cor,
           "Marca" : self.marca,
           "Modelo": self.modelo
       }
         

# Car.maxVelocity(self)