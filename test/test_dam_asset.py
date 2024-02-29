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

from dam.models.dam_asset import DamAsset

class TestDamAsset(unittest.TestCase):
    """DamAsset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DamAsset:
        """Test DamAsset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DamAsset`
        """
        model = DamAsset()
        if include_optional:
            return DamAsset(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                type = 'UNKNOWN',
                code = '',
                metadata = [
                    dam.models.asset_metadata.AssetMetadata(
                        key = '', 
                        value = '', )
                    ],
                grn = '',
                public_url = ''
            )
        else:
            return DamAsset(
        )
        """

    def testDamAsset(self):
        """Test DamAsset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
