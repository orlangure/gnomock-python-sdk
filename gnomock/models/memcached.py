# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Memcached(object):
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
        'values': 'object',
        'byte_values': 'object',
        'version': 'str'
    }

    attribute_map = {
        'values': 'values',
        'byte_values': 'byteValues',
        'version': 'version'
    }

    def __init__(self, values=None, byte_values=None, version='latest', local_vars_configuration=None):  # noqa: E501
        """Memcached - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._byte_values = None
        self._version = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if byte_values is not None:
            self.byte_values = byte_values
        if version is not None:
            self.version = version

    @property
    def values(self):
        """Gets the values of this Memcached.  # noqa: E501

        A list of key/value pairs to create in the container.  # noqa: E501

        :return: The values of this Memcached.  # noqa: E501
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Memcached.

        A list of key/value pairs to create in the container.  # noqa: E501

        :param values: The values of this Memcached.  # noqa: E501
        :type: object
        """

        self._values = values

    @property
    def byte_values(self):
        """Gets the byte_values of this Memcached.  # noqa: E501

        A list of key/value pairs to create in the container. Values are base64 strings.  # noqa: E501

        :return: The byte_values of this Memcached.  # noqa: E501
        :rtype: object
        """
        return self._byte_values

    @byte_values.setter
    def byte_values(self, byte_values):
        """Sets the byte_values of this Memcached.

        A list of key/value pairs to create in the container. Values are base64 strings.  # noqa: E501

        :param byte_values: The byte_values of this Memcached.  # noqa: E501
        :type: object
        """

        self._byte_values = byte_values

    @property
    def version(self):
        """Gets the version of this Memcached.  # noqa: E501

        Docker image tag (version)  # noqa: E501

        :return: The version of this Memcached.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Memcached.

        Docker image tag (version)  # noqa: E501

        :param version: The version of this Memcached.  # noqa: E501
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
        if not isinstance(other, Memcached):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Memcached):
            return True

        return self.to_dict() != other.to_dict()
