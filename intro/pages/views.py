from django.shortcuts import render
import random

def index(request):
    name = '홍성이'
    number = '130'
    lotto_numbers = random.sample(range(1, 46), 6)
    return render(request, "pages/lotto.html", {'name': name, 'number': number, 'lotto_numbers': lotto_numbers})
    

# Create your views here.
