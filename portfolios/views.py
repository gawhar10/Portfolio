from django.shortcuts import render
from .models import Portfolio


def index(request):
    """The home page for my portfolios."""
    return render(request, 'portfolios/index.html')


def portfolios(request):
    """show all Portfolio items."""
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'portfolios/portfolios.html', context)


def portfolio(request, portfolio_id):
    """Detail page for a single portfolio item."""
    portfolio = Portfolio.objects.get(id=portfolio_id)
    context = {'portfolio': portfolio}
    return render(request, 'portfolios/portfolio.html', context)
