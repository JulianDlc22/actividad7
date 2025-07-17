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
                    cursos_estudiante = {}

                    for i in range(noCursos):

                        print(f"Curso {i+1} " )
                        nombreCurso = input("Ingrese nombre Curso: ")
                        notaTarea = int(input("Ingrese la nota de la Tarea: "))

                        if  0 < notaTarea <= 100:
                            notaParcial = int(input("Ingrese la nota del Parcial: "))

                            if 0 < notaParcial <= 100:
                                notaProyecto = int(input("Ingrese la nota del Proyecto: "))

                                if 0 < notaProyecto <= 100:

                                    promedio = CalcularPromedio(notaTarea,notaParcial,notaProyecto)
                                    codigoCurso = i+1

                                    estudiantes[carnet] = {
                                        "nombre": nombre,
                                        "edad": edad,
                                        "carrera": carrera,
                                        "cursos_estudiante": cursos_estudiante

                                    }

                                    cursos_estudiante[codigoCurso] = {

                                        "nombreCurso": nombreCurso,
                                        "notaTarea": notaTarea,
                                        "notaParcial": notaParcial,
                                        "notaProyecto": notaProyecto,
                                        "promedio": promedio

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
                    print(f"Carnet: {carnet}")
                    print(f"Nombre: {datos['nombre']}")
                    print(f"Edad: {datos['edad']}")
                    print(f"Carrera: {datos['carrera']}")


                    for codigoCurso,datosCurso in datos['cursos_estudiante'].items():

                        print(f"Nombre Curso: {datosCurso['nombreCurso']}")
                        print(f"Nota Tarea : {datosCurso['notaParcial']}")
                        print(f"Nota Parcial : {datosCurso['notaParcial']}")
                        print(f"Nota Proyecto : {datosCurso['notaProyecto']}")
                        print(f"Promedio: {datosCurso['promedio']}")





    except:
        print("Opcion no valida")
