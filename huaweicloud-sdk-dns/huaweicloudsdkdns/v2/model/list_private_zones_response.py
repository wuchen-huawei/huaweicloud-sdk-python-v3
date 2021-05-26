# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPrivateZonesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'links': 'PageLink',
        'metadata': 'Metedata',
        'zones': 'list[PrivateZoneResp]'
    }

    attribute_map = {
        'links': 'links',
        'metadata': 'metadata',
        'zones': 'zones'
    }

    def __init__(self, links=None, metadata=None, zones=None):
        """ListPrivateZonesResponse - a model defined in huaweicloud sdk"""
        
        super(ListPrivateZonesResponse, self).__init__()

        self._links = None
        self._metadata = None
        self._zones = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata
        if zones is not None:
            self.zones = zones

    @property
    def links(self):
        """Gets the links of this ListPrivateZonesResponse.


        :return: The links of this ListPrivateZonesResponse.
        :rtype: PageLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListPrivateZonesResponse.


        :param links: The links of this ListPrivateZonesResponse.
        :type: PageLink
        """
        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this ListPrivateZonesResponse.


        :return: The metadata of this ListPrivateZonesResponse.
        :rtype: Metedata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ListPrivateZonesResponse.


        :param metadata: The metadata of this ListPrivateZonesResponse.
        :type: Metedata
        """
        self._metadata = metadata

    @property
    def zones(self):
        """Gets the zones of this ListPrivateZonesResponse.


        :return: The zones of this ListPrivateZonesResponse.
        :rtype: list[PrivateZoneResp]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this ListPrivateZonesResponse.


        :param zones: The zones of this ListPrivateZonesResponse.
        :type: list[PrivateZoneResp]
        """
        self._zones = zones

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
        if not isinstance(other, ListPrivateZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
