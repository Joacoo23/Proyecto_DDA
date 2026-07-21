import os

class curso():
    def __init__(self, id, nombre_curso, costo, participantes_esperados, prioridad):
        self.id = id
        self.nombre_curso = nombre_curso
        self.costo = costo
        self.participantes_esperados = participantes_esperados
        self.prioridad = prioridad

    def mostrar_datos(self):
        print(f"{self.id} {self.nombre_curso} | Costo: ${self.costo} | Part. Esperados: {self.participantes_esperados} | Prioridad: {self.prioridad}")

def ejecutar_greedy(cursos_disponibles, presupuesto_max):
    cursos_ordenados = sorted(cursos_disponibles, key=lambda c: c.participantes_esperados / c.costo, reverse=True)
    seleccionados = []
    gasto = 0
    participantes = 0
    
    for c in cursos_ordenados:
        if gasto + c.costo <= presupuesto_max:
            seleccionados.append(c)
            gasto += c.costo
            participantes += c.participantes_esperados
            
    return seleccionados, gasto, participantes

def ejecutar_backtracking(cursos_disponibles, presupuesto_max):
    mejor_participantes = 0
    mejor_combinacion = []
    mejor_costo = 0

    def backtrack(indice, costo_actual, part_actuales, combinacion_actual):
        nonlocal mejor_participantes, mejor_combinacion, mejor_costo
        
        if costo_actual > presupuesto_max:
            return
            
        if part_actuales > mejor_participantes:
            mejor_participantes = part_actuales
            mejor_combinacion = combinacion_actual.copy()
            mejor_costo = costo_actual

        for i in range(indice, len(cursos_disponibles)):
            combinacion_actual.append(cursos_disponibles[i])
            backtrack(
                i + 1, 
                costo_actual + cursos_disponibles[i].costo, 
                part_actuales + cursos_disponibles[i].participantes_esperados, 
                combinacion_actual
            )
            combinacion_actual.pop()

    backtrack(0, 0, 0, [])
    return mejor_combinacion, mejor_costo, mejor_participantes

datos = [
    curso("C01", "Python Aplicado", 35000000, 95, "Alta"),
    curso("C02", "Power BI", 45000000, 100, "Alta"),
    curso("C03", "Excel Intermedio", 15000000, 40, "Media"),
    curso("C04", "IA Generativa", 20000000, 60, "Alta"),
    curso("C05", "Gestión Ágil", 18000000, 55, "Media"),
    curso("C06", "SQL Para Análisis de Datos", 25000000, 70, "Alta"),
    curso("C07", "GitHub Básico", 12000000, 30, "Baja"),
    curso("C08", "Linux Inicial", 10000000, 25, "Baja"),
    curso("C09", "Computación en la Nube", 30000000, 80, "Alta"),
    curso("C10", "Ciberseguridad Básica", 22000000, 65, "Media")
]

opcion = None
costo_acumulado = 0
Presupuesto = 120000000
Participantes_beneficiados = 0

res_greedy_cursos = []
res_greedy_costo = 0
res_greedy_part = 0
greedy_ejecutado = False

res_back_cursos = []
res_back_costo = 0
res_back_part = 0
back_ejecutado = False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- MENU DE OPCIONES ---')
    print('1.- Mostrar todos los cursos disponibles.')
    print('2.- Mostrar presupuesto.')
    print('3.- Ejecutar algoritmo Greedy.')
    print('4.- Ejecutar algoritmo Backtracking.')
    print('5.- Mostrar los cursos seleccionados.')
    print('6.- Mostrar costo total y participantes beneficiados.')
    print('7.- Comparar resultados.')
    print('8.- Mostrar analisis de complejidad.')
    print('9.- Salir')

    try:
        opcion = int(input('Ingresar una opcion: '))
    except ValueError:
        print('Solicitud ingresada incorrecta, por favor ingrese un numero (1-9) para hacer una solicitud.')
        input('Presiona Enter para continuar...')
        continue

    if opcion == 1:
        for d in datos:
            d.mostrar_datos()
        input('Presione Enter para continuar...')

    elif opcion == 2:
        print(f"El presupuesto disponible total es de ${Presupuesto}")
        input('Presione Enter para continuar...')

    elif opcion == 3:
        res_greedy_cursos, res_greedy_costo, res_greedy_part = ejecutar_greedy(datos, Presupuesto)
        greedy_ejecutado = True
        print('¡Algoritmo Greedy ejecutado con éxito!')
        input('Presione Enter para continuar...')

    elif opcion == 4:
        res_back_cursos, res_back_costo, res_back_part = ejecutar_backtracking(datos, Presupuesto)
        back_ejecutado = True
        print('¡Algoritmo Backtracking ejecutado con éxito!')
        input('Presione Enter para continuar...')

    elif opcion == 5:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- MENU DE OPCIONES DE CURSOS ---')
            print('Elige los cursos seleccionados segun el algoritmo que deseas mostrar.')
            print('1.- Cursos segun algoritmo Greedy.')
            print('2.- Cursos segun algoritmo Backtracking.')
            print('3.- Salir')
            
            try:
                opcion_algoritmo = int(input('Seleccione una opcion: '))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                input('Presiona Enter para continuar...')
                continue
                
            if opcion_algoritmo == 1:
                if greedy_ejecutado:
                    print("\nCursos seleccionados por GREEDY:")
                    for c in res_greedy_cursos:
                        print(f"- {c.nombre_curso} (Costo: ${c.costo}, Part: {c.participantes_esperados})")
                else:
                    print("\nDebes ejecutar el algoritmo Greedy (Opción 3) primero.")
            elif opcion_algoritmo == 2:
                if back_ejecutado:
                    print("\nCursos seleccionados por BACKTRACKING:")
                    for c in res_back_cursos:
                        print(f"- {c.nombre_curso} (Costo: ${c.costo}, Part: {c.participantes_esperados})")
                else:
                    print("\nDebes ejecutar el algoritmo Backtracking (Opción 4) primero.")
            elif opcion_algoritmo == 3:
                print('Saliendo del menu de cursos...')
                break
            else:
                print('Valor no valido, ingresa la opcion 1, 2 o 3.')
            input('Presiona Enter para continuar...')

    elif opcion == 6:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--- MENU DE OPCIONES DE ALGORITMOS ---')
            print('Elige mostrar los presupuestos y participantes segun algoritmo.')
            print('1.- Algoritmo Greedy.')
            print('2.- Algoritmo Backtracking.')
            print('3.- Salir')
            
            try:
                opcion_algoritmo2 = int(input('Seleccione una opcion: '))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                input('Presiona Enter para continuar...')
                continue
                
            if opcion_algoritmo2 == 1:
                if greedy_ejecutado:
                    print(f"\nResultados GREEDY:")
                    print(f"Presupuesto utilizado: ${res_greedy_costo} / ${Presupuesto}")
                    print(f"Participantes beneficiados: {res_greedy_part}")
                else:
                    print("\nDebes ejecutar el algoritmo Greedy primero.")
            elif opcion_algoritmo2 == 2:
                if back_ejecutado:
                    print(f"\nResultados BACKTRACKING:")
                    print(f"Presupuesto utilizado: ${res_back_costo} / ${Presupuesto}")
                    print(f"Participantes beneficiados: {res_back_part}")
                else:
                    print("\nDebes ejecutar el algoritmo Backtracking primero.")
            elif opcion_algoritmo2 == 3:
                print('Saliendo del menu de algoritmos...')
                break
            else:
                print('Valor no valido, ingresa la opcion 1, 2 o 3.')
            input('Presiona Enter para continuar...')

    elif opcion == 7:
        if not greedy_ejecutado or not back_ejecutado:
            print("Debes ejecutar ambos algoritmos (opciones 3 y 4) antes de comparar.")
        else:
            print("\n--- COMPARACIÓN DE RESULTADOS ---")
            print(f"Greedy       -> Participantes: {res_greedy_part} | Costo: ${res_greedy_costo}")
            print(f"Backtracking -> Participantes: {res_back_part} | Costo: ${res_back_costo}")
            print("-" * 35)
            if res_back_part > res_greedy_part:
                print("Conclusión: Backtracking encontró una mejor combinación de cursos para aprovechar el presupuesto.")
            elif res_back_part == res_greedy_part:
                print("Conclusión: Ambos algoritmos encontraron soluciones igual de óptimas.")
            else:
                print("Conclusión: Greedy obtuvo mejores resultados (esto no debería ocurrir teóricamente si Backtracking es el óptimo, a menos que haya empates de peso).")
        input('Presiona Enter para continuar...')

    elif opcion == 8:
        print("\n--- ANÁLISIS DE COMPLEJIDAD ---")
        print("1. Algoritmo Greedy:")
        print("   - Tiempo: O(N log N) debido a la función de ordenamiento.")
        print("   - Espacio: O(N) para almacenar la lista de seleccionados.")
        print("   - Pros: Extremadamente rápido y consume muy poca memoria.")
        print("   - Contras: Puede dejar presupuesto sin usar y no garantizar la solución óptima.")
        print("\n2. Algoritmo Backtracking:")
        print("   - Tiempo: O(2^N) en el peor de los casos, ya que evalúa incluir o no incluir cada curso.")
        print("   - Espacio: O(N) por la profundidad del árbol de recursión (Call Stack).")
        print("   - Pros: Garantiza encontrar la combinación absolutamente óptima.")
        print("   - Contras: Si 'N' (cantidad de cursos) crece mucho, el tiempo de ejecución se vuelve inviable.")
        input('Presiona Enter para continuar...')

    elif opcion == 9:
        print('Saliendo del programa, gracias por quedarte conmigo...')
        input('Presione Enter para finalizar.')
        break