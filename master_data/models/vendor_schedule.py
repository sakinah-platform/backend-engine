from django.db import models
from django.core.exceptions import ValidationError
from django_softdelete.models import SoftDeleteModel

from backend.system_utility.system_constant import DAYS, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
from master_data.models.vendor import Vendor


class Day(models.TextChoices):

    MONDAY = DAYS.get(MONDAY)
    TUESDAY = DAYS.get(TUESDAY)
    WEDNESDAY = DAYS.get(WEDNESDAY)
    THURSDAY = DAYS.get(THURSDAY)
    FRIDAY = DAYS.get(FRIDAY)
    SATURDAY = DAYS.get(SATURDAY)
    SUNDAY = DAYS.get(SUNDAY)


class VendorSchedule(SoftDeleteModel):

    start_time = models.TimeField(blank=False,
                                  null=False)
    end_time = models.TimeField(blank=False,
                                null=False)
    day = models.CharField(choices=Day.choices,
                           blank=False,
                           null=False)
    vendor = models.ForeignKey(Vendor,
                               related_name='schedules',
                               on_delete=models.PROTECT,
                               blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "vendor_schedule"
        get_latest_by = ["-created_at"]

    def __str__(self):
        return f"{self.day}, {self.start_time} to {self.end_time}"

    def validate_unique(self, exclude=None):
        schedule = VendorSchedule.objects.filter(vendor=self.vendor,
                                                 start_time=self.start_time,
                                                 end_time=self.end_time,
                                                 day=self.day)
        if schedule.exists():
            raise ValidationError(f'Schedule for {self.vendor.name} already exists')
