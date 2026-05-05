from django.urls import path
from apps.Claro import views

urlpatterns = [
    path(
        route="Claro/health-check",
        view=views.health_check,
        name="health-check",
    ),
    
    path(
        route="Claro/consultar-cpf-na-base-de-dados/<str:cpf>",
        view=views.consultar_cpf_no_db,
        name="consultar-cpf-na-base-de-dados",
    ),

]
