from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from udala.mapadigitala.content.digital_map import IDigitalMap
from udala.mapadigitala.testing import UDALA_MAPADIGITALA_INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility

import unittest


class DigitalMapIntegrationTest(unittest.TestCase):
    layer = UDALA_MAPADIGITALA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_digital_map_schema(self):
        fti = queryUtility(IDexterityFTI, name="DigitalMap")
        schema = fti.lookupSchema()
        self.assertEqual(IDigitalMap, schema)

    def test_ct_digital_map_fti(self):
        fti = queryUtility(IDexterityFTI, name="DigitalMap")
        self.assertTrue(fti)

    def test_ct_digital_map_factory(self):
        fti = queryUtility(IDexterityFTI, name="DigitalMap")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDigitalMap.providedBy(obj),
            f"IDigitalMap not provided by {obj}!",
        )

    def test_ct_digital_map_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="DigitalMap",
            id="digital_map",
        )

        self.assertTrue(
            IDigitalMap.providedBy(obj),
            f"IDigitalMap not provided by {obj.id}!",
        )

        parent = obj.__parent__
        self.assertIn("digital_map", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("digital_map", parent.objectIds())

    def test_ct_digital_map_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="DigitalMap")
        self.assertTrue(fti.global_allow, f"{fti.id} is not globally addable!")
