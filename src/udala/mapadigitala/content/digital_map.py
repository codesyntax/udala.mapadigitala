# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from plone.namedfile.field import NamedBlobFile
from udala.mapadigitala import _


class IDigitalMap(model.Schema):
    """ Marker interface and Dexterity Python Schema for DigitalMap
    """
    service_name = schema.TextLine(
        title=_(
            u'Service name',
        ),
        description=_(
            u'This name will be shown in the upper right corner of the page',
        ),
        default=u'',
        required=False,
        readonly=False,
    )

    shown_widgets = schema.Set(
        title=_(
            "Select available widgets",
        ),
        value_type=schema.Choice(
            vocabulary="udala.mapadigitala.widgets",
        ),
        required=False,
        default={
            "Measure",
            "CapasBase",
            "LayerList",
            "SearchGroup",
            "eDraw",
            "ElevationProfile",
            "Print",
            "Share",
            "ZoomSlider",
            "MyLocation",
            "FullScreen",
            "widgets_2D_3D",
            "StreetViewButton",
            "Zoominfo",
            "HomeButton",
            "SearchNora",
            "SwipeBasemap",
            "CleanMap",
            "ObtenerCota",
            "MarcarPunto",
            "Transparency",
            "verviewMap",
            "more_icon",
            "DescargaCartografia",
            "DescargaMapaComoImagen",
            "pixels2",
            "eBookmark",
            "NoInfo",
            "Help",
            "shortcuts",
            "FotoVuelo",
        },
        # defaultFactory=get_default_shown_widgets,
        readonly=False,
    )

    shown_layers = schema.Set(
        title=_(
            "Select available map layers",
        ),
        value_type=schema.Choice(
            vocabulary="udala.mapadigitala.layers",
        ),
        required=False,
        default={
            "NOMBRESGEOGRAFICOS_EUS_1997",
            "KARTOGRAFIA_EUS_4096",
            "LIMITES_EUS_4526",
            "LOCALIZACION_EUS_4336",
            "INGURUMENA_EUS_6566",
            "URA_EUS_7015",
            "AGRICULTURA_EUS_3611",
            "PLANEAMIENTO_EUS_1397",
            "SEGURIDAD_EUS_2035",
            "SALUD_EUS_575",
            "SERVICIOS_CIUDADANIA_EUS_7573",
            "VIVIENDA_EUS_1693",
            "SOCIEDAD_EUS_5230",
            "KULTURA_EUS_9851",
            "ECONOMIA_EUS_330",
            "LANBIDE_EUS_9941",
            "GOGORA_EUS_5321",
            "ITELAZPI_EUS_8976",
        },
        # defaultFactory=get_default_shown_layers,
        readonly=False,
    )

    # Make sure you add import: from plone.namedfile.field import NamedBlobFile
    bounding_xml = NamedBlobFile(
        title=_(
            'Upload the XML file that represents the sorrounding towns, in order to show them grayed',
        ),
        required=False,
        readonly=False,
    )

@implementer(IDigitalMap)
class DigitalMap(Item):
    """ Content-type class for IDigitalMap
    """
