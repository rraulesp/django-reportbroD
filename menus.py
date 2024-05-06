from django.urls import reverse


def get_menu_items(request):
    """Returns application menu items with special class for active menu item."""
    return {
      "active_page":"reportlist",
      "menu": ( {'url': reverse('reportbroD:list'), 'label': "ReportBro Admin",
        'icon': "nav-icon ti ti-pencil-alt",  'id':'reportlist' },
        
        {'url': reverse('reportbroD:docs'), 'label': "Documentación de ReportBro Admin ",
        'icon': "nav-icon ti ti-comment-alt",  'id':  'reportdocs' },
        
         {'url': 'https://www.reportbro.com/doc/tutorial', 'label': "Tutorial de ReportBro Designer",
        'icon': "nav-icon fa fa-book",  'id': 'reportbro' },
        
         {'url': reverse('admin:index'), 'label': "Administración del Sitio",
        'icon': "nav-icon fa fa-users",  'id': 'admin' },
        
         {'url': '/', 'label': "Inicio",
        'icon': "nav-icon ti ti-rocket",  'id': 'home'}
         )
         }



