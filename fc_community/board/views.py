from django.shortcuts import render
from .models import Board
# Create your views here.

def board_list(request):

    boards = Board.objects.all().order_by('-id') # id를 역순으로(최신)

    return render(request, 'board_list.html', {'boards':boards})