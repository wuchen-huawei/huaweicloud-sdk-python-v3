# coding: utf-8

import pprint
import re

import six





class AudioExtendSettings:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'output_policy': 'str',
        'channels': 'list[str]'
    }

    attribute_map = {
        'output_policy': 'output_policy',
        'channels': 'channels'
    }

    def __init__(self, output_policy=None, channels=None):
        """AudioExtendSettings - a model defined in huaweicloud sdk"""
        
        

        self._output_policy = None
        self._channels = None
        self.discriminator = None

        if output_policy is not None:
            self.output_policy = output_policy
        if channels is not None:
            self.channels = channels

    @property
    def output_policy(self):
        """Gets the output_policy of this AudioExtendSettings.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :return: The output_policy of this AudioExtendSettings.
        :rtype: str
        """
        return self._output_policy

    @output_policy.setter
    def output_policy(self, output_policy):
        """Sets the output_policy of this AudioExtendSettings.

        输出策略。  取值如下： - discard - transcode  >- 当视频参数中的“output_policy”为\"discard\"，且音频参数中的“output_policy”为“transcode”时，表示只输出音频。 >- 当视频参数中的“output_policy”为\"transcode\"，且音频参数中的“output_policy”为“discard”时，表示只输出视频。 >- 同时为\"discard\"时不合法。 >- 同时为“transcode”时，表示输出音视频。 

        :param output_policy: The output_policy of this AudioExtendSettings.
        :type: str
        """
        self._output_policy = output_policy

    @property
    def channels(self):
        """Gets the channels of this AudioExtendSettings.

        声道列表。用来覆盖模板组中的同名字段，如果不配置，则以模板组中的参数为准。 

        :return: The channels of this AudioExtendSettings.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioExtendSettings.

        声道列表。用来覆盖模板组中的同名字段，如果不配置，则以模板组中的参数为准。 

        :param channels: The channels of this AudioExtendSettings.
        :type: list[str]
        """
        self._channels = channels

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
        if not isinstance(other, AudioExtendSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
