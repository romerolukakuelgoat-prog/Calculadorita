## CALCULADORA - VERSIÓN 4 
# Autor(a): Renato Lazaro
# ===========================================
print("Calculadora")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n 1.Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = input("\n Seleccione una opcion:")

if opcion =="1":
  print("\ La suma es:", num1 + num2)

elif opcion == "2":
  print("\n La resta es:", num1 - num2)

else: opcion == "3":  
  print("\n La multiplicacion es:",num1 * num2)

elif opcion =="4":
  if num2 !=0:
    print("\n La division es:" , num1/num2)
  else:
    print("No se puede dividir entre cero.")

else:
  print("\n Opcion no valida.")
