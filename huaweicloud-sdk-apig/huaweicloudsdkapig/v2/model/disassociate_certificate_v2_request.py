# coding: utf-8

import pprint
import re

import six





class DisassociateCertificateV2Request:


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
        'domain_id': 'str',
        'group_id': 'str',
        'certificate_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'domain_id': 'domain_id',
        'group_id': 'group_id',
        'certificate_id': 'certificate_id'
    }

    def __init__(self, instance_id=None, domain_id=None, group_id=None, certificate_id=None):
        """DisassociateCertificateV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._domain_id = None
        self._group_id = None
        self._certificate_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.domain_id = domain_id
        self.group_id = group_id
        self.certificate_id = certificate_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DisassociateCertificateV2Request.

        实例编号

        :return: The instance_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DisassociateCertificateV2Request.

        实例编号

        :param instance_id: The instance_id of this DisassociateCertificateV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def domain_id(self):
        """Gets the domain_id of this DisassociateCertificateV2Request.

        域名的编号

        :return: The domain_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DisassociateCertificateV2Request.

        域名的编号

        :param domain_id: The domain_id of this DisassociateCertificateV2Request.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def group_id(self):
        """Gets the group_id of this DisassociateCertificateV2Request.

        分组的编号

        :return: The group_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DisassociateCertificateV2Request.

        分组的编号

        :param group_id: The group_id of this DisassociateCertificateV2Request.
        :type: str
        """
        self._group_id = group_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this DisassociateCertificateV2Request.

        证书的编号

        :return: The certificate_id of this DisassociateCertificateV2Request.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this DisassociateCertificateV2Request.

        证书的编号

        :param certificate_id: The certificate_id of this DisassociateCertificateV2Request.
        :type: str
        """
        self._certificate_id = certificate_id

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
        if not isinstance(other, DisassociateCertificateV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
