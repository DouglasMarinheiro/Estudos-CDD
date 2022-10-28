class ingresso():
    def __init__(self,valor):
        self.valor=valor

    def ImprimeValor(self):
        print(f'Valor do Ingresso é : {self.valor}')


class IngressoVip(ingresso):
    def __init__(self,valor):
        super().__init__(valor)

    def ImprimeVip(self):
        print(f'O valor do ingresso Vip é : {self.valor*1.50} ')