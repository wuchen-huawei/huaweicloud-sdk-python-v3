# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateImageResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'data_origin': 'str',
        'description': 'str',
        'image_location': 'str',
        'image_size': 'str',
        'image_source_type': 'str',
        'imagetype': 'str',
        'is_config_init': 'str',
        'isregistered': 'str',
        'originalimagename': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'platform': 'str',
        'productcode': 'str',
        'support_diskintensive': 'str',
        'support_highperformance': 'str',
        'support_kvm': 'str',
        'support_kvm_gpu_type': 'str',
        'support_kvm_infiniband': 'str',
        'support_largememory': 'str',
        'support_xen': 'str',
        'support_xen_gpu_type': 'str',
        'support_xen_hana': 'str',
        'system_support_market': 'bool',
        'checksum': 'str',
        'container_format': 'str',
        'created_at': 'str',
        'disk_format': 'str',
        'enterprise_project_id': 'str',
        'file': 'str',
        'id': 'str',
        'min_disk': 'int',
        'min_ram': 'int',
        'name': 'str',
        'owner': 'str',
        'protected': 'bool',
        'schema': 'str',
        '_self': 'str',
        'size': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'updated_at': 'str',
        'virtual_env_type': 'str',
        'virtual_size': 'int',
        'visibility': 'str',
        'architecture': 'str',
        'support_fc_inject': 'str',
        'hw_firmware_type': 'str',
        'support_arm': 'str',
        'max_ram': 'str',
        'system__cmkid': 'str',
        'os_feature_list': 'str',
        'account_code': 'str',
        'hw_vif_multiqueue_enabled': 'str'
    }

    attribute_map = {
        'backup_id': '__backup_id',
        'data_origin': '__data_origin',
        'description': '__description',
        'image_location': '__image_location',
        'image_size': '__image_size',
        'image_source_type': '__image_source_type',
        'imagetype': '__imagetype',
        'is_config_init': '__is_config_init',
        'isregistered': '__isregistered',
        'originalimagename': '__originalimagename',
        'os_bit': '__os_bit',
        'os_type': '__os_type',
        'os_version': '__os_version',
        'platform': '__platform',
        'productcode': '__productcode',
        'support_diskintensive': '__support_diskintensive',
        'support_highperformance': '__support_highperformance',
        'support_kvm': '__support_kvm',
        'support_kvm_gpu_type': '__support_kvm_gpu_type',
        'support_kvm_infiniband': '__support_kvm_infiniband',
        'support_largememory': '__support_largememory',
        'support_xen': '__support_xen',
        'support_xen_gpu_type': '__support_xen_gpu_type',
        'support_xen_hana': '__support_xen_hana',
        'system_support_market': '__system_support_market',
        'checksum': 'checksum',
        'container_format': 'container_format',
        'created_at': 'created_at',
        'disk_format': 'disk_format',
        'enterprise_project_id': 'enterprise_project_id',
        'file': 'file',
        'id': 'id',
        'min_disk': 'min_disk',
        'min_ram': 'min_ram',
        'name': 'name',
        'owner': 'owner',
        'protected': 'protected',
        'schema': 'schema',
        '_self': 'self',
        'size': 'size',
        'status': 'status',
        'tags': 'tags',
        'updated_at': 'updated_at',
        'virtual_env_type': 'virtual_env_type',
        'virtual_size': 'virtual_size',
        'visibility': 'visibility',
        'architecture': 'architecture',
        'support_fc_inject': '__support_fc_inject',
        'hw_firmware_type': 'hw_firmware_type',
        'support_arm': '__support_arm',
        'max_ram': 'max_ram',
        'system__cmkid': '__system__cmkid',
        'os_feature_list': '__os_feature_list',
        'account_code': '__account_code',
        'hw_vif_multiqueue_enabled': 'hw_vif_multiqueue_enabled'
    }

    def __init__(self, backup_id=None, data_origin=None, description=None, image_location=None, image_size=None, image_source_type=None, imagetype=None, is_config_init=None, isregistered=None, originalimagename=None, os_bit=None, os_type=None, os_version=None, platform=None, productcode=None, support_diskintensive=None, support_highperformance=None, support_kvm=None, support_kvm_gpu_type=None, support_kvm_infiniband=None, support_largememory=None, support_xen=None, support_xen_gpu_type=None, support_xen_hana=None, system_support_market=None, checksum=None, container_format=None, created_at=None, disk_format=None, enterprise_project_id=None, file=None, id=None, min_disk=None, min_ram=None, name=None, owner=None, protected=None, schema=None, _self=None, size=None, status=None, tags=None, updated_at=None, virtual_env_type=None, virtual_size=None, visibility=None, architecture=None, support_fc_inject=None, hw_firmware_type=None, support_arm=None, max_ram=None, system__cmkid=None, os_feature_list=None, account_code=None, hw_vif_multiqueue_enabled=None):
        """UpdateImageResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateImageResponse, self).__init__()

        self._backup_id = None
        self._data_origin = None
        self._description = None
        self._image_location = None
        self._image_size = None
        self._image_source_type = None
        self._imagetype = None
        self._is_config_init = None
        self._isregistered = None
        self._originalimagename = None
        self._os_bit = None
        self._os_type = None
        self._os_version = None
        self._platform = None
        self._productcode = None
        self._support_diskintensive = None
        self._support_highperformance = None
        self._support_kvm = None
        self._support_kvm_gpu_type = None
        self._support_kvm_infiniband = None
        self._support_largememory = None
        self._support_xen = None
        self._support_xen_gpu_type = None
        self._support_xen_hana = None
        self._system_support_market = None
        self._checksum = None
        self._container_format = None
        self._created_at = None
        self._disk_format = None
        self._enterprise_project_id = None
        self._file = None
        self._id = None
        self._min_disk = None
        self._min_ram = None
        self._name = None
        self._owner = None
        self._protected = None
        self._schema = None
        self.__self = None
        self._size = None
        self._status = None
        self._tags = None
        self._updated_at = None
        self._virtual_env_type = None
        self._virtual_size = None
        self._visibility = None
        self._architecture = None
        self._support_fc_inject = None
        self._hw_firmware_type = None
        self._support_arm = None
        self._max_ram = None
        self._system__cmkid = None
        self._os_feature_list = None
        self._account_code = None
        self._hw_vif_multiqueue_enabled = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if data_origin is not None:
            self.data_origin = data_origin
        if description is not None:
            self.description = description
        if image_location is not None:
            self.image_location = image_location
        if image_size is not None:
            self.image_size = image_size
        if image_source_type is not None:
            self.image_source_type = image_source_type
        if imagetype is not None:
            self.imagetype = imagetype
        if is_config_init is not None:
            self.is_config_init = is_config_init
        if isregistered is not None:
            self.isregistered = isregistered
        if originalimagename is not None:
            self.originalimagename = originalimagename
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if platform is not None:
            self.platform = platform
        if productcode is not None:
            self.productcode = productcode
        if support_diskintensive is not None:
            self.support_diskintensive = support_diskintensive
        if support_highperformance is not None:
            self.support_highperformance = support_highperformance
        if support_kvm is not None:
            self.support_kvm = support_kvm
        if support_kvm_gpu_type is not None:
            self.support_kvm_gpu_type = support_kvm_gpu_type
        if support_kvm_infiniband is not None:
            self.support_kvm_infiniband = support_kvm_infiniband
        if support_largememory is not None:
            self.support_largememory = support_largememory
        if support_xen is not None:
            self.support_xen = support_xen
        if support_xen_gpu_type is not None:
            self.support_xen_gpu_type = support_xen_gpu_type
        if support_xen_hana is not None:
            self.support_xen_hana = support_xen_hana
        if system_support_market is not None:
            self.system_support_market = system_support_market
        if checksum is not None:
            self.checksum = checksum
        if container_format is not None:
            self.container_format = container_format
        if created_at is not None:
            self.created_at = created_at
        if disk_format is not None:
            self.disk_format = disk_format
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file is not None:
            self.file = file
        if id is not None:
            self.id = id
        if min_disk is not None:
            self.min_disk = min_disk
        if min_ram is not None:
            self.min_ram = min_ram
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if protected is not None:
            self.protected = protected
        if schema is not None:
            self.schema = schema
        if _self is not None:
            self._self = _self
        if size is not None:
            self.size = size
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if updated_at is not None:
            self.updated_at = updated_at
        if virtual_env_type is not None:
            self.virtual_env_type = virtual_env_type
        if virtual_size is not None:
            self.virtual_size = virtual_size
        if visibility is not None:
            self.visibility = visibility
        if architecture is not None:
            self.architecture = architecture
        if support_fc_inject is not None:
            self.support_fc_inject = support_fc_inject
        if hw_firmware_type is not None:
            self.hw_firmware_type = hw_firmware_type
        if support_arm is not None:
            self.support_arm = support_arm
        if max_ram is not None:
            self.max_ram = max_ram
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if os_feature_list is not None:
            self.os_feature_list = os_feature_list
        if account_code is not None:
            self.account_code = account_code
        if hw_vif_multiqueue_enabled is not None:
            self.hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled

    @property
    def backup_id(self):
        """Gets the backup_id of this UpdateImageResponse.

        备份ID。如果是备份创建的镜像，则填写为备份的ID，否则为空

        :return: The backup_id of this UpdateImageResponse.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this UpdateImageResponse.

        备份ID。如果是备份创建的镜像，则填写为备份的ID，否则为空

        :param backup_id: The backup_id of this UpdateImageResponse.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def data_origin(self):
        """Gets the data_origin of this UpdateImageResponse.

        镜像来源。公共镜像为空

        :return: The data_origin of this UpdateImageResponse.
        :rtype: str
        """
        return self._data_origin

    @data_origin.setter
    def data_origin(self, data_origin):
        """Sets the data_origin of this UpdateImageResponse.

        镜像来源。公共镜像为空

        :param data_origin: The data_origin of this UpdateImageResponse.
        :type: str
        """
        self._data_origin = data_origin

    @property
    def description(self):
        """Gets the description of this UpdateImageResponse.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :return: The description of this UpdateImageResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateImageResponse.

        镜像描述信息。 支持字母、数字、中文等，不支持回车、<、 >，长度不能超过1024个字符。

        :param description: The description of this UpdateImageResponse.
        :type: str
        """
        self._description = description

    @property
    def image_location(self):
        """Gets the image_location of this UpdateImageResponse.

        镜像的存储位置

        :return: The image_location of this UpdateImageResponse.
        :rtype: str
        """
        return self._image_location

    @image_location.setter
    def image_location(self, image_location):
        """Sets the image_location of this UpdateImageResponse.

        镜像的存储位置

        :param image_location: The image_location of this UpdateImageResponse.
        :type: str
        """
        self._image_location = image_location

    @property
    def image_size(self):
        """Gets the image_size of this UpdateImageResponse.

        镜像文件的大小，单位为字节

        :return: The image_size of this UpdateImageResponse.
        :rtype: str
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this UpdateImageResponse.

        镜像文件的大小，单位为字节

        :param image_size: The image_size of this UpdateImageResponse.
        :type: str
        """
        self._image_size = image_size

    @property
    def image_source_type(self):
        """Gets the image_source_type of this UpdateImageResponse.

        镜像后端存储类型，目前只支持uds

        :return: The image_source_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._image_source_type

    @image_source_type.setter
    def image_source_type(self, image_source_type):
        """Sets the image_source_type of this UpdateImageResponse.

        镜像后端存储类型，目前只支持uds

        :param image_source_type: The image_source_type of this UpdateImageResponse.
        :type: str
        """
        self._image_source_type = image_source_type

    @property
    def imagetype(self):
        """Gets the imagetype of this UpdateImageResponse.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared

        :return: The imagetype of this UpdateImageResponse.
        :rtype: str
        """
        return self._imagetype

    @imagetype.setter
    def imagetype(self, imagetype):
        """Sets the imagetype of this UpdateImageResponse.

        镜像类型，目前支持以下类型： 公共镜像：gold 私有镜像：private 共享镜像：shared

        :param imagetype: The imagetype of this UpdateImageResponse.
        :type: str
        """
        self._imagetype = imagetype

    @property
    def is_config_init(self):
        """Gets the is_config_init of this UpdateImageResponse.

        是否完成了初始化配置。取值为true或false。如果用户确定完成了初始化配置，则可以设置为true，否则设置为false。默认为false。

        :return: The is_config_init of this UpdateImageResponse.
        :rtype: str
        """
        return self._is_config_init

    @is_config_init.setter
    def is_config_init(self, is_config_init):
        """Sets the is_config_init of this UpdateImageResponse.

        是否完成了初始化配置。取值为true或false。如果用户确定完成了初始化配置，则可以设置为true，否则设置为false。默认为false。

        :param is_config_init: The is_config_init of this UpdateImageResponse.
        :type: str
        """
        self._is_config_init = is_config_init

    @property
    def isregistered(self):
        """Gets the isregistered of this UpdateImageResponse.

        是否是注册过的镜像，取值为“true”或者“false”

        :return: The isregistered of this UpdateImageResponse.
        :rtype: str
        """
        return self._isregistered

    @isregistered.setter
    def isregistered(self, isregistered):
        """Sets the isregistered of this UpdateImageResponse.

        是否是注册过的镜像，取值为“true”或者“false”

        :param isregistered: The isregistered of this UpdateImageResponse.
        :type: str
        """
        self._isregistered = isregistered

    @property
    def originalimagename(self):
        """Gets the originalimagename of this UpdateImageResponse.

        父镜像ID。公共镜像或通过文件创建的私有镜像，取值为空

        :return: The originalimagename of this UpdateImageResponse.
        :rtype: str
        """
        return self._originalimagename

    @originalimagename.setter
    def originalimagename(self, originalimagename):
        """Sets the originalimagename of this UpdateImageResponse.

        父镜像ID。公共镜像或通过文件创建的私有镜像，取值为空

        :param originalimagename: The originalimagename of this UpdateImageResponse.
        :type: str
        """
        self._originalimagename = originalimagename

    @property
    def os_bit(self):
        """Gets the os_bit of this UpdateImageResponse.

        操作系统位数，一般取值为“32”或者“64”

        :return: The os_bit of this UpdateImageResponse.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        """Sets the os_bit of this UpdateImageResponse.

        操作系统位数，一般取值为“32”或者“64”

        :param os_bit: The os_bit of this UpdateImageResponse.
        :type: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        """Gets the os_type of this UpdateImageResponse.

        操作系统类型，目前取值Linux， Windows，Other

        :return: The os_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this UpdateImageResponse.

        操作系统类型，目前取值Linux， Windows，Other

        :param os_type: The os_type of this UpdateImageResponse.
        :type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        """Gets the os_version of this UpdateImageResponse.

        操作系统具体版本

        :return: The os_version of this UpdateImageResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this UpdateImageResponse.

        操作系统具体版本

        :param os_version: The os_version of this UpdateImageResponse.
        :type: str
        """
        self._os_version = os_version

    @property
    def platform(self):
        """Gets the platform of this UpdateImageResponse.

        镜像平台分类

        :return: The platform of this UpdateImageResponse.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UpdateImageResponse.

        镜像平台分类

        :param platform: The platform of this UpdateImageResponse.
        :type: str
        """
        self._platform = platform

    @property
    def productcode(self):
        """Gets the productcode of this UpdateImageResponse.

        市场镜像的产品ID

        :return: The productcode of this UpdateImageResponse.
        :rtype: str
        """
        return self._productcode

    @productcode.setter
    def productcode(self, productcode):
        """Sets the productcode of this UpdateImageResponse.

        市场镜像的产品ID

        :param productcode: The productcode of this UpdateImageResponse.
        :type: str
        """
        self._productcode = productcode

    @property
    def support_diskintensive(self):
        """Gets the support_diskintensive of this UpdateImageResponse.

        镜像来源表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :return: The support_diskintensive of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_diskintensive

    @support_diskintensive.setter
    def support_diskintensive(self, support_diskintensive):
        """Sets the support_diskintensive of this UpdateImageResponse.

        镜像来源表示该镜像支持密集存储。如果镜像支持密集存储性能，则值为true，否则无需增加该属性。

        :param support_diskintensive: The support_diskintensive of this UpdateImageResponse.
        :type: str
        """
        self._support_diskintensive = support_diskintensive

    @property
    def support_highperformance(self):
        """Gets the support_highperformance of this UpdateImageResponse.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :return: The support_highperformance of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_highperformance

    @support_highperformance.setter
    def support_highperformance(self, support_highperformance):
        """Sets the support_highperformance of this UpdateImageResponse.

        表示该镜像支持高计算性能。如果镜像支持高计算性能，则值为true，否则无需增加该属性。

        :param support_highperformance: The support_highperformance of this UpdateImageResponse.
        :type: str
        """
        self._support_highperformance = support_highperformance

    @property
    def support_kvm(self):
        """Gets the support_kvm of this UpdateImageResponse.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :return: The support_kvm of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_kvm

    @support_kvm.setter
    def support_kvm(self, support_kvm):
        """Sets the support_kvm of this UpdateImageResponse.

        如果镜像支持KVM，取值为true，否则无需增加该属性。

        :param support_kvm: The support_kvm of this UpdateImageResponse.
        :type: str
        """
        self._support_kvm = support_kvm

    @property
    def support_kvm_gpu_type(self):
        """Gets the support_kvm_gpu_type of this UpdateImageResponse.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_kvm_gpu_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_kvm_gpu_type

    @support_kvm_gpu_type.setter
    def support_kvm_gpu_type(self, support_kvm_gpu_type):
        """Sets the support_kvm_gpu_type of this UpdateImageResponse.

        表示该镜像是支持KVM虚拟化平台下的GPU类型，如果不支持KVM虚拟机下GPU类型，无需添加该属性。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_kvm_gpu_type: The support_kvm_gpu_type of this UpdateImageResponse.
        :type: str
        """
        self._support_kvm_gpu_type = support_kvm_gpu_type

    @property
    def support_kvm_infiniband(self):
        """Gets the support_kvm_infiniband of this UpdateImageResponse.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :return: The support_kvm_infiniband of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_kvm_infiniband

    @support_kvm_infiniband.setter
    def support_kvm_infiniband(self, support_kvm_infiniband):
        """Sets the support_kvm_infiniband of this UpdateImageResponse.

        如果镜像支持KVM虚拟化下Infiniband网卡类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”属性不共存。

        :param support_kvm_infiniband: The support_kvm_infiniband of this UpdateImageResponse.
        :type: str
        """
        self._support_kvm_infiniband = support_kvm_infiniband

    @property
    def support_largememory(self):
        """Gets the support_largememory of this UpdateImageResponse.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :return: The support_largememory of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_largememory

    @support_largememory.setter
    def support_largememory(self, support_largememory):
        """Sets the support_largememory of this UpdateImageResponse.

        表示该镜像支持超大内存。如果镜像支持超大内存，取值为true，否则无需增加该属性。

        :param support_largememory: The support_largememory of this UpdateImageResponse.
        :type: str
        """
        self._support_largememory = support_largememory

    @property
    def support_xen(self):
        """Gets the support_xen of this UpdateImageResponse.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :return: The support_xen of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_xen

    @support_xen.setter
    def support_xen(self, support_xen):
        """Sets the support_xen of this UpdateImageResponse.

        如果镜像支持XEN，取值为true，否则无需增加该属性。

        :param support_xen: The support_xen of this UpdateImageResponse.
        :type: str
        """
        self._support_xen = support_xen

    @property
    def support_xen_gpu_type(self):
        """Gets the support_xen_gpu_type of this UpdateImageResponse.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性            。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :return: The support_xen_gpu_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_xen_gpu_type

    @support_xen_gpu_type.setter
    def support_xen_gpu_type(self, support_xen_gpu_type):
        """Sets the support_xen_gpu_type of this UpdateImageResponse.

        表示该镜像是支持XEN虚拟化平台下的GPU优化类型，如果不支持XEN虚拟化下GPU类型，无需添加该属性            。该属性与“__support_xen”和“__support_kvm”属性不共存。

        :param support_xen_gpu_type: The support_xen_gpu_type of this UpdateImageResponse.
        :type: str
        """
        self._support_xen_gpu_type = support_xen_gpu_type

    @property
    def support_xen_hana(self):
        """Gets the support_xen_hana of this UpdateImageResponse.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”             和“__support_kvm”属性不共存。

        :return: The support_xen_hana of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_xen_hana

    @support_xen_hana.setter
    def support_xen_hana(self, support_xen_hana):
        """Sets the support_xen_hana of this UpdateImageResponse.

        如果镜像支持XEN虚拟化下HANA类型，取值为true。否则，无需添加该属性。该属性与“__support_xen”             和“__support_kvm”属性不共存。

        :param support_xen_hana: The support_xen_hana of this UpdateImageResponse.
        :type: str
        """
        self._support_xen_hana = support_xen_hana

    @property
    def system_support_market(self):
        """Gets the system_support_market of this UpdateImageResponse.

        表示当前镜像是否支持发布为市场镜像,true表示支持,false 表示不支持

        :return: The system_support_market of this UpdateImageResponse.
        :rtype: bool
        """
        return self._system_support_market

    @system_support_market.setter
    def system_support_market(self, system_support_market):
        """Sets the system_support_market of this UpdateImageResponse.

        表示当前镜像是否支持发布为市场镜像,true表示支持,false 表示不支持

        :param system_support_market: The system_support_market of this UpdateImageResponse.
        :type: bool
        """
        self._system_support_market = system_support_market

    @property
    def checksum(self):
        """Gets the checksum of this UpdateImageResponse.

        目前暂时不使用

        :return: The checksum of this UpdateImageResponse.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this UpdateImageResponse.

        目前暂时不使用

        :param checksum: The checksum of this UpdateImageResponse.
        :type: str
        """
        self._checksum = checksum

    @property
    def container_format(self):
        """Gets the container_format of this UpdateImageResponse.

        容器类型

        :return: The container_format of this UpdateImageResponse.
        :rtype: str
        """
        return self._container_format

    @container_format.setter
    def container_format(self, container_format):
        """Sets the container_format of this UpdateImageResponse.

        容器类型

        :param container_format: The container_format of this UpdateImageResponse.
        :type: str
        """
        self._container_format = container_format

    @property
    def created_at(self):
        """Gets the created_at of this UpdateImageResponse.

        创建时间。格式为UTC时间

        :return: The created_at of this UpdateImageResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateImageResponse.

        创建时间。格式为UTC时间

        :param created_at: The created_at of this UpdateImageResponse.
        :type: str
        """
        self._created_at = created_at

    @property
    def disk_format(self):
        """Gets the disk_format of this UpdateImageResponse.

        镜像的格式，目前支持vhd，zvhd、raw，qcow2。默认值是vhd

        :return: The disk_format of this UpdateImageResponse.
        :rtype: str
        """
        return self._disk_format

    @disk_format.setter
    def disk_format(self, disk_format):
        """Sets the disk_format of this UpdateImageResponse.

        镜像的格式，目前支持vhd，zvhd、raw，qcow2。默认值是vhd

        :param disk_format: The disk_format of this UpdateImageResponse.
        :type: str
        """
        self._disk_format = disk_format

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdateImageResponse.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目，取值为UUID，表示属于该UUID对应的企业项目。

        :return: The enterprise_project_id of this UpdateImageResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdateImageResponse.

        表示当前镜像所属的企业项目。取值为0或无该值，表示属于default企业项目，取值为UUID，表示属于该UUID对应的企业项目。

        :param enterprise_project_id: The enterprise_project_id of this UpdateImageResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file(self):
        """Gets the file of this UpdateImageResponse.

        镜像文件下载和上传链接

        :return: The file of this UpdateImageResponse.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UpdateImageResponse.

        镜像文件下载和上传链接

        :param file: The file of this UpdateImageResponse.
        :type: str
        """
        self._file = file

    @property
    def id(self):
        """Gets the id of this UpdateImageResponse.

        镜像ID

        :return: The id of this UpdateImageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateImageResponse.

        镜像ID

        :param id: The id of this UpdateImageResponse.
        :type: str
        """
        self._id = id

    @property
    def min_disk(self):
        """Gets the min_disk of this UpdateImageResponse.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :return: The min_disk of this UpdateImageResponse.
        :rtype: int
        """
        return self._min_disk

    @min_disk.setter
    def min_disk(self, min_disk):
        """Sets the min_disk of this UpdateImageResponse.

        镜像运行需要的最小磁盘容量，单位为GB。取值为40～1024GB。

        :param min_disk: The min_disk of this UpdateImageResponse.
        :type: int
        """
        self._min_disk = min_disk

    @property
    def min_ram(self):
        """Gets the min_ram of this UpdateImageResponse.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0

        :return: The min_ram of this UpdateImageResponse.
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this UpdateImageResponse.

        镜像运行需要的最小内存，单位为MB。参数取值依据弹性云服务器的规格限制，默认设置为0

        :param min_ram: The min_ram of this UpdateImageResponse.
        :type: int
        """
        self._min_ram = min_ram

    @property
    def name(self):
        """Gets the name of this UpdateImageResponse.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :return: The name of this UpdateImageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateImageResponse.

        镜像名称。 名称的首尾字母不能为空格。 名称的长度至为1～128位。 名称包含以下4种字符： 大写字母 小写字母 数字 特殊字符包含-、.、_、空格和中文。

        :param name: The name of this UpdateImageResponse.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this UpdateImageResponse.

        镜像属于哪个租户

        :return: The owner of this UpdateImageResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateImageResponse.

        镜像属于哪个租户

        :param owner: The owner of this UpdateImageResponse.
        :type: str
        """
        self._owner = owner

    @property
    def protected(self):
        """Gets the protected of this UpdateImageResponse.

        是否是受保护的，受保护的镜像不允许删除。取值为true或false

        :return: The protected of this UpdateImageResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this UpdateImageResponse.

        是否是受保护的，受保护的镜像不允许删除。取值为true或false

        :param protected: The protected of this UpdateImageResponse.
        :type: bool
        """
        self._protected = protected

    @property
    def schema(self):
        """Gets the schema of this UpdateImageResponse.

        镜像视图

        :return: The schema of this UpdateImageResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this UpdateImageResponse.

        镜像视图

        :param schema: The schema of this UpdateImageResponse.
        :type: str
        """
        self._schema = schema

    @property
    def _self(self):
        """Gets the _self of this UpdateImageResponse.

        镜像链接信息

        :return: The _self of this UpdateImageResponse.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this UpdateImageResponse.

        镜像链接信息

        :param _self: The _self of this UpdateImageResponse.
        :type: str
        """
        self.__self = _self

    @property
    def size(self):
        """Gets the size of this UpdateImageResponse.

        目前暂时不使用

        :return: The size of this UpdateImageResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UpdateImageResponse.

        目前暂时不使用

        :param size: The size of this UpdateImageResponse.
        :type: int
        """
        self._size = size

    @property
    def status(self):
        """Gets the status of this UpdateImageResponse.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待 上传镜像文件。saving：表示镜像 正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用

        :return: The status of this UpdateImageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateImageResponse.

        镜像状态。取值如下：queued：表示镜像元数据已经创建成功，等待 上传镜像文件。saving：表示镜像 正在上传文件到后端存储。deleted：表示镜像已经删除。killed：表示镜像上传错误。active：表示镜像可以正常使用

        :param status: The status of this UpdateImageResponse.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this UpdateImageResponse.

        镜像标签列表

        :return: The tags of this UpdateImageResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateImageResponse.

        镜像标签列表

        :param tags: The tags of this UpdateImageResponse.
        :type: list[str]
        """
        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this UpdateImageResponse.

        更新时间。格式为UTC时间

        :return: The updated_at of this UpdateImageResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UpdateImageResponse.

        更新时间。格式为UTC时间

        :param updated_at: The updated_at of this UpdateImageResponse.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def virtual_env_type(self):
        """Gets the virtual_env_type of this UpdateImageResponse.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取Dat            aImage，如果是裸金属服务器镜像，则取值是Ironic

        :return: The virtual_env_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._virtual_env_type

    @virtual_env_type.setter
    def virtual_env_type(self, virtual_env_type):
        """Sets the virtual_env_type of this UpdateImageResponse.

        镜像使用环境类型：FusionCompute，Ironic，DataImage。如果弹性云服务器镜像，则取值为FusionCompute，如果是数据卷镜像则取Dat            aImage，如果是裸金属服务器镜像，则取值是Ironic

        :param virtual_env_type: The virtual_env_type of this UpdateImageResponse.
        :type: str
        """
        self._virtual_env_type = virtual_env_type

    @property
    def virtual_size(self):
        """Gets the virtual_size of this UpdateImageResponse.

        目前暂时不使用

        :return: The virtual_size of this UpdateImageResponse.
        :rtype: int
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        """Sets the virtual_size of this UpdateImageResponse.

        目前暂时不使用

        :param virtual_size: The virtual_size of this UpdateImageResponse.
        :type: int
        """
        self._virtual_size = virtual_size

    @property
    def visibility(self):
        """Gets the visibility of this UpdateImageResponse.

        是否被其他租户可见，取值为private或public

        :return: The visibility of this UpdateImageResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this UpdateImageResponse.

        是否被其他租户可见，取值为private或public

        :param visibility: The visibility of this UpdateImageResponse.
        :type: str
        """
        self._visibility = visibility

    @property
    def architecture(self):
        """Gets the architecture of this UpdateImageResponse.

        镜像架构类型。取值包括： x86 arm

        :return: The architecture of this UpdateImageResponse.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this UpdateImageResponse.

        镜像架构类型。取值包括： x86 arm

        :param architecture: The architecture of this UpdateImageResponse.
        :type: str
        """
        self._architecture = architecture

    @property
    def support_fc_inject(self):
        """Gets the support_fc_inject of this UpdateImageResponse.

        表示当前镜像支持CloudInit密码/密钥注入方式，建议设置为\"true\"或者\"false\"。 如果取值为\"true\"，表示该镜像不支持CloudInit注入密码/密钥，其他取值时表示支持CloudInit注入密钥/密码。

        :return: The support_fc_inject of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_fc_inject

    @support_fc_inject.setter
    def support_fc_inject(self, support_fc_inject):
        """Sets the support_fc_inject of this UpdateImageResponse.

        表示当前镜像支持CloudInit密码/密钥注入方式，建议设置为\"true\"或者\"false\"。 如果取值为\"true\"，表示该镜像不支持CloudInit注入密码/密钥，其他取值时表示支持CloudInit注入密钥/密码。

        :param support_fc_inject: The support_fc_inject of this UpdateImageResponse.
        :type: str
        """
        self._support_fc_inject = support_fc_inject

    @property
    def hw_firmware_type(self):
        """Gets the hw_firmware_type of this UpdateImageResponse.

        云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :return: The hw_firmware_type of this UpdateImageResponse.
        :rtype: str
        """
        return self._hw_firmware_type

    @hw_firmware_type.setter
    def hw_firmware_type(self, hw_firmware_type):
        """Sets the hw_firmware_type of this UpdateImageResponse.

        云服务器的启动方式。目前支持： bios：表示bios引导启动。 uefi：表示uefi引导启动。

        :param hw_firmware_type: The hw_firmware_type of this UpdateImageResponse.
        :type: str
        """
        self._hw_firmware_type = hw_firmware_type

    @property
    def support_arm(self):
        """Gets the support_arm of this UpdateImageResponse.

        是否是ARM架构类型的镜像，取值为“true”或者“false”。

        :return: The support_arm of this UpdateImageResponse.
        :rtype: str
        """
        return self._support_arm

    @support_arm.setter
    def support_arm(self, support_arm):
        """Sets the support_arm of this UpdateImageResponse.

        是否是ARM架构类型的镜像，取值为“true”或者“false”。

        :param support_arm: The support_arm of this UpdateImageResponse.
        :type: str
        """
        self._support_arm = support_arm

    @property
    def max_ram(self):
        """Gets the max_ram of this UpdateImageResponse.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :return: The max_ram of this UpdateImageResponse.
        :rtype: str
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        """Sets the max_ram of this UpdateImageResponse.

        镜像支持的最大内存，单位为MB。取值可以参考云服务器规格限制，一般不设置。

        :param max_ram: The max_ram of this UpdateImageResponse.
        :type: str
        """
        self._max_ram = max_ram

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this UpdateImageResponse.

        加密镜像所使用的密钥ID。

        :return: The system__cmkid of this UpdateImageResponse.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this UpdateImageResponse.

        加密镜像所使用的密钥ID。

        :param system__cmkid: The system__cmkid of this UpdateImageResponse.
        :type: str
        """
        self._system__cmkid = system__cmkid

    @property
    def os_feature_list(self):
        """Gets the os_feature_list of this UpdateImageResponse.

        镜像附加属性。该属性采用JSON格式来标识镜像支持的高级特性清单。

        :return: The os_feature_list of this UpdateImageResponse.
        :rtype: str
        """
        return self._os_feature_list

    @os_feature_list.setter
    def os_feature_list(self, os_feature_list):
        """Sets the os_feature_list of this UpdateImageResponse.

        镜像附加属性。该属性采用JSON格式来标识镜像支持的高级特性清单。

        :param os_feature_list: The os_feature_list of this UpdateImageResponse.
        :type: str
        """
        self._os_feature_list = os_feature_list

    @property
    def account_code(self):
        """Gets the account_code of this UpdateImageResponse.

        收费镜像标识。

        :return: The account_code of this UpdateImageResponse.
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this UpdateImageResponse.

        收费镜像标识。

        :param account_code: The account_code of this UpdateImageResponse.
        :type: str
        """
        self._account_code = account_code

    @property
    def hw_vif_multiqueue_enabled(self):
        """Gets the hw_vif_multiqueue_enabled of this UpdateImageResponse.

        镜像是否支持网卡多队列。取值为“true”或者“false”。

        :return: The hw_vif_multiqueue_enabled of this UpdateImageResponse.
        :rtype: str
        """
        return self._hw_vif_multiqueue_enabled

    @hw_vif_multiqueue_enabled.setter
    def hw_vif_multiqueue_enabled(self, hw_vif_multiqueue_enabled):
        """Sets the hw_vif_multiqueue_enabled of this UpdateImageResponse.

        镜像是否支持网卡多队列。取值为“true”或者“false”。

        :param hw_vif_multiqueue_enabled: The hw_vif_multiqueue_enabled of this UpdateImageResponse.
        :type: str
        """
        self._hw_vif_multiqueue_enabled = hw_vif_multiqueue_enabled

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
        if not isinstance(other, UpdateImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
