from django.shortcuts import render
from django.http import JsonResponse
from .models import Card

# Create your views here.

def get(request):
    card = Card.objects.all()
    data = {
        'card': [
            {'id': Card.id, 'nome': Card.nome}
            for card in card
        ]
    }
    return JsonResponse(data)

def save(request):
    if request.method == 'POST':
        vnome = request.POST.get("nome")
        vdescricao = request.POST.get("descricao")
        vstatus = request.POST.get("status")
        novo_card = Card.objects.create(nome=vnome, descricao=vdescricao, status=vstatus)
        cards = Card.objects.all()
        data = {
            'novo_card': {
                'nome': novo_card.nome,
                'descricao': novo_card.descricao,
                'status': novo_card.status
            },
            'todos_cards': [
                {'nome': card.nome, 'descricao': card.descricao, 'status': card.status} 
                for card in cards
            ]
        }
        return JsonResponse(data)