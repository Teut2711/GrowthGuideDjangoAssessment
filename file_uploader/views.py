from enum import Enum
import os
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
import pandas as pd
from file_uploader.forms import FileUploadModelForm
from file_uploader.models import FileUpload
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import FileResponse, HttpResponse


def get_excel_response(file_path):
    df = pd.read_excel(file_path)
    return df.to_html()


def get_csv_response(file_path):
    df = pd.read_csv(file_path)
    return df.to_html()


def file_download_view(request, file_name, command):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)

    if command == "open":
        if file_path.endswith(".csv"):
            html_string = get_csv_response(file_path)
        else:
            html_string = get_excel_response(file_path)

        return HttpResponse(html_string)
    else:
        return FileResponse(
            open(file_path, "rb"), filename=file_name, as_attachment=True
        )


class FileUploadCreateView(LoginRequiredMixin, CreateView):
    model = FileUpload
    form_class = FileUploadModelForm

    def form_valid(self, form):
        messages.success(self.request, "Upload successful!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("file_upload_create")


class FileUploadListView(LoginRequiredMixin, ListView):
    model = FileUpload


class FileUploadDeleteView(DeleteView):
    model = FileUpload

    def get_success_url(self):
        return reverse("file_upload_list")
