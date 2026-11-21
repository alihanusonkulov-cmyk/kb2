# --- ЗАДАЧА 1 ---
name = input("Атыңызды жазыңыз: ").strip()
if not name:
    print("Имя не введено")
else:
    print(f"Привет, {name}! Длина имени: {len(name)}. {name.upper()}")