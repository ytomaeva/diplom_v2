from django.shortcuts import render

from main.models import Variants


def index(request):
    variants = Variants.objects.all()  # получаем все объекты из модели Variants
    context = {'variants': variants}  # формируем контекст для передачи в шаблон
    return render(request, 'index.html', context)  # возвращаем сформированный контекст в шаблон index.html
