# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.19.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Mssql(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'db': 'str',
        'password': 'str',
        'queries': 'list[str]',
        'queries_files': 'list[str]',
        'license': 'bool',
        'version': 'str'
    }

    attribute_map = {
        'db': 'db',
        'password': 'password',
        'queries': 'queries',
        'queries_files': 'queries_files',
        'license': 'license',
        'version': 'version'
    }

    def __init__(self, db='mydb', password='Gn0m!ck~', queries=None, queries_files=None, license=None, version='latest', local_vars_configuration=None):  # noqa: E501
        """Mssql - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._db = None
        self._password = None
        self._queries = None
        self._queries_files = None
        self._license = None
        self._version = None
        self.discriminator = None

        if db is not None:
            self.db = db
        if password is not None:
            self.password = password
        if queries is not None:
            self.queries = queries
        if queries_files is not None:
            self.queries_files = queries_files
        self.license = license
        if version is not None:
            self.version = version

    @property
    def db(self):
        """Gets the db of this Mssql.  # noqa: E501

        Database name to create.  # noqa: E501

        :return: The db of this Mssql.  # noqa: E501
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this Mssql.

        Database name to create.  # noqa: E501

        :param db: The db of this Mssql.  # noqa: E501
        :type: str
        """

        self._db = db

    @property
    def password(self):
        """Gets the password of this Mssql.  # noqa: E501

        Superuser password.  # noqa: E501

        :return: The password of this Mssql.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Mssql.

        Superuser password.  # noqa: E501

        :param password: The password of this Mssql.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def queries(self):
        """Gets the queries of this Mssql.  # noqa: E501

        A list of queries to execute while setting up the container.   # noqa: E501

        :return: The queries of this Mssql.  # noqa: E501
        :rtype: list[str]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this Mssql.

        A list of queries to execute while setting up the container.   # noqa: E501

        :param queries: The queries of this Mssql.  # noqa: E501
        :type: list[str]
        """

        self._queries = queries

    @property
    def queries_files(self):
        """Gets the queries_files of this Mssql.  # noqa: E501

        SQL files to execute while setting up container state.  # noqa: E501

        :return: The queries_files of this Mssql.  # noqa: E501
        :rtype: list[str]
        """
        return self._queries_files

    @queries_files.setter
    def queries_files(self, queries_files):
        """Sets the queries_files of this Mssql.

        SQL files to execute while setting up container state.  # noqa: E501

        :param queries_files: The queries_files of this Mssql.  # noqa: E501
        :type: list[str]
        """

        self._queries_files = queries_files

    @property
    def license(self):
        """Gets the license of this Mssql.  # noqa: E501

        Accept or decline Microsoft SQL Server license.  # noqa: E501

        :return: The license of this Mssql.  # noqa: E501
        :rtype: bool
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Mssql.

        Accept or decline Microsoft SQL Server license.  # noqa: E501

        :param license: The license of this Mssql.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and license is None:  # noqa: E501
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

    @property
    def version(self):
        """Gets the version of this Mssql.  # noqa: E501

        Docker image tag (version)  # noqa: E501

        :return: The version of this Mssql.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Mssql.

        Docker image tag (version)  # noqa: E501

        :param version: The version of this Mssql.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Mssql):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mssql):
            return True

        return self.to_dict() != other.to_dict()
