# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 0.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gnomock
from gnomock.models.options import Options  # noqa: E501
from gnomock.rest import ApiException

class TestOptions(unittest.TestCase):
    """Options unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Options
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gnomock.models.options.Options()  # noqa: E501
        if include_optional :
            return Options(
                wait_timeout = 60000000000, 
                env = [
                    'ENV_VAR_NAME=some-value'
                    ], 
                tag = 'latest'
            )
        else :
            return Options(
        )

    def testOptions(self):
        """Test Options"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
