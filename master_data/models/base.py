from django.db import models


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_flag=False)
