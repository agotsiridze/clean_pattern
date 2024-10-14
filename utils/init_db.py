from config import Base, engine
from models import Region, City


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Region.metadata.create_all(bind=engine)
    City.metadata.create_all(bind=engine)
