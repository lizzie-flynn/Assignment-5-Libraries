# inventory_spotcheck.py

import requests

# Step 1 — Student Key
student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

total_skus = 0
reorder_count = 0

# Step 4 — Threshold Logic
if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

# Step 2 — SKU Loop
while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("Invalid SKU. Try again.")
        continue

    # Step 3 — On-hand validation
    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("Must be 0 or greater.")
                continue
            break
        except ValueError:
            print("Invalid number.")

    total_skus += 1

    if on_hand < threshold:
        reorder_count += 1

# Step 6 — API Term
if seed % 2 == 0:
    term = "weezer"
else:
    term = "drake"

api_status = "OK"
song_count = "N/A"

# Step 7 & 8 — API Request
try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={
            "entity": "song",
            "limit": 5,
            "term": term
        },
        timeout=5
    )

    if response.status_code != 200:
        api_status = "FAILED"
    else:
        data = response.json()

        if "results" not in data:
            api_status = "INVALID_RESPONSE"
        else:
            count = 0
            for item in data["results"]:
                if item.get("kind") == "song":
                    count += 1
            song_count = count

except requests.exceptions.RequestException:
    api_status = "FAILED"
except ValueError:
    api_status = "INVALID_RESPONSE"

# Step 10 — Output
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {song_count}")
print(f"API status: {api_status}")