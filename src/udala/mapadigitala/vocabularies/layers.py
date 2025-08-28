# -*- coding: utf-8 -*-

# from plone import api
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implementer
from udala.mapadigitala import _
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem(object):
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class Layers(object):
    """
    """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem("NOMBRESGEOGRAFICOS_EUS_1997", "NOMBRESGEOGRAFICOS_EUS_1997"),
            VocabItem("KARTOGRAFIA_EUS_4096", "KARTOGRAFIA_EUS_4096"),
            VocabItem("LIMITES_EUS_4526", "LIMITES_EUS_4526"),
            VocabItem("LOCALIZACION_EUS_4336", "LOCALIZACION_EUS_4336"),
            VocabItem("INGURUMENA_EUS_6566", "INGURUMENA_EUS_6566"),
            VocabItem("URA_EUS_7015", "URA_EUS_7015"),
            VocabItem("AGRICULTURA_EUS_3611", "AGRICULTURA_EUS_3611"),
            VocabItem("PLANEAMIENTO_EUS_1397", "PLANEAMIENTO_EUS_1397"),
            VocabItem("SEGURIDAD_EUS_2035", "SEGURIDAD_EUS_2035"),
            VocabItem("SALUD_EUS_575", "SALUD_EUS_575"),
            VocabItem("SERVICIOS_CIUDADANIA_EUS_7573", "SERVICIOS_CIUDADANIA_EUS_7573"),
            VocabItem("VIVIENDA_EUS_1693", "VIVIENDA_EUS_1693"),
            VocabItem("SOCIEDAD_EUS_5230", "SOCIEDAD_EUS_5230"),
            VocabItem("KULTURA_EUS_9851", "KULTURA_EUS_9851"),
            VocabItem("ECONOMIA_EUS_330", "ECONOMIA_EUS_330"),
            VocabItem("LANBIDE_EUS_9941", "LANBIDE_EUS_9941"),
            VocabItem("GOGORA_EUS_5321", "GOGORA_EUS_5321"),
            VocabItem("ITELAZPI_EUS_8976", "ITELAZPI_EUS_8976"),
        ]

        if not IDexterityContent.providedBy(context):
            req = getRequest()
            context = req.PARENTS[0]

        # create a list of SimpleTerm items:
        terms = []
        for item in items:
            terms.append(
                SimpleTerm(
                    value=item.token,
                    token=str(item.token),
                    title=item.value,
                )
            )
        # Create a SimpleVocabulary from the terms list and return it:
        return SimpleVocabulary(terms)


LayersFactory = Layers()
