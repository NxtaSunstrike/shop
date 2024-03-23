from sqlalchemy import select

from bot.databases.base import Cloth,async_session
            
async def get_cloths():
    async with async_session() as session:
        result = await session.execute(select(Cloth))
        return result.scalars().all()

async def get_cloth_by_id(id):
    async with async_session() as session:
        result = await session.execute(select(Cloth).where(Cloth.id == id))
        return result.scalars().first()
        
    
