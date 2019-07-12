from rest_framework.routers import DefaultRouter
from .viewsets import *

router= DefaultRouter()

router.register(r'clientgroup',ClinetGroupViewset,base_name='clientgroup'),
router.register(r'suppliergroup',SuppliersGroupViewset,base_name='suppliersgroup'),
router.register(r'productgroup',ProductGroupViewset,base_name='productgroup'),
router.register(r'client',ClientViewset,base_name='client'),
router.register(r'supplier',SupplierViewset,base_name='supplier'),
router.register(r'account',AccountViewset,base_name='account'),
router.register(r'expensecategory',ExpenseCategoryViewset,base_name='expensecategory'),
router.register(r'incomecategory',IncomeCategoryViewset,base_name='incomecategory'),
router.register(r'bank',BankViewset,base_name='bank'),
router.register(r'paymentmethod',PaymentMethodViewset,base_name='paymentmethod'),
router.register(r'recieved',RecieveModelViewset,base_name='recieved'),
router.register(r'expense',ExpenseModelViewset,base_name='expense'),
router.register(r'supplierpayment',SupplierPaymentViewset,base_name='supplierpayment'),
router.register(r'transfer',TransferModelViewset,base_name='transfer'),
router.register(r'product',ProductViewset,base_name='product'),
router.register(r'purchasproduct',PurchaseProductViewset,base_name='purchasproduct'),
router.register(r'returnproduct',PurchaseReturnViewset,base_name='returnproduct'),

