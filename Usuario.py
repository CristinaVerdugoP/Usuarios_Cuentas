from Banco import Cuenta_Bancaria
class Usuario:
    def __init__(self, nombre, balance, interes, n_cuenta):
        self.nombre = nombre
        self.mis_cuentas = []
        self.cuenta = Cuenta_Bancaria(n_cuenta, balance, interes)
        self.mis_cuentas.append(self.cuenta)
    
    def deposito(self, monto):
        self.cuenta.hacer_deposito(monto)
        return self

    def retiro(self,monto):
        self.cuenta.hacer_retiro(monto)
        return self

    def balance_cuenta(self):
        self.cuenta.mostrar_balance()
        return self

    def crear_cuentas(self, n_cuenta):
        cuenta_nueva = Cuenta_Bancaria(n_cuenta, balance = 0, interes = 0.02)
        self.mis_cuentas.append(cuenta_nueva)
        return self

    def info_cuentas(self):
        for cuenta in self.mis_cuentas:
            print("La cuenta n°",cuenta.n_cuenta, "tiene un balance de:", cuenta.balance)
        return self

    def deposito_cuenta(self, n_cuenta, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.n_cuenta == n_cuenta:
                cuenta.hacer_deposito(monto)
                print("Se hizo un deposito en la cuenta #", n_cuenta, "-- Balance actual", cuenta.balance)
        return self

    def retiro_cuentas(self, n_cuenta, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.n_cuenta == n_cuenta:
                cuenta.hacer_retiro(monto)
                print("Se hizo un retiro en la cuenta #", n_cuenta, "-- Balance actual", cuenta.balance)
        return self

cuenta1 = Usuario("Rosita", 600, 0.02, 1)

cuenta1.deposito(200).retiro(40).balance_cuenta()

cuenta1.crear_cuentas(2).deposito_cuenta(2, 500).retiro_cuentas(2,50)
cuenta1.deposito_cuenta(1,300).info_cuentas()


