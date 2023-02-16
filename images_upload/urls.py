from django.urls import path
from .views import ImageList, ImageDetail


urlpatterns = [
    path('<int:pk>/', ImageDetail.as_view(), name="image_detail"),
    path('', ImageList.as_view(), name="image_list"),
]
