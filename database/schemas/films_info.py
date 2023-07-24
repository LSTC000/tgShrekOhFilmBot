from database.database_setup import BaseModel

from sqlalchemy import Column, Integer, SmallInteger, TEXT, LargeBinary, DateTime, sql, func


class FilmsInfo(BaseModel):
    __tablename__ = 'films_info'

    # Film info code id.
    code_id = Column(Integer, primary_key=True, nullable=False)
    # Film id.
    film_id = Column(Integer, nullable=False)
    # Year of the film.
    film_year = Column(SmallInteger, nullable=False)
    # Score of the film.
    film_score = Column(SmallInteger, nullable=False)
    # Image preview of the film.
    film_image = Column(LargeBinary, nullable=False)
    # Description of the film.
    film_desc = Column(TEXT, nullable=False)
    # Created film info date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
