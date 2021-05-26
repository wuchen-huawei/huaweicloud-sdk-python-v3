# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateNewBlockchainResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'blockchain_name': 'str',
        'operation_id': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'blockchain_name': 'blockchain_name',
        'operation_id': 'operation_id'
    }

    def __init__(self, blockchain_id=None, blockchain_name=None, operation_id=None):
        """CreateNewBlockchainResponse - a model defined in huaweicloud sdk"""
        
        super(CreateNewBlockchainResponse, self).__init__()

        self._blockchain_id = None
        self._blockchain_name = None
        self._operation_id = None
        self.discriminator = None

        if blockchain_id is not None:
            self.blockchain_id = blockchain_id
        if blockchain_name is not None:
            self.blockchain_name = blockchain_name
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this CreateNewBlockchainResponse.

        服务实例ID

        :return: The blockchain_id of this CreateNewBlockchainResponse.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this CreateNewBlockchainResponse.

        服务实例ID

        :param blockchain_id: The blockchain_id of this CreateNewBlockchainResponse.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def blockchain_name(self):
        """Gets the blockchain_name of this CreateNewBlockchainResponse.

        服务实例名

        :return: The blockchain_name of this CreateNewBlockchainResponse.
        :rtype: str
        """
        return self._blockchain_name

    @blockchain_name.setter
    def blockchain_name(self, blockchain_name):
        """Sets the blockchain_name of this CreateNewBlockchainResponse.

        服务实例名

        :param blockchain_name: The blockchain_name of this CreateNewBlockchainResponse.
        :type: str
        """
        self._blockchain_name = blockchain_name

    @property
    def operation_id(self):
        """Gets the operation_id of this CreateNewBlockchainResponse.

        操作ID

        :return: The operation_id of this CreateNewBlockchainResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this CreateNewBlockchainResponse.

        操作ID

        :param operation_id: The operation_id of this CreateNewBlockchainResponse.
        :type: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, CreateNewBlockchainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
