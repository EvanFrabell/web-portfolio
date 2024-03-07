from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter


from application.models import Baseball
from application.serializers import BaseballSerializer


def home(request):
    return render(request, 'main.html')


def projects(request):
    return render(request, 'projects.html')


def tutorials(request):
    return render(request, 'tutorials.html')


def sabermetrics(request):
    qs = Baseball.objects.all()
    player = request.GET.get('player')
    team = request.GET.get('team')
    yearid = request.GET.get('yearid')

    if player != '' and player is not None:
        qs = qs.filter(player__icontains=player).order_by('player', 'yearid', 'team')

    if team != '' and team is not None:
        qs = qs.filter(team__icontains=team).order_by('yearid', 'team', 'player')

    if yearid != '' and yearid is not None:
        qs = qs.filter(yearid__icontains=yearid).order_by('yearid', 'team', 'player')
    #
    if player is None and team is None and yearid is None:
        qs = None

    context = {
        'base_rec': qs
    }
    return render(request, 'sabermetrics.html', context)


def about(request):
    return render(request, 'about.html')


class SabermetricList(generics.ListAPIView):
    queryset = Baseball.objects.all()
    serializer_class = BaseballSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['player', 'team', 'yearid']
