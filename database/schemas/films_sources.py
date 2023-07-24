from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, Integer, BOOLEAN, VARCHAR, DateTime, sql, func


class FilmsSources(BaseModel):
    __tablename__ = 'films_sources'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'reviews_id_seq\')'))
    # Film info code id.
    code_id = Column(Integer, nullable=False)
    # Name of source.
    source_name = Column(VARCHAR(32), nullable=False)
    # Link of source.
    source_link = Column(VARCHAR(2048), nullable=False)
    # True if source is official, else - False.
    source_official = Column(BOOLEAN, nullable=False)
    # Created film source date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
