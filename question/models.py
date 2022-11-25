import json
from multiprocessing.dummy import Array
from jsonfield import JSONCharField
import jsonfield

from pandas import array
from django.db import models
from django.utils.timezone import now
from utils.models import JSONField
from account.models import User

from utils.models import RichTextField

class Question(models.Model):
    title = models.TextField(default="None")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    problem_id = models.IntegerField()
    contest_id = models.IntegerField()
    content = RichTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    submission_id = models.TextField()
    answer_registered = models.BooleanField(default=True)
    answer_id = models.IntegerField(null=True)
    