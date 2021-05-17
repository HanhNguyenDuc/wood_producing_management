from wood_producing.views.foreman import TaskDetailView
from wood_producing.views.api_duc import add_provider
from wood_producing.views.approve_material_request import ApproveMaterialRequest
from wood_producing.views.api import delete_product, delete_task
from wood_producing.views.storage_manager import AddProduct, EditMaterial, EditProduct, ImportChooseMaterial, ImportMaterialFromProvider, AddMaterial, MaterialBase, ProductManagement
from wood_producing.views.statistic import MaterialStatistic, ProductionStatistic
from wood_producing.views.seller import CreateOrder, PublishOrder, ListOrder, OrderDetail
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
    path('seller/', views.ListOrder.as_view(), name='list_order'),
    path('seller/order_detail/<int:order_id>/', views.OrderDetail.as_view(), name='order_detail'),
    path('seller/order_detail/<int:order_id>/publish', views.PublishOrder.as_view(), name='publish_order'),
    path('statistic/production', views.ProductionStatistic.as_view(), name='production_statistic'),
    path('statistic/profit', views.ProfitStatistic.as_view(), name='profit_statistic'),
    path('statistic/material', views.MaterialStatistic.as_view(), name='material_statistic'),
    path('storage_manager/manage_material',views.MaterialBase.as_view(), name="manage_material"),
    path('storage_manager/import_material', views.ImportMaterialFromProvider.as_view(), name='import_material'),
    path('storage_manager/add_material', views.AddMaterial.as_view(), name='add_material'),
    path('storage_manager/edit_material/<int:material_id>', views.EditMaterial.as_view(), name='edit_material'),
    path('api/material/delete_material', views.delete_material, name='delete_material'),
    path('storage_manager/product_manage', views.ProductManagement.as_view(), name='manage_product'),
    path('storage_manager/product_manage/add_product', views.AddProduct.as_view(), name='add_product'),
    path('storage_manager/product_manage/edit_product/<int:product_id>', views.EditProduct.as_view(), name='edit_product'),
    path('storage_manager/list_material_request', views.ListMaterialRequest.as_view(), name="select_material_request"),
    path('storage_manager/approve_material_request/<int:material_request_id>', views.ApproveMaterialRequest.as_view(), name="approve_material_request"),
    path('api/product/delete_product',views.delete_product, name='delete_product'),
    path('foreman', views.ForemanMainView.as_view(), name="foreman_main_view"),
    path('foreman/edit_task/<int:task_id>', views.EditTaskView.as_view()),
    path('foreman/view_task/<int:task_id>', views.TaskDetailView.as_view()),
    path('api/task/delete_task', views.delete_task, name='delete_task'),
    path('storage_manager/import_material/choose_provider', views.ImportChooseProvider.as_view(), name='choose_provider'),
    path('api_duc/provider/add_provider', views.add_provider, name = 'add_provider'),
    path('api_duc/provider/choose_provider', views.choose_provider, name = 'choose'),
    path('storage_manager/import_material/choose_material', views.ImportChooseMaterial.as_view(), name='choose_material'),
    path('api/statistic/statistic_profit', views.statistic_profit, name='statistic_profit'),
    path('api/statistic/statistic_production', views.statistic_production, name='statistic_production'),
    path('api/statistic/statistic_material', views.statistic_material, name='statistic_material'),
    path('api/material/request_material', views.create_material_request, name='request_material'),
    path('api/customer/add', views.add_user, name='add_user'),
    path('api/product/searchProductbyName', views.search_product_by_name, name='search_product_by_name'),
    path('api/customer/search_customer_by_name', views.search_customer_by_name, name='search_customer_by_name'),

    path('', views.Index.as_view(), name='index')
]