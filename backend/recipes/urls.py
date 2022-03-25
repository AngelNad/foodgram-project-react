from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientsViewSet, RecipeViewSet, TagsViewSet

v1 = DefaultRouter()
v1.register(r'recipes', RecipeViewSet, basename='recipes')
v1.register(r'ingredients', IngredientsViewSet, basename='ingredients')
v1.register(r'tags', TagsViewSet, basename='tags')


urlpatterns = [
    path('', include(v1.urls)),
]
