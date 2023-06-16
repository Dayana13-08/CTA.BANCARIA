#GOYA GILER DAYANA DENISSE

from Cuenta import Cuenta

class CuentaCorriente (Cuenta):

    def __init__(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_cheque=bool):
        self._tiene_cheque= tiene_cheque
        super(CuentaCorriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

    @property
    def tiene_cheque(self):
        return self._tiene_cheque

    @tiene_cheque.setter
    def tiene_cheque(self, tiene_cheque):
        self._tiene_cheque = tiene_cheque
        return self._saldo

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if __name__=='__main__':
    CuentaCorriente = CuentaCorriente('0908528798', 'narda', '250', bool)

    CuentaCorriente.mostrar_saldo()
    CuentaCorriente.credito(1500)

    CuentaCorriente.mostrar_saldo()
    CuentaCorriente.debito(40)

    print(CuentaCorriente)