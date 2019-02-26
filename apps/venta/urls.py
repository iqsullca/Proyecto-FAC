from django.urls import path, include, reverse
from . import views
app_name = 'venta'
urlpatterns = [
	path('', views.index, name='index'),
	path('nuevo', views.ClienteCreate.as_view(), name='cliente_crear'),
	path('listar', views.ClienteList.as_view(), name='cliente_listar'),
	path('editar/<int:pk>', views.ClienteUpdate.as_view(), name='cliente_editar'),
	path('eliminar/<int:pk>', views.ClienteDelete.as_view(), name='cliente_eliminar'),
]