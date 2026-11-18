# --- ЗАДАЧА 1 ---
name = input("Атыңызды жазыңыз: ").strip()
if not name:
    print("Имя не введено")
else:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")


# --- ЗАДАЧА 2 ---
a = int(input("Биринчи санды жазыңыз (a): "))
b = int(input("Экинчи санды жазыңыз (b): "))

base = f"сумма={a + b}, разность={a - b}, произведение={a * b}"
if b == 0:
    print(f"{base}, деление на ноль")
else:
    print(f"{base}, частное={a / b:.2f}, остаток={a % b}")


# --- ЗАДАЧА 3 ---
n = int(input("Текшерүү үчүн бир сан жазыңыз: "))

parity = "чётное" if n % 2 == 0 else "нечётное"
if n > 0:
    sign = "положительное"
elif n < 0:
    sign = "отрицательное"
else:
    sign = "ноль"
mult5 = "да" if n % 5 == 0 else "нет"

print(f"{parity}, {sign}, кратно 5: {mult5}")


# --- ЗАДАЧА 4 ---
nums = [int(input(f"{i + 1}-санды жазыңыз: ")) for i in range(3)]
asc = sorted(nums)
desc = sorted(nums, reverse=True)

print("по возрастанию:", *asc)
print("по убыванию:", *desc)
print(f"мин={asc}, макс={asc[-1]}")


# --- ЗАДАЧА 5 ---
n = int(input("Көбөйтүү жадыбалы үчүн N санын жазыңыз: "))
for i in range(1, n + 1):
    row = [f"{i * j:<3}" for j in range(1, n + 1)]
    print("".join(row).rstrip())
