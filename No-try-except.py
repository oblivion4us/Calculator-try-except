num_1 = float(input("Введите 1-е число: "))
num_2 = float(input("Введите 2-е число: "))
process = input("Введите необхожимое действие (* - для умножения, / - для деления, + - для сложения, - - для вычитания): ")
if process == "*":
  print(num_1 * num_2)
elif process == "/":
  if num_2 == 0:
    print("На ноль делить нельзя!")
  else:
    print(num_1/num_2)
elif process == "+":
  print(num_1 + num_2)
elif process == "-":
  print(num_1 - num_2)
else:
  print("Неизвестная операция")