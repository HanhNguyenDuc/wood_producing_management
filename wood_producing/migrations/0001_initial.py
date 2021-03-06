# Generated by Django 3.1.7 on 2021-05-08 03:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wood_producing.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
                ('role', models.SmallIntegerField(choices=[(3, 'FOREMAN'), (wood_producing.enums.UserRole['PRODUCING_MANAGER'], 'PRODUCING_MANAGER'), (2, 'STORAGE_MANAGER'), (4, 'DIRECTOR')], default=3)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exportbill',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('manager', models.IntegerField(blank=True, db_column='Manager', null=True)),
                ('customer', models.IntegerField(blank=True, db_column='Customer', null=True)),
                ('totalincome', models.FloatField(blank=True, db_column='TotalIncome', null=True)),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Importbill',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('manager', models.IntegerField(blank=True, db_column='Manager', null=True)),
                ('provider', models.IntegerField(blank=True, db_column='Provider', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Importedmaterial',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('material', models.IntegerField(blank=True, db_column='Material', null=True)),
                ('price', models.FloatField(db_column='Price')),
                ('importbillid', models.ForeignKey(db_column='ImportBillID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.importbill')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('quantity', models.FloatField(blank=True, db_column='Quantity', null=True)),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Materialofprovider',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('material', models.IntegerField(blank=True, db_column='Material', null=True)),
                ('price', models.FloatField(db_column='Price')),
                ('provider', models.IntegerField(blank=True, db_column='Provider', null=True)),
                ('importedmaterialid', models.ForeignKey(db_column='ImportedMaterialID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.importedmaterial')),
                ('materialid', models.ForeignKey(db_column='MaterialID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.material')),
            ],
        ),
        migrations.CreateModel(
            name='Materialrequest',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('customer', models.IntegerField(blank=True, db_column='Customer', null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Orderedproduct',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('price', models.FloatField(db_column='Price')),
                ('product', models.IntegerField(blank=True, db_column='Product', null=True)),
                ('quantity', models.IntegerField(db_column='Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
                ('price', models.FloatField(db_column='Price')),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('iddesign', models.CharField(blank=True, db_column='IdDesign', max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
                ('discriminator', models.CharField(db_column='Discriminator', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('manager', models.IntegerField(blank=True, db_column='Manager', null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.company')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('product', models.IntegerField(blank=True, db_column='Product', null=True)),
                ('orderedproductid', models.ForeignKey(db_column='OrderedProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.orderedproduct')),
                ('userid', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExportbillListproduct',
            fields=[
                ('exportbillid', models.OneToOneField(db_column='ExportBillID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.exportbill')),
                ('exportbillindex', models.IntegerField(db_column='ExportBillIndex')),
                ('listproduct', models.IntegerField(blank=True, db_column='ListProduct', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImportbillListmaterial',
            fields=[
                ('importbillid', models.OneToOneField(db_column='ImportBillID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.importbill')),
                ('importbillindex', models.IntegerField(db_column='ImportBillIndex')),
                ('listmaterial', models.IntegerField(blank=True, db_column='ListMaterial', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialrequestListmaterial',
            fields=[
                ('materialrequestid', models.OneToOneField(db_column='MaterialRequestID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.materialrequest')),
                ('materialrequestindex', models.IntegerField(db_column='MaterialRequestIndex')),
                ('listmaterial', models.IntegerField(blank=True, db_column='ListMaterial', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderListproduct',
            fields=[
                ('orderid', models.OneToOneField(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.order')),
                ('orderindex', models.IntegerField(db_column='OrderIndex')),
                ('listproduct', models.IntegerField(blank=True, db_column='ListProduct', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductListmaterial',
            fields=[
                ('productid', models.OneToOneField(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.product')),
                ('productindex', models.IntegerField(db_column='ProductIndex')),
                ('listmaterial', models.IntegerField(blank=True, db_column='ListMaterial', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StorageListmaterial',
            fields=[
                ('storageid', models.OneToOneField(db_column='StorageID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.storage')),
                ('storageindex', models.IntegerField(db_column='StorageIndex')),
                ('listmaterial', models.IntegerField(blank=True, db_column='ListMaterial', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskListprogress',
            fields=[
                ('taskid', models.OneToOneField(db_column='TaskID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.task')),
                ('taskindex', models.IntegerField(db_column='TaskIndex')),
                ('listprogress', models.IntegerField(blank=True, db_column='ListProgress', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskListrequest',
            fields=[
                ('taskid', models.OneToOneField(db_column='TaskID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wood_producing.task')),
                ('taskindex', models.IntegerField(db_column='TaskIndex')),
                ('listrequest', models.IntegerField(blank=True, db_column='ListRequest', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('desc', models.CharField(blank=True, db_column='Desc', max_length=255, null=True)),
                ('companyid', models.ForeignKey(db_column='CompanyID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.company')),
            ],
        ),
        migrations.CreateModel(
            name='Taskprogress',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('progress', models.IntegerField(blank=True, db_column='Progress', null=True)),
                ('task', models.IntegerField(blank=True, db_column='Task', null=True)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateField(blank=True, db_column='EndDate', null=True)),
                ('progressid', models.ForeignKey(db_column='ProgressID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.progress')),
                ('taskid', models.ForeignKey(db_column='TaskID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.task')),
            ],
        ),
        migrations.CreateModel(
            name='Requestedmaterial',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('material', models.IntegerField(blank=True, db_column='Material', null=True)),
                ('quantity', models.FloatField(db_column='Quantity')),
                ('materialrequestid', models.ForeignKey(db_column='MaterialRequestID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.materialrequest')),
            ],
        ),
        migrations.CreateModel(
            name='Productexported',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('price', models.FloatField(db_column='Price')),
                ('product', models.IntegerField(blank=True, db_column='Product', null=True)),
                ('productid', models.IntegerField(db_column='ProductID')),
                ('exportbillid', models.ForeignKey(db_column='ExportBillID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.exportbill')),
            ],
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='productexportedid',
            field=models.ForeignKey(db_column='ProductExportedID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.productexported'),
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='storageid',
            field=models.ForeignKey(db_column='StorageID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.storage'),
        ),
        migrations.AddField(
            model_name='materialrequest',
            name='storageid',
            field=models.ForeignKey(db_column='StorageID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.storage'),
        ),
        migrations.AddField(
            model_name='materialrequest',
            name='taskid',
            field=models.ForeignKey(db_column='TaskID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.task'),
        ),
        migrations.CreateModel(
            name='Materialofproviderinstorage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('material', models.IntegerField(blank=True, db_column='Material', null=True)),
                ('quantity', models.FloatField(db_column='Quantity')),
                ('materialofproviderid', models.ForeignKey(db_column='MaterialOfProviderID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.materialofprovider')),
                ('requestedmaterialid', models.ForeignKey(blank=True, db_column='RequestedMaterialID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.requestedmaterial')),
                ('storageid', models.ForeignKey(db_column='StorageID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.storage')),
            ],
        ),
        migrations.AddField(
            model_name='materialofprovider',
            name='providerid',
            field=models.ForeignKey(db_column='ProviderID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.provider'),
        ),
        migrations.CreateModel(
            name='Materialinproduct',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('materialid', models.ForeignKey(db_column='MaterialID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.material')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.product')),
            ],
        ),
        migrations.AddField(
            model_name='importbill',
            name='providerid',
            field=models.ForeignKey(db_column='ProviderID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.provider'),
        ),
        migrations.AddField(
            model_name='user',
            name='companyid',
            field=models.ForeignKey(db_column='CompanyID', on_delete=django.db.models.deletion.DO_NOTHING, to='wood_producing.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
