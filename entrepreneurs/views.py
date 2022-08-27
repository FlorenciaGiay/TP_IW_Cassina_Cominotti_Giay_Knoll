from django.shortcuts import render
import datetime
from django.contrib.auth.decorators import login_required


emprendedores = [
    {
        'tipo': 'Artesanias',
        'nombre': 'Alondra',
        'content': 'Hago pulseras :)',
        'date_posted': datetime.datetime(2022, 8, 23, 7, 00, 00),
    },
    {
        'tipo': 'Gastronomia',
        'nombre': 'Mas chica la milanesa',
        'content': 'Hago comida :P',
        'date_posted': datetime.datetime(2022, 8, 23, 6, 00, 00),
    },
    {
        'tipo': 'Indumentaria',
        'nombre': 'Vestite bien',
        'content': 'Hago ropa XD',
        'date_posted': datetime.datetime(2022, 8, 22, 23, 00, 00),
    },
]

@login_required
def home(request):
    context = { 'emprendedores': emprendedores }
    return render(request, 'entrepreneurs/home.html', context)