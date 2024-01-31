from decorators import authenticate_class, validate_password
from typing import Any

@authenticate_class
class MyClass:
    """
    Clase que requiere autenticación para su instanciación y contraseña válida para ciertos métodos.

    Attributes:
        username (str): El nombre de usuario.
        password (str): La contraseña del usuario.
    """

    def __init__(self, username: str, password: str) -> None:
        """
        Inicializa la clase con un nombre de usuario y contraseña.

        Args:
            username (str): El nombre de usuario.
            password (str): La contraseña del usuario.
        """
        self.username = username
        self.password = password

    def say_hello(self) -> None:
        print(f"Hi {self.username}, welcome to our system!")

    @validate_password
    def show_password(self) -> None:
        print(
            f"Hi {self.username}, your password starts by: {self.password[:4]}{len(self.password[4:])*'*'}")


my_class = MyClass("ivancapo1", "testpwd33")
my_class.say_hello()
my_class.show_password()
