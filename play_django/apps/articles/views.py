from django.shortcuts import render
from rest_framework import generic, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import(AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Tag, Comment


class ArticleViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = Article.objects.select_related('author', 'author__user')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #serializer
    #renderer

    def get_queryset(self):
        return self.queryset
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)
        
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            queryset = queryset.filter(tags__tag=tag)
        
        favorited_by = self.request.query_params.get('favorited', None)
        if favorited_by is not None:
            queryset = queryset.filter(
                favorited_by__user__username=favorited_by
            )

        return queryset

    
