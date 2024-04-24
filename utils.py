import datetime
import decimal
import json
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _
from .models import ReportDefinition
from django.db import models
from itertools import chain


def create_base_report_template(name):
    # use a predefined report definition so you don't have to start from scratch in this demo app,
    # for a real world app you would probably start with an empty report if nothing was saved previously

    report_definition = ""

    ReportDefinition.objects.create(
        name=name,
        report_definition=json.dumps(report_definition),
        last_modified_at=datetime.datetime.now())




def json_default(obj):
    """Serializes decimal and date values, can be used for json encoder."""
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    if isinstance(obj, datetime.date):
        return str(obj)
    raise TypeError




def to_dict(instance):
    """Esta función permite convertir un objeto de tipo Model a un diccionario
    para que su información pueda ser pasada como parámetro a ReportBro"""
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        if isinstance(f, models.DateTimeField):
            if f.value_from_object(instance) is not None:
                data[f.name] = f.value_from_object(instance).isoformat()
            else:
                data[f.name] = None
        elif isinstance(f, models.ImageField):
            if f.value_from_object(instance) is not None:
                formato= f.value_from_object(instance).url.split(".")[-1]
                data[f.name] = convert_to_base64(f.value_from_object(instance).url, formato)
            else:
                data[f.name] = None
        else:
            data[f.name] = f.value_from_object(instance)
    return data


def convert_list_to_dict(listado):
    """Convierte una query o lista de elementos de la clase Model en un 
    diccionario entendible para ReportBro"""

    lista=[to_dict(elem) for elem in listado ]
    return lista


def convert_to_base64(path, format_image):
    """
    Nota: path se refiere a la ruta de la imagen y  format_image se refiere al fomato de la imagen (jpg, png, jpeg, etc)
    Este método permite convertir una imagen jpg o png a una imagen en base 64 
    para que ReportBro pueda renderizarla como parte de sus parámetros  """
    import base64
    from django.conf import settings
    print(str(settings.BASE_DIR)+path)
    
    with open(str(settings.BASE_DIR)+path, "rb") as image_file:
        return f"data:image/{format_image};base64,{base64.b64encode(image_file.read()).decode('utf-8')}"
    


