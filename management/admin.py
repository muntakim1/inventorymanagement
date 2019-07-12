from django.contrib import admin
from .models import *


admin.site.register(ClientGroup)
admin.site.register(SupplierGroup)

admin.site.register(Supplier)
admin.site.register(AccountModel)

admin.site.register(ProductGroup)
admin.site.register(Client)

admin.site.register(ExpenseCategoryModel)
admin.site.register(IncomeCategoryModel)

admin.site.register(Bank)
admin.site.register(PaymentMethodModel)

admin.site.register(RecieveModel)
admin.site.register(ExpenseModel)

admin.site.register(SupplierPayment)
admin.site.register(TransferModel)

admin.site.register(Product)
admin.site.register(PurchaseProduct)

admin.site.register(PurchaseReturn)
admin.site.register(OfficePurchases)

admin.site.register(BalanceSheet)
admin.site.register(AccountStatement)

admin.site.register(CompanyProfile)
admin.site.register(ProfitModel)

admin.site.register(UserProfile)

