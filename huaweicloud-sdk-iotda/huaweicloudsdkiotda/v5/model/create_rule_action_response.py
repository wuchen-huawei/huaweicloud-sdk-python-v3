# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateRuleActionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action_id': 'str',
        'rule_id': 'str',
        'app_id': 'str',
        'channel': 'str',
        'channel_detail': 'ChannelDetail',
        'batch': 'bool'
    }

    attribute_map = {
        'action_id': 'action_id',
        'rule_id': 'rule_id',
        'app_id': 'app_id',
        'channel': 'channel',
        'channel_detail': 'channel_detail',
        'batch': 'batch'
    }

    def __init__(self, action_id=None, rule_id=None, app_id=None, channel=None, channel_detail=None, batch=None):
        """CreateRuleActionResponse - a model defined in huaweicloud sdk"""
        
        super(CreateRuleActionResponse, self).__init__()

        self._action_id = None
        self._rule_id = None
        self._app_id = None
        self._channel = None
        self._channel_detail = None
        self._batch = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if rule_id is not None:
            self.rule_id = rule_id
        if app_id is not None:
            self.app_id = app_id
        if channel is not None:
            self.channel = channel
        if channel_detail is not None:
            self.channel_detail = channel_detail
        if batch is not None:
            self.batch = batch

    @property
    def action_id(self):
        """Gets the action_id of this CreateRuleActionResponse.

        规则动作ID，用于唯一标识一条规则动作，在创建规则动作时由物联网平台分配获得，创建时无需携带，由平台统一分配唯一的action_id。

        :return: The action_id of this CreateRuleActionResponse.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this CreateRuleActionResponse.

        规则动作ID，用于唯一标识一条规则动作，在创建规则动作时由物联网平台分配获得，创建时无需携带，由平台统一分配唯一的action_id。

        :param action_id: The action_id of this CreateRuleActionResponse.
        :type: str
        """
        self._action_id = action_id

    @property
    def rule_id(self):
        """Gets the rule_id of this CreateRuleActionResponse.

        规则动作对应的的规则触发条件ID。

        :return: The rule_id of this CreateRuleActionResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CreateRuleActionResponse.

        规则动作对应的的规则触发条件ID。

        :param rule_id: The rule_id of this CreateRuleActionResponse.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def app_id(self):
        """Gets the app_id of this CreateRuleActionResponse.

        资源空间ID。

        :return: The app_id of this CreateRuleActionResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateRuleActionResponse.

        资源空间ID。

        :param app_id: The app_id of this CreateRuleActionResponse.
        :type: str
        """
        self._app_id = app_id

    @property
    def channel(self):
        """Gets the channel of this CreateRuleActionResponse.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。 

        :return: The channel of this CreateRuleActionResponse.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CreateRuleActionResponse.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - DIS_FORWARDING：转发DIS服务消息类型。 - OBS_FORWARDING：转发OBS服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 - DMS_KAFKA_FORWARDING：转发kafka消息类型。 

        :param channel: The channel of this CreateRuleActionResponse.
        :type: str
        """
        self._channel = channel

    @property
    def channel_detail(self):
        """Gets the channel_detail of this CreateRuleActionResponse.


        :return: The channel_detail of this CreateRuleActionResponse.
        :rtype: ChannelDetail
        """
        return self._channel_detail

    @channel_detail.setter
    def channel_detail(self, channel_detail):
        """Sets the channel_detail of this CreateRuleActionResponse.


        :param channel_detail: The channel_detail of this CreateRuleActionResponse.
        :type: ChannelDetail
        """
        self._channel_detail = channel_detail

    @property
    def batch(self):
        """Gets the batch of this CreateRuleActionResponse.

        是否支持批量接收推送消息。

        :return: The batch of this CreateRuleActionResponse.
        :rtype: bool
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this CreateRuleActionResponse.

        是否支持批量接收推送消息。

        :param batch: The batch of this CreateRuleActionResponse.
        :type: bool
        """
        self._batch = batch

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
        if not isinstance(other, CreateRuleActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
