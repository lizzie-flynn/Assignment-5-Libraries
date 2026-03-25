# pos_checkout.py

# Step 1 — Student Key
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

subtotal = 0.0
total_units = 0

# Step 2 — Item Entry Loop
while True:
    item_name = input("Item name: ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == "":
        print("Invalid item name. Try again.")
        continue

    # Unit price validation
    while True:
        try:
            unit_price = float(input("Unit price: "))
            if unit_price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid price. Enter a number.")

    # Quantity validation
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Enter an integer.")

    subtotal += unit_price * quantity
    total_units += quantity

# Step 5 — Discount Logic
if total_units >= 10 or subtotal >= 100:
    discount_percent = 10
    discount_amount = subtotal * 0.10
else:
    discount_percent = 0
    discount_amount = 0

total = subtotal - discount_amount

# Step 6 — Seed-Based Perk
perk_applied = "NO"

if seed % 2 == 1:
    total -= 3.00
    perk_applied = "YES"

if total < 0:
    total = 0.00

# Step 7 — Output
print(f"Seed: {seed}")
print(f"Units: {total_units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Perk applied: {perk_applied}")
print(f"Total: ${total:.2f}")