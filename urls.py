from django.urls import path

from .reportcore import *
from .views import *

app_name = "reportbroD"
urlpatterns = [
    path("", ReportList.as_view(), name="list"),
    path("create/", CreateReport.as_view(), name="create"),
    path("import/", importreport, name="import"),
    path("edit/<int:pk>", EditReport.as_view(), name="edit"),
    path("delete/<int:id>", deletereport, name="delete"),
    path("duplicate/<int:id>", duplicatereport, name="duplicate"),
    path("export/<int:id>", exportreport, name="exportation"),
    path("docs/", docs_view, name="docs"),
    path("template/<int:pk>/", edit, name="template"),
    path("run/", run, name="report_run"),
    path("save/<int:pk>/", save, name="report_save"),
]
