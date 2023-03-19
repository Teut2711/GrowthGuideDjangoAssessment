from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return filename


class FileUpload(models.Model):
    file = models.FileField(upload_to=user_directory_path)
