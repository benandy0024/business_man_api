from rest_framework import generics,mixins,permissions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum,Avg,Count
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import render,Http404

from products.models import  Expense
from.serializer import ExpenseSerialiser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL
@api_view(['GET'])
def expense_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Expense.objects.all()
        serializer = ExpenseSerialiser(snippets, many=True)
        return Response(serializer.data)

class CreateExpense(generics.CreateAPIView):
   permissions=[]
   authentication_classes = [SessionAuthentication]
   serializer_class = ExpenseSerialiser
   queryset = Expense
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)


# class ExpenseListView(generics.ListAPIView, mixins.CreateModelMixin):
#     serializer_class = ExpenseSerialiser
#     permission_classes = [permissions.AllowAny]
#     def get(self, request, *args, **kwargs):
#         qs = Expense.objects.all()
#         qs_exp = qs.filter(user=request.user)
#         serializer = ExpenseSerialiser(qs_exp, many=True)
#         sum = qs_exp.aggregate(Sum('total'))['total__sum']
#         return Response({'weekly_sum': sum if sum else 0,'objects':serializer.data})
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#     def perform_create(self, serializer):
#         user=self.request.user
#         serializer.save(user=user)

class DeleteExpenseApiView(APIView):
    """
    delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

