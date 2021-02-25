from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from.views import DeleteExpenseApiView,expense_list
urlpatterns = [
    path(r'item', expense_list, name='item'),
    # path(r'create', ExpenseCreateView.as_view(), name='item'),
    path('item/<int:pk>/', DeleteExpenseApiView.as_view())

]
