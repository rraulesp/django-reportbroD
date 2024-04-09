from django.urls import reverse


def get_menu_items(request):
    """Returns application menu items with special class for active menu item."""
    return {
      "active_page":"",
      "menu": ( {'url': reverse('reportbroD:list'), 'label': "ReportBro Designer",
        'icon': "nav-icon ti ti-pencil-alt",  'id':'reportlist' },
        
        {'url': reverse('reportbroD:docs'), 'label': "Designer Documentación",
        'icon': "nav-icon ti ti-comment-alt",  'id':  'reportdocs' },
        
         {'url': reverse('admin:index'), 'label': "Administración del Sitio",
        'icon': "nav-icon fa fa-users",  'id': '' },
        
         {'url': '/', 'label': "Inicio",
        'icon': "nav-icon ti ti-rocket",  'id': ''}
         )
         }



