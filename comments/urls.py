from fastapi import APIRouter, Depends
from typing import List

from .db_service import DBService
from .schemas import (
    ArticleCreate,
    ArticleOut,
    CommentArticleCreate,
    CommentArticleOut,
    CommentCommentCreate,
    CommentCommentOut,
)

router = APIRouter()


@router.post("/articles", response_model=ArticleOut)
def add_article(
        article_data: ArticleCreate,
        service: DBService = Depends(),

):
    return service.create_article(article_data)


@router.post("/articles/{article_id}/comments", response_model=CommentArticleOut)
def add_comment_to_article(
        article_id: int,
        comment_data: CommentArticleCreate,
        service: DBService = Depends(),

):
    return service.create_comment_to_article(article_id, comment_data)


@router.post("/comments/{comment_id}", response_model=CommentCommentOut, )
def add_comment_to_comment(
        comment_id: int,
        comment_data: CommentCommentCreate,
        service: DBService = Depends()
):
    return service.create_comment_to_comment(comment_id, comment_data)


@router.get("/articles/{article_id}/comments", response_model=List[CommentArticleOut])
def get_comments_to_article(
        article_id: int,
        service: DBService = Depends()
):
    return service.retrieve_comments_to_article(article_id)


@router.get("/comments/{comment_id}", response_model=List[CommentCommentOut])
def get_comments_to_comment(
        comment_id: int,
        service: DBService = Depends()
):
    return service.retrieve_comments_to_comment(comment_id)
