from django.shortcuts import render, redirect
from fingen.models import *
from fingen.forms import *


# def soma_receitas():
    # receitas = Transacao.objects.filter
    # print(receitas)

# soma_receitas()

def home(request):
    transacoes = Transacao.objects.all().order_by('-data')
    
    query = request.GET.get("q")
    if query:
        transacoes = transacoes.filter(titulo__icontains=query)
        
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fingen:home')
    else:
        form = TransacaoForm()

    
    context = {
        'form': form,
        'transacoes': transacoes
    }
    return render(request, 'pages/home.html', context)
