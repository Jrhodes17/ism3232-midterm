orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]
from business_rules import (calculate_license_total, needs_contract_review, gets_trainer, total_licensed, largest_license, format_license_line)

print("Cloudstep Software - Order Report")

for order in orders:
    print(format_license_line(order))

contract_reviews_count = 0 
trainers_count = 0

for order in orders:
    total = calculate_license_total(order)
    if needs_contract_review(order["seats"], total):
        contract_reviews_count = contract_reviews_count + 1
    if gets_trainer(order["seats"], order["education"]):
        trainers_count = trainers_count + 1

total_val = total_licensed(orders)
num_orders = len(orders)

if num_orders > 0:
    avg_val = total_val / num_orders
else: 
    avg_val = 0.0

largest_company = largest_license(orders)

print(f"Orders: {num_orders}")
print(f"Total licensed: ${total_val:.2f}")
print(f"Average license total: ${avg_val:2f}")
print(f"Largest license total: {largest_company}")
print(f"Contract reviews needed: {contract_reviews_count}")
print(f"Trainers assigned: {trainers_count}")
