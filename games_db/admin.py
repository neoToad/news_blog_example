from django.contrib import admin
from .models import Article, ArticleContent, Author, Contact, Connection, EmailList


class ArticleContentInline(admin.TabularInline):
    model = ArticleContent
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleContentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Contact)
admin.site.register(EmailList)
admin.site.register(Connection)