from django.urls import path
from .views import blogListViews, CreatePostView,blogDetalleView,blogUpdateView,blogdelete

app_name = "blog"

urlpatterns =[
    path("", blogListViews.as_view(), name="home"),
    path("create/", CreatePostView.as_view(), name="create"),
    path("<int:pk>/", blogDetalleView.as_view(), name="detalle"),
    path("<int:pk>/update", blogUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", blogdelete.as_view(), name="delete"),
]