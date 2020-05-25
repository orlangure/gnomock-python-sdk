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
from gnomock.models.splunk import Splunk  # noqa: E501
from gnomock.rest import ApiException

class TestSplunk(unittest.TestCase):
    """Splunk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Splunk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gnomock.models.splunk.Splunk()  # noqa: E501
        if include_optional :
            return Splunk(
                values = [
                    gnomock.models.splunk_values.SplunkValues(
                        event = 'something happened', 
                        index = 'main', 
                        source = 'web', 
                        sourcetype = 'http', 
                        time = 1588269752, )
                    ], 
                values_file = '/home/gnomock/project/testdata/splunk/events.jsonl', 
                accept_license = True, 
                admin_password = 'p@s$w0rD', 
                version = '8.0.2.1'
            )
        else :
            return Splunk(
                accept_license = True,
                admin_password = 'p@s$w0rD',
        )

    def testSplunk(self):
        """Test Splunk"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
