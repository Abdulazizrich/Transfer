from django.shortcuts import render
from mainApp.models import *
from datetime import date


def index(request):
    return render(request, 'index.html')


def clubs(request):
    context = {
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs.html', context)


def players(request):
    context = {
        'players': Player.objects.all()
    }
    return render(request, 'players.html', context)


def davlat_club(request, count_name):
    context = {
        'clubs': Club.objects.filter(davlat__nom__contains=count_name)
    }
    return render(request, 'country_clubs.html', context)


def u_20(request):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana = hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    players = Player.objects.filter(t_yil__gt=yangi_sana)
    context = {
        'players': players
    }
    return render(request, 'U-20 players.html', context=context)


def transfer_2023(request):
    context = {
        'transfer': Transfer.objects.filter(mavsum="2022-2023")
    }
    return render(request, 'latest-transfers.html', context)


def stats(request):
    return render(request, 'stats.html')


def t_records(request):
    context = {
        'records': Transfer.objects.all()
    }
    return render(request, 'stats/transfer-records.html', context)


def about(request):
    return render(request, 'about.html')


def club_players(request, nom):
    context = {
        'players': Player.objects.filter(club=Club.objects.get(nom=nom))
    }
    print(Player.objects.filter(club=Club.objects.get(nom=nom)))
    return render(request, 'club-players.html', context)


def tryouts(request):
    return render(request, 'tryouts.html')


def records150(request):
    context = {
        'records': Transfer.objects.order_by('-narx')[:150]
    }
    return render(request, 'stats/150-accurate-predictions.html', context)


def top50(request):
    return render(request, 'stats/top-50-clubs-by-expenditure-in-2021.html')


def top502(request):
    return render(request, 'stats/top-50-clubs-by-income-in-2021.html')


def archive(request):
    return render(request, 'transfer-archive.html')

def season(request):
    return render(request, '2017-18season.html')