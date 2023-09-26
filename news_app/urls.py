from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, HomePageView,\
    LocalNewsView,ForeignNewsView,TechnologyNewsView,SportNewsView,NewsUpdateView,\
    NewsDeleteView,NewsCreateView,admin_page_view,SearchResultsList

urlpatterns = [
    path('',HomePageView.as_view(),name = 'home_page'),
    path('news/',news_list , name = 'all_news_list'),
    path('news/ <slug:news>/',news_detail,name="news_detail_page"),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name = 'news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name = 'news_delete'),
    path('news/create/', NewsCreateView.as_view(), name = 'news_create'),
    path('contact-us/',ContactPageView.as_view(),name = 'contact_page'),
    path('404-page/',ContactPageView.as_view(),name = '404_page'),
    path('news/local/',LocalNewsView.as_view(),name = 'local_news_page'),
    path('news/foreign/',ForeignNewsView.as_view(),name = 'foreign_news_page'),
    path('news/technology/',TechnologyNewsView.as_view(),name = 'technology_news_page'),
    path('news/sport/',SportNewsView.as_view(),name = 'sport_news_page'),
    path('pages/adminpage/', admin_page_view, name = 'admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name = 'search_results'),

]