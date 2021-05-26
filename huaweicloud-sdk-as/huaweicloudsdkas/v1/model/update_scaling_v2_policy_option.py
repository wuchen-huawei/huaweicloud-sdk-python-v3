# coding: utf-8

import pprint
import re

import six





class UpdateScalingV2PolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_policy_name': 'str',
        'scaling_resource_id': 'str',
        'scaling_resource_type': 'str',
        'scaling_policy_type': 'str',
        'alarm_id': 'str',
        'scheduled_policy': 'ScheduledPolicy',
        'scaling_policy_action': 'ScalingPolicyActionV2',
        'cool_down_time': 'int'
    }

    attribute_map = {
        'scaling_policy_name': 'scaling_policy_name',
        'scaling_resource_id': 'scaling_resource_id',
        'scaling_resource_type': 'scaling_resource_type',
        'scaling_policy_type': 'scaling_policy_type',
        'alarm_id': 'alarm_id',
        'scheduled_policy': 'scheduled_policy',
        'scaling_policy_action': 'scaling_policy_action',
        'cool_down_time': 'cool_down_time'
    }

    def __init__(self, scaling_policy_name=None, scaling_resource_id=None, scaling_resource_type=None, scaling_policy_type=None, alarm_id=None, scheduled_policy=None, scaling_policy_action=None, cool_down_time=None):
        """UpdateScalingV2PolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._scaling_policy_name = None
        self._scaling_resource_id = None
        self._scaling_resource_type = None
        self._scaling_policy_type = None
        self._alarm_id = None
        self._scheduled_policy = None
        self._scaling_policy_action = None
        self._cool_down_time = None
        self.discriminator = None

        if scaling_policy_name is not None:
            self.scaling_policy_name = scaling_policy_name
        if scaling_resource_id is not None:
            self.scaling_resource_id = scaling_resource_id
        if scaling_resource_type is not None:
            self.scaling_resource_type = scaling_resource_type
        if scaling_policy_type is not None:
            self.scaling_policy_type = scaling_policy_type
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if scheduled_policy is not None:
            self.scheduled_policy = scheduled_policy
        if scaling_policy_action is not None:
            self.scaling_policy_action = scaling_policy_action
        if cool_down_time is not None:
            self.cool_down_time = cool_down_time

    @property
    def scaling_policy_name(self):
        """Gets the scaling_policy_name of this UpdateScalingV2PolicyOption.

        策略名称（1-64）字符，可以用中文、字母、数字、下划线、中划线的组合。

        :return: The scaling_policy_name of this UpdateScalingV2PolicyOption.
        :rtype: str
        """
        return self._scaling_policy_name

    @scaling_policy_name.setter
    def scaling_policy_name(self, scaling_policy_name):
        """Sets the scaling_policy_name of this UpdateScalingV2PolicyOption.

        策略名称（1-64）字符，可以用中文、字母、数字、下划线、中划线的组合。

        :param scaling_policy_name: The scaling_policy_name of this UpdateScalingV2PolicyOption.
        :type: str
        """
        self._scaling_policy_name = scaling_policy_name

    @property
    def scaling_resource_id(self):
        """Gets the scaling_resource_id of this UpdateScalingV2PolicyOption.

        伸缩资源ID，伸缩组唯一标识或带宽唯一标识。如果scaling_resource_type为SCALING_GROUP，对应伸缩组唯一标识。如果scaling_resource_type为BANDWIDTH，对应带宽唯一标识。

        :return: The scaling_resource_id of this UpdateScalingV2PolicyOption.
        :rtype: str
        """
        return self._scaling_resource_id

    @scaling_resource_id.setter
    def scaling_resource_id(self, scaling_resource_id):
        """Sets the scaling_resource_id of this UpdateScalingV2PolicyOption.

        伸缩资源ID，伸缩组唯一标识或带宽唯一标识。如果scaling_resource_type为SCALING_GROUP，对应伸缩组唯一标识。如果scaling_resource_type为BANDWIDTH，对应带宽唯一标识。

        :param scaling_resource_id: The scaling_resource_id of this UpdateScalingV2PolicyOption.
        :type: str
        """
        self._scaling_resource_id = scaling_resource_id

    @property
    def scaling_resource_type(self):
        """Gets the scaling_resource_type of this UpdateScalingV2PolicyOption.

        伸缩资源类型。伸缩组：SCALING_GROUP。带宽：BANDWIDTH。

        :return: The scaling_resource_type of this UpdateScalingV2PolicyOption.
        :rtype: str
        """
        return self._scaling_resource_type

    @scaling_resource_type.setter
    def scaling_resource_type(self, scaling_resource_type):
        """Sets the scaling_resource_type of this UpdateScalingV2PolicyOption.

        伸缩资源类型。伸缩组：SCALING_GROUP。带宽：BANDWIDTH。

        :param scaling_resource_type: The scaling_resource_type of this UpdateScalingV2PolicyOption.
        :type: str
        """
        self._scaling_resource_type = scaling_resource_type

    @property
    def scaling_policy_type(self):
        """Gets the scaling_policy_type of this UpdateScalingV2PolicyOption.

        策略类型。告警策略：ALARM（与alarm_id对应）；定时策略：SCHEDULED（与scheduled_policy对应）；周期策略：RECURRENCE（与scheduled_policy对应）

        :return: The scaling_policy_type of this UpdateScalingV2PolicyOption.
        :rtype: str
        """
        return self._scaling_policy_type

    @scaling_policy_type.setter
    def scaling_policy_type(self, scaling_policy_type):
        """Sets the scaling_policy_type of this UpdateScalingV2PolicyOption.

        策略类型。告警策略：ALARM（与alarm_id对应）；定时策略：SCHEDULED（与scheduled_policy对应）；周期策略：RECURRENCE（与scheduled_policy对应）

        :param scaling_policy_type: The scaling_policy_type of this UpdateScalingV2PolicyOption.
        :type: str
        """
        self._scaling_policy_type = scaling_policy_type

    @property
    def alarm_id(self):
        """Gets the alarm_id of this UpdateScalingV2PolicyOption.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :return: The alarm_id of this UpdateScalingV2PolicyOption.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this UpdateScalingV2PolicyOption.

        告警ID，即告警规则的ID，当scaling_policy_type为ALARM时该项必选，此时scheduled_policy不生效。创建告警策略成功后，会自动为该告警ID对应的告警规则的alarm_actions字段增加类型为autoscaling的告警触发动作。告警ID通过查询云监控告警规则列表获取，详见《云监控API参考》的“查询告警规则列表”。

        :param alarm_id: The alarm_id of this UpdateScalingV2PolicyOption.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def scheduled_policy(self):
        """Gets the scheduled_policy of this UpdateScalingV2PolicyOption.


        :return: The scheduled_policy of this UpdateScalingV2PolicyOption.
        :rtype: ScheduledPolicy
        """
        return self._scheduled_policy

    @scheduled_policy.setter
    def scheduled_policy(self, scheduled_policy):
        """Sets the scheduled_policy of this UpdateScalingV2PolicyOption.


        :param scheduled_policy: The scheduled_policy of this UpdateScalingV2PolicyOption.
        :type: ScheduledPolicy
        """
        self._scheduled_policy = scheduled_policy

    @property
    def scaling_policy_action(self):
        """Gets the scaling_policy_action of this UpdateScalingV2PolicyOption.


        :return: The scaling_policy_action of this UpdateScalingV2PolicyOption.
        :rtype: ScalingPolicyActionV2
        """
        return self._scaling_policy_action

    @scaling_policy_action.setter
    def scaling_policy_action(self, scaling_policy_action):
        """Sets the scaling_policy_action of this UpdateScalingV2PolicyOption.


        :param scaling_policy_action: The scaling_policy_action of this UpdateScalingV2PolicyOption.
        :type: ScalingPolicyActionV2
        """
        self._scaling_policy_action = scaling_policy_action

    @property
    def cool_down_time(self):
        """Gets the cool_down_time of this UpdateScalingV2PolicyOption.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :return: The cool_down_time of this UpdateScalingV2PolicyOption.
        :rtype: int
        """
        return self._cool_down_time

    @cool_down_time.setter
    def cool_down_time(self, cool_down_time):
        """Sets the cool_down_time of this UpdateScalingV2PolicyOption.

        冷却时间，取值范围0-86400，默认为300，单位是秒。

        :param cool_down_time: The cool_down_time of this UpdateScalingV2PolicyOption.
        :type: int
        """
        self._cool_down_time = cool_down_time

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
        if not isinstance(other, UpdateScalingV2PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
