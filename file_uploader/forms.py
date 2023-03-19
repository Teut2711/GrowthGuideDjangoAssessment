from django import forms
from file_uploader.models import FileUpload
from django.core.validators import FileExtensionValidator


class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = "__all__"
        widgets = {
            "file": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": ".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel",
                }
            )
        }
