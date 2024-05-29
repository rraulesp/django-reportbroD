# django-reportbroD
A Django app to create, use and export ReportBro reports (free version) with a admin. 

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![lib](https://badgen.net/badge/Export/PDF-XLSX/red?) ![JS](https://badgen.net/badge/Js/Reportbro_Designer/blue?icon=doc)  ![lib](https://badgen.net/badge/Package/Reportbro-lib/red?icon=doc)

Quick start
-----------

1. Add "django_reportbroD" to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [
... ,
'django_reportbroD.apps.ReportbrodConfig',
   ]

```

2. Include the reportbroD URLconf in your project urls.py like this:

```
   path("reportbroD/", include("django_reportbroD.urls", namespace="reportbroD")),  
```


3.  Run ``python manage.py migrate`` to create the models and to migrating to data base.

4. Start the development server.

5. Visit the ``/reportbroD/`` URL to create/update/edit/duplicate/remove reports.




> **Traslations** 
>
>The next step is optional if you want to use in Spanish and English, otherwise it isn't necessary.

1. Add LocaleMiddleware to your MIDDLEWARE list in your settings. This allows the reporting app to have translation in Spanish and English. 
 ```
        MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    ...
            ],  
```

2. Include the i18N URLconf in your project urls.py like this:

```
   path("i18n/", include("django.conf.urls.i18n")),  
```




Using report
-----------

1. Create a app to using the view file or other file .py for defining the view function to show/export selected report
 ```   
  from django_reportbroD.utils import convert_to_base64, convert_list_to_dict, to_dict, export_report_by_code, export_report_by_name, export_report_from_JSON
  
   def generar_pdf(request):
   
     products=Product.objects.all()
   
     #converting in a dictionary
     productos=[to_dict(p) for p in products]
   
     imagen= convert_to_base64(products.first().imagen.url, 'jpg')
   
     data={
            "productos":productos,
            "imagen":imagen
          }
   
     code_report= 12

     return export_report_by_code(template_code=code_report, data=data, extension="pdf")

def generar_xls(request):
   
     products=Product.objects.all()
   
     #converting in a dictionary
     productos=[to_dict(p) for p in products]
   
     imagen= convert_to_base64(products.first().imagen.url, 'jpg')
   
     data={
   "productos":productos,
   "imagen":imagen
    }
   

     return export_report_by_name(template_name="Plantilla de obrero" , data=data, extension="xlsx")


def generar_reporte(request):
   
     products=Product.objects.all()
   
     #converting in a dictionary
     productos=[to_dict(p) for p in products]
   
     imagen= convert_to_base64(products.first().imagen.url, 'jpg')
   
     data={
   "productos":productos,
   "imagen":imagen
    }
   

     return export_report_from_JSON(path_json="reporte.json", data=data, extension="xlsx")
 
   ```


2. Include a report into Django Admin through a action function.

```

# admin.py 
from .views import reporte
...

def reportbro(modeladmin, request, queryset):
    w=queryset.first()
    if w:
        return reporte(request, w.code)

reportbro.short_description="Working Report"

@admin.register(Working)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("worker","date", "hours","payhorary", "descount", "pay_extra", "pay" )
    list_filter=["date", "worker"]
    list_display_links = ("worker","date" )
    actions=[reportbro]
```

> **Parameter >>** **download = True**
>
>In this case,  download parameter from export_report_by_code, export_report_by_name and export_report_from_JSON functions must be "True" to avoid any errors when the report format is "pdf".

```
#views.py 
from django_reportbroD.utils import convert_to_base64, convert_list_to_dict, to_dict, export_report_by_code, export_report_by_name, export_report_from_JSON
  ...

def reporte(request, code):

    worker=Worker.objects.filter(code=code).first()
    workings=Working.objects.filter(worker=worker)
    
    asistencia= [
{
    "date": w.date.date,
    "payhorary" : w.payhorary,
    "descount" : w.descount,
    "pay_extra" : w.pay_extra,
    "pay" : w.pay,
    
    }
for w in workings
    ]

    trabajador=to_dict(worker)
    trabajador["horary"]=worker.horary.horario()
    trabajador["area"]=worker.area.Area()


    data={
        "worker":trabajador,
        "working": asistencia,
        "date":datetime.datetime.now()
    }

    return export_report_by_code(template_code=7, data=data, file="nuevo", download=True)
```
