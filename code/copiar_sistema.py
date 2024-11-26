import os
from pathlib import Path


def copiar(origen: Path, destino: dict[str, Path]) -> None:
    try:
        for usuario, ruta in destino.items():
            while True:
                confirmacion = input(f"¿{usuario}? s/n: ")
                if confirmacion.lower() in ("s", "n"):
                    break
                else:
                    continue

            print(f"{usuario:*^60} ")

            comando = f'xcopy "{origen / "Sistema.exe"}" "{ruta}" /d /y /z'
            os.system(comando)

            comando = f'xcopy "{origen.resolve().parent / "*.pdf"}" "{ruta}" /d /y /z'
            os.system(comando)

            if usuario == "Eduardo":
                comando = f'xcopy "{origen.resolve().parent / "estadistica.exe"}" "{ruta}" /d /y /z'
                os.system(comando)
                comando = f'xcopy "{origen.resolve().parent / "consultas.accdb"}" "{ruta}" /d /y /z'
                os.system(comando)
    except KeyboardInterrupt:
        exit(1)
    except Exception as error:
        print("Error:", error)


def obtener_rutas() -> tuple[Path, dict[str, Path]]:
    origen = Path(r"E:\oficina\codigo")
    destino = {"Esteban": Path(r"E:\oficina"),
        "Eduardo": Path(r"\\c1-scj-6223185\Users\econcina\Desktop\Sistema"),
        "Adriana": Path(r"\\C1-SCJ-4760704\Sistema"),
        "Natalia": Path(r"\\C1-SCJ-4633555\Users\nmendoza\Desktop\Sistema"),
        "Elina": Path(r"\\C1-SCJ-4760578\Users\esampieri\Desktop\Sistema"),
        "Graciela": Path(r"\\C1-SCJ-4844499\Users\magutierrez\Desktop\Sistema"),
        "Archivo": Path(r"\\RPI-572-CUPI\Users\archivo\Desktop\Destruccion"),
    }
    return origen, destino


def main():
    copiar(*obtener_rutas())
    os.system("pause")


main()
