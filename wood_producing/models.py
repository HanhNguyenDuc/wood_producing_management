# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django import db
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .enums import *


class User(AbstractUser):
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.
    role = models.SmallIntegerField(
        null=False,
        blank=False,
        default=UserRole.FOREMAN.value,
        choices=[
            (UserRole.FOREMAN.value, UserRole.FOREMAN.name),
            (UserRole.PRODUCING_MANAGER, UserRole.PRODUCING_MANAGER.name),
            (UserRole.STORAGE_MANAGER.value, UserRole.STORAGE_MANAGER.name),
            (UserRole.DIRECTOR.value, UserRole.DIRECTOR.name),
        ]
    )
    status = models.CharField(db_column='status', max_length=100, default="Available")


class Provider(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.



class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.



class Customer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.



class Exportbill(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    totalincome = models.FloatField(db_column='TotalIncome', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.



class Importbill(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True)  # Field name made lowercase.
    provider = models.IntegerField(db_column='Provider', blank=True, null=True)  # Field name made lowercase.
    providerid = models.ForeignKey('Provider', models.DO_NOTHING, db_column='ProviderID')  # Field name made lowercase.




class Importedmaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material = models.IntegerField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    importbillid = models.ForeignKey(Importbill, models.DO_NOTHING, db_column='ImportBillID')  # Field name made lowercase.



class Material(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.


class Materialinproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='MaterialID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    quantity = models.IntegerField(default=2)
    description = models.CharField(max_length=300, default="is a main material")


class Materialofprovider(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # material = models.ForeignKey(Material, models.CASCADE, db_column='Material')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    # provider = models.ForeignKey(Provider, db_column='Provider', blank=True, null=True)  # Field name made lowercase.
    importedmaterialid = models.ForeignKey(Importedmaterial, models.DO_NOTHING, db_column='ImportedMaterialID', null=True)  # Field name made lowercase.
    providerid = models.ForeignKey('Provider', models.DO_NOTHING, db_column='ProviderID')  # Field name made lowercase.
    materialid = models.ForeignKey(Material, models.DO_NOTHING, db_column='MaterialID')  # Field name made lowercase.



class Materialofproviderinstorage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    storageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='StorageID')  # Field name made lowercase.
    materialofproviderid = models.ForeignKey(Materialofprovider, models.DO_NOTHING, db_column='MaterialOfProviderID')  # Field name made lowercase.



class Materialrequest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material = models.ForeignKey('Material', models.CASCADE, db_column='material')
    taskid = models.ForeignKey('Task', models.CASCADE, db_column='TaskID')  # Field name made lowercase.
    storageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='StorageID', null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(db_column='is_approve', default=False)
    quantity = models.IntegerField(default=10)
    create_at = models.DateTimeField(db_column="create_at")


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, default="")
    duedate = models.DateTimeField(db_column='duedate', max_length=255)
    create_at = models.DateTimeField(db_column='create_at')

class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iddesign = models.CharField(db_column='IdDesign', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=255)  # Field name made lowercase.

class Orderedproduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    storageid = models.ForeignKey('Storage', models.DO_NOTHING, db_column='StorageID')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    product = models.ForeignKey(Product, db_column='Product', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    productexportedid = models.ForeignKey('Productexported', models.CASCADE, db_column='ProductExportedID', null=True)  # Field name made lowercase.
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)



class Productexported(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    product = models.IntegerField(db_column='Product', blank=True, null=True)  # Field name made lowercase.
    exportbillid = models.ForeignKey(Exportbill, models.DO_NOTHING, db_column='ExportBillID')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductID')  # Field name made lowercase.



class Progress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.


class Requestedmaterial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    materialofproviderinstorageid = models.ForeignKey(Materialofproviderinstorage, models.CASCADE, null=True)
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    materialrequestid = models.ForeignKey(Materialrequest, models.DO_NOTHING, db_column='MaterialRequestID')  # Field name made lowercase.



class Storage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    manager = models.ForeignKey(User, db_column='Manager', null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.




class Task(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=255)
    orderedproductid = models.ForeignKey(Orderedproduct, models.DO_NOTHING, db_column='OrderedProductID')  # Field name made lowercase.
    product = models.IntegerField(db_column='Product', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', null=True)  # Field name made lowercase.
    progress = models.ForeignKey('Progress', models.CASCADE, db_column='progress', null=True)
    priority = models.CharField(db_column='priority', max_length=10, default="low")
    quantity = models.IntegerField(db_column='quantity', default=0)
    estimated = models.DateTimeField(db_column='estimated')
    create_at = models.DateTimeField(db_column="create_at")
    update_at = models.DateTimeField(db_column="update_at")
    status = models.CharField(db_column='status', default="doing", max_length=100)


class Taskprogress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Task, models.CASCADE, db_column='TaskID')  # Field name made lowercase.
    progressid = models.ForeignKey(Progress, models.CASCADE, db_column='ProgressID')  # Field name made lowercase.
    percentage = models.IntegerField(default=0)


class Workshop(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
