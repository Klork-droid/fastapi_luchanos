from collections.abc import Generator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

import settings

engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
