from ormopt_part2.db.session import SessionLocal, engine
from ormopt_part2.models import base, actor, address, city, country, inventory, rental
from sqlalchemy.orm import joinedload, selectinload, subqueryload
from sqlalchemy import Index
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone

def main():
    RUNS = 50
    data = [np.zeros(RUNS) for _ in range(3)]

    print('================= Start Samplg Filtering Queries for Rental (No Index) =================')
    for x in range(RUNS):
        session = SessionLocal()
        start_time = time.time()
        rentals = session.query(rental.Rental).filter(
            rental.Rental.return_date < datetime(2022, 6, 22, tzinfo=timezone.utc)
        ).order_by(rental.Rental.return_date).limit(100).all()
        data[0][x] = time.time() - start_time
        session.commit()

    print('================= Start Samplg Filtering Queries for Rental (Wrong Index) =================')

    idx_customerid_returndate = Index('idx_customerid_returndate', rental.Rental.customer_id, rental.Rental.return_date)
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        db_name = conn.engine.url.database
        print("Connected to database:", db_name, " Creating index idx_customerid_returndate")
        idx_customerid_returndate.create(conn)

    for x in range(RUNS):
        session = SessionLocal()
        start_time = time.time()
        rentals = session.query(rental.Rental).filter(
            rental.Rental.return_date < datetime(2022, 6, 22, tzinfo=timezone.utc)
        ).order_by(rental.Rental.return_date).limit(100).all()
        data[1][x] = time.time() - start_time
        session.commit()
    
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        idx_customerid_returndate.drop(conn)

    print('================= Start Samplg Filtering Queries for Rental (Right Index) =================')

    idx_returndate_customerid = Index('idx_returndate_customerid', rental.Rental.return_date, rental.Rental.customer_id)
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        idx_returndate_customerid.create(conn)

    for x in range(RUNS):
        session = SessionLocal()
        start_time = time.time()
        rentals = session.query(rental.Rental).filter(
            rental.Rental.return_date < datetime(2022, 6, 22, tzinfo=timezone.utc)
        ).order_by(rental.Rental.return_date).limit(100).all()
        data[2][x] = time.time() - start_time
        session.commit()

    
    with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
        idx_returndate_customerid.drop(conn)

    print("data:", data)
    labels = ["No index", "Wrong order", "Correct order"]

    plt.figure(figsize=(7,5))
    plt.boxplot(data, labels=labels)

    plt.ylabel("Execution time (s)")
    plt.title("Benchmark of Index Settings")
    plt.grid(axis='y', linestyle="--", alpha=0.6)

    plt.savefig('different_index_settings.png')

if __name__ == "__main__":
    main()

# Activate the venv (for python 3.9), then
# python3 -m ormopt_part2_part2.research_missing_indexes