from django.urls import path
from .views import ServiceDescriptionView,ServiceView,OrderView, PortfolioListView


urlpatterns = [
    path('',ServiceView.as_view()),
    path('<int:pk>',ServiceDescriptionView.as_view()),
    path('order',OrderView.as_view()),
    path('portfolio',PortfolioListView.as_view()),
    path('portfolio/<int:service_id>',PortfolioListView.as_view()),
]