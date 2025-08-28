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
            'Select available widgets',
        ),
        value_type=schema.Choice(
            vocabulary="udala.mapadigitala.widgets",
        ),
        required=False,
        default=set([
            'Folder',
            'Image',
        ]),
        # defaultFactory=get_default_shown_widgets,
        readonly=False,
    )


    shown_layers = schema.Set(
        title=_(
            'Select available map layers',
        ),
        value_type=schema.Choice(
            vocabulary="udala.mapadigitala.layers",
        ),
        required=False,
        default=set([
            'Folder',
            'Image',
        ]),
        # defaultFactory=get_default_shown_layers,
        readonly=False,
    )

@implementer(IDigitalMap)
class DigitalMap(Item):
    """ Content-type class for IDigitalMap
    """
