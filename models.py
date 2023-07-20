from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()


# marker class Base

class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column("lastname", String)

    def __init__(self, firstname, lastname, **kw: Any):
        super().__init__(**kw)
        self.first_name = firstname
        self.last_name = lastname

