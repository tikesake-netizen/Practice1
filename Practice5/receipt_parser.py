import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

total = re.search(r"Итого:\s*\n\s*([\d\s]+,\d+)", text, re.IGNORECASE)

if total:
    print("Общая сумма:", total.group(1))
else:
    print("Общая сумма не найдена")




date_time = re.search(r"(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)

if date_time:
    print("Дата:", date_time.group(1))
    print("Время:", date_time.group(2))
else:
    print("Дата и время не найдены")



receipt_number = re.search(r"Фискальный признак:\s*(\d+)", text)

if receipt_number:
    print("Фискальный признак:", receipt_number.group(1))
else:
    print("Фискальный признак не найден")




seller = re.search(r"Филиал\s+(.+)", text)

if seller:
    print("Продавец:", seller.group(1))
else:
    print("Продавец не найден")



products = re.findall(
    r"^\d+\.\s*\n(.+)\n(\d+,\d+)\s*x\s*(\d+,\d+)",
    text,
    re.MULTILINE
)

print("\nТовары:")

for name, quantity, price in products:
    print("Название:", name)
    print("Количество:", quantity)
    print("Цена:", price)
    print()





print("\n" + "=" * 40)
print("ИНФОРМАЦИЯ О ЧЕКЕ")
print("=" * 40)

if seller:
    print("Продавец:", seller.group(1))

if date_time:
    print("Дата:", date_time.group(1))
    print("Время:", date_time.group(2))

if total:
    print("Общая сумма:", total.group(1))

if receipt_number:
    print("Фискальный признак:", receipt_number.group(1))

print("=" * 40)









