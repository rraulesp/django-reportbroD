from django.urls import reverse

from django.utils.translation import gettext as _


def get_menu_items(request):
    """Returns application menu items with special class for active menu item."""
    return {
      "active_page":"reportlist",
      "menu": ( {'url': reverse('reportbroD:list'), 'label': "ReportBro Admin",
        'icon': "nav-icon ti ti-pencil-alt",  'id':'reportlist' },
        
        {'url': reverse('reportbroD:docs'), 'label': _("opt1"),
        'icon': "nav-icon ti ti-comment-alt",  'id':  'reportdocs' },
        
         {'url': 'https://www.reportbro.com/doc/tutorial', 'label': _("opt2"),
        'icon': "nav-icon fa fa-book",  'id': 'reportbro' },
        
         {'url': reverse('admin:index'), 'label': _("opt3"),
        'icon': "nav-icon fa fa-users",  'id': 'admin' },
        
         {'url': '/', 'label': _("opt4"),
        'icon': "nav-icon ti ti-rocket",  'id': 'home'}
         ),
         
        "reportbro_langs": (  
    {"code":"es", "name_local":"Español"},
     {"code":"en", "name_local":"English"} 
              )

         }



