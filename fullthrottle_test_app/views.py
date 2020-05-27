from django.shortcuts import render
from rest_framework.response import Response
from .models import *
import datetime

# Create your views here.
from rest_framework.views import APIView


class DataView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        periods = ActivityPeriod.objects.all()
        members = list()
        for i in users:
            name = i.name
            id = i.id
            timezone = i.timezone
            activity_periods = []
            for j in periods:
                if j.u_id == id:
                    activity_periods.append(
                        {"start_time": datetime.datetime.strftime(j.start_time, "%b %d %Y  %H:%M %p"),
                         "end_time": datetime.datetime.strftime(j.end_time, "%b %d %Y  %H:%M %p")})
            members.append({"id": id, "real_name": name, "tz": timezone, "activity_periods": activity_periods})

        return Response({"ok": True, "members": members})
