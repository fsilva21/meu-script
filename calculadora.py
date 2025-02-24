print("Calculadora básica")
num1 = float(input("Digite o primeiro número: "))
operador = str(input("Digite '+' para adição. Digite '-' para subtração. Digite '*' para multiplicação. Digite '/' para divisão. "))
num2 = float(input("Digite o segundo número: "))
if operador == "+":
  print(f"Resultado: {num1 + num2:.2f}")
elif operador == "-":
  print(f"Resultado: {num1 - num2:.2f}")
elif operador == "*":
  print(f"Resultado: {num1 * num2:.2f}")
elif operador == "/":
  print(f"Resultado: {num1 / num2:.2f}")
else:
  print("Por favor, digite um operador válido e tente novamente.")


