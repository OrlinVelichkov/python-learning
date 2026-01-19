budget = float(input())
flour_price = float(input())

# Изчисляване на цените за 1 козунак (loaf)
eggs_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price_needed = milk_price_per_liter * 0.250

loaf_price = flour_price + eggs_price + milk_price_needed

loaves_count = 0
colored_eggs = 0

# Готвим, докато бюджетът е по-голям от цената на един козунак
while budget >= loaf_price:
budget -= loaf_price
loaves_count += 1
colored_eggs += 3

# На всеки 3-ти хляб губим яйца
if loaves_count % 3 == 0:
lost_eggs = loaves_count - 2
colored_eggs -= lost_eggs

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")