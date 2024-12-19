from django.db import models
from django_softdelete.models import SoftDeleteModel


class City(SoftDeleteModel):

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "master_city"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return self.name
