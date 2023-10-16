a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

sum = a + b 
diff = a - b
mult = a * b
avg = (a + b)/2
diff_abs = max(abs(a),abs(b)) - min(abs(a),abs(b))
quo = a / b

print(f'Сумма чисел {sum}')
print(f'Разность равна {diff}')
print(f'Произведение равно {mult}')
print(f'Среднее арифмитическое равно {avg}')
print(f'Разность максимального и минимального по модулю равна {diff_abs}')
print(f'Частное двух чисел равна {quo}')
