from database.database_setup import BaseModel

from sqlalchemy import Column, Integer, VARCHAR, DateTime, sql, func


class Films(BaseModel):
    __tablename__ = 'films'

    # Film id.
    film_id = Column(Integer, primary_key=True, nullable=False)
    # Film name.
    film_name = Column(VARCHAR(128), nullable=False)
    # Created film date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
