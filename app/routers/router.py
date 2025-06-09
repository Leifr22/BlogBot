from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Annotated,List
from sqlalchemy import insert, select, update, delete


from app.backend.db_depends import get_db

from app.schemas import CreatePost,ReadPost
from app.models.models import Post


router=APIRouter()

@router.get('/posts',response_model=List[ReadPost])
async def get_all_posts(db: Annotated[AsyncSession,Depends(get_db)]):
    result=await db.execute(select(Post).order_by(Post.date.desc()))
    posts=result.scalars().all()
    return posts
@router.get('/posts/{post_id}',response_model=ReadPost)
async def get_post(db:Annotated[AsyncSession,Depends(get_db)],post_id:int):
    result=await db.execute(select(Post).where(Post.id==post_id))
    post=result.scalar_one_or_none()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='No posts found')
    return post
@router.post('/posts',response_model=ReadPost)
async def create_posts(db:Annotated[AsyncSession,Depends(get_db)],post:CreatePost):
    posts=Post(title=post.title,main_text=post.main_text)
    db.add(posts)
    await db.commit()
    await db.refresh(posts)
    return posts
@router.put('/posts/{post_id}',response_model=ReadPost)
async def update_posts(db:Annotated[AsyncSession,Depends(get_db)],post_id: int,update_posts:CreatePost):
    result=await db.execute(select(Post).where(Post.id==post_id))
    posts=result.scalar_one_or_none()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No posts found')
    posts.title=update_posts.title
    posts.main_text=update_posts.main_text
    await db.commit()
    await db.refresh(posts)
    return posts
@router.delete('/posts/{post_id}',response_model=ReadPost)
async def delete_post(db:Annotated[AsyncSession,Depends(get_db)],post_id: int):
    result=await db.execute(select(Post).where(Post.id==post_id))
    posts=result.scalar_one_or_none()
    if posts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No posts found')
    await db.delete(posts)
    await db.commit()
    return posts

