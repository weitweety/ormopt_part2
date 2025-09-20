from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/pagila_large", echo=True)
SessionLocal = sessionmaker(bind=engine)
