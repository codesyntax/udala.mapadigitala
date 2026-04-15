# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile

# from plone.namedfile import field as namedfile
from plone.supermodel import model
from udala.mapadigitala import _

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer


class IDigitalMap(model.Schema):
    """Marker interface and Dexterity Python Schema for DigitalMap"""

    service_name = schema.TextLine(
        title=_(
            "Service name",
        ),
        description=_(
            "This name will be shown in the upper right corner of the page",
        ),
        default="",
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

    xmax = schema.Int(
        title=_("X max"),
        description=_(
            "Set the maximum X coordinate of the map initial extent. "
            "The coordinates must be in UTM format.",
        ),
        default=564360,
        required=True,
        readonly=False,
    )

    xmin = schema.Int(
        title=_("X min"),
        description=_(
            "Set the minimum X coordinate of the map initial extent. "
            "The coordinates must be in UTM format.",
        ),
        default=555884,
        required=True,
        readonly=False,
    )
    ymax = schema.Int(
        title=_("Y max"),
        description=_(
            "Set the maximum Y coordinate of the map initial extent. "
            "The coordinates must be in UTM format.",
        ),
        default=4772585,
        required=True,
        readonly=False,
    )
    ymin = schema.Int(
        title=_("Y min"),
        description=_(
            "Set the minimum Y coordinate of the map initial extent."
            "The coordinates must be in UTM format.",
        ),
        default=4785736,
        required=True,
        readonly=False,
    )

    zoom = schema.Int(
        title=_("Zoom"),
        description=_(
            "Set the initial zoom level of the map. "
            "The zoom levels are from 0 (the whole world) to 20 (the maximum detail).",
        ),
        default=12,
        required=True,
        readonly=False,
    )

    # Make sure you add import: from plone.namedfile.field import NamedBlobFile
    bounding_xml = NamedBlobFile(
        title=_(
            "Upload the XML file that represents the sorrounding towns, "
            "in order to show them grayed",
        ),
        required=False,
        readonly=False,
    )


alsoProvides(IDigitalMap["shown_widgets"], ILanguageIndependentField)
alsoProvides(IDigitalMap["shown_layers"], ILanguageIndependentField)
alsoProvides(IDigitalMap["bounding_xml"], ILanguageIndependentField)


@implementer(IDigitalMap)
class DigitalMap(Item):
    """Content-type class for IDigitalMap"""
