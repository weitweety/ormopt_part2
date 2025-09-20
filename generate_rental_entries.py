# This code is generated from ChatGPT with specified date range of each column

import csv
import random
from datetime import datetime, timedelta, timezone

# Output CSV path
OUTPUT_FILE = "/tmp/rental_data.csv"

# Configurable number of rows
NUM_ROWS = 500000

# Date range for rental_date (with timezone offsets applied)
start_date = datetime(2022, 2, 14, 16, 16, 3, tzinfo=timezone(timedelta(hours=1)))
end_date   = datetime(2022, 8, 23, 23, 50, 12, tzinfo=timezone(timedelta(hours=2)))

# Function to generate a random datetime within a range
def random_datetime(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

# Generate CSV
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header
    writer.writerow(["rental_date", "inventory_id", "customer_id", "return_date", "staff_id"])
    
    for _ in range(NUM_ROWS):
        rental_date = random_datetime(start_date, end_date)
        
        # Random return_date between 1 and 10 days after rental_date
        return_date = rental_date + timedelta(days=random.randint(1, 10))
        
        inventory_id = random.randint(1, 4581)
        customer_id  = random.randint(1, 599)
        staff_id     = random.randint(0, 1499)
        
        # PostgreSQL expects ISO 8601 format with timezone
        writer.writerow([
            rental_date.isoformat(),
            inventory_id,
            customer_id,
            return_date.isoformat(),
            staff_id
        ])

print(f"CSV file '{OUTPUT_FILE}' with {NUM_ROWS} rows generated successfully.")