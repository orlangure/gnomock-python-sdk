# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gnomock
from gnomock.models.localstack import Localstack  # noqa: E501
from gnomock.rest import ApiException

class TestLocalstack(unittest.TestCase):
    """Localstack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Localstack
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gnomock.models.localstack.Localstack()  # noqa: E501
        if include_optional :
            return Localstack(
                services = ["s3","ses"], 
                s3_path = '/home/gnomock/project/testdata/s3', 
                version = 'latest'
            )
        else :
            return Localstack(
                services = ["s3","ses"],
        )

    def testLocalstack(self):
        """Test Localstack"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
