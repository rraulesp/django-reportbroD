from django.conf import settings
from appconf import AppConf

class ReportBroDConf(AppConf):
    ADMIN = False
    JSON_TEMPLATE = ""

    class Meta:
        prefix = 'reportbrod'