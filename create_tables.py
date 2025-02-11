from core.configs import settings
from core.database import engine


async def create_tables() -> None:
    import models.__all_models
    print('Creating all tables in database...')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DATABASE_BaseModel.metadata.drop_all)
        await conn.run_sync(settings.DATABASE_BaseModel.metadata.create_all)
    print('Tables created with success!')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
