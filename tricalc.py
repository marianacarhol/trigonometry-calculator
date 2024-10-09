# Solicita al usuario que ingrese su nombre
user = input("Bienvenido usuario, ingrese su nombre: ") 

def main():   
# Función principal para realizar operaciones matemáticas
      def operaciones():
        import math
        num = 1 # Contador de opciones
        # Lista de opciones
        opciones_1 = ["Cateto", "Hipotenusa", "Angulos Internos", "Seno",
                  "Coseno", "Tangente", "Cosecante", "Secante", "Cotangente", 
                  "Perimetro del triangulo", "Area del triangulo", "Tipo de Triángulo",
                  "Ley de Coseno: 2 Lados y un angulo","Ley de Coseno: 3 lados","Teorema de Tales"]

        # Función para calcular el cateto faltante
        def cateto():
              while True:
                try:
                  cateto_ady = float(input("Ingresa la medida de tu cateto adyacente en cm: "))
                  cateto_hip = float(input("Ingresa la medida de tu hipotenusa en cm: "))
                  resultado = math.sqrt((cateto_hip**2) - (cateto_ady**2))
                  return(f"Tu cateto faltante mide {resultado:.2f} cm")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular la hipotenusa        
        def hipotenusa():
              while True:
                try:
                  cateto_ady = float(input("Ingresa tu cateto adyacente: "))
                  cateto_op = float(input("Ingresa tu cateto opuesto: "))
                  resultado = math.sqrt((cateto_op**2) + (cateto_ady**2))
                  return(f"Tu hipotenusa mide {resultado:.2f} cm")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular el ángulo faltante en un triángulo
        def angulos_internos():
              while True:
                try:
                  angulo_1 = int(input("Inserta tu angulo A: "))
                  angulo_2 = int(input("Inserta tu angulo B: "))
                  angulo_3 = (180 - (angulo_1 + angulo_2))
                  return(f"Tu angulo faltante mide {angulo_3:.2f}°")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular el seno del ángulo       
        def sen():
              while True:
                try:
                  cat_op = float(input("Ingresa la medida de tu cateto opuesto en cm: "))
                  hip = float(input("Ingresa la medida de tu hipotenusa en cm: "))
                  seno = cat_op/hip
                  seno_rad = math.asin(seno)
                  seno_grad = math.degrees(seno_rad)
                  return(f"Tu angulo es {seno_grad:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular el coseno del ángulo
        def cos():
              while True:
                try:
                  cat_ady = float(input("Ingresa la medida de tu cateto adyacente en cm: "))
                  hip = float(input("Ingresa la medida de tu hipotenusa en cm: "))
                  cos = cat_ady/hip
                  cos_rad = math.acos(cos)
                  cos_grad = math.degrees(cos_rad)
                  return(f"Tu angulo es {cos_grad:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular la tangente del ángulo
        def tan():
              while True:
                try:
                  cat_op = float(input("Ingresa la medida de tu cateto opuesto en cm: "))
                  cat_ady = float(input("Ingresa la medida de tu cateto adyacente en cm: "))
                  tan = cat_op/cat_ady
                  tan_rad = math.atan(tan)
                  tan_grad = math.degrees(tan_rad)
                  return(f"Tu angulo es {tan_grad:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular la cosecante del ángulo
        def csc():
              while True:
                try:
                  # Solicitar medidas del cateto opuesto y la hipotenusa
                  cat_op = float(input("Ingresa la medida de tu cateto opuesto en cm: "))
                  hip = float(input("Ingresa la medida de tu hipotenusa en cm: "))
                  # Cálculo de la cosecante y conversión a grados
                  csc_seno = 1/(hip/cat_op)
                  csc_rad = math.asin(csc_seno)
                  csc_deg = math.degrees(csc_rad)
                  return(f"Tu angulo es {csc_deg:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular la secante del ángulo
        def sec():
              while True:
                try:
                  # Solicitar medidas del cateto adyacente y la hipotenusa
                  cat_ady = float(input("Ingresa la medida de tu cateto adyacente en cm: "))
                  hip = float(input("Ingresa la medida de tu hipotenusa en cm: "))
                  # Cálculo de la secante y conversión a grados
                  sec_cos = 1/(hip/cat_ady)
                  sec_rad = math.acos(sec_cos)
                  sec_grad = math.degrees(sec_rad)
                  return(f"Tu angulo es {sec_grad:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular la cotangente del ángulo        
        def cot():
              while True:
                try:
                  # Solicitar medidas de los catetos
                  cat_op = float(input("Ingresa la medida de tu cateto opuesto en cm: "))
                  cat_ady = float(input("Ingresa la medida de tu cateto adyacente en cm: "))
                  # Cálculo de la cotangente y conversión a grados
                  cot_tan = 1/(cat_ady/cat_op)
                  cot_rad = math.atan(cot_tan)
                  cot_deg = math.degrees(cot_rad)
                  return(f"Tu angulo es {cot_deg:.2f}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular el perímetro de un triángulo
        def perimetro_triangulo():
              while True:
                try:
                  # Solicitar las longitudes de los lados del triángulo
                  lado1 = float(input("¿cuánto mide tu primer lado? "))
                  lado2 = float(input("¿cuánto mide tu segundo lado? "))
                  lado3 = float(input("¿cuánto mide tu tercer lado? "))

                  # Función interna para calcular el perímetro
                  def perimetro_triangulo(a,b,c):
                    suma = a + b + c
                    return suma
                  
                  return(f"el perímetro de tu triángulo es {perimetro_triangulo(lado1,lado2,lado3)}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para calcular el área de un triángulo
        def area_triangulo():
              while True:
                try:
                  # Solicitar base y altura del triángulo
                  base = float(input("¿cuánto mide tu base? "))
                  altura = float(input("¿cuánto mide tu altura? "))

                  # Función interna para calcular el área
                  def area_triangulo(a,b):
                    division = (a*b)/2   # Área = (base * altura) / 2
                    return division
                  
                  return(f"el área de tu_triángulo es {area_triangulo(base,altura)}")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        # Función para determinar el tipo de triángulo según sus ángulos
        def tipo_triangulo():
              while True:
                try:
                  # Solicitar medidas de los ángulos
                  angulo_a = int(input("¿cuánto mide tu angulo a? "))
                  angulo_b = int(input("¿cuánto mide tu angulo b? "))
                  angulo_c = int(input("¿cuánto mide tu angulo c? "))

                  # Determinar tipo de triángulo
                  if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
                    return("Tu figura es un triangulo rectangulo")

                  elif angulo_a > 90 < 180 or angulo_b > 90 < 180 or angulo_c > 90 < 180:
                    return("Tu figura es un triangulo obtusangulo")

                  elif angulo_a < 90 and angulo_b < 90 and angulo_c < 90:
                    return("Tu figura es un triangulo acutangulo")

                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        #Función Ley de Cosenos 1        
        def ley_cos_1():
              while True:
                try:
                  print("LEY DE COSENOS")
                  print("1.- Tengo 2 lados y 1 ángulo --> para hallar el lado restante") 
                  #El usuario tiene la medida de dos lados y un ángulo y por medio de la ley de cosenos calculará el lado restante

                  ladoa = float(input("Ingresa el valor del lado a en cm: "))
                  ladob = float(input("Ingresa el valor del lado b en cm: "))
                  anguloc = int(input("Ingresa el valor del ángulo c (grados): "))

                  # Cálculo del lado restante usando la ley de cosenos
                  C = math.sqrt((ladoa**2) + (ladob**2) - 2 * ladoa * ladob * math.cos(math.radians(anguloc)))
                  return(C)
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        #Función Ley de Cosenos 2         
        def ley_cos_2():
              while True:
                try:
                  print("LEY DE COSENOS")
                  print("Tengo 3 lados --> para hallar un ángulo") 
                  #El usuario tiene la medida de tres ángulos y por medio de la
                  #ley de cosenos calculará un ángulo del triángulo (el que el usuario pida)

                  ladoa = float(input("Ingresa el valor del lado a en cm :"))
                  ladob = float(input("Ingresa el valor del lado b en cm :"))
                  ladoc = float(input("Ingresa el valor del lado c en cm :"))
                  opcionangulo = int(input("¿que ángulo quieres calcular (ingresa el número correspondiente)?: A(1), B(2), C(3)"))

                  # Cálculo del ángulo A
                  if opcionangulo == 1:
                      angulo = math.acos(((-ladoa**2) + (ladob**2) + (ladoc**2)) / (2*ladob*ladoc))
                      x = angulo*180/math.pi # Conversión de radianes a grados
                      return(x)
                
                  # Cálculo del ángulo B
                  elif opcionangulo == 2:
                      angulo = math.acos(((-(ladob**2) + (ladoa**2) + (ladoc**2)) / 2*ladoa*ladoc))
                      x = angulo*180/math.pi
                      return(x)

                  # Cálculo del ángulo C
                  elif opcionangulo == 3:
                      angulo = math.acos(((-(ladoc**2) + (ladoa**2) + (ladob**2)) / 2*ladoa*ladob))
                      x = angulo*180/math.pi
                      return(x)
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue

        #Función del Teorema de Tales
        def teorema_tales():
              while True:
                try:
                  print(f"Escribe el valor de la medida del lado del triangulo que tiene un solo lado,el triangulo",end="")
                  print("que tiene un valor en el mismo lado pero del otro triangulo y los lados restantes del triangulo que los tenga")
                  lado1 = float(input("Dame el lado del triangulo que no tiene sus otros dos lados:"))
                  lado2 = float(input("Dame el lado del triangulo que tiene un valor en el mismo lado que el triangulo de un solo valor:"))
                  lado3 = float(input("Dame el valor del lado que falta:"))
                  lado4 = float(input("Dame el valor del lado que falta:"))

                  # Cálculos basados en la relación de lados
                  if lado1 < lado2:
                    lado5 = lado3/(lado2/lado1)
                    lado6 = lado4/(lado2/lado1)
                    return(f"los lados restantes del triangulo son: {lado5} y {lado6}")
                  elif lado1 > lado2:
                    lado5 = lado3*(lado1/lado2)
                    lado6 = lado4*(lado1/lado2)
                    return(f"los lados restantes del triangulo son: {lado5} y {lado6}")
                  else:
                    return("los valores son iguales de los triagulos que tienen un valor en el mismo lado")
                except ValueError:
                  print("El valor que ingresaste no es valido")
                  continue
        #--------------

        # Se imprime una lista de opciones y se permite al usuario seleccionar una acción
        for x in opciones_1:
            print(f"{str(num)}.- {x}")
            num += 1
        while True:
          try:
            opcion = int(input(f"Ingrese el número de acción que desea realizar, {user}: "))   # Solicita la opción al usuario
            break
          except ValueError:
            print("La opción que ingreso no es valida")
            continue

        print(opciones_1[int(opcion)-1]) # Muestra la opción seleccionada

        # Lista de funciones que se pueden ejecutar
        funciones=[cateto,hipotenusa,angulos_internos,sen,cos,tan,
                  csc,sec,cot,perimetro_triangulo,area_triangulo,
                  tipo_triangulo,ley_cos_1,ley_cos_2,teorema_tales]

        resultado=(funciones[opcion-1]()) # Llama a la función seleccionada y guarda el resultado
        return(resultado) # Retorna el resultado
      
      #Función para graficar
      def grafica():
        import numpy as np
        import matplotlib.pyplot as plt
        # Solicitar el ángulo al usuario en grados
        while True:  
            try:
                print("Se utilizara la formula y= sin(ángulo + 5t), para poder graficar el movimiento de seno del angulo introducido,")
                print("en donde cada segundo se le agregara un multiplo de 5 grados")       
                angulo = float(input("Ingrese el ángulo en grados: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el ángulo.")
                continue
        # Crear una lista de tiempo de 0 a 100 segundos
        tiempo = np.arange(0, 100, 1)


        # Calcular los valores de y (seno del ángulo + múltiplos de 5 grados por segundo)
        y_vals = [np.sin(np.radians(angulo + 5 * t)) for t in tiempo]

        # Graficar los valores
        plt.figure(figsize=(8, 6))
        plt.plot(tiempo, y_vals, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('seno(Angulo + 5t)')
        plt.grid(True)
        plt.show() # Muestra la gráfica

      num = 0
      acciones_1 = ["operaciones", "graficar"] # Opciones de acciones
      acciones_2 = [operaciones, grafica]
      for x in acciones_1:
          num+=1
          print(f"{str(num)}.- {x}")

    #Imprime las opciones y le pregunta al usuario por su elección
      while True:
        try:
          accion=int(input(f"Que desea hacer, {user}: "))
          print(acciones_2[accion-1]()) # Llama a la función correspondiente a la acción seleccionada
          break
        except ValueError:
          print("La opción que ingreso no es valida")
          continue
        except IndexError:
          print("La opción que ingreso no es valida")
          continue

# Llama a la función main
main()
while True:
    opcion_final = input("Salir? [si] [no] ")

    # Si el usuario ingresa "si", se rompe el bucle y el programa finaliza
    if opcion_final == "si":
        break
    
    # Si el usuario ingresa "no", se vuelve a llamar a la función principal
    if opcion_final == "no":
        main()
    
    # Si el usuario ingresa una opción no válida, se informa y se repite el bucle
    else:
      print("La opción que ingreso no es valida")
      continue