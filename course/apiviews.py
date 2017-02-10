from course.models import *
from course.serializers import *

from rest_framework import viewsets, filters, generics, views

import sys, inspect, itertools
from rest_framework.exceptions import APIException, ParseError, PermissionDenied
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.utils import timezone
from django.conf import settings

from .utils import get_model_concrete_fields

import requests




class UserCourseRelationshipViewSet(viewsets.ModelViewSet):
    """
    defines the relationship between Instructor user and courses
    """
    api_name = 'usercourserelationship'
    queryset = UserCourseRelationship.objects.all()
    serializer_class = UserCourseRelationshipSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user',)



class CourseViewSet(viewsets.ModelViewSet):
    """
    defines the Course objects 
    """
    api_name = 'course'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    http_method_names =['get']
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('course_code',)


class CourseClassDateRelationship(viewsets.ModelViewSet):
    """
    defines the CourseClassDateRelationship objects 
    """
    api_name = 'courseclassdaterelationship'
    queryset = CourseClassDateRelationship.objects.all()
    serializer_class = CourseClassDateRelationshipSerializer
    http_method_names =['get']
    permission_classes = (AllowAny,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('course_code',)


class LessonViewSet(viewsets.ModelViewSet):
    """
    defines the Course objects 
    """
    api_name = 'lesson'
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('course',)


class ChallengeViewSet(viewsets.ModelViewSet):
    """
    defines the School objects that could be associated with a user under UserSchoolRelation
    """
    api_name = 'challenge'
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('lesson',)


class TrophyViewSet(viewsets.ModelViewSet):
    """
    defines the School objects that could be associated with a user under UserSchoolRelation
    """
    api_name = 'trophy'
    queryset = Trophy.objects.all()
    serializer_class = TrophySerializer
    permission_classes = (IsAuthenticated,)


class ChallengeRecordViewSet(viewsets.ModelViewSet):
    """
    defines the Challenge records to denote the progress of the user in the challenges, also used in determining earned trophies
    """
    api_name = 'challengerecord'
    queryset = ChallengeRecord.objects.all()
    serializer_class = ChallengeRecordSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user',)

class ChallengeProgressViewSet(viewsets.ModelViewSet):
    """
    defines the user's progress within a challenge which may have multiple questions. progress within a challenge is recognized by a signature
    \n the MD5 signature can be generated using a question's text for example
    """
    api_name = 'challengeprogress'
    queryset = ChallengeProgress.objects.all()
    serializer_class = ChallengeProgressSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'challenge')


class TrophyRecordViewSet(viewsets.ModelViewSet):
    """
    defines the School objects that could be associated with a user under UserSchoolRelation
    """
    api_name = 'trophyrecord'
    queryset = TrophyRecord.objects.all()
    serializer_class = TrophyRecordSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user',)

class SendConfirmationView(views.APIView):
    """
\n    1. POST a payload with name and email to invite a user 
    """

    api_name = 'sendconfirmation'

    # this endpoint should be public so anyone can sign up
    permission_classes = (IsAuthenticated, )
    http_method_names =['post']

    def post(self, request, format=None, *args, **kwargs):
        user = request.user

        print 'sendconfirmation...', user.email

        manual_send_confirmation_mail(user)

        # complete_signup(self.request._request, user,
        #     True,
        #     None)

        r = {'id': user.id, 'email': user.email}

        return Response(r)

class CodeNinjaCacheUpdateView(views.APIView):
    """
    \n POST to update CodeNinjaCache
    """
    api_name = 'codeninjacacheupdate'

    # this endpoint should be public so anyone can sign up
    permission_classes = (AllowAny, )
    http_method_names =['post']
    cnHeaders = {'Authorization': settings.CNKEY}
    
    def updateCourse(self, c, classDates = []):
        """
        suppose code ninja passes a payload of a course, update or create the records on nectar
        ie:
        c = {
          "name": "Playful Discovery of Robotics",
          "age_group": "6-8",
          "course_icon_url": "https://firstcode-codeninjas-v3.s3.amazonaws.com/hk/uploads/course_module/50/course_icon_url/icon_robotics.jpg",
          "course_code": "CC16-AT-RO-1219-SW",
          "location": "Sheung Wan",
          "start_date": "2016-12-19",
          "end_date": "2016-12-23",
          "start_time": "2000-01-01T10:00:00.000Z",
          "end_time": "2000-01-01T12:00:00.000Z",
          "capacity": 8,
          "enrollment_count": 5,
          "eventbrite_tag": "28953934999",
          "active": true,
          "remark": "5-day camp, 10 hours total."
        }

        """

        if c['course_code'] is None or len(c['course_code']) == 0:
            # skip items that are not valid
            return None, False

        # filter out certain keys that should not be overwritten
        c = {k:v for (k,v) in c.items() if k not in ['id'] and k in get_model_concrete_fields(Course) }

        course, created = Course.objects.update_or_create(
            # filter by
            course_code = c['course_code'],


            # name =  c['name'],
            # age_group = c['age_group'],
            # course_icon_url = c['course_icon_url'],
            # location = c['location'],
            # start_date = c['start_date'],
            # end_date = c['end_date'],
            # start_time = c['start_time'],
            # end_time = c['end_time'],
            # capacity = c['capacity'],
            # enrollment_count = c['enrollment_count'],
            # # eventbrite_tag = c['eventbrite_tag'],
            # active = c['active'],
            # remark = c['remark'],

            defaults = c,
        )

        # update course time info, but only for term courses, camps and events have their class dates saved during model save, see models.py
        if course.evenr_type == 'term':
            course.updateClassDates(classDates)

        # print 'course created', course.id, created, course.course_code





        return course, created

    def processCamps(self, payload_ids, subdomain= None):
        """
        processes the returned data for camps
        """

        memo = {}

        for i in payload_ids:
            # attempt to poll data from 

            # r = requests.get('http://hk.firstcodeacademy.com/api/camps/3/offerings', headers=self.cnHeaders)
            # print r.json()

            obj = None

            try:
                r = requests.get(i, headers=self.cnHeaders, verify=False)
                data = r.json()

                # print i

                # filter out certain keys that should not be overwritten
                data = {k:v for (k,v) in data.items() if k not in ['id'] }

                obj, created = CodeNinjaCache.objects.update_or_create(
                    # filter by this
                    endpoint = i,

                    # insert / update this
                    defaults = { 'data': data },
                )

                # print obj, created, obj.data, obj.data.get('offerings', [])

                # camps have start / end dates lodged inside the course object
                # courseDates = obj.getCourseDates()


            
                if obj:
                    for c in obj.data.get('offerings', []):

                        # inject subdomain to c
                        c['subdomain'] = subdomain
                        
                        # print 'offering', c

                        if c['course_code'] not in memo:
                            c['cnType'] = 'camps'
                            self.updateCourse(c, classDates = [])
                        
                        memo[c['course_code']] = c

            except Exception as e: 
                print 'CodeNinjaCacheUpdate', e, i




        return memo

    def processPrograms(self, payload_ids, subdomain = None):
        """
        processes the returned data for camps
        """

        memo = {}

        for i in payload_ids:
            # attempt to poll data from 

            # r = requests.get('http://hk.firstcodeacademy.com/api/camps/3/offerings', headers=self.cnHeaders)
            # print r.json()

            obj = None

            try:
                r = requests.get(i, headers=self.cnHeaders, verify=False)
                data = r.json()

                # filter out certain keys that should not be overwritten
                data = {k:v for (k,v) in data.items() if k not in ['id'] }

                obj, created = CodeNinjaCache.objects.update_or_create(
                    # filter by this
                    endpoint = i,

                    # insert / update this
                    defaults = { 'data': data },
                )

                # programs have dates listed in class_dates field , extract them
                # courseDates are supplied as a dict of {<weekday>: [<datetime>...]}
                courseDates = obj.getCourseDates()


                weekdayMapping = {
                    'mon': 0,
                    'tue': 1,
                    'wed': 2,
                    'thu': 3,
                    'fri': 4,
                    'sat': 5,
                    'sun': 6,
                }


            
                if obj:   
                    for c in obj.data.get('offerings', []):
                        
                        # print 'offering', c

                        # inject subdomain to c
                        c['subdomain'] = subdomain

                        if c['course_code'] not in memo:
                            c['cnType'] = 'programs'

                            # courseDates are supplied as a dict of {<weekday>: [<datetime>...]}
                            # classDates only selects the time of date
                            classDates = []

                            # these are 'Mon', 'Tue'
                            class_day = c.get('class_day', '')

                            # is the translated numerical mapping as specified in weekdayMapping
                            class_weekday = weekdayMapping.get(class_day.lower(), None)
                            if class_weekday is not None:
                                classDates = courseDates.get(class_weekday, [])
                                # print 'extracted classDates', classDates


                            self.updateCourse(c, classDates = classDates)
                        
                        memo[c['course_code']] = c


            except Exception as e: 
                print 'CodeNinjaCacheUpdate', e, i


        return memo

    def post(self, request, format=None, *args, **kwargs):
        verifyToken = request.data.get('verifyToken')

        # confirm that frontend has a signature passed
        if verifyToken != settings.VERIFYTOKEN:
            raise PermissionDenied('Verification Token missing or invalid')

        # needed for codeninja verification

        countriesUrl = 'http://www.firstcodeacademy.com/api/countries'
        r = requests.get(countriesUrl, headers = self.cnHeaders, verify=False)

        # print r, r.status_code, r.text, self.cnHeaders

        countriesData = r.json()
        subdomains = [i['subdomain'] for i in countriesData]


        allcampsMemo = {}
        allprogramsMemo = {}

        for s in subdomains:

            # take a look at the active camps first
            activeCampsUrl = 'http://{}.firstcodeacademy.com/api/camps'.format(s)
            r = requests.get(activeCampsUrl, headers = self.cnHeaders, verify=False)
            activeCampsData = r.json()

            activeCampsData_ids = ['http://{}.firstcodeacademy.com/api/camps/{}'.format(s ,i['id']) for i in activeCampsData]
            print 'activeCampsData_ids', activeCampsData_ids

            # now we can start polling endpoint
            campsMemo = self.processCamps(activeCampsData_ids, subdomain = s)
            for k in campsMemo:
                allcampsMemo[k] = campsMemo[k]




            # take a look at the programs
            activeProgramsUrl = 'http://{}.firstcodeacademy.com/api/programs'.format(s)
            r = requests.get(activeProgramsUrl, headers = self.cnHeaders, verify=False)
            activeProgramsData = r.json()

            activeProgramsData_ids = ['http://{}.firstcodeacademy.com/api/programs/{}'.format(s, i['id']) for i in activeProgramsData]
            print 'activeProgramsData_ids', activeProgramsData_ids

            # now we can start polling endpoint
            # missing course_code, abort
            # programsMemo = None
            programsMemo = self.processPrograms(activeProgramsData_ids, subdomain = s)
            for k in programsMemo:
                allprogramsMemo[k] = programsMemo[k]




        





        r = {'status': 'success', 
        'campsMemo': allcampsMemo, 
        'programsMemo': allprogramsMemo}

        return Response(r)


    
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
clsmembers = filter(lambda x: issubclass(x[1], viewsets.ModelViewSet )  \
                    or issubclass(x[1], viewsets.ReadOnlyModelViewSet ) \
                    or issubclass(x[1], views.APIView ) \
                    # or issubclass(x[1], CreateAPIView ) \
                    , clsmembers)
