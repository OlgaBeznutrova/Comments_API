from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ArticleBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


class ArticleCreate(ArticleBase):
    pass


class ArticleOut(ArticleBase):
    id: int


class CommentBase(BaseModel):
    text: str

    class Config:
        orm_mode = True


class CommentArticleCreate(CommentBase):
    pass


class CommentCommentOut(CommentBase):
    id: int
    created_at: datetime
    parent: "CommentCommentOut" = None


class CommentArticleOut(CommentCommentOut, CommentBase):
    id: int
    created_at: datetime
    article: Optional[ArticleOut] = None


class CommentCommentCreate(CommentBase):
    pass
