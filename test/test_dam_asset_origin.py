# coding: utf-8

"""
    Dam Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dam.models.dam_asset_origin import DamAssetOrigin

class TestDamAssetOrigin(unittest.TestCase):
    """DamAssetOrigin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DamAssetOrigin:
        """Test DamAssetOrigin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DamAssetOrigin`
        """
        model = DamAssetOrigin()
        if include_optional:
            return DamAssetOrigin(
                url = '',
                type = 'EXTERNAL'
            )
        else:
            return DamAssetOrigin(
        )
        """

    def testDamAssetOrigin(self):
        """Test DamAssetOrigin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
