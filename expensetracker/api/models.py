from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    budget = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    CHOICE = [('D', 'Debit'), ('C', 'Credit')]
    name = models.CharField(max_length=6, choices=CHOICE, default='D')

    class Meta:
        verbose_name_plural = "Transaction Type"

    def __str__(self):
        return dict(self.CHOICE)[self.name]


class Transactions(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    transaction_date = models.DateField()

    class Meta:
        verbose_name_plural = "Transactions"

    def __str__(self):
        return self.name

