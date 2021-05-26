# coding: utf-8

import pprint
import re

import six





class ListBareMetalServersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'name': 'str',
        'status': 'str',
        'limit': 'int',
        'offset': 'int',
        'tags': 'str',
        'reservation_id': 'str',
        'detail': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'reservation_id': 'reservation_id',
        'detail': 'detail',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, flavor=None, name=None, status=None, limit=None, offset=None, tags=None, reservation_id=None, detail=None, enterprise_project_id=None):
        """ListBareMetalServersRequest - a model defined in huaweicloud sdk"""
        
        

        self._flavor = None
        self._name = None
        self._status = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._reservation_id = None
        self._detail = None
        self._enterprise_project_id = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if reservation_id is not None:
            self.reservation_id = reservation_id
        if detail is not None:
            self.detail = detail
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def flavor(self):
        """Gets the flavor of this ListBareMetalServersRequest.

        裸金属服务器规格ID

        :return: The flavor of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ListBareMetalServersRequest.

        裸金属服务器规格ID

        :param flavor: The flavor of this ListBareMetalServersRequest.
        :type: str
        """
        self._flavor = flavor

    @property
    def name(self):
        """Gets the name of this ListBareMetalServersRequest.

        裸金属服务器名称

        :return: The name of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBareMetalServersRequest.

        裸金属服务器名称

        :param name: The name of this ListBareMetalServersRequest.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListBareMetalServersRequest.

        裸金属服务器状态,只有管理员可以使用DELETED状态过滤查询已经删除的裸金属服务器。取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、REBOOT、REBUILD、SHUTOFF

        :return: The status of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBareMetalServersRequest.

        裸金属服务器状态,只有管理员可以使用DELETED状态过滤查询已经删除的裸金属服务器。取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、REBOOT、REBUILD、SHUTOFF

        :param status: The status of this ListBareMetalServersRequest.
        :type: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListBareMetalServersRequest.

        每页返回裸金属服务器的条数，默认值是25，最大值为1000。limit为每页返回裸金属服务器详情的条数

        :return: The limit of this ListBareMetalServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBareMetalServersRequest.

        每页返回裸金属服务器的条数，默认值是25，最大值为1000。limit为每页返回裸金属服务器详情的条数

        :param limit: The limit of this ListBareMetalServersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListBareMetalServersRequest.

        此接口为分页查询接口:不传offset参数，返回结果是符合条件的裸金属服务器总条数,servers列表为空。传offset参数，offset为查询页码，起始页码为1，每页查询的条数为limit值。此接口为分页查询接口，offset为查询页码（起始页码为1），返回值包括总条数和裸金属详情列表传入offset：按limit值分页（limit默认为1000），返回第offset页裸金属服务器详情列表和总条数，总条数最大值为limit，不足按实际情况返回。不传入offset传入limit ：返回裸金属服务器详情列表和总条数，总条数最大值为limit，不足按实际情况返回。。不传入limit：按25条分页，返回第1页裸金属服务器详情列表，总条数最大值为25，不足按实际情况返回。

        :return: The offset of this ListBareMetalServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBareMetalServersRequest.

        此接口为分页查询接口:不传offset参数，返回结果是符合条件的裸金属服务器总条数,servers列表为空。传offset参数，offset为查询页码，起始页码为1，每页查询的条数为limit值。此接口为分页查询接口，offset为查询页码（起始页码为1），返回值包括总条数和裸金属详情列表传入offset：按limit值分页（limit默认为1000），返回第offset页裸金属服务器详情列表和总条数，总条数最大值为limit，不足按实际情况返回。不传入offset传入limit ：返回裸金属服务器详情列表和总条数，总条数最大值为limit，不足按实际情况返回。。不传入limit：按25条分页，返回第1页裸金属服务器详情列表，总条数最大值为25，不足按实际情况返回。

        :param offset: The offset of this ListBareMetalServersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ListBareMetalServersRequest.

        裸金属服务器标签：__type_baremetal

        :return: The tags of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListBareMetalServersRequest.

        裸金属服务器标签：__type_baremetal

        :param tags: The tags of this ListBareMetalServersRequest.
        :type: str
        """
        self._tags = tags

    @property
    def reservation_id(self):
        """Gets the reservation_id of this ListBareMetalServersRequest.

        批量创建裸金属服务器时，指定返回的ID，用于查询本次批量创建的裸金属服务器

        :return: The reservation_id of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        """Sets the reservation_id of this ListBareMetalServersRequest.

        批量创建裸金属服务器时，指定返回的ID，用于查询本次批量创建的裸金属服务器

        :param reservation_id: The reservation_id of this ListBareMetalServersRequest.
        :type: str
        """
        self._reservation_id = reservation_id

    @property
    def detail(self):
        """Gets the detail of this ListBareMetalServersRequest.

        查询裸金属服务器结果的详细级别，级别越高，查询到的裸金属服务器信息越多，默认为4。可使用的级别为 1，2，3，4，5

        :return: The detail of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListBareMetalServersRequest.

        查询裸金属服务器结果的详细级别，级别越高，查询到的裸金属服务器信息越多，默认为4。可使用的级别为 1，2，3，4，5

        :param detail: The detail of this ListBareMetalServersRequest.
        :type: str
        """
        self._detail = detail

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBareMetalServersRequest.

        查询绑定某个企业项目的裸金属服务器

        :return: The enterprise_project_id of this ListBareMetalServersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBareMetalServersRequest.

        查询绑定某个企业项目的裸金属服务器

        :param enterprise_project_id: The enterprise_project_id of this ListBareMetalServersRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListBareMetalServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
