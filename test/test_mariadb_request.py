# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gnomock
from gnomock.models.mariadb_request import MariadbRequest  # noqa: E501
from gnomock.rest import ApiException

class TestMariadbRequest(unittest.TestCase):
    """MariadbRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MariadbRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gnomock.models.mariadb_request.MariadbRequest()  # noqa: E501
        if include_optional :
            return MariadbRequest(
                preset = gnomock.models.mariadb.Mariadb(
                    db = 'mydb', 
                    user = 'gnomock', 
                    password = 'gnoria', 
                    queries = ["create table foo(bar int)","insert into foo(bar) values(1)"], 
                    queries_files = ["/home/gnomock/project/testdata/mysql/queries.sql"], 
                    version = 'latest', ), 
                options = gnomock.models.options.Options(
                    timeout = 60000000000, 
                    env = [
                        'ENV_VAR_NAME=some-value'
                        ], 
                    debug = True, 
                    container_name = 'gnomock', )
            )
        else :
            return MariadbRequest(
        )

    def testMariadbRequest(self):
        """Test MariadbRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
