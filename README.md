# django-reportbroD
A Django app to create and use ReportBro reports with a sample admin.

Quick start
-----------

1. Add "reportbroD" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
   
                ... ,
   'django_reportbroD.apps.ReportbrodConfig',

   ]

```
2. Add 'django_reportbroD.menus.get_menu_items' to your OPTIONS.context_processors in your TEMPLATES settings. This enables the use of menu for the installed report app. 
 ```
        'OPTIONS': {
   
            'context_processors': [...,
'django_reportbroD.menus.get_menu_items'
   
            ],
            
        }
```

3. Include the reportbroD URLconf in your project urls.py like this:

   path("reportbroD/", include("django_reportbroD.urls", namespace="reportbroD")),

4. Run ``python manage.py migrate`` to create the models and to migrating to data base.

5. Start the development server.

6. Visit the ``/reportbroD/`` URL to create/update/edit/duplicate/remove reports.


Using report
-----------

1. Create a app to using the view file or other file .py for defining the view function to show/export selected report
 ```
  from django_reportbroD.utils import convert_to_base64, convert_list_to_dict, to_dict
  from django_reportbroD.reportcore import reportPDF, reportXLSX
  
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

     return reportPDF(request, code_report, data, file="reporte productos")
 
   ```

