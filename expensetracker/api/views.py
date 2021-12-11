from django.shortcuts import render, HttpResponse, get_object_or_404
from .serializers import CategorySerializer, TransactionsSerializer, TransactionTypeSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Transactions, TransactionType

# Create your views here.

#
# def index(request):
#     return HttpResponse("Hello World")


class CategoryView(APIView):
    def get(self, request, name=None):
        if name:
            item = Category.objects.get(name=name)
            serializer = CategorySerializer(item)
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name=None):
        item = get_object_or_404(Category, name=name)
        item.delete()
        return Response({
            "status": "success",
            "data": "Category Deleted"
        })
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer
    #
    # def post(self):
    #     if not self.request.session.exists(self.request.session.session_key):
    #         self.request.session.create()


class TransactionTypeView(generics.ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer


class TransactionsView(APIView):
    # queryset = Transactions.objects.all()
    # serializer_class = TransactionsSerializer

    def get(self, request):
        items = Transactions.objects.all()
        serializer = TransactionsSerializer(items, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(Transactions, id=id)
        item.delete()
        return Response({
            "status": "success",
            "data": "Transaction Deleted"
        })
