# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateAddonInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'Metadata',
        'spec': 'InstanceSpec',
        'status': 'AddonInstanceStatus'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, spec=None, status=None):
        """CreateAddonInstanceResponse - a model defined in huaweicloud sdk"""
        
        super(CreateAddonInstanceResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def kind(self):
        """Gets the kind of this CreateAddonInstanceResponse.

        API类型，固定值“Addon”，该值不可修改。

        :return: The kind of this CreateAddonInstanceResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this CreateAddonInstanceResponse.

        API类型，固定值“Addon”，该值不可修改。

        :param kind: The kind of this CreateAddonInstanceResponse.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this CreateAddonInstanceResponse.

        API版本，固定值“v3”，该值不可修改。

        :return: The api_version of this CreateAddonInstanceResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CreateAddonInstanceResponse.

        API版本，固定值“v3”，该值不可修改。

        :param api_version: The api_version of this CreateAddonInstanceResponse.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """Gets the metadata of this CreateAddonInstanceResponse.


        :return: The metadata of this CreateAddonInstanceResponse.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateAddonInstanceResponse.


        :param metadata: The metadata of this CreateAddonInstanceResponse.
        :type: Metadata
        """
        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this CreateAddonInstanceResponse.


        :return: The spec of this CreateAddonInstanceResponse.
        :rtype: InstanceSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CreateAddonInstanceResponse.


        :param spec: The spec of this CreateAddonInstanceResponse.
        :type: InstanceSpec
        """
        self._spec = spec

    @property
    def status(self):
        """Gets the status of this CreateAddonInstanceResponse.


        :return: The status of this CreateAddonInstanceResponse.
        :rtype: AddonInstanceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateAddonInstanceResponse.


        :param status: The status of this CreateAddonInstanceResponse.
        :type: AddonInstanceStatus
        """
        self._status = status

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, CreateAddonInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
