import json
import os
from datetime import datetime

# Archivo donde se almacenarán los datos de los gastos
DATA_FILE = 'gastos.json'

def cargar_datos():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

def guardar_datos(gastos):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(gastos, file, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def registrar_gasto(gastos):
    try:
        descripcion = input("Descripción del gasto: ")
        categoria = input("Categoría (alimentación, transporte, entretenimiento, etc.): ")
        fecha = input("Fecha (YYYY-MM-DD): ")
        monto = float(input("Monto: "))

        gasto = {
            'descripcion': descripcion,
            'categoria': categoria,
            'fecha': fecha,
            'monto': monto
        }

        gastos.append(gasto)
        guardar_datos(gastos)
        print("Gasto registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el gasto: {e}")

def consultar_gastos(gastos):
    try:
        criterio = input("Buscar por categoría (c) o rango de fechas (f)? ")
        
        if criterio == 'c':
            categoria = input("Ingrese la categoría: ")
            resultados = [gasto for gasto in gastos if gasto['categoria'] == categoria]
        elif criterio == 'f':
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            resultados = [gasto for gasto in gastos if fecha_inicio <= gasto['fecha'] <= fecha_fin]
        else:
            print("Criterio no válido.")
            return

        if resultados:
            for gasto in resultados:
                print(f"Descripción: {gasto['descripcion']}, Categoría: {gasto['categoria']}, Fecha: {gasto['fecha']}, Monto: {gasto['monto']}")
        else:
            print("No se encontraron gastos que coincidan con la consulta.")
    except Exception as e:
        print(f"Error al consultar los gastos: {e}")

def estadisticas_gastos(gastos):
    try:
        total_gastos = sum(gasto['monto'] for gasto in gastos)
        dias = (datetime.today() - datetime.strptime(min(gasto['fecha'] for gasto in gastos), "%Y-%m-%d")).days + 1
        promedio_diario = total_gastos / dias

        categorias = {}
        for gasto in gastos:
            if gasto['categoria'] in categorias:
                categorias[gasto['categoria']] += gasto['monto']
            else:
                categorias[gasto['categoria']] = gasto['monto']
        
        categoria_mayor_gasto = max(categorias, key=categorias.get)

        print(f"Total de gastos: {total_gastos}")
        print(f"Promedio diario de gastos: {promedio_diario:.2f}")
        print(f"Categoría con mayor gasto acumulado: {categoria_mayor_gasto}")
    except Exception as e:
        print(f"Error al calcular las estadísticas de gastos: {e}")

def actualizar_gasto(gastos):
    try:
        descripcion = input("Ingrese la descripción del gasto a actualizar: ")
        for gasto in gastos:
            if gasto['descripcion'] == descripcion:
                gasto['categoria'] = input("Nueva categoría: ")
                gasto['fecha'] = input("Nueva fecha (YYYY-MM-DD): ")
                gasto['monto'] = float(input("Nuevo monto: "))
                guardar_datos(gastos)
                print("Gasto actualizado exitosamente.")
                return
        print("Gasto no encontrado.")
    except Exception as e:
        print(f"Error al actualizar el gasto: {e}")

def eliminar_gasto(gastos):
    try:
        descripcion = input("Ingrese la descripción del gasto a eliminar: ")
        for gasto in gastos:
            if gasto['descripcion'] == descripcion:
                gastos.remove(gasto)
                guardar_datos(gastos)
                print("Gasto eliminado exitosamente.")
                return
        print("Gasto no encontrado.")
    except Exception as e:
        print(f"Error al eliminar el gasto: {e}")

def main():
    gastos = cargar_datos()
    
    while True:
        print("\n1. Registrar gasto")
        print("2. Consultar gastos")
        print("3. Estadísticas de gastos")
        print("4. Actualizar gasto")
        print("5. Eliminar gasto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                registrar_gasto(gastos)
            elif opcion == '2':
                consultar_gastos(gastos)
            elif opcion == '3':
                estadisticas_gastos(gastos)
            elif opcion == '4':
                actualizar_gasto(gastos)
            elif opcion == '5':
                eliminar_gasto(gastos)
            elif opcion == '6':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error al ejecutar la opción seleccionada: {e}")

if __name__ == "__main__":
    main()
