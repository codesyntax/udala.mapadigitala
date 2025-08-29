# from plone import api
from plone.dexterity.interfaces import IDexterityContent
from zope.globalrequest import getRequest
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class VocabItem:
    def __init__(self, token, value):
        self.token = token
        self.value = value


@implementer(IVocabularyFactory)
class Widgets:
    """ """

    def __call__(self, context):
        # Just an example list of content for our vocabulary,
        # this can be any static or dynamic data, a catalog result for example.
        items = [
            VocabItem("Measure", "Measure"),
            VocabItem("CapasBase", "CapasBase"),
            VocabItem("LayerList", "LayerList"),
            VocabItem("SearchGroup", "SearchGroup"),
            VocabItem("eDraw", "eDraw"),
            VocabItem("ElevationProfile", "ElevationProfile"),
            VocabItem("Print", "Print"),
            VocabItem("Share", "Share"),
            VocabItem("ZoomSlider", "ZoomSlider"),
            VocabItem("MyLocation", "MyLocation"),
            VocabItem("FullScreen", "FullScreen"),
            VocabItem("widgets_2D_3D", "widgets_2D_3D"),
            VocabItem("StreetViewButton", "StreetViewButton"),
            VocabItem("Zoominfo", "Zoominfo"),
            VocabItem("HomeButton", "HomeButton"),
            VocabItem("SearchNora", "SearchNora"),
            VocabItem("SwipeBasemap", "SwipeBasemap"),
            VocabItem("CleanMap", "CleanMap"),
            VocabItem("ObtenerCota", "ObtenerCota"),
            VocabItem("MarcarPunto", "MarcarPunto"),
            VocabItem("Transparency", "Transparency"),
            VocabItem("verviewMap", "verviewMap"),
            VocabItem("more_icon", "more_icon"),
            VocabItem("DescargaCartografia", "DescargaCartografia"),
            VocabItem("DescargaMapaComoImagen", "DescargaMapaComoImagen"),
            VocabItem("pixels2", "pixels2"),
            VocabItem("eBookmark", "eBookmark"),
            VocabItem("NoInfo", "NoInfo"),
            VocabItem("Help", "Help"),
            VocabItem("shortcuts", "shortcuts"),
            VocabItem("FotoVuelo", "FotoVuelo"),
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


WidgetsFactory = Widgets()
