import math

CONSTANT = math.pi
strings = "Esta es una cadena"  # comment
fstring = f"Prueba: '{strings}'\n"
booleans_none = {"true": True, "false": False, "none": None}
operations = 12 > 2 and 23 == 23 < 100 + 12 * 2 / 2

def function(num1: int, num2: int) -> float | None:
    """Función que recibe dos enteros para dividirlos"""
    x = 0
    if num2 > x:
        return num1 / num2
    return None

function(num1=12, num2=2)

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

class User(Person, object):
    def generate_password(self) -> str:
        return self.name[::-1]

user = User("Hello")