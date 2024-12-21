from django.urls import path
from .views import (
    MaterialListView,
    MaterialDetailView,
    FileCreateView,
    FileListView,
    download_file,
    SellListView,
    ChartListView,
    MaterialAPIListView,
    MaterialAPIOneView,
)

app_name = "shop"

urlpatterns = [
    path("mat", MaterialListView.as_view(), name="mat-list"),
    path("mat/<int:pk>", MaterialDetailView.as_view(), name="mat-detail"),
    path("mat/api", MaterialAPIListView.as_view(), name="api"),
    path("mat/api/<int:pk>", MaterialAPIOneView.as_view(), name="api-one-action"),
    path("files/upload", FileCreateView.as_view(), name="file-upload"),
    path("files", FileListView.as_view(), name="files-list"),
    path("files/download/<path:name>", download_file, name="file-download"),
    path("fixtures/", SellListView.as_view(), name="fixtures"),
    path("fixtures/charts", ChartListView.as_view(), name="charts"),
]
