from django.shortcuts import render

from .services import currencies


def index(request):
    if request.method == 'POST':
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

            return render(request, 'main/index.html', {'result': result, 'currencies': currencies})

    return render(request, 'main/index.html', {'title': 'CurEx', 'currencies': currencies})
