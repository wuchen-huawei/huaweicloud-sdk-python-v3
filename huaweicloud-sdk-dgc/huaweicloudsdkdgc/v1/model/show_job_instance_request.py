# coding: utf-8

import pprint
import re

import six





class ShowJobInstanceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'instance_id': 'instance_id'
    }

    def __init__(self, job_name=None, instance_id=None):
        """ShowJobInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._job_name = None
        self._instance_id = None
        self.discriminator = None

        self.job_name = job_name
        self.instance_id = instance_id

    @property
    def job_name(self):
        """Gets the job_name of this ShowJobInstanceRequest.

        作业名称.

        :return: The job_name of this ShowJobInstanceRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowJobInstanceRequest.

        作业名称.

        :param job_name: The job_name of this ShowJobInstanceRequest.
        :type: str
        """
        self._job_name = job_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowJobInstanceRequest.

        作业实例id.

        :return: The instance_id of this ShowJobInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowJobInstanceRequest.

        作业实例id.

        :param instance_id: The instance_id of this ShowJobInstanceRequest.
        :type: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowJobInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
