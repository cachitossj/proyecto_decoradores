import os
import csv
import re
from typing import List, Dict


def get_users(file_name: str) -> List[Dict[str, str]]:
    """
    Lee un archivo CSV con usuarios y devuelve una lista de diccionarios.

    Args:
        file_name (str): El nombre del archivo CSV.

    Returns:
        List[Dict[str, str]]: Lista de diccionarios con usuarios y contraseñas.
    """
    with open(f"{os.path.dirname(__file__)}/{file_name}", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data


def authenticate(username: str, pwd: str) -> bool:
    """
    Valida si un usuario existe en el archivo de usuarios.

    Args:
        username (str): El nombre de usuario.
        pwd (str): La contraseña del usuario.

    Returns:
        bool: True si el usuario está autenticado, False de lo contrario.
    """
    user = {
        "username": username, 
        "password": pwd
    }
    all_users = get_users("users.csv")
    return user in all_users


def is_valid_password(pwd: str) -> bool:
    """
    Comprueba si la contraseña ingresada sigue las siguientes condiciones:
     - Al menos 8 carácteres
     - Debe limitarse a, aunque no exige específicamente, ninguno de los siguientes:
         - letras mayúsculas: A-Z
         - letras minúsculas: a-z
         - números: 0-9
         - cualquiera de los caracteres especiales: @#$%^&+=

    Args:
        pwd (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False de lo contrario.
    """
    if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", pwd):
        return True
    else:
        return False
