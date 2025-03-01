# coding: utf-8

import pprint
import re

import six





class ListRoutingRulesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'resource': 'str',
        'event': 'str',
        'app_type': 'str',
        'app_id': 'str',
        'rule_name': 'str',
        'limit': 'int',
        'marker': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'resource': 'resource',
        'event': 'event',
        'app_type': 'app_type',
        'app_id': 'app_id',
        'rule_name': 'rule_name',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, resource=None, event=None, app_type=None, app_id=None, rule_name=None, limit=None, marker=None, offset=None):
        """ListRoutingRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._resource = None
        self._event = None
        self._app_type = None
        self._app_id = None
        self._rule_name = None
        self._limit = None
        self._marker = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if resource is not None:
            self.resource = resource
        if event is not None:
            self.event = event
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id
        if rule_name is not None:
            self.rule_name = rule_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRoutingRulesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRoutingRulesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ListRoutingRulesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def resource(self):
        """Gets the resource of this ListRoutingRulesRequest.

        订阅的资源名称： - device：设备。 - device.property：设备属性。 - device.message：设备消息。 - device.message.status：设备消息状态。 - device.status：设备状态。 - batchtask：批量任务。 - product：产品。 - device.command.status：设备异步命令状态。 

        :return: The resource of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ListRoutingRulesRequest.

        订阅的资源名称： - device：设备。 - device.property：设备属性。 - device.message：设备消息。 - device.message.status：设备消息状态。 - device.status：设备状态。 - batchtask：批量任务。 - product：产品。 - device.command.status：设备异步命令状态。 

        :param resource: The resource of this ListRoutingRulesRequest.
        :type: str
        """
        self._resource = resource

    @property
    def event(self):
        """Gets the event of this ListRoutingRulesRequest.

        订阅的资源事件，取值范围：与资源有关，不同的资源，事件不同 event需要与resource关联使用，具体的“resource：event”映射关系如下： - device：create（设备添加） - device：delete（设备删除） - device：update（设备更新） - device.status：update （设备状态变更） - device.property：report（设备属性上报） - device.message：report（设备消息上报） - device.message.status：update（设备消息状态变更） - batchtask：update （批量任务状态变更） - product：create（产品添加） - product：delete（产品删除） - product：update（产品更新） - device.command.status：update（设备异步命令状态更新）。 

        :return: The event of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this ListRoutingRulesRequest.

        订阅的资源事件，取值范围：与资源有关，不同的资源，事件不同 event需要与resource关联使用，具体的“resource：event”映射关系如下： - device：create（设备添加） - device：delete（设备删除） - device：update（设备更新） - device.status：update （设备状态变更） - device.property：report（设备属性上报） - device.message：report（设备消息上报） - device.message.status：update（设备消息状态变更） - batchtask：update （批量任务状态变更） - product：create（产品添加） - product：delete（产品删除） - product：update（产品更新） - device.command.status：update（设备异步命令状态更新）。 

        :param event: The event of this ListRoutingRulesRequest.
        :type: str
        """
        self._event = event

    @property
    def app_type(self):
        """Gets the app_type of this ListRoutingRulesRequest.

        租户规则的生效范围，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。如果类型为APP，可携带app_id查询指定资源空间下的规则动作列表，不携带app_id则查询[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下的规则列表。 

        :return: The app_type of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ListRoutingRulesRequest.

        租户规则的生效范围，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。如果类型为APP，可携带app_id查询指定资源空间下的规则动作列表，不携带app_id则查询[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下的规则列表。 

        :param app_type: The app_type of this ListRoutingRulesRequest.
        :type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this ListRoutingRulesRequest.

        资源空间ID。此参数为非必选参数，携带app_id查询指定资源空间下的规则动作列表，不携带app_id则查询[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下的规则动作列表。

        :return: The app_id of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRoutingRulesRequest.

        资源空间ID。此参数为非必选参数，携带app_id查询指定资源空间下的规则动作列表，不携带app_id则查询[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下的规则动作列表。

        :param app_id: The app_id of this ListRoutingRulesRequest.
        :type: str
        """
        self._app_id = app_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ListRoutingRulesRequest.

        用户自定义的规则名称

        :return: The rule_name of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ListRoutingRulesRequest.

        用户自定义的规则名称

        :param rule_name: The rule_name of this ListRoutingRulesRequest.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def limit(self):
        """Gets the limit of this ListRoutingRulesRequest.

        分页查询时每页显示的记录数。默认每页10条记录，最大设定每页50条记录，取值范围为1-50的整数。

        :return: The limit of this ListRoutingRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRoutingRulesRequest.

        分页查询时每页显示的记录数。默认每页10条记录，最大设定每页50条记录，取值范围为1-50的整数。

        :param limit: The limit of this ListRoutingRulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListRoutingRulesRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 

        :return: The marker of this ListRoutingRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRoutingRulesRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。 

        :param marker: The marker of this ListRoutingRulesRequest.
        :type: str
        """
        self._marker = marker

    @property
    def offset(self):
        """Gets the offset of this ListRoutingRulesRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。 - 限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :return: The offset of this ListRoutingRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRoutingRulesRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。 - 限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :param offset: The offset of this ListRoutingRulesRequest.
        :type: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRoutingRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
