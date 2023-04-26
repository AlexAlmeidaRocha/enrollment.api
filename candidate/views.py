from django.shortcuts import render

from candidate.models import Candidate
from candidate.serializers import CandidateSerializer

from rest_framework import viewsets

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer