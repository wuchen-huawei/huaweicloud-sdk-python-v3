# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListServerGroupsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_groups': 'list[ListServerGroupsResult]',
        'page_info': 'ListServerGroupsPageInfoResult'
    }

    attribute_map = {
        'server_groups': 'server_groups',
        'page_info': 'page_info'
    }

    def __init__(self, server_groups=None, page_info=None):
        """ListServerGroupsResponse - a model defined in huaweicloud sdk"""
        
        super(ListServerGroupsResponse, self).__init__()

        self._server_groups = None
        self._page_info = None
        self.discriminator = None

        if server_groups is not None:
            self.server_groups = server_groups
        if page_info is not None:
            self.page_info = page_info

    @property
    def server_groups(self):
        """Gets the server_groups of this ListServerGroupsResponse.

        弹性云服务器组信息

        :return: The server_groups of this ListServerGroupsResponse.
        :rtype: list[ListServerGroupsResult]
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this ListServerGroupsResponse.

        弹性云服务器组信息

        :param server_groups: The server_groups of this ListServerGroupsResponse.
        :type: list[ListServerGroupsResult]
        """
        self._server_groups = server_groups

    @property
    def page_info(self):
        """Gets the page_info of this ListServerGroupsResponse.


        :return: The page_info of this ListServerGroupsResponse.
        :rtype: ListServerGroupsPageInfoResult
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListServerGroupsResponse.


        :param page_info: The page_info of this ListServerGroupsResponse.
        :type: ListServerGroupsPageInfoResult
        """
        self._page_info = page_info

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
        if not isinstance(other, ListServerGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
