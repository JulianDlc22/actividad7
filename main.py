def Menu():
    print("--MENU--")
    print("1. Registrar Estudiantes")
    print("2. Mostrar Estudiantes y sus cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")

def CalcularPromedio(nota1,nota2,nota3):

    promedio = (nota1 + nota2 + nota3)/3
    return promedio

estudiantes= {}

op = 0

while op != 4:

    Menu()
    opcionMenu = input("\nIngrese la Opcion: ")

    try:
        op = int(opcionMenu)

        match op:
            case 1:
                carnet = int(input("Ingrese el Carnet: "))
                nombre = input("Ingrese nombre completo: ")
                edad = int(input("Ingrese la edad: "))
                carrera = input("Ingrese la carrera: ")

                noCursos = int(input("\nCuantos Cursos desea Ingresar?(Maximo 5 cursos): "))
                if noCursos <= 5:

                    for i in range(noCursos):

                        print(f"Curso {i+1} " )
                        nombreCurso = input("Ingrese nombre Curso: ")
                        notaCurso = int(input("Ingrese la nota de la  Tarea: "))

                        if  0 < notaCurso <= 100:
                            notaParcial = int(input("Ingrese la nota del Parcial: "))

                            if 0 < notaParcial <= 100:
                                notaProyecto = int(input("Ingrese la nota del Proyecto: "))

                                if 0 < notaProyecto <= 100:

                                    promedio = calcularPromedio(notaTarea,notaParcial,notaProyecto)

                                    estudiantes[carnet] = {
                                        "nombre" : nombre,
                                        "edad" : edad,
                                        "carrera" : carrera,
                                        "nombreCurso" : {

                                            "notaTarea" : notaTarea,
                                            "notaParcial" : notaParcial,
                                            "notaProyecto": notaProyecto,
                                            "Promedio" : promedio

                                        }

                                    }

                                else:
                                    print("Error_Ingreso una nota invalida")
                                    i -= 1

                            else:
                                print("Error_Ingreso una nota invalida")
                                i-=1

                        else:
                            print("Error_Ingreso una nota invalida")
                            break

                else:
                    print ("Maximo 5 cursos")

            case 2:
                print("\n--Estudiantes Registrados--")
                print("\n")
                for carnet,datos in estudiantes.items():
                    print(f"Carnet {carnet}")
                    print(f"Nombre: {datos['nombre']}")
                    print(f"Edad: {datos['edad']}")
                    print(f"Carrera: {datos['carrera']}")

                    for nombreCurso,datosCurso in datos.items():
                        print(f"Nombre Curso: {nombreCurso}")
                        print(f"Nota Tarea : {datosCurso['notaParcial']}")
                        print(f"Nota Parcial : {datosCurso['notaParcial']}")
                        print(f"Nota Proyecto : {datosCurso['notaProyecto']}")



    except:
        print("Opcion no valida")
