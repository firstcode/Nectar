from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.forms import ModelForm
from datetime import datetime
from django.db.models import Count


from datetime import timedelta
import dateutil.parser
import uuid, os

DEFAULT_PROFILE_PICTURE_URL = 'http://placehold.it/350x350'

role_UserCourseRelationship_choices = (
    ('S', 'student'),
    ('I', 'instructor'),
)

class UserCourseRelationship(models.Model):
  """
  this takes care of both student enrollment and instructor assignment
  """
  user = models.ForeignKey('profiles.User')
  course = models.ForeignKey('Course')

  role = models.CharField(max_length=1, default='S', choices = role_UserCourseRelationship_choices)

  class Meta:
    unique_together = ('user', 'course',)


class Course(models.Model):
  name = models.CharField(max_length=255, blank=False)
  course_code = models.CharField(max_length=255, blank=False)
  course_icon_url = models.URLField(blank=True, default=DEFAULT_PROFILE_PICTURE_URL)
  eventbrite_tag = models.CharField(max_length=255, blank=True)



from django.contrib.postgres.fields import JSONField

def awardDefinition_default():
    return {}

class Challenge(models.Model):
  name = models.CharField(max_length=255, blank=False)
  order = models.IntegerField(blank = True, default = 0)
  createdDate = models.DateTimeField(default=timezone.now)

  # ruleDefinition: will determine what kind of challenges will load

  # this determines what kind of awards are given when challenge is completed
  awardDefinition = JSONField(default = awardDefinition_default)

  # each challenge when completed results in a ChallengeRecord, to mark that the challenge is completed
  point = models.IntegerField(blank = False, default = 10)



class Trophy(models.Model):
  name = models.CharField(max_length=255, blank=False)
  avatar_url = models.URLField('avatar_url',blank=True, default=DEFAULT_PROFILE_PICTURE_URL)

  # describes how many points are required to attain trophy
  threshold = models.IntegerField(blank = False, default = 100)


class ChallengeRecord(models.Model):
  """ 
  this is where students record their points for challenges, each challenge has to work towards some trophy
  """
  createdDate = models.DateTimeField(default=timezone.now)

  trophy = models.ForeignKey('trophy',null = True)
  user = models.ForeignKey('profiles.User')
  point = models.IntegerField(blank = False, default = 10)


class TrophyRecord(models.Model):
  """ 
  when students accumulate challenge points and cross a trophy's threshold, they win a trophy, each user can only win a trophy once
  """
  createdDate = models.DateTimeField(default=timezone.now)
  trophy = models.ForeignKey('trophy')
  user = models.ForeignKey('profiles.User')

  class Meta:
    unique_together = ('user', 'trophy',)










