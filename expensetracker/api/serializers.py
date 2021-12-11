from rest_framework import serializers
from .models import Category, Transactions, TransactionType


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        # fields = ('id', 'name')
        fields = '__all__'


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id', 'name', 'amount', 'category_id', 'transaction_type', 'transaction_date')
