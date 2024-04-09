from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from .models import ReportDefinition
from django.views.generic import ListView, CreateView, UpdateView
from .forms import ReportForm
from django.urls import reverse_lazy
from datetime import datetime


# Create your views here.

def indexreport(request):
    return render (request, 'index.html')


class ReportList(ListView):
    model=ReportDefinition
    template_name="index.html"
    paginate_by=4
    ordering= ('-last_modified_at', 'name')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['active_page']="reportlist"
        
        return context



def deletereport(request, id):
    reporte=get_object_or_404(ReportDefinition, pk=id)
    reporte.delete()
    return redirect("reportbroD:list")

class CreateReport(CreateView):
    model=ReportDefinition
    template_name="create.html"
    form_class=ReportForm
    success_url=reverse_lazy("reportbroD:list")
    
class EditReport(UpdateView):
    model=ReportDefinition
    template_name="edit.html"
    form_class=ReportForm
    success_url=reverse_lazy("reportbroD:list")
    context_object_name="reporte"


    


def docs_view(request):
    context={}
    context['active_page']="reportdocs"
    return render(request, "document.html", context) 



def duplicatereport(request, id):
    reporte=get_object_or_404(ReportDefinition, pk=id)
    now = datetime.now()
    ReportDefinition.objects.create(
            name=reporte.name+" "+now.isoformat(),
            report_definition=reporte.report_definition,
            remark=reporte.remark,  
            last_modified_at=now )
    
    return redirect("reportbroD:list")