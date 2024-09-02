import json
from datetime import datetime

from django.db import models
from django.utils.translation import gettext as _


# store report requests for testing, used by ReportBro Designer
# for preview of pdf and xlsx
class ReportRequest(models.Model):
    key = models.CharField(max_length=36)
    report_definition = models.TextField()
    data = models.TextField()
    is_test_data = models.BooleanField()
    pdf_file = models.BinaryField(null=True)
    pdf_file_size = models.IntegerField(null=True)
    created_on = models.DateTimeField()

    class Meta:
        db_table = "report_request"


# report definition for our album report which is used for printing
# the pdf with the album list. When the report is saved
# in ReportBro Designer it will be stored in this table.
class ReportDefinition(models.Model):
    report_definition = models.TextField(default=json.dumps(""))
    name = models.CharField(max_length=200, unique=True, verbose_name="Nombre")
    remark = models.TextField(null=True, blank=True, verbose_name="Descripción")
    last_modified_at = models.DateTimeField(default=datetime.now())

    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ("name",):
            return _("unique")
        else:
            return super(ReportDefinition, self).unique_error_message(
                model_class, unique_check
            )

    class Meta:
        db_table = "report_definition"
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "report_definition": self.report_definition,
            "name": self.name,
            "remark": self.remark,
            "last_modified_at": self.last_modified_at.isoformat(),
        }
