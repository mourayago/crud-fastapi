from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] | None = None


sqlite_file_name = "hero_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Deadpool", secret_name="wolvedead")
hero_2 = Hero(name="Spiderman", secret_name="spider pig")
hero_3 = Hero(name="fat joe", secret_name="fatty", age=13)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()