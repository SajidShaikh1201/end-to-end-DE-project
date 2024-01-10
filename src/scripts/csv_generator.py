import csv
import os
import random
from datetime import datetime, timedelta
from resources import config

customers = list(range(1, 21))
store_ids = list(range(101, 104))
product_data = {
    'Rice': 40.75,
    'Dal': 60.50,
    'Oil': 120.00,
    'Sugar': 35.99,
    'Flour': 25.50,
    'Tea Leaves': 55.25,
    'Spices': 45.00,
    'Salt': 15.75,
    'Milk': 25.99,
    'Bread': 30.50
}

sales_person = {
    101: [1, 2, 3],
    102: [4, 5, 6],
    103: [7, 8, 9],
}

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 1)

file_location = config.local_file_location
csv_file_path = os.path.join(file_location, "sales_data.csv")

with open(csv_file_path, "w", newline="") as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(["customer_id", "store_id", "product_name", "sales_date", "sales_person_id", "price", "quantity",
                        "total_cost"])

    for _ in range(5):
        customer_id = random.choice(customers)
        store_id = random.choice(store_ids)
        product_name = random.choice(list(product_data.keys()))
        sales_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        sales_person_id = random.choice(sales_person[store_id])
        quantity = random.choice(range(1, 10))
        price = product_data[product_name]
        total_cost = price * quantity

        csvwriter.writerow([customer_id, store_id, product_name, sales_date.strftime("%Y-%m-%d"), sales_person_id,
                            price, quantity, total_cost])

print("CSV data generated successfully.....")
