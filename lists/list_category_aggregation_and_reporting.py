#20.08.2026 - 22:45h
# 🥊 Coding Mission 4 — Category Sales Report
sales = [
    ["Keyboard", "Electronics", 70, 4],
    ["Mouse", "Electronics", 25, 10],
    ["Desk", "Furniture", 420, 2],
    ["Monitor", "Electronics", 350, 3],
    ["Chair", "Furniture", 180, 5],
    ["Laptop", "Electronics", 1200, 1],
    ["Lamp", "Furniture", 65, 8],
    ["Webcam", "Electronics", 90, 6]
]
electronics_units = 0
electronics_revenue = 0
furniture_units = 0
furniture_revenue = 0
for sale in sales:
    if sale[3] >=3:
        if sale[1] == 'Electronics':
            electronics_units += sale[3]
            electronics_revenue += sale[2] * sale[3]
        elif sale[1] == 'Furniture':
            furniture_units += sale[3]
            furniture_revenue += sale[2] * sale[3]
category_summary = [
    ["Electronics", electronics_units, electronics_revenue],
    ["Furniture", furniture_units, furniture_revenue]
]
category_summary.sort(key=lambda item: item[2], reverse=True)
print(category_summary)
for category, units, revenue in category_summary:
    print(f'{category} | Unit sold: {units} | Revenue: {revenue}')