from datetime import datetime
from django.db.models import Sum,Avg,Max,Min,Count
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from expense.permissions import IsOwner
from expense.serializers import ExpenseSerializer
from expense.models import Expense
# Create your views here.
class ExpenseCreate(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        serializers_instance = ExpenseSerializer(data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save(user=request.user)
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class ExpenseList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        expense = Expense.objects.filter(user=request.user)
        serializers_instance = ExpenseSerializer(expense,many=True)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)
class ExpenseRetrieve(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]
    def get(self,request,pk):
        expense = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,expense)
        serializers_instance = ExpenseSerializer(expense)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)
class ExpenseUpdate(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]
    def put(self,request,pk):
        expense = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,expense)
        serializers_instance = ExpenseSerializer(instance=expense,data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class ExpenseDelete(APIView):
    def delete(self,request,pk):
        expense = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,expense)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ExpenseSummary(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        today_date =datetime.now().date()
        today_total =0
        qs = Expense.objects.filter(user=request.user,created__date=today_date)

        if qs:
            today_total = qs.aggregate(total=Sum('amount')).get('total')
        return Response({'todays_total':today_total},status=status.HTTP_200_OK)