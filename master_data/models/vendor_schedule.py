from django.db import models

from master_data.models.vendor import Vendor
from master_data.models.base import BaseModelManager


class Day(models.TextChoices):

    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'


class VendorSchedule(models.Model):

    start_time = models.TimeField(blank=False,
                                  null=False)
    end_time = models.TimeField(blank=False,
                                null=False)
    day = models.CharField(choices=Day.choices,
                           blank=False,
                           null=False)
    vendor = models.ForeignKey(Vendor,
                               on_delete=models.PROTECT,
                               blank=False)
    deleted_flag = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:

        db_table = "master_vendor_schedule"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return f"{self.day}, {self.start_time} to {self.end_time}"
