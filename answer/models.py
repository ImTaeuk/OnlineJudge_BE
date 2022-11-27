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

from utils.shortcuts import rand_str

class Answer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    submission_id = models.TextField()
    question_id = models.IntegerField(null=True)