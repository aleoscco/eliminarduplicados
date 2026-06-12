#!/usr/bin/env python3
# eliminar_duplicados.py
# Elimina líneas duplicadas de un archivo .txt conservando la primera aparición.
# Compatible con Termux, Linux, Windows y macOS.

import argparse
from pathlib import Path


def eliminar_duplicados(
    archivo_entrada: Path,
    archivo_salida: Path,
    ignorar_mayusculas: bool = False,
    ignorar_espacios: bool = False,
) -> tuple[int, int]:
    """
    Lee un archivo de texto y guarda otro sin líneas duplicadas.

    Retorna:
        total_lineas: cantidad total de líneas leídas
        lineas_unicas: cantidad de líneas guardadas
    """
    vistas = set()
    lineas_unicas = []
    total_lineas = 0

    with archivo_entrada.open("r", encoding="utf-8", errors="replace") as f:
        for linea in f:
            total_lineas += 1

            clave = linea
            if ignorar_espacios:
                clave = clave.strip()
            if ignorar_mayusculas:
                clave = clave.lower()

            if clave not in vistas:
                vistas.add(clave)
                lineas_unicas.append(linea)

    with archivo_salida.open("w", encoding="utf-8") as f:
        f.writelines(lineas_unicas)

    return total_lineas, len(lineas_unicas)


def main():
    parser = argparse.ArgumentParser(
        description="Elimina líneas duplicadas de un archivo de texto conservando la primera aparición."
    )

    parser.add_argument(
        "entrada",
        help="Ruta del archivo .txt de entrada. Ejemplo: lista.txt"
    )

    parser.add_argument(
        "-o", "--salida",
        default="sin_duplicados.txt",
        help="Nombre del archivo de salida. Por defecto: sin_duplicados.txt"
    )

    parser.add_argument(
        "--ignorar-mayusculas",
        action="store_true",
        help="Considera iguales las líneas aunque tengan mayúsculas/minúsculas distintas."
    )

    parser.add_argument(
        "--ignorar-espacios",
        action="store_true",
        help="Considera iguales las líneas aunque tengan espacios al inicio o final."
    )

    args = parser.parse_args()

    archivo_entrada = Path(args.entrada)
    archivo_salida = Path(args.salida)

    if not archivo_entrada.exists():
        print(f"Error: no existe el archivo de entrada: {archivo_entrada}")
        return

    total, unicas = eliminar_duplicados(
        archivo_entrada=archivo_entrada,
        archivo_salida=archivo_salida,
        ignorar_mayusculas=args.ignorar_mayusculas,
        ignorar_espacios=args.ignorar_espacios,
    )

    duplicadas = total - unicas

    print("Proceso terminado correctamente.")
    print(f"Líneas leídas: {total}")
    print(f"Líneas únicas guardadas: {unicas}")
    print(f"Líneas duplicadas eliminadas: {duplicadas}")
    print(f"Archivo generado: {archivo_salida}")


if __name__ == "__main__":
    main()
