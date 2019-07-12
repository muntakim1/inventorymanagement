from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils import timezone
from django.contrib.auth.models import User

# Group Model.
class ClientGroup(models.Model):
    GroupName=models.CharField(max_length=50)
    def __str__(self):
        return self.GroupName
    
# Group Model.
class SupplierGroup(models.Model):
    GroupName=models.CharField(max_length=50)
    def __str__(self):
        return self.GroupName

#Group Model.
class ProductGroup(models.Model):
    GroupName=models.CharField(max_length=50)
    def __str__(self):
        return self.GroupName

# ExpenseCategory Model.
class ExpenseCategoryModel(models.Model):
    Expense_Category=models.CharField(max_length=50)
    def __str__(self):
        return self.Expense_Category
    
# IncomeCategory Model.
class IncomeCategoryModel(models.Model):
    Income_Category=models.CharField(max_length=50)
    def __str__(self):
        return self.Income_Category


# Bank Model.
class Bank(models.Model):
    Bank_Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Bank_Name

# PaymentMethod Model.
class PaymentMethodModel(models.Model):
    PaymentMethod=models.CharField(max_length=50)
    def __str__(self):
        return self.PaymentMethod


# Client Model.
class Client(models.Model):
    Company_Name = models.CharField(max_length=255)
    Proprietor_Name = models.CharField(max_length=255)
    Phone_Number_1 = PhoneNumberField()
    Phone_Number_2 = PhoneNumberField(blank=True)
    Email= models.EmailField(max_length=254)
    Date_Of_Birth = models.DateField(blank=False)
    Address= models.TextField(blank=False)
    City=models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=5)
    Country=CountryField()
    Group = models.ForeignKey(ClientGroup,on_delete=models.CASCADE)
    def __str__(self):
        return self.Company_Name

#Balance Sheet
class BalanceSheet(models.Model):
    Date= models.DateField(default=timezone.now)
    Opening_Balance = models.DecimalField(max_digits=5, decimal_places=2)
    Collection = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Collection = models.DecimalField(max_digits=5, decimal_places=2)
    Expenses = models.DecimalField(max_digits=5, decimal_places=2)
    Closing_Balance = models.DecimalField(max_digits=5, decimal_places=2)

# Supplier Model.
class Supplier(models.Model):
    Company_Name = models.CharField(max_length=255)
    Proprietor_Name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile/supplier/%Y/',blank=True)
    Phone_Number_1 = PhoneNumberField()
    Phone_Number_2 = PhoneNumberField(blank=True)
    Email= models.EmailField(max_length=254)
    Date_Of_Birth = models.DateField(blank=False)
    Address= models.TextField(blank=False)
    City=models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=5)
    Country=CountryField()
    Group = models.ForeignKey(SupplierGroup,on_delete=models.CASCADE)
    def __str__(self):
        return self.Company_Name
        
# Account Model.
class AccountModel(models.Model):
    Accoutn_Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=50)
    Initial_Balance= models.DecimalField(max_digits=5, decimal_places=2)
    Account_Number= models.CharField(max_length=10)
    Contact_Person = models.CharField(max_length=50)
    Phone_Number=PhoneNumberField()
    def __str__(self):
        return self.Accoutn_Title

#Account Statement

class AccountStatement(models.Model):
    types=[
        ('1','Invoice'),
        ('2','Collection')
    ]
    Date = models.DateField(default=timezone.now)
    Account = models.ForeignKey(Bank,on_delete=models.CASCADE)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Type = models.CharField(max_length=50,choices=types)
    Amount = models.DecimalField(max_digits=5, decimal_places=2)
    Description  = models.TextField()
    Credit = models.DecimalField(max_digits=5, decimal_places=2)
    Debit = models.DecimalField(max_digits=5, decimal_places=2)
    Balance = models.DecimalField(max_digits=5, decimal_places=2)


# RecieveModel Model.
class RecieveModel(models.Model):
    Client=models.ForeignKey(Client, on_delete=models.CASCADE)
    Date=models.DateField(default=timezone.now)
    Account= models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    Description = models.TextField()
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey(IncomeCategoryModel, on_delete=models.CASCADE) 
    Payment_Method=models.ForeignKey(PaymentMethodModel, on_delete=models.CASCADE)
    Bank_Name=models.ForeignKey(Bank, on_delete=models.CASCADE)
    Chequee_No=models.CharField(max_length=50)
    

# ExpenseModel Model.
class ExpenseModel(models.Model):
    Account=models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    Date=models.DateField(default=timezone.now)
    Description = models.TextField()
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey(ExpenseCategoryModel, on_delete=models.CASCADE) 
    Payment_Method=models.ForeignKey(PaymentMethodModel, on_delete=models.CASCADE)
    Bank_Name=models.ForeignKey(Bank, on_delete=models.CASCADE)
    Chequee_No=models.CharField(max_length=50)
    Expense_Voucher = models.ImageField(upload_to="Voucher/")

# SupplierPayment Model.
class SupplierPayment(models.Model):
    Account= models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    Date=models.DateField(default=timezone.now)
    Supplier_Name= models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Category = models.ForeignKey(ExpenseCategoryModel, on_delete=models.CASCADE) 
    Payment_Method=models.ForeignKey(PaymentMethodModel, on_delete=models.CASCADE)
    Bank_Name=models.ForeignKey(Bank, on_delete=models.CASCADE)
    Chequee_No=models.CharField(max_length=50)
    Description = models.TextField()
    Amount=models.DecimalField(max_digits=10, decimal_places=2)

#Profit Model
class ProfitModel(models.Model):
    Total_Profit=models.DecimalField(max_digits=5, decimal_places=2)
    Date = Date=models.DateField( default=timezone.now)

# TransferModel Model.
class TransferModel(models.Model):
    Money_From=models.ForeignKey(PaymentMethodModel,related_name='+', on_delete=models.CASCADE)
    Mpney_To = models.ForeignKey(PaymentMethodModel,related_name='+', on_delete=models.CASCADE)
    Date=models.DateField( default=timezone.now)
    Description=models.TextField()
    Amount=models.DecimalField(max_digits=10, decimal_places=2)
    Tags = models.CharField( max_length=50)
    Method= models.ForeignKey(PaymentMethodModel, on_delete=models.CASCADE)
    Reference=models.CharField(max_length=50)

#Office Purchases
class OfficePurchases(models.Model):
     Date = models.DateField( default=timezone.now)
     Supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
     Item_Name = models.CharField(max_length=200)
     Quantity = models.IntegerField()
     Rate = models.DecimalField(max_digits=5, decimal_places=2)
     Total = models.DecimalField(max_digits=5, decimal_places=2)
     Decription = models.TextField()
# Product Model.
class Product(models.Model):
    Product_Name = models.CharField(max_length=50)
    Images_1= models.ImageField(upload_to="product/")
    Images_2= models.ImageField(upload_to="product/",blank=True)
    Product_Description = models.TextField()
    Product_Unit = models.CharField(max_length=50) 
    Carton = models.IntegerField()
    Group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.Product_Name
 
# PurchaseProduct Model.   
class PurchaseProduct(models.Model):
    Supplier_Name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Product,on_delete=models.CASCADE)
    Date = models.DateField( default=timezone.now)
    Buy_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Sell_Price = models.DecimalField(max_digits=5, decimal_places=2)
    Note = models.TextField(blank=True)

# PurchaseReturn Model.
class PurchaseReturn(models.Model):
    Supplier_Name = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Product,on_delete=models.CASCADE)
    Date = models.DateField( default=timezone.now)
    Return_Quantity = models.IntegerField()
    BuyPrice = models.DecimalField(max_digits=5, decimal_places=2)
    Note = models.TextField(blank=True)

#Profile
class UserProfile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    profile_Picture = models.ImageField(upload_to='user/profile/%Y/',blank=True)
    Designation = models.CharField(max_length=200)
    Address = models.CharField(max_length=255)
    Phone_Number = PhoneNumberField()

#Company Profile
class CompanyProfile(models.Model):
    Company_Name = models.CharField(max_length=50)
    Company_Moto = models.CharField(max_length=50)
    Logo = models.ImageField(upload_to='logo/%Y/')
    Address = models.CharField(max_length=100)
    Country = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Phone_Number = PhoneNumberField()
    State = models.CharField(max_length=50)
    Post_Code = models.CharField(max_length=10)
    Currency = models.CharField(max_length=4)

