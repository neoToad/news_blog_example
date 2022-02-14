from django.shortcuts import render, redirect
from .models import Article
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from django.http import HttpResponse
import random
from itertools import chain
from .forms import ContactForm
from django.core.paginator import Paginator
from .models import EmailList
from .forms import EmailListForm
from django.db.models import Q
from django_user_agents.utils import get_user_agent


def index(request):
    title = 'WhichGa.me - A video game news website!'
    pg_description = 'A website with video game news, deals, guides, and reviews!'
    article_list = Article.objects.order_by('-date_added')

    search_post = request.GET.get('search')

    if search_post:
        article_list = Article.objects.filter(Q(title__icontains=search_post)
                                              | Q(description__icontains=search_post))
        context = {'articles': article_list, 'search': search_post, }
        return render(request, "games_db/search.html", context)
    else:
        article_list = Article.objects.all().order_by('-date_added')

    context = {'articles': article_list, 'title': title,}
    return render(request, "games_db/index.html", context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {}
    user_agent = get_user_agent(request)

    # if article.ad_name:
    #     ad = article.ad_name
    # else:
    if user_agent.is_mobile:
        ads = [
            'APEX/KINGUIN',
            'GMG/APEX',
        ]

    else:
        # ads logic
        ads = [
            'APEX/KINGUIN',
            'GMG/APEX',
            'CROSSOUT_DESK',
        ]

    ad = random.choice(ads)

    # hitcount logic
    hit_count = get_hitcount_model().objects.get_for_object(article)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    title = article.title

    # Paginate Contents
    article_contents = article.article_contents.order_by('id')
    paginator = Paginator(article_contents, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    connections_list = Article.objects.filter(connections__in=article.connections.all()).exclude(id=article_id).values_list('id', flat=True)

    if len(connections_list) > 2:
        connections = random.sample(list(connections_list), 3)

    else:
        connections = []

    three_connections = Article.objects.filter(id__in=connections)

    most_popular = Article.objects.order_by('-hit_count_generic__hits').exclude(id=article_id).exclude(id__in=connections)[:20]
    items = list(chain(three_connections, most_popular))

    random_articles = random.sample(items, 6)

    # others_list = Article.objects.order_by('-date_added').exclude(title__in=random_articles).exclude(id=article_id)[:6]
    # articles = list(chain(random_articles, others_list,))

    context['current_article'] = article
    context['same_game_articles'] = random_articles
    context['paragraphs'] = page_obj
    context['title'] = title
    context['ad'] = ad
    context['first_page_false'] = page_obj.has_previous()

    return render(request, "games_db/article.html", context)


def newest(request):
    title = 'WhichGa.me - Video Game Guides'
    article_list = Article.objects.order_by('-date_added')
    paginator = Paginator(article_list, 6)
    page_number = request.GET.get('page')
    page_articles = paginator.get_page(page_number)
    context = {'articles': page_articles, 'title': title}
    return render(request, "games_db/newest.html", context)


def popular(request):
    title = 'WhichGa.me - Video Game Guides'
    article_list = Article.objects.order_by('-hit_count_generic__hits')
    paginator = Paginator(article_list, 6)
    page_number = request.GET.get('page')
    page_articles = paginator.get_page(page_number)
    context = {'articles': page_articles, 'title': title}
    return render(request, "games_db/popular.html", context)


def cookie_policy(request):
    return render(request, "games_db/cookie-policy.html")


def privacy_policy(request):
    return render(request, "games_db/privacy-policy.html")


def terms(request):
    return render(request, "games_db/terms.html")


def dmca(request):
    return render(request, "games_db/dmca.html")


def accessibility(request):
    return render(request, "games_db/accessibility.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'games_db/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, "games_db/contact.html", context)

