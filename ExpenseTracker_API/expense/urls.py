"""
URL configuration for ExpenseTracker_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from expense import views
urlpatterns = [
    path("expense",views.ExpenseCreate.as_view()),
    path("list",views.ExpenseList.as_view()),
    path("retrieve/<int:pk>",views.ExpenseRetrieve.as_view()),
    path("update/<int:pk>",views.ExpenseUpdate.as_view()),
    path("delete/<int:pk>",views.ExpenseDelete.as_view()),
    path("summary",views.ExpenseSummary.as_view()),
]
