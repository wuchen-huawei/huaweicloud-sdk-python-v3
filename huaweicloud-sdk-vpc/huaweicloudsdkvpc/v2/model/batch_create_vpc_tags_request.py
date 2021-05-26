# coding: utf-8

import pprint
import re

import six





class BatchCreateVpcTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'body': 'BatchCreateVpcTagsRequestBody'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'body': 'body'
    }

    def __init__(self, vpc_id=None, body=None):
        """BatchCreateVpcTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._vpc_id = None
        self._body = None
        self.discriminator = None

        self.vpc_id = vpc_id
        if body is not None:
            self.body = body

    @property
    def vpc_id(self):
        """Gets the vpc_id of this BatchCreateVpcTagsRequest.

        功能说明：虚拟私有云唯一标识 取值范围：合法UUID 约束：ID对应的VPC必须存在

        :return: The vpc_id of this BatchCreateVpcTagsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this BatchCreateVpcTagsRequest.

        功能说明：虚拟私有云唯一标识 取值范围：合法UUID 约束：ID对应的VPC必须存在

        :param vpc_id: The vpc_id of this BatchCreateVpcTagsRequest.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def body(self):
        """Gets the body of this BatchCreateVpcTagsRequest.


        :return: The body of this BatchCreateVpcTagsRequest.
        :rtype: BatchCreateVpcTagsRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchCreateVpcTagsRequest.


        :param body: The body of this BatchCreateVpcTagsRequest.
        :type: BatchCreateVpcTagsRequestBody
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
        if not isinstance(other, BatchCreateVpcTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
