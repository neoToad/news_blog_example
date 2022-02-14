from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.urls import include

app_name = 'game_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:article_id>/', views.article, name='article'),
    path('newest', views.newest, name='newest'),
    path('popular', views.popular, name='popular'),

    path('cookie-policy', views.cookie_policy, name='cookie_policy'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('terms', views.terms, name='terms'),
    path('dmca', views.dmca, name='dmca'),
    path('accessibility-policy', views.accessibility, name='accessibility'),

    path('contact', views.contact_view, name='contact'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]