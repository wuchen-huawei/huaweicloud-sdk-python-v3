# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowTemplateDetailResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'is_build_in': 'bool',
        'region': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'is_watch': 'bool',
        'description': 'str',
        'parameter': 'list[TemplateParam]',
        'flow': 'object',
        'states': 'object'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'is_build_in': 'is_build_in',
        'region': 'region',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'is_watch': 'is_watch',
        'description': 'description',
        'parameter': 'parameter',
        'flow': 'flow',
        'states': 'states'
    }

    def __init__(self, template_id=None, template_name=None, template_type=None, user_id=None, user_name=None, domain_id=None, domain_name=None, is_build_in=None, region=None, project_id=None, project_name=None, is_watch=None, description=None, parameter=None, flow=None, states=None):
        """ShowTemplateDetailResponse - a model defined in huaweicloud sdk"""
        
        super(ShowTemplateDetailResponse, self).__init__()

        self._template_id = None
        self._template_name = None
        self._template_type = None
        self._user_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._is_build_in = None
        self._region = None
        self._project_id = None
        self._project_name = None
        self._is_watch = None
        self._description = None
        self._parameter = None
        self._flow = None
        self._states = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if is_build_in is not None:
            self.is_build_in = is_build_in
        if region is not None:
            self.region = region
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if is_watch is not None:
            self.is_watch = is_watch
        if description is not None:
            self.description = description
        if parameter is not None:
            self.parameter = parameter
        if flow is not None:
            self.flow = flow
        if states is not None:
            self.states = states

    @property
    def template_id(self):
        """Gets the template_id of this ShowTemplateDetailResponse.

        模板ID

        :return: The template_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowTemplateDetailResponse.

        模板ID

        :param template_id: The template_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this ShowTemplateDetailResponse.

        模板名字

        :return: The template_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ShowTemplateDetailResponse.

        模板名字

        :param template_name: The template_name of this ShowTemplateDetailResponse.
        :type: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        """Gets the template_type of this ShowTemplateDetailResponse.

        模板类型

        :return: The template_type of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ShowTemplateDetailResponse.

        模板类型

        :param template_type: The template_type of this ShowTemplateDetailResponse.
        :type: str
        """
        self._template_type = template_type

    @property
    def user_id(self):
        """Gets the user_id of this ShowTemplateDetailResponse.

        用户ID

        :return: The user_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowTemplateDetailResponse.

        用户ID

        :param user_id: The user_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowTemplateDetailResponse.

        用户名字

        :return: The user_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowTemplateDetailResponse.

        用户名字

        :param user_name: The user_name of this ShowTemplateDetailResponse.
        :type: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowTemplateDetailResponse.

        租户ID

        :return: The domain_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowTemplateDetailResponse.

        租户ID

        :param domain_id: The domain_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowTemplateDetailResponse.

        租户名字

        :return: The domain_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowTemplateDetailResponse.

        租户名字

        :param domain_name: The domain_name of this ShowTemplateDetailResponse.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def is_build_in(self):
        """Gets the is_build_in of this ShowTemplateDetailResponse.

        是否内置模板

        :return: The is_build_in of this ShowTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_build_in

    @is_build_in.setter
    def is_build_in(self, is_build_in):
        """Sets the is_build_in of this ShowTemplateDetailResponse.

        是否内置模板

        :param is_build_in: The is_build_in of this ShowTemplateDetailResponse.
        :type: bool
        """
        self._is_build_in = is_build_in

    @property
    def region(self):
        """Gets the region of this ShowTemplateDetailResponse.

        region

        :return: The region of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowTemplateDetailResponse.

        region

        :param region: The region of this ShowTemplateDetailResponse.
        :type: str
        """
        self._region = region

    @property
    def project_id(self):
        """Gets the project_id of this ShowTemplateDetailResponse.

        项目ID

        :return: The project_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowTemplateDetailResponse.

        项目ID

        :param project_id: The project_id of this ShowTemplateDetailResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowTemplateDetailResponse.

        项目名字

        :return: The project_name of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowTemplateDetailResponse.

        项目名字

        :param project_name: The project_name of this ShowTemplateDetailResponse.
        :type: str
        """
        self._project_name = project_name

    @property
    def is_watch(self):
        """Gets the is_watch of this ShowTemplateDetailResponse.

        是否关注

        :return: The is_watch of this ShowTemplateDetailResponse.
        :rtype: bool
        """
        return self._is_watch

    @is_watch.setter
    def is_watch(self, is_watch):
        """Sets the is_watch of this ShowTemplateDetailResponse.

        是否关注

        :param is_watch: The is_watch of this ShowTemplateDetailResponse.
        :type: bool
        """
        self._is_watch = is_watch

    @property
    def description(self):
        """Gets the description of this ShowTemplateDetailResponse.

        模板描述

        :return: The description of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowTemplateDetailResponse.

        模板描述

        :param description: The description of this ShowTemplateDetailResponse.
        :type: str
        """
        self._description = description

    @property
    def parameter(self):
        """Gets the parameter of this ShowTemplateDetailResponse.

        模板参数

        :return: The parameter of this ShowTemplateDetailResponse.
        :rtype: list[TemplateParam]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ShowTemplateDetailResponse.

        模板参数

        :param parameter: The parameter of this ShowTemplateDetailResponse.
        :type: list[TemplateParam]
        """
        self._parameter = parameter

    @property
    def flow(self):
        """Gets the flow of this ShowTemplateDetailResponse.

        编排flow，map类型数据

        :return: The flow of this ShowTemplateDetailResponse.
        :rtype: object
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this ShowTemplateDetailResponse.

        编排flow，map类型数据

        :param flow: The flow of this ShowTemplateDetailResponse.
        :type: object
        """
        self._flow = flow

    @property
    def states(self):
        """Gets the states of this ShowTemplateDetailResponse.

        子任务states，map类型数据

        :return: The states of this ShowTemplateDetailResponse.
        :rtype: object
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this ShowTemplateDetailResponse.

        子任务states，map类型数据

        :param states: The states of this ShowTemplateDetailResponse.
        :type: object
        """
        self._states = states

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
        if not isinstance(other, ShowTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
