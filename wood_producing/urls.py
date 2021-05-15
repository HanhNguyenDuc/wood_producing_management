from wood_producing.views.api import delete_task
from wood_producing.views.storage_manager import EditMaterial, ImportMaterialFromProvider, AddMaterial, MaterialBase, ProductManagement
from wood_producing.views.statistic import MaterialStatistic, ProductionStatistic
from wood_producing.views.seller import CreateOrder, PublishOrder
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/change_password',views.ChangePasswordView.as_view(), name="change_password"),
    path('user/login', views.LoginView.as_view(template_name="wood_producing/user_base/login.html"), name="login"),
    path('user/logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),
    path('producing_manager', views.MainProducingManagerView.as_view(), name='main_product'),
    path('producing_manager/order_detail/<int:order_id>', views.ManageTaskView.as_view()),
    path('producing_manager/order_detail/add_task/<int:ordered_product_id>', views.AddTaskView.as_view(), name='ask_task'),
    path('seller/create_order', views.CreateOrder.as_view(), name='create_order'),
    path('seller/publish_order', views.PublishOrder.as_view(), name='publish_order'),
    path('statistic/production', views.ProductionStatistic.as_view(), name='production_statistic'),
    path('statistic/profit', views.ProfitStatistic.as_view(), name='profit_statistic'),
    path('statistic/material', views.MaterialStatistic.as_view(), name='material_statistic'),
    path('storage_manager/material_base',views.MaterialBase.as_view(), name="material_base"),
    path('storage_manager/import_material', views.ImportMaterialFromProvider.as_view(), name='import_material'),
    path('storage_manager/add_material', views.AddMaterial.as_view(), name='add_material'),
    path('storage_manager/edit_material', views.EditMaterial.as_view(), name='edit_material'),
    path('storage_manager/product_manage', views.ProductManagement.as_view(), name='product_manage'),
    path('api/task/delete_task', views.delete_task, name='delete_task'),
    path('', views.Index.as_view(), name='index')
]