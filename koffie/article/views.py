from django.contrib.auth.decorators import login_required
from article.models import Article, Tag, Article_Tags
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    something = Article.objects.all().order_by('-votes_up', '-added_date')
    return render_to_response('article/index.html', {'articles':something})

@login_required
def browse_tag(request, tagname):
    _tag = get_object_or_404(Tag, name=tagname)
    articles_by_tag = Article.objects.filter(tags=_tag).order_by('-votes_up', '-added_date')
    return render_to_response('article/index.html', {'articles':articles_by_tag})
