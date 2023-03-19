"""GrowthGuideDjangoAssessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from file_uploader.views import (
    FileUploadCreateView,
    FileUploadDeleteView,
    FileUploadListView,
    file_download_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", FileUploadCreateView.as_view(), name="file_upload_create"),
    path("", FileUploadListView.as_view(), name="file_upload_list"),
    path(
        "delete/<int:pk>",
        FileUploadDeleteView.as_view(),
        name="file_upload_delete",
    ),
    path(
        "download/<str:file_name>/<str:command>",
        file_download_view,
        name="file_download",
    ),
]
