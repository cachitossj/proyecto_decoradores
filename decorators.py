import functools
from typing import Callable, Type

from utils import authenticate, is_valid_password


def authenticate_class(cls: Type) -> Callable:
    """
    Decorador para autenticar la clase antes de su instanciación.

    Args:
        cls (Type): La clase a decorar.

    Returns:
        Callable: La función decorada.
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        """
        Función envoltorio que realiza la autenticación antes de instanciar la clase.

        Returns:
            Type: La instancia de la clase.
        Raises:
            Exception: Si el usuario no está autorizado.
        """
        if authenticate(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception('Unauthorized User')
    return wrapper


def validate_password(func: Callable) -> Callable:
    """
    Decorador para validar la contraseña antes de ejecutar el método.

    Args:
        func (Callable): El método a decorar.

    Returns:
        Callable: La función decorada.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Función envoltorio que valida la contraseña antes de ejecutar el método.

        Returns:
            Any: El resultado del método.
        Raises:
            Exception: Si la contraseña no es válida.
        """
        username, password = self.username, self.password
        if authenticate(username, password):
            return func(self, *args, **kwargs)
        else:
            raise Exception('Usuario no autorizado')
    return wrapper
