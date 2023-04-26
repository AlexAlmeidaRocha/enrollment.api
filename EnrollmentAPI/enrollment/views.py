from django.shortcuts import render

from enrollment.models import Enrollment
from enrollment.serializers import EnrollmentSerializer

from rest_framework import viewsets
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
