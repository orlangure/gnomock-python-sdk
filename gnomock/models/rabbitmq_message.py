# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class RabbitmqMessage(object):
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
        'queue': 'str',
        'content_type': 'str',
        'string_body': 'str',
        'body': 'str'
    }

    attribute_map = {
        'queue': 'queue',
        'content_type': 'content_type',
        'string_body': 'string_body',
        'body': 'body'
    }

    def __init__(self, queue=None, content_type=None, string_body=None, body=None, local_vars_configuration=None):  # noqa: E501
        """RabbitmqMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queue = None
        self._content_type = None
        self._string_body = None
        self._body = None
        self.discriminator = None

        if queue is not None:
            self.queue = queue
        if content_type is not None:
            self.content_type = content_type
        if string_body is not None:
            self.string_body = string_body
        if body is not None:
            self.body = body

    @property
    def queue(self):
        """Gets the queue of this RabbitmqMessage.  # noqa: E501


        :return: The queue of this RabbitmqMessage.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this RabbitmqMessage.


        :param queue: The queue of this RabbitmqMessage.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def content_type(self):
        """Gets the content_type of this RabbitmqMessage.  # noqa: E501


        :return: The content_type of this RabbitmqMessage.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this RabbitmqMessage.


        :param content_type: The content_type of this RabbitmqMessage.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def string_body(self):
        """Gets the string_body of this RabbitmqMessage.  # noqa: E501


        :return: The string_body of this RabbitmqMessage.  # noqa: E501
        :rtype: str
        """
        return self._string_body

    @string_body.setter
    def string_body(self, string_body):
        """Sets the string_body of this RabbitmqMessage.


        :param string_body: The string_body of this RabbitmqMessage.  # noqa: E501
        :type: str
        """

        self._string_body = string_body

    @property
    def body(self):
        """Gets the body of this RabbitmqMessage.  # noqa: E501


        :return: The body of this RabbitmqMessage.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RabbitmqMessage.


        :param body: The body of this RabbitmqMessage.  # noqa: E501
        :type: str
        """

        self._body = body

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
        if not isinstance(other, RabbitmqMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RabbitmqMessage):
            return True

        return self.to_dict() != other.to_dict()