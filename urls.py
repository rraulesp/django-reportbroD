"""
URL configuration for Clases project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from  .reportcore import *

app_name="reportbroD"
urlpatterns = [
    path("", ReportList.as_view(), name="list"),
    path("create/", CreateReport.as_view(), name="create"),
    path("edit/<int:pk>", EditReport.as_view(), name="edit"),
    path("delete/<int:id>", deletereport, name="delete"),
     path("duplicate/<int:id>", duplicatereport, name="duplicate"),
    path("docs/", docs_view, name="docs"),
    path("template/<int:pk>/", edit, name="template"),
    path("run/", run, name="report_run"),
    path("save/<int:pk>/", save, name="report_save"),
#     path("agregar/", addgroup, name="add_group"),
# path("editar/<int:group>", editgroup, name="edit_group"),
# path("eliminar/<int:group>", delete_group, name="delet_group"),
# path("exportpdf/",show_reportGroups , name="exportg"),
# path("exportxlsx/",show_reportexcell , name="exportx")

]
