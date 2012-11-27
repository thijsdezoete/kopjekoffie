from django.contrib.auth.decorators import login_required
from article.models import Article, Tag, Article_Tags
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from forms import ArticleForm

def index(request):
    something = Article.objects.all().order_by('-votes_up', '-added_date')
    return render_to_response('article/index.html', {'articles':something})

@login_required
def browse_tag(request, tagname):
    _tag = get_object_or_404(Tag, name=tagname)
    articles_by_tag = Article.objects.filter(tags=_tag).order_by('-votes_up', '-added_date')
    return render_to_response('article/index.html', {'articles':articles_by_tag})

@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']
        
            recipients = ['thijsdezoete@gmail.com']
            message = 'Tags: %s' % form.cleaned_data['tags']
            from django.core.mail import send_mail
            send_mail('New article: %s' % form.cleaned_data['link'], message, 'thijsdezoete@gmail.com', recipients)
            request.META['wsgi.errors'].write('TEST')
            return HttpResponseRedirect('/')
    else:
        form = ArticleForm()

    return render_to_response('article/add_article.html', 
        {'form':form},
        context_instance=RequestContext(request)
    )

#form = PartialAuthorForm(request.POST)
#author = form.save(commit=False)
#author.title = 'Mr'
#author.save()
