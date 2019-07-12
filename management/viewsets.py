from rest_framework import viewsets
from .serializers import *

class ClinetGroupViewset(viewsets.ModelViewSet):
    serializer_class=ClinetGroupSerializer
    queryset=ClientGroup.objects.all()

class SuppliersGroupViewset(viewsets.ModelViewSet):
    serializer_class=SuppliersGroupSerializer
    queryset=SupplierGroup.objects.all()

class ProductGroupViewset(viewsets.ModelViewSet):
    serializer_class=ProductGroupSerializer
    queryset=ProductGroup.objects.all()

class ClientViewset(viewsets.ModelViewSet):
    serializer_class=ClientSerializer
    queryset=Client.objects.all()

class SupplierViewset(viewsets.ModelViewSet):
    serializer_class=SupplierSerializer
    queryset=Supplier.objects.all()

class AccountViewset(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=AccountModel.objects.all()

class ExpenseCategoryViewset(viewsets.ModelViewSet):
    serializer_class=ExpenseCategorySerializer
    queryset=ExpenseCategoryModel.objects.all()

class IncomeCategoryViewset(viewsets.ModelViewSet):
    serializer_class=IncomeCategorySerializer
    queryset=IncomeCategoryModel.objects.all()

class BankViewset(viewsets.ModelViewSet):
    serializer_class=BankSerializer
    queryset=Bank.objects.all()

class PaymentMethodViewset(viewsets.ModelViewSet):
    serializer_class=PaymentMethodSerializer
    queryset=PaymentMethodModel.objects.all()

class RecieveModelViewset(viewsets.ModelViewSet):
    serializer_class=RecieveModelSerializer
    queryset=RecieveModel.objects.all()

class ExpenseModelViewset(viewsets.ModelViewSet):
    serializer_class=ExpenseModelSerializer
    queryset=ExpenseModel.objects.all()

class SupplierPaymentViewset(viewsets.ModelViewSet):
    serializer_class=SupplierPaymentSerializer
    queryset=SupplierPayment.objects.all()

class TransferModelViewset(viewsets.ModelViewSet):
    serializer_class=TransferModelSerializer
    queryset=TransferModel.objects.all()

class ProductViewset(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=PurchaseProduct.objects.all()

class PurchaseProductViewset(viewsets.ModelViewSet):
    serializer_class=PurchaseProductSerializer
    queryset=PurchaseProduct.objects.all()

class PurchaseReturnViewset(viewsets.ModelViewSet):
    serializer_class=PurchaseReturnSerializer
    queryset=PurchaseReturn.objects.all()

class OfficePurchasesViewset(viewsets.ModelViewSet):
    serializer_class=OfficePurchasesSerializer
    queryset=OfficePurchases.objects.all()

class BalanceSheetViewset(viewsets.ModelViewSet):
    serializer_class=BalanceSheetSerializer
    queryset=BalanceSheet.objects.all()

class ProfitViewset(viewsets.ModelViewSet):
    serializer_class=ProfitSerializer
    queryset=ProfitModel.objects.all()

class AccountStatementViewset(viewsets.ModelViewSet):
    serializer_class=AccountStatementSerializer
    queryset=AccountStatement.objects.all()

class CompanyProfileViewset(viewsets.ModelViewSet):
    serializer_class=CompanyProfileSerializer
    queryset=CompanyProfile.objects.all()
    
class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()