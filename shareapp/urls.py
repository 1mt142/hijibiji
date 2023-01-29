from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-delete'),
]
