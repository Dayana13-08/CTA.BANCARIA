#GOYA GILER DAYANA DENISSE

from Cuenta import Cuenta

class CuentaAhorro (Cuenta):
    def __init__(self, interes: float= 0, numero= None, nombrepropietario= None, saldo:float=0):
        self._interes = interes
        super(CuentaAhorro, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

        @property
        def interes(self):
            return self._interes

        @interes.setter
        def interes(self, interes):
            self._interes = interes


        def pagar_interes(self):
            self._saldo = self._saldo + ((float(self._saldo) * int(self._interes))/100)
            return self._saldo
if __name__ == '__main__':
        CuentaAhorro = CuentaAhorro (5,'0908528798', 'narda', '220')

        CuentaAhorro.mostrar_saldo()
        CuentaAhorro.credito(1300)

        CuentaAhorro.mostrar_saldo()
        CuentaAhorro.debito(20)

        print(CuentaAhorro)