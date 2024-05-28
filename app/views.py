from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def leaderBoard(request):
    return render(request, 'Leaderboard.html')

def whitePaper(request):
    return render(request, 'WhitePaper.html')