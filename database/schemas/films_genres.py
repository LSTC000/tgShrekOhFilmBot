from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, Integer, DateTime, sql, func


class FilmsGenres(BaseModel):
    __tablename__ = 'films_genres'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'films_genres_id_seq\')'))
    # Film info code id.
    code_id = Column(Integer, nullable=False)
    # Genre id.
    genre_id = Column(Integer, nullable=False)
    # Created film genre date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
