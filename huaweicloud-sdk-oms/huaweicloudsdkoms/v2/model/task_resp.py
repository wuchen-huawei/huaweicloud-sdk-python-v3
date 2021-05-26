# coding: utf-8

import pprint
import re

import six





class TaskResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'complete_size': 'int',
        'description': 'str',
        'dst_node': 'DstNodeResp',
        'enable_failed_object_recording': 'bool',
        'enable_kms': 'bool',
        'enable_restore': 'bool',
        'error_reason': 'ErrorReasonResp',
        'failed_num': 'int',
        'failed_object_record': 'FailedObjectRecordDto',
        'group_id': 'str',
        'id': 'int',
        'is_query_over': 'bool',
        'left_time': 'int',
        'migrate_since': 'int',
        'migrate_speed': 'int',
        'name': 'str',
        'progress': 'float',
        'real_size': 'int',
        'skipped_num': 'int',
        'src_node': 'SrcNodeResp',
        'start_time': 'int',
        'status': 'int',
        'successful_num': 'int',
        'task_type': 'str',
        'total_num': 'int',
        'total_size': 'int',
        'total_time': 'int',
        'smn_info': 'SmnInfo',
        'source_cdn': 'SourceCdnResp'
    }

    attribute_map = {
        'bandwidth_policy': 'bandwidth_policy',
        'complete_size': 'complete_size',
        'description': 'description',
        'dst_node': 'dst_node',
        'enable_failed_object_recording': 'enable_failed_object_recording',
        'enable_kms': 'enable_kms',
        'enable_restore': 'enable_restore',
        'error_reason': 'error_reason',
        'failed_num': 'failed_num',
        'failed_object_record': 'failed_object_record',
        'group_id': 'group_id',
        'id': 'id',
        'is_query_over': 'is_query_over',
        'left_time': 'left_time',
        'migrate_since': 'migrate_since',
        'migrate_speed': 'migrate_speed',
        'name': 'name',
        'progress': 'progress',
        'real_size': 'real_size',
        'skipped_num': 'skipped_num',
        'src_node': 'src_node',
        'start_time': 'start_time',
        'status': 'status',
        'successful_num': 'successful_num',
        'task_type': 'task_type',
        'total_num': 'total_num',
        'total_size': 'total_size',
        'total_time': 'total_time',
        'smn_info': 'smn_info',
        'source_cdn': 'source_cdn'
    }

    def __init__(self, bandwidth_policy=None, complete_size=None, description=None, dst_node=None, enable_failed_object_recording=None, enable_kms=None, enable_restore=None, error_reason=None, failed_num=None, failed_object_record=None, group_id=None, id=None, is_query_over=None, left_time=None, migrate_since=None, migrate_speed=None, name=None, progress=None, real_size=None, skipped_num=None, src_node=None, start_time=None, status=None, successful_num=None, task_type=None, total_num=None, total_size=None, total_time=None, smn_info=None, source_cdn=None):
        """TaskResp - a model defined in huaweicloud sdk"""
        
        

        self._bandwidth_policy = None
        self._complete_size = None
        self._description = None
        self._dst_node = None
        self._enable_failed_object_recording = None
        self._enable_kms = None
        self._enable_restore = None
        self._error_reason = None
        self._failed_num = None
        self._failed_object_record = None
        self._group_id = None
        self._id = None
        self._is_query_over = None
        self._left_time = None
        self._migrate_since = None
        self._migrate_speed = None
        self._name = None
        self._progress = None
        self._real_size = None
        self._skipped_num = None
        self._src_node = None
        self._start_time = None
        self._status = None
        self._successful_num = None
        self._task_type = None
        self._total_num = None
        self._total_size = None
        self._total_time = None
        self._smn_info = None
        self._source_cdn = None
        self.discriminator = None

        if bandwidth_policy is not None:
            self.bandwidth_policy = bandwidth_policy
        if complete_size is not None:
            self.complete_size = complete_size
        if description is not None:
            self.description = description
        if dst_node is not None:
            self.dst_node = dst_node
        if enable_failed_object_recording is not None:
            self.enable_failed_object_recording = enable_failed_object_recording
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if error_reason is not None:
            self.error_reason = error_reason
        if failed_num is not None:
            self.failed_num = failed_num
        if failed_object_record is not None:
            self.failed_object_record = failed_object_record
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if is_query_over is not None:
            self.is_query_over = is_query_over
        if left_time is not None:
            self.left_time = left_time
        if migrate_since is not None:
            self.migrate_since = migrate_since
        if migrate_speed is not None:
            self.migrate_speed = migrate_speed
        if name is not None:
            self.name = name
        if progress is not None:
            self.progress = progress
        if real_size is not None:
            self.real_size = real_size
        if skipped_num is not None:
            self.skipped_num = skipped_num
        if src_node is not None:
            self.src_node = src_node
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if successful_num is not None:
            self.successful_num = successful_num
        if task_type is not None:
            self.task_type = task_type
        if total_num is not None:
            self.total_num = total_num
        if total_size is not None:
            self.total_size = total_size
        if total_time is not None:
            self.total_time = total_time
        if smn_info is not None:
            self.smn_info = smn_info
        if source_cdn is not None:
            self.source_cdn = source_cdn

    @property
    def bandwidth_policy(self):
        """Gets the bandwidth_policy of this TaskResp.

        流量控制策略，每个任务最多可设置5条限速策略。

        :return: The bandwidth_policy of this TaskResp.
        :rtype: list[BandwidthPolicyDto]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        """Sets the bandwidth_policy of this TaskResp.

        流量控制策略，每个任务最多可设置5条限速策略。

        :param bandwidth_policy: The bandwidth_policy of this TaskResp.
        :type: list[BandwidthPolicyDto]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def complete_size(self):
        """Gets the complete_size of this TaskResp.

        任务迁移完成大小（Byte）。

        :return: The complete_size of this TaskResp.
        :rtype: int
        """
        return self._complete_size

    @complete_size.setter
    def complete_size(self, complete_size):
        """Sets the complete_size of this TaskResp.

        任务迁移完成大小（Byte）。

        :param complete_size: The complete_size of this TaskResp.
        :type: int
        """
        self._complete_size = complete_size

    @property
    def description(self):
        """Gets the description of this TaskResp.

        任务描述，没有设置时为空字符串。

        :return: The description of this TaskResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskResp.

        任务描述，没有设置时为空字符串。

        :param description: The description of this TaskResp.
        :type: str
        """
        self._description = description

    @property
    def dst_node(self):
        """Gets the dst_node of this TaskResp.


        :return: The dst_node of this TaskResp.
        :rtype: DstNodeResp
        """
        return self._dst_node

    @dst_node.setter
    def dst_node(self, dst_node):
        """Sets the dst_node of this TaskResp.


        :param dst_node: The dst_node of this TaskResp.
        :type: DstNodeResp
        """
        self._dst_node = dst_node

    @property
    def enable_failed_object_recording(self):
        """Gets the enable_failed_object_recording of this TaskResp.

        是否记录失败对象。开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :return: The enable_failed_object_recording of this TaskResp.
        :rtype: bool
        """
        return self._enable_failed_object_recording

    @enable_failed_object_recording.setter
    def enable_failed_object_recording(self, enable_failed_object_recording):
        """Sets the enable_failed_object_recording of this TaskResp.

        是否记录失败对象。开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :param enable_failed_object_recording: The enable_failed_object_recording of this TaskResp.
        :type: bool
        """
        self._enable_failed_object_recording = enable_failed_object_recording

    @property
    def enable_kms(self):
        """Gets the enable_kms of this TaskResp.

        存储入OBS时是否使用KMS加密。

        :return: The enable_kms of this TaskResp.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        """Sets the enable_kms of this TaskResp.

        存储入OBS时是否使用KMS加密。

        :param enable_kms: The enable_kms of this TaskResp.
        :type: bool
        """
        self._enable_kms = enable_kms

    @property
    def enable_restore(self):
        """Gets the enable_restore of this TaskResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :return: The enable_restore of this TaskResp.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        """Sets the enable_restore of this TaskResp.

        是否自动解冻归档数据，（由于对象存储解冻需要源端存储等待一定时间，开启自动解冻会对迁移速度有较大影响，建议先完成归档存储数据解冻后再启动迁移）。 开启后，如果遇到归档类型数据，会自动解冻再进行迁移；如果遇到归档类型的对象直接跳过相应对象，系统默认对象迁移失败并记录相关信息到失败对象列表中。

        :param enable_restore: The enable_restore of this TaskResp.
        :type: bool
        """
        self._enable_restore = enable_restore

    @property
    def error_reason(self):
        """Gets the error_reason of this TaskResp.


        :return: The error_reason of this TaskResp.
        :rtype: ErrorReasonResp
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        """Sets the error_reason of this TaskResp.


        :param error_reason: The error_reason of this TaskResp.
        :type: ErrorReasonResp
        """
        self._error_reason = error_reason

    @property
    def failed_num(self):
        """Gets the failed_num of this TaskResp.

        迁移失败对象数量。

        :return: The failed_num of this TaskResp.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this TaskResp.

        迁移失败对象数量。

        :param failed_num: The failed_num of this TaskResp.
        :type: int
        """
        self._failed_num = failed_num

    @property
    def failed_object_record(self):
        """Gets the failed_object_record of this TaskResp.


        :return: The failed_object_record of this TaskResp.
        :rtype: FailedObjectRecordDto
        """
        return self._failed_object_record

    @failed_object_record.setter
    def failed_object_record(self, failed_object_record):
        """Sets the failed_object_record of this TaskResp.


        :param failed_object_record: The failed_object_record of this TaskResp.
        :type: FailedObjectRecordDto
        """
        self._failed_object_record = failed_object_record

    @property
    def group_id(self):
        """Gets the group_id of this TaskResp.

        迁移任务组ID，当任务由迁移任务组创建时会包含迁移任务组的id信息。

        :return: The group_id of this TaskResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this TaskResp.

        迁移任务组ID，当任务由迁移任务组创建时会包含迁移任务组的id信息。

        :param group_id: The group_id of this TaskResp.
        :type: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this TaskResp.

        任务ID。

        :return: The id of this TaskResp.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskResp.

        任务ID。

        :param id: The id of this TaskResp.
        :type: int
        """
        self._id = id

    @property
    def is_query_over(self):
        """Gets the is_query_over of this TaskResp.

        迁移任务是否完成源端对象统计数据扫描。

        :return: The is_query_over of this TaskResp.
        :rtype: bool
        """
        return self._is_query_over

    @is_query_over.setter
    def is_query_over(self, is_query_over):
        """Sets the is_query_over of this TaskResp.

        迁移任务是否完成源端对象统计数据扫描。

        :param is_query_over: The is_query_over of this TaskResp.
        :type: bool
        """
        self._is_query_over = is_query_over

    @property
    def left_time(self):
        """Gets the left_time of this TaskResp.

        任务剩余时间（毫秒）。

        :return: The left_time of this TaskResp.
        :rtype: int
        """
        return self._left_time

    @left_time.setter
    def left_time(self, left_time):
        """Sets the left_time of this TaskResp.

        任务剩余时间（毫秒）。

        :param left_time: The left_time of this TaskResp.
        :type: int
        """
        self._left_time = left_time

    @property
    def migrate_since(self):
        """Gets the migrate_since of this TaskResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :return: The migrate_since of this TaskResp.
        :rtype: int
        """
        return self._migrate_since

    @migrate_since.setter
    def migrate_since(self, migrate_since):
        """Sets the migrate_since of this TaskResp.

        迁移指定时间（时间戳，毫秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认为0，表示不设置迁移指定时间。

        :param migrate_since: The migrate_since of this TaskResp.
        :type: int
        """
        self._migrate_since = migrate_since

    @property
    def migrate_speed(self):
        """Gets the migrate_speed of this TaskResp.

        任务迁移速度（Byte/s）。

        :return: The migrate_speed of this TaskResp.
        :rtype: int
        """
        return self._migrate_speed

    @migrate_speed.setter
    def migrate_speed(self, migrate_speed):
        """Sets the migrate_speed of this TaskResp.

        任务迁移速度（Byte/s）。

        :param migrate_speed: The migrate_speed of this TaskResp.
        :type: int
        """
        self._migrate_speed = migrate_speed

    @property
    def name(self):
        """Gets the name of this TaskResp.

        任务名称。

        :return: The name of this TaskResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskResp.

        任务名称。

        :param name: The name of this TaskResp.
        :type: str
        """
        self._name = name

    @property
    def progress(self):
        """Gets the progress of this TaskResp.

        任务进度，例如：0.522代表任务进度为52.2%，1代表任务进度为100%。

        :return: The progress of this TaskResp.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this TaskResp.

        任务进度，例如：0.522代表任务进度为52.2%，1代表任务进度为100%。

        :param progress: The progress of this TaskResp.
        :type: float
        """
        self._progress = progress

    @property
    def real_size(self):
        """Gets the real_size of this TaskResp.

        实际迁移对象总大小（Byte），忽略对象的大小不会统计在内。

        :return: The real_size of this TaskResp.
        :rtype: int
        """
        return self._real_size

    @real_size.setter
    def real_size(self, real_size):
        """Sets the real_size of this TaskResp.

        实际迁移对象总大小（Byte），忽略对象的大小不会统计在内。

        :param real_size: The real_size of this TaskResp.
        :type: int
        """
        self._real_size = real_size

    @property
    def skipped_num(self):
        """Gets the skipped_num of this TaskResp.

        迁移忽略对象数（存在以下两种情况会自动跳过：1.源端对象最后修改时间在迁移指定时间前；2.目的端已有该对象。）

        :return: The skipped_num of this TaskResp.
        :rtype: int
        """
        return self._skipped_num

    @skipped_num.setter
    def skipped_num(self, skipped_num):
        """Sets the skipped_num of this TaskResp.

        迁移忽略对象数（存在以下两种情况会自动跳过：1.源端对象最后修改时间在迁移指定时间前；2.目的端已有该对象。）

        :param skipped_num: The skipped_num of this TaskResp.
        :type: int
        """
        self._skipped_num = skipped_num

    @property
    def src_node(self):
        """Gets the src_node of this TaskResp.


        :return: The src_node of this TaskResp.
        :rtype: SrcNodeResp
        """
        return self._src_node

    @src_node.setter
    def src_node(self, src_node):
        """Sets the src_node of this TaskResp.


        :param src_node: The src_node of this TaskResp.
        :type: SrcNodeResp
        """
        self._src_node = src_node

    @property
    def start_time(self):
        """Gets the start_time of this TaskResp.

        任务启动时间（Unix时间戳，毫秒）。

        :return: The start_time of this TaskResp.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskResp.

        任务启动时间（Unix时间戳，毫秒）。

        :param start_time: The start_time of this TaskResp.
        :type: int
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this TaskResp.

        任务状态。 1：等待调度 2：正在执行 3：停止 4：失败 5：成功

        :return: The status of this TaskResp.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskResp.

        任务状态。 1：等待调度 2：正在执行 3：停止 4：失败 5：成功

        :param status: The status of this TaskResp.
        :type: int
        """
        self._status = status

    @property
    def successful_num(self):
        """Gets the successful_num of this TaskResp.

        迁移成功对象数量。

        :return: The successful_num of this TaskResp.
        :rtype: int
        """
        return self._successful_num

    @successful_num.setter
    def successful_num(self, successful_num):
        """Sets the successful_num of this TaskResp.

        迁移成功对象数量。

        :param successful_num: The successful_num of this TaskResp.
        :type: int
        """
        self._successful_num = successful_num

    @property
    def task_type(self):
        """Gets the task_type of this TaskResp.

        任务类型，为空默认设置为object。 list：对象列表迁移 object：文件/文件夹迁移 prefix：对象前缀迁移 url_list: url对象列表

        :return: The task_type of this TaskResp.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskResp.

        任务类型，为空默认设置为object。 list：对象列表迁移 object：文件/文件夹迁移 prefix：对象前缀迁移 url_list: url对象列表

        :param task_type: The task_type of this TaskResp.
        :type: str
        """
        self._task_type = task_type

    @property
    def total_num(self):
        """Gets the total_num of this TaskResp.

        迁移任务对象总数量。

        :return: The total_num of this TaskResp.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this TaskResp.

        迁移任务对象总数量。

        :param total_num: The total_num of this TaskResp.
        :type: int
        """
        self._total_num = total_num

    @property
    def total_size(self):
        """Gets the total_size of this TaskResp.

        任务迁移总大小（Byte）。

        :return: The total_size of this TaskResp.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this TaskResp.

        任务迁移总大小（Byte）。

        :param total_size: The total_size of this TaskResp.
        :type: int
        """
        self._total_size = total_size

    @property
    def total_time(self):
        """Gets the total_time of this TaskResp.

        任务总耗时（毫秒）。

        :return: The total_time of this TaskResp.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this TaskResp.

        任务总耗时（毫秒）。

        :param total_time: The total_time of this TaskResp.
        :type: int
        """
        self._total_time = total_time

    @property
    def smn_info(self):
        """Gets the smn_info of this TaskResp.


        :return: The smn_info of this TaskResp.
        :rtype: SmnInfo
        """
        return self._smn_info

    @smn_info.setter
    def smn_info(self, smn_info):
        """Sets the smn_info of this TaskResp.


        :param smn_info: The smn_info of this TaskResp.
        :type: SmnInfo
        """
        self._smn_info = smn_info

    @property
    def source_cdn(self):
        """Gets the source_cdn of this TaskResp.


        :return: The source_cdn of this TaskResp.
        :rtype: SourceCdnResp
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        """Sets the source_cdn of this TaskResp.


        :param source_cdn: The source_cdn of this TaskResp.
        :type: SourceCdnResp
        """
        self._source_cdn = source_cdn

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
        if not isinstance(other, TaskResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
