from django.contrib import admin
from article.models import Article
from article.models import Tag
from article.models import Article_Tags

class TagInline(admin.TabularInline):
    model = Article.tags.through
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['link', 'name']}),
        ('Votes', {'fields': ['votes_up', 'votes_down'], 'classes': ['collapse']}),
    ]
    inlines = [TagInline]
    list_display = ('nice_name', 'all_tags', 'votes_up', 'added_date')


admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)

