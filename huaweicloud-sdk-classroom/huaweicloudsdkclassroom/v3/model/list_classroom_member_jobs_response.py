# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListClassroomMemberJobsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'jobs': 'list[MemberJobCard]',
        'total': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'total': 'total'
    }

    def __init__(self, jobs=None, total=None):
        """ListClassroomMemberJobsResponse - a model defined in huaweicloud sdk"""
        
        super(ListClassroomMemberJobsResponse, self).__init__()

        self._jobs = None
        self._total = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if total is not None:
            self.total = total

    @property
    def jobs(self):
        """Gets the jobs of this ListClassroomMemberJobsResponse.

        课堂下作业列表信息

        :return: The jobs of this ListClassroomMemberJobsResponse.
        :rtype: list[MemberJobCard]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListClassroomMemberJobsResponse.

        课堂下作业列表信息

        :param jobs: The jobs of this ListClassroomMemberJobsResponse.
        :type: list[MemberJobCard]
        """
        self._jobs = jobs

    @property
    def total(self):
        """Gets the total of this ListClassroomMemberJobsResponse.

        学生作业总数

        :return: The total of this ListClassroomMemberJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListClassroomMemberJobsResponse.

        学生作业总数

        :param total: The total of this ListClassroomMemberJobsResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ListClassroomMemberJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
