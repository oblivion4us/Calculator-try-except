try:
  try:
      num_1 = float(input("Введите 1-е число: "))
  except ValueError:
      raise ValueError("Некорректный ввод первого числа")

  try:
      num_2 = float(input("Введите 2-е число: "))
  except ValueError:
      raise ValueError("Некорректный ввод второго числа")

  process = input("Введите необходимое действие (* - для умножения, / - для деления, + - для сложения, - - для вычитания): ")

  if process == "*":
      print(num_1 * num_2)
  elif process == "/":
      try:
          print(num_1 / num_2)
      except ZeroDivisionError:
          print("На ноль делить нельзя!")
  elif process == "+":
      print(num_1 + num_2)
  elif process == "-":
      print(num_1 - num_2)
  else:
      raise ValueError("Неизвестная операция")
except ValueError as ve:
  print(f"Ошибка: {ve}")
except ZeroDivisionError:
  print("На ноль делить нельзя!")