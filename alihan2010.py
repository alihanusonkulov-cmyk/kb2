text = input("Введите строку: ")

# Учитываем как русские, так и английские гласные (судя по примеру с "Python")
vowels_list = "аеёиоуыэюяaeiouy"

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():  # Проверяем, является ли символ буквой (игнорируем пробелы, цифры, знаки)
        if char in vowels_list:
            vowels += 1
        else:
            consonants += 1

print(f"гласных={vowels}, согласных={consonants}")
