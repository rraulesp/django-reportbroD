import json
from itertools import chain

from django.db import models
from django.http import HttpResponseServerError
from PIL import Image, ImageDraw, ImageOps

from .models import ReportDefinition
from .reportcore import reportPDF, reportXLSX


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
                formato = f.value_from_object(instance).url.split(".")[-1]
                data[f.name] = convert_to_base64(
                    f.value_from_object(instance).url, formato
                )
            else:
                data[f.name] = None
        else:
            data[f.name] = f.value_from_object(instance)
    return data


def convert_list_to_dict(listado):
    """Convierte una query o lista de elementos de la clase Model en un
    diccionario entendible para ReportBro"""

    lista = [to_dict(elem) for elem in listado]
    return lista


def convert_to_base64(path, format_image):
    """
    Nota: path se refiere a la ruta de la imagen y  format_image se refiere al fomato de la imagen (jpg, png, jpeg, etc)
    Este método permite convertir una imagen jpg o png a una imagen en base 64
      para que ReportBro pueda renderizarla como parte de sus parámetros"""
    import base64

    from django.conf import settings

    with open(str(settings.BASE_DIR) + path, "rb") as image_file:
        return f"data:image/{format_image};base64,{base64.b64encode(image_file.read()).decode('utf-8')}"


def export_report_by_code(
    template_code, data, extension="pdf", file="reporte", download=False
):
    """Export a report using its code
    view_mode: Its the way in the report pdf is going to download through the navegator. Two options:
    1. download =False, (inline) >the pdf report is showed in the navegator and the user can download it handly or making print, etc.
    2. download =True (attachment) >the pdf report is downloaded directly into pc

    """

    report = ReportDefinition.objects.filter(pk=template_code).first()

    if not report:
        return HttpResponseServerError("Este reporte no se encuentra disponible")

    if extension.lower() == "xlsx":
        return reportXLSX(report.report_definition, data, file)

    return reportPDF(report.report_definition, data, file, download)


def export_report_by_name(
    template_name, data, extension="pdf", file="reporte", download=False
):
    """Export a report using its name
    view_mode: Its the way in the report pdf is going to download through the navegator. Two options:
    1. download =False, (inline) >the pdf report is showed in the navegator and the user can download it handly or making print, etc.
    2. download =True (attachment) >the pdf report is downloaded directly into pc
    """

    report = ReportDefinition.objects.filter(name=template_name).first()

    if not report:
        return HttpResponseServerError("Este reporte no se encuentra disponible")

    if extension.lower() == "xlsx":
        return reportXLSX(report.report_definition, data, file)

    return reportPDF(report.report_definition, data, file, download)


def export_report_from_JSON(
    path_json, data, extension="pdf", file="reporte", download=False
):
    """Export a report using a JSON template report.
    view_mode: Its the way in the report pdf is going to download through the navegator. Two options:
    1. download =False, (inline) >the pdf report is showed in the navegator and the user can download it handly or making print, etc.
    2. download =True (attachment) >the pdf report is downloaded directly into pc
    """

    try:
        with open(path_json) as json_file:
            report = json.load(json_file)
    except FileNotFoundError:
        return HttpResponseServerError("La ruta especificada no contiene la plantilla.")
    except json.JSONDecodeError:
        return HttpResponseServerError("El fichero no tiene un formato adecuado.")

    if extension.lower() == "xlsx":
        return reportXLSX(report["report_definition"], data, file)

    return reportPDF(report["report_definition"], data, file, download)
