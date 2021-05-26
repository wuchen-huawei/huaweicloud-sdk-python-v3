# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBuiltInPolicyDefinitionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'policy_type': 'str',
        'description': 'str',
        'policy_rule_type': 'str',
        'policy_rule': 'object',
        'keywords': 'list[str]',
        'parameters': 'dict(str, PolicyParameterDefinition)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'policy_type': 'policy_type',
        'description': 'description',
        'policy_rule_type': 'policy_rule_type',
        'policy_rule': 'policy_rule',
        'keywords': 'keywords',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, name=None, policy_type=None, description=None, policy_rule_type=None, policy_rule=None, keywords=None, parameters=None):
        """ShowBuiltInPolicyDefinitionResponse - a model defined in huaweicloud sdk"""
        
        super(ShowBuiltInPolicyDefinitionResponse, self).__init__()

        self._id = None
        self._name = None
        self._policy_type = None
        self._description = None
        self._policy_rule_type = None
        self._policy_rule = None
        self._keywords = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policy_type is not None:
            self.policy_type = policy_type
        if description is not None:
            self.description = description
        if policy_rule_type is not None:
            self.policy_rule_type = policy_rule_type
        if policy_rule is not None:
            self.policy_rule = policy_rule
        if keywords is not None:
            self.keywords = keywords
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this ShowBuiltInPolicyDefinitionResponse.

        策略id

        :return: The id of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowBuiltInPolicyDefinitionResponse.

        策略id

        :param id: The id of this ShowBuiltInPolicyDefinitionResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowBuiltInPolicyDefinitionResponse.

        策略名字

        :return: The name of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowBuiltInPolicyDefinitionResponse.

        策略名字

        :param name: The name of this ShowBuiltInPolicyDefinitionResponse.
        :type: str
        """
        self._name = name

    @property
    def policy_type(self):
        """Gets the policy_type of this ShowBuiltInPolicyDefinitionResponse.

        策略类型

        :return: The policy_type of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this ShowBuiltInPolicyDefinitionResponse.

        策略类型

        :param policy_type: The policy_type of this ShowBuiltInPolicyDefinitionResponse.
        :type: str
        """
        self._policy_type = policy_type

    @property
    def description(self):
        """Gets the description of this ShowBuiltInPolicyDefinitionResponse.

        策略描述

        :return: The description of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowBuiltInPolicyDefinitionResponse.

        策略描述

        :param description: The description of this ShowBuiltInPolicyDefinitionResponse.
        :type: str
        """
        self._description = description

    @property
    def policy_rule_type(self):
        """Gets the policy_rule_type of this ShowBuiltInPolicyDefinitionResponse.

        策略语法类型

        :return: The policy_rule_type of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: str
        """
        return self._policy_rule_type

    @policy_rule_type.setter
    def policy_rule_type(self, policy_rule_type):
        """Sets the policy_rule_type of this ShowBuiltInPolicyDefinitionResponse.

        策略语法类型

        :param policy_rule_type: The policy_rule_type of this ShowBuiltInPolicyDefinitionResponse.
        :type: str
        """
        self._policy_rule_type = policy_rule_type

    @property
    def policy_rule(self):
        """Gets the policy_rule of this ShowBuiltInPolicyDefinitionResponse.

        策略规则

        :return: The policy_rule of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: object
        """
        return self._policy_rule

    @policy_rule.setter
    def policy_rule(self, policy_rule):
        """Sets the policy_rule of this ShowBuiltInPolicyDefinitionResponse.

        策略规则

        :param policy_rule: The policy_rule of this ShowBuiltInPolicyDefinitionResponse.
        :type: object
        """
        self._policy_rule = policy_rule

    @property
    def keywords(self):
        """Gets the keywords of this ShowBuiltInPolicyDefinitionResponse.

        关键词列表

        :return: The keywords of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this ShowBuiltInPolicyDefinitionResponse.

        关键词列表

        :param keywords: The keywords of this ShowBuiltInPolicyDefinitionResponse.
        :type: list[str]
        """
        self._keywords = keywords

    @property
    def parameters(self):
        """Gets the parameters of this ShowBuiltInPolicyDefinitionResponse.

        策略参数

        :return: The parameters of this ShowBuiltInPolicyDefinitionResponse.
        :rtype: dict(str, PolicyParameterDefinition)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ShowBuiltInPolicyDefinitionResponse.

        策略参数

        :param parameters: The parameters of this ShowBuiltInPolicyDefinitionResponse.
        :type: dict(str, PolicyParameterDefinition)
        """
        self._parameters = parameters

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
        if not isinstance(other, ShowBuiltInPolicyDefinitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
