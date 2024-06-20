from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.to_do.model import GroupTasks
from src.to_do.schemas import GroupCreate

router = APIRouter(
    prefix="/group",
    tags=["Chat"]
)


@router.get("/get")
async def get_groups(session: AsyncSession = Depends(get_async_session)):
    query = select(GroupTasks)
    result = await session.execute(query)
    return result.all()


@router.post("/add")
async def post_group(new_group: GroupCreate, session: AsyncSession = Depends(get_async_session)):
    query = insert(GroupTasks).values(**new_group.dict())
    result = await session.execute(query)
    await session.commit()
    return {"status": result.all()}


