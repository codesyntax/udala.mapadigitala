# -*- coding: utf-8 -*-
from udala.mapadigitala.testing import UDALA_MAPADIGITALA_FUNCTIONAL_TESTING
from udala.mapadigitala.testing import UDALA_MAPADIGITALA_INTEGRATION_TESTING
from udala.mapadigitala.views.digital_map_view import IDigitalMapView
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = UDALA_MAPADIGITALA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='view'
        )
        self.assertTrue(IDigitalMapView.providedBy(view))

    def test_view_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='view'
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = IDigitalMapView.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = UDALA_MAPADIGITALA_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
