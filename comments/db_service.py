import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from django.db import IntegrityError
from fastapi import HTTPException
from starlette import status
from typing import List

from .models import Article, Comment

from .schemas import (
    ArticleCreate,
    CommentArticleCreate,
    CommentCommentCreate
)


class DBService:

    # get article object by id
    @classmethod
    def _get_article(cls, article_id):
        try:
            article = Article.objects.get(id=article_id)
            return article
        except Article.DoesNotExist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Article not found"
            )

    # get comment object by id
    @classmethod
    def _get_comment(cls, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            return comment
        except Comment.DoesNotExist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Comment not found"
            )

    # add an article
    def create_article(self, article_data: ArticleCreate) -> Article:
        try:
            article = Article.objects.create(**article_data.dict())
            return article
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Article has already been added"
            )

    # add a comment to the article
    def create_comment_to_article(self, article_id: int, comment_data: CommentArticleCreate) -> Comment:
        article = self._get_article(article_id)
        comment = Comment.objects.create(**comment_data.dict(), article=article)
        return comment

    # add a comment to the comment
    def create_comment_to_comment(self, comment_id: int, comment_data: CommentCommentCreate) -> Comment:
        comment = self._get_comment(comment_id)
        responding_comment = Comment.objects.create(**comment_data.dict(), parent=comment)
        return responding_comment

    # get comments up to 3rd level
    def retrieve_comments_to_article(self, article_id) -> List[Comment]:
        article = self._get_article(article_id)
        nodes = article.comments.all()
        comments = nodes.get_descendants(include_self=True).filter(level__lte=3)
        if comments:
            return list(comments)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No responding comments"
        )

    # get all comments to the comment
    def retrieve_comments_to_comment(self, comment_id) -> List[Comment]:
        comment = self._get_comment(comment_id)
        comments = comment.get_descendants()
        if comments:
            return list(comments)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There are no comments for comment"
        )
