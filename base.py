import datetime
import decimal
import json

from .models import ReportDefinition


def create_base_report_template(name):
    # use a predefined report definition so you don't have to start from scratch in this demo app,
    # for a real world app you would probably start with an empty report if nothing was saved previously

    report_definition = ""

    ReportDefinition.objects.create(
        name=name,
        report_definition=json.dumps(report_definition),
        last_modified_at=datetime.datetime.now(),
    )


def json_default(obj):
    """Serializes decimal and date values, can be used for json encoder."""
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, datetime.date):
        return str(obj)
    raise TypeError
