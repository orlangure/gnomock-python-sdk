# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Localstack(object):
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
        'services': 'list[str]',
        's3_path': 'str'
    }

    attribute_map = {
        'services': 'services',
        's3_path': 's3_path'
    }

    def __init__(self, services=None, s3_path=None, local_vars_configuration=None):  # noqa: E501
        """Localstack - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._services = None
        self._s3_path = None
        self.discriminator = None

        self.services = services
        if s3_path is not None:
            self.s3_path = s3_path

    @property
    def services(self):
        """Gets the services of this Localstack.  # noqa: E501

        A list of localstack services to start  # noqa: E501

        :return: The services of this Localstack.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Localstack.

        A list of localstack services to start  # noqa: E501

        :param services: The services of this Localstack.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and services is None:  # noqa: E501
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501
        allowed_values = ["apigateway", "cloudformation", "cloudwatch", "logs", "events", "dynamodb", "dynamodbstreams", "ec2", "es", "firehose", "iam", "kinesis", "kms", "lambda", "redshift", "route53", "s3", "secretsmanager", "ses", "sns", "sqs", "ssm", "sts", "stepfunctions"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(services).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `services` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(services) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._services = services

    @property
    def s3_path(self):
        """Gets the s3_path of this Localstack.  # noqa: E501

        Path to folder to setup initial S3 state. Top level folders are used as buckets; all child folders and files are uploaded as-is   # noqa: E501

        :return: The s3_path of this Localstack.  # noqa: E501
        :rtype: str
        """
        return self._s3_path

    @s3_path.setter
    def s3_path(self, s3_path):
        """Sets the s3_path of this Localstack.

        Path to folder to setup initial S3 state. Top level folders are used as buckets; all child folders and files are uploaded as-is   # noqa: E501

        :param s3_path: The s3_path of this Localstack.  # noqa: E501
        :type: str
        """

        self._s3_path = s3_path

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
        if not isinstance(other, Localstack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Localstack):
            return True

        return self.to_dict() != other.to_dict()
