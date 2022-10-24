import os


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

class Client(Person):
    def __init__(self, name, lastname, account_number, balance):
        super().__init__(name, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'Hola {self.name} {self.lastname}! Bienvenido a tu cuenta!'

    def deposit(self, total):
        if total <= 0:
            print(f'No se puede ingresar {total}, solo números mayores a 0')
        else:
            self.balance += total
        
    def withdraw(self, total):
        if total <= self.balance:
            self.balance -= total
            print(f'Total retirado ${total}')
        elif total > self.balance:
            print('\nNo tenés suficiente saldo para realizar esta transacción')
            print(f'Intentaste retirar ${total} de ${self.balance}')

def create_client():
    format_console()
    user_name = input('¿Cómo es tu nombre?: ').capitalize()
    user_lastname = input('¿Cómo es tu apellido?: ').capitalize()

    person = Person(user_name, user_lastname)

    return person

def init_app():
    client = Client(person.name, person.lastname, 1, 100)
    
    # format_console()
    print(client)
    print("""\nElige una operación:
    [1] - Mira tu cuenta
    [2] - Depositar
    [3] - Retirar
    [4] - Finalizar
    """)
    user_select()

def user_select():
    operation_selected = int(input('Escribe el numero de la operación a realizar aquí: '))
    while True:
        if operation_selected not in range(1, 5):
            format_console()
            print('No es posible acceder a esa operación')
            operation_selected = int(input('Escribe el numero de la operación a realizar aquí: '))            
            continue
        else:
            options(operation_selected)
            break
    
def options(user_select):
    if user_select == 1:
        format_console()
        account_settings()
        another_operation()
    elif user_select == 2:
        format_console()
        account_deposit()
        another_operation()
    elif user_select == 3:
        format_console()
        account_withdraw()
        another_operation()
    elif user_select == 4:
        format_console()
        print('Nos vemos en la próxima transacción!')

def account_settings():
    print('=========== Tu cuenta ===========')
    print(f'Nombre de usuario: {client.name} {client.lastname} \nNúmero de cuenta: {client.account_number} \nBalance: ${client.balance}')

def account_deposit():
    total_deposit = int(input('¿Cuánto dinero querés depositar?: '))
    client.deposit(total_deposit)
    print(f'Tu balance es de ${client.balance}')

def account_withdraw():
    print(f'Saldo disponible: ${client.balance}')
    total_withdraw = int(input('¿Cuánto dinero querés retirar?: '))
    client.withdraw(total_withdraw)

def another_operation():
    question = input('\n¿Desea realizar otra operación?: ').lower()
    
    if question == 'si':
        init_app()
    else: 
        print('Nos vemos la próxima!')

def format_console():
    return os.system('cls')


person = create_client()
client = Client(person.name, person.lastname, 1000, 0)
init_app()