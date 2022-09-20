class Cuenta_Bancaria:

    nombre_banco = "Banco Pitius"
    lista_cuentas = []

    def __init__(self, n_cuenta, balance, interes):
        self.n_cuenta = n_cuenta
        self.balance = balance
        self.interes = interes
        Cuenta_Bancaria.lista_cuentas.append(self)

    def hacer_deposito(self,deposito):
        self.balance += deposito
        return self

    def hacer_retiro(self, retiro):
        if self.balance > retiro:
            self.balance -= retiro
        else:
            print("Fondos insuficientes, te restaremos $5")
            self.balance -= 5
        return self

    def mostrar_balance(self):
        print("Balance actual:", self.balance)
        return self
    
    def generar_interes(self):
        self.balance = self.balance + (self.balance * self.interes)
        return self

    @classmethod
    def todas_las_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            print("Esta cuenta tiene un balance de:", cuenta.balance, "Y tiene u interés de:", cuenta.interes)