from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, DateTime, sql, func


class Genres(BaseModel):
    __tablename__ = 'genres'

    # Genre id.
    genre_id = Column(BigInteger, primary_key=True, nullable=False)
    # Genre name.
    genre_name = Column(VARCHAR(32), nullable=True)
    # Created review date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
