from django.contrib.auth.decorators import login_required
from article.models import Article
from django.shortcuts import render_to_response

@login_required
def index(request):
    something = Article.objects.all()
    return render_to_response('article/index.html', {'articles':something})
