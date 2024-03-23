from sqlalchemy import BigInteger,Integer
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine
from sqlalchemy import String


engine = create_async_engine("sqlite+aiosqlite:///test.db",echo = True)

async_session = async_sessionmaker(engine)



class Base(AsyncAttrs,DeclarativeBase):
    pass

class Cloth(Base):
    __tablename__ = "cloth"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name :  Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(String)
    price : Mapped[int] = mapped_column(BigInteger)
    count : Mapped[int] = mapped_column(Integer)
    photo_path : Mapped[str] = mapped_column(String)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        






