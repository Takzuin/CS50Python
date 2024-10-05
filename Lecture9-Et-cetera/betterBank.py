class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        """Depositar dinero en la cuenta."""
        self._balance += n

    def withdraw(self, n):
        """Retirar dinero de la cuenta, si hay suficiente balance."""
        if n > self._balance:
            print("Fondos insuficientes.")
        else:
            self._balance -= n

def main():
    account = Account()
    while True:
        print("\n1-Para depositar")
        print("2-Para retirar")
        print("3-Para salir")
        
        action = input("Elija una opción de 1-3: ")
        if action not in ('1', '2', '3'):
            print("Opción inválida. Intente de nuevo.")
            continue
        
        action = int(action)
        
        if action == 1:
            try:
                i = float(input("Dinero a depositar: "))
                if i < 0:
                    print("No se puede depositar una cantidad negativa.")
                else:
                    account.deposit(i)
                    print(f"Nuevo balance: {account.balance}")
            except ValueError:
                print("Por favor, introduzca un número válido.")

        elif action == 2:
            try:
                i = float(input("Dinero a retirar: "))
                if i < 0:
                    print("No se puede retirar una cantidad negativa.")
                else:
                    account.withdraw(i)
                    print(f"Nuevo balance: {account.balance}")
            except ValueError:
                print("Por favor, introduzca un número válido.")

        elif action == 3:
            print("Saliendo del programa.")
            break

        print(f"Balance actual: {account.balance}")

main()
