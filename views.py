import json
from datetime import datetime
from typing import Any

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, UpdateView

from .forms import ReportForm, ReportImpForm
from .models import ReportDefinition
from .menus import get_menu_items, reportbro_langs

# Create your views here.


class ReportList(ListView):
    model = ReportDefinition
    template_name = "reportbrod/index.html"
    paginate_by = 4
    ordering = ("-last_modified_at", "name")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_page"] = "reportlist"
        context["menu"] = get_menu_items()
        context["reportbro_langs"] = reportbro_langs()

        return context


def deletereport(request, id):
    reporte = get_object_or_404(ReportDefinition, pk=id)
    reporte.delete()
    return redirect("reportbroD:list")


class CreateReport(CreateView):
    model = ReportDefinition
    template_name = "reportbrod/create.html"
    form_class = ReportForm
    success_url = reverse_lazy("reportbroD:list")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_page"] = "reportlist"
        context["menu"] = get_menu_items()
        context["reportbro_langs"] = reportbro_langs()

        return context


class EditReport(UpdateView):
    model = ReportDefinition
    template_name = "reportbrod/edit.html"
    form_class = ReportForm
    success_url = reverse_lazy("reportbroD:list")
    context_object_name = "reporte"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_page"] = "reportlist"
        context["menu"] = get_menu_items()
        context["reportbro_langs"] = reportbro_langs()

        return context


def docs_view(request):
    context = {}
    context["active_page"] = "reportdocs"
    context["menu"] = get_menu_items()
    context["reportbro_langs"] = reportbro_langs()
    return render(request, "reportbrod/document.html", context)


def duplicatereport(request, id):
    reporte = get_object_or_404(ReportDefinition, pk=id)
    now = datetime.now()
    ReportDefinition.objects.create(
        name=reporte.name + " " + now.isoformat(),
        report_definition=reporte.report_definition,
        remark=reporte.remark,
        last_modified_at=now,
    )

    return redirect("reportbroD:list")


def exportreport(request, id):
    reporte = get_object_or_404(ReportDefinition, pk=id)

    exportation = json.dumps(reporte.to_dict())
    response = HttpResponse(exportation, content_type="application/force-download")
    response["Content-Disposition"] = f"attachment; filename={reporte.name}.json"
    return response


def importreport(request):
    context = {}
    context["active_page"] = "reportlist"
    context["menu"] = get_menu_items()
    context["reportbro_langs"] = reportbro_langs()

    if request.method == "POST":
        form = ReportImpForm(request.POST, request.FILES)

        if form.is_valid():
            cd = request.FILES["template"]
            actual = datetime.now()

            try:
                file = json.load(cd)
                namereport = (
                    file["name"]
                    if ReportDefinition.objects.filter(name=file["name"]).first()
                    is None
                    else file["name"] + " " + actual.isoformat()
                )
                ReportDefinition.objects.create(
                    name=namereport,
                    report_definition=file["report_definition"],
                    remark=file["remark"],
                    last_modified_at=actual,
                )
            except:
                context["form"] = ReportImpForm()
                context["error"] = _("not_format")
                return render(
                    request,
                    "import.html",
                    context,
                )

            return redirect("reportbroD:list")

    context["form"] = ReportImpForm()

    return render(request, "reportbrod/import.html", context)
