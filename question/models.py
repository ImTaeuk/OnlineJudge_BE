import json
from multiprocessing.dummy import Array
from jsonfield import JSONCharField
import jsonfield

from pandas import array
from django.db import models
from django.utils.timezone import now
from utils.models import JSONField

from utils.models import RichTextField

class Question(models.Model):
    id = models.TextField(db_index=True, primary_key=True)
    title = models.TextField(default="None")
    created_by = models.TextField(unique=True)
    problem_id = models.IntegerField(null=False)
    contest_id = models.IntegerField(null=True)
    content = RichTextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    submission_id = models.IntegerField(null=False)
    answer_registered = models.BooleanField(default=False)
    answer_id = models.IntegerField(null=True)
