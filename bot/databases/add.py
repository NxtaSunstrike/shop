from bot.databases.base import Cloth,async_session

            
async def add_cloth(cloths:dict[str|int]):
    async with async_session() as session:
        async with session.begin():
            clothe = Cloth(
                name = cloths['name'], 
                description = cloths['description'], 
                count = cloths['count'], 
                price = cloths['price'],
                photo_path = cloths['photo_path']
                )
            session.add(clothe)

