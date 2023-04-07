from django.shortcuts import render

from .forms import ExchangeForm
from .services import currencies


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
            currency = currencies[receive]['Cur_Abbreviation']

            return render(request, 'main/index.html', {'form': form, 'result': result, 'currency': currency})

    form = ExchangeForm()
    return render(request, 'main/index.html', {'title': 'CurEx', 'currencies': currencies, 'form': form})
