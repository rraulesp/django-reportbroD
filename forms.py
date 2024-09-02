from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ReportDefinition


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportDefinition
        fields = ["name", "remark"]
        labels = {"name": "Nombre", "remark": "Descripcion"}

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "nombre",
                    "placeholder": _("holdern"),
                }
            ),
            "remark": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "3",
                    "id": "desc",
                    "placeholder": _("holderd"),
                }
            ),
        }


class ReportImpForm(forms.Form):
    template = forms.FileField(
        label="Plantilla",
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file",
                "id": "filetemplate",
                "placeholder": _("holderf"),
            }
        ),
    )
