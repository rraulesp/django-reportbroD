from django.urls import reverse
from django.utils.translation import gettext as _


def get_menu_items():
    """Returns application menu items with special class for active menu item."""
    return (
        {
            "url": reverse("reportbroD:list"),
            "label": "ReportBro Admin",
            "icon": "nav-icon ti ti-pencil-alt",
            "id": "reportlist",
        },
        {
            "url": reverse("reportbroD:docs"),
            "label": _("opt1"),
            "icon": "nav-icon ti ti-comment-alt",
            "id": "reportdocs",
        },
        {
            "url": "https://www.reportbro.com/doc/tutorial",
            "label": _("opt2"),
            "icon": "nav-icon fa fa-book",
            "id": "reportbro",
            "target": True,
        },
        {
            "url": "/",
            "label": _("opt4"),
            "icon": "nav-icon ti ti-home",
            "id": "home",
        },
    )


def reportbro_langs():
    return (
        {"code": "es", "name_local": "Español"},
        {"code": "en", "name_local": "English"},
    )
