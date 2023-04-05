from django.shortcuts import render

from .services import currencies
from .forms import ExchangeForm


def index(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        give = request.POST.get('give')
        receive = request.POST.get('receive')
        amount = int(request.POST.get('amount'))

        if give and receive:
            if give == 'BYN':
                result = currencies[receive]['Cur_Scale'] / currencies[receive]['Cur_OfficialRate'] * amount
            elif receive == 'BYN':
                result = currencies[give]['Cur_OfficialRate'] / currencies[give]['Cur_Scale'] * amount
            else:
                result = currencies[give]['Cur_OfficialRate'] / currencies[give]['Cur_Scale'] * amount / \
                         currencies[receive]['Cur_OfficialRate'] * currencies[receive]['Cur_Scale']

            return render(request, 'main/index.html', {'result': result, 'currencies': currencies, 'form': form})

    form = ExchangeForm()
    return render(request, 'main/index.html', {'title': 'CurEx', 'currencies': currencies, 'form': form})