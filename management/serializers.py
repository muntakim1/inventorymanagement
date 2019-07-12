from rest_framework import serializers
from .models import ClientGroup,SupplierGroup,ProductGroup,Client,Supplier,Account,ExpenseCategoryModel,IncomeCategoryModel,Bank,PaymentMethodModel,RecieveModel,ExpenseModel,SupplierPayment,TransferModel,Product,PurchaseProduct,PurchaseReturn

class ClinetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClientGroup
        fields=('id','GroupName')

class SuppliersGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplierGroup
        fields=('id','GroupName')

class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductGroup
        fields=('id','GroupName')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseCategoryModel
        fields='__all__'

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=IncomeCategoryModel
        fields='__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentMethodModel
        fields='__all__'
        
class RecieveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecieveModel
        fields='__all__'

class ExpenseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseModel
        fields='__all__'

class SupplierPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupplierPayment
        fields='__all__'

class TransferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TransferModel
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class PurchaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseProduct
        fields='__all__'

class PurchaseReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseReturn
        fields='__all__'
