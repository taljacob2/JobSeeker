from django.db import models
from .job_type import JobType
from .location import Location
from .years_of_experience import YearsOfExperience


class Preference(models.Model):
    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    years_of_experience = models.ForeignKey(YearsOfExperience, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)
