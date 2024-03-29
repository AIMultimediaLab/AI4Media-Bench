from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    # path(r'^competition/create', views.CompetitionFormView.as_view(), name="competition_create"),
    # path('competition/view/<int:competition_pk>/', views.CompetitionDetailView.as_view()),
    path('search', views.SearchView.as_view(), name="search"),
    path('organize', views.OrganizeView.as_view(), name="organize"),
    path('server_status', views.ServerStatusView.as_view(), name="server_status"),
    # path('test', views.CompetitionListTestView.as_view()),
    path('license/', views.license_view, name='license'),
    path('notice/', views.notice_view, name='notice'),
]
