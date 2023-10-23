from django.urls import path, include
from tracker import views


urlpatterns = [
    path("", views.index, name='home'),
    path("budget/", views.budget, name='budget'),
    path("add_expense/", views.add_expense, name='add_expense'),
    path("add_income/", views.add_income, name='add_income'),
]