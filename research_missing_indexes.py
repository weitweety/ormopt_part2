from ormopt.db.session import SessionLocal
from ormopt.models import base, actor, address, city, country, inventory, rental
from sqlalchemy.orm import joinedload, selectinload, subqueryload
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone



def main():
    # base.Base.registry.configure()
    session = SessionLocal()

    #TODO: PG Try
    # -- 1. No indexes for return_date
    # -- 2. Index for (??, return_date)
    # -- 3. Index for (return_date, ...)

    print('================= Start Samplg Filtering Queries for Rental =================')
    try:
        start_time = time.time()
        rentals = session.query(rental.Rental).filter(
            rental.Rental.return_date < datetime(2022, 6, 22, tzinfo=timezone.utc)
        ).order_by(rental.Rental.return_date).limit(10)
        print(time.time() - start_time)

        # Print results
        for rent in rentals:
            print(rent.rental_id, rent.inventory_id, rent.return_date)
    except Exception as e:
        print('Query Error', e)


if __name__ == "__main__":
    main()

# Activate the venv (for python 3.9), then
# python3 -m ormopt_part2.research_missing_indexes