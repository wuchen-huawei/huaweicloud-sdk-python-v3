# coding: utf-8

import pprint
import re

import six





class QosParticipantInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'conference_id': 'str',
        'participant_id': 'str',
        'user_uuid': 'str',
        'display_name': 'str',
        'dept_name': 'str',
        'terminal_type': 'str',
        'role': 'str',
        'ip_address': 'str',
        'country': 'str',
        'province': 'str',
        'city': 'str',
        'app_version': 'str',
        'join_time': 'int',
        'left_time': 'int',
        'system_info': 'str',
        'network_type': 'str',
        'alarm': 'str',
        'audio_alarm_send': 'str',
        'video_alarm_send': 'str',
        'screen_alarm_send': 'str',
        'audio_alarm_rec': 'str',
        'video_alarm_rec': 'str',
        'screen_alarm_rec': 'str',
        'cpu_alarm': 'str',
        'microphone_info': 'str',
        'speaker_info': 'str',
        'camera_info': 'str',
        'data_center': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'conference_id': 'conferenceID',
        'participant_id': 'participantID',
        'user_uuid': 'userUUID',
        'display_name': 'displayName',
        'dept_name': 'deptName',
        'terminal_type': 'terminalType',
        'role': 'role',
        'ip_address': 'ipAddress',
        'country': 'country',
        'province': 'province',
        'city': 'city',
        'app_version': 'appVersion',
        'join_time': 'joinTime',
        'left_time': 'leftTime',
        'system_info': 'systemInfo',
        'network_type': 'networkType',
        'alarm': 'alarm',
        'audio_alarm_send': 'audioAlarmSend',
        'video_alarm_send': 'videoAlarmSend',
        'screen_alarm_send': 'screenAlarmSend',
        'audio_alarm_rec': 'audioAlarmRec',
        'video_alarm_rec': 'videoAlarmRec',
        'screen_alarm_rec': 'screenAlarmRec',
        'cpu_alarm': 'cpuAlarm',
        'microphone_info': 'microphoneInfo',
        'speaker_info': 'speakerInfo',
        'camera_info': 'cameraInfo',
        'data_center': 'dataCenter'
    }

    def __init__(self, conf_uuid=None, conference_id=None, participant_id=None, user_uuid=None, display_name=None, dept_name=None, terminal_type=None, role=None, ip_address=None, country=None, province=None, city=None, app_version=None, join_time=None, left_time=None, system_info=None, network_type=None, alarm=None, audio_alarm_send=None, video_alarm_send=None, screen_alarm_send=None, audio_alarm_rec=None, video_alarm_rec=None, screen_alarm_rec=None, cpu_alarm=None, microphone_info=None, speaker_info=None, camera_info=None, data_center=None):
        """QosParticipantInfo - a model defined in huaweicloud sdk"""
        
        

        self._conf_uuid = None
        self._conference_id = None
        self._participant_id = None
        self._user_uuid = None
        self._display_name = None
        self._dept_name = None
        self._terminal_type = None
        self._role = None
        self._ip_address = None
        self._country = None
        self._province = None
        self._city = None
        self._app_version = None
        self._join_time = None
        self._left_time = None
        self._system_info = None
        self._network_type = None
        self._alarm = None
        self._audio_alarm_send = None
        self._video_alarm_send = None
        self._screen_alarm_send = None
        self._audio_alarm_rec = None
        self._video_alarm_rec = None
        self._screen_alarm_rec = None
        self._cpu_alarm = None
        self._microphone_info = None
        self._speaker_info = None
        self._camera_info = None
        self._data_center = None
        self.discriminator = None

        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if conference_id is not None:
            self.conference_id = conference_id
        if participant_id is not None:
            self.participant_id = participant_id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if display_name is not None:
            self.display_name = display_name
        if dept_name is not None:
            self.dept_name = dept_name
        if terminal_type is not None:
            self.terminal_type = terminal_type
        if role is not None:
            self.role = role
        if ip_address is not None:
            self.ip_address = ip_address
        if country is not None:
            self.country = country
        if province is not None:
            self.province = province
        if city is not None:
            self.city = city
        if app_version is not None:
            self.app_version = app_version
        if join_time is not None:
            self.join_time = join_time
        if left_time is not None:
            self.left_time = left_time
        if system_info is not None:
            self.system_info = system_info
        if network_type is not None:
            self.network_type = network_type
        if alarm is not None:
            self.alarm = alarm
        if audio_alarm_send is not None:
            self.audio_alarm_send = audio_alarm_send
        if video_alarm_send is not None:
            self.video_alarm_send = video_alarm_send
        if screen_alarm_send is not None:
            self.screen_alarm_send = screen_alarm_send
        if audio_alarm_rec is not None:
            self.audio_alarm_rec = audio_alarm_rec
        if video_alarm_rec is not None:
            self.video_alarm_rec = video_alarm_rec
        if screen_alarm_rec is not None:
            self.screen_alarm_rec = screen_alarm_rec
        if cpu_alarm is not None:
            self.cpu_alarm = cpu_alarm
        if microphone_info is not None:
            self.microphone_info = microphone_info
        if speaker_info is not None:
            self.speaker_info = speaker_info
        if camera_info is not None:
            self.camera_info = camera_info
        if data_center is not None:
            self.data_center = data_center

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this QosParticipantInfo.

        会议的UUID。

        :return: The conf_uuid of this QosParticipantInfo.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this QosParticipantInfo.

        会议的UUID。

        :param conf_uuid: The conf_uuid of this QosParticipantInfo.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conference_id(self):
        """Gets the conference_id of this QosParticipantInfo.

        会议ID。

        :return: The conference_id of this QosParticipantInfo.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this QosParticipantInfo.

        会议ID。

        :param conference_id: The conference_id of this QosParticipantInfo.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def participant_id(self):
        """Gets the participant_id of this QosParticipantInfo.

        入会UUID。

        :return: The participant_id of this QosParticipantInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this QosParticipantInfo.

        入会UUID。

        :param participant_id: The participant_id of this QosParticipantInfo.
        :type: str
        """
        self._participant_id = participant_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this QosParticipantInfo.

        用户UUID。

        :return: The user_uuid of this QosParticipantInfo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this QosParticipantInfo.

        用户UUID。

        :param user_uuid: The user_uuid of this QosParticipantInfo.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def display_name(self):
        """Gets the display_name of this QosParticipantInfo.

        与会者的名称（昵称）。

        :return: The display_name of this QosParticipantInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this QosParticipantInfo.

        与会者的名称（昵称）。

        :param display_name: The display_name of this QosParticipantInfo.
        :type: str
        """
        self._display_name = display_name

    @property
    def dept_name(self):
        """Gets the dept_name of this QosParticipantInfo.

        部门。

        :return: The dept_name of this QosParticipantInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this QosParticipantInfo.

        部门。

        :param dept_name: The dept_name of this QosParticipantInfo.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def terminal_type(self):
        """Gets the terminal_type of this QosParticipantInfo.

        入会终端类型。 - PC: PC机。 - MOBILE: 手机。 - PAD：PAD设备。 - MAC：MAC设备。 - WEB：WEB方式入会，如通过WebRTC入会。 - ROOM: 会议室。 - 硬件终端：显示具体的硬件设备类型，如TE50, HUAWEI IDEAHUB, CISCO等。 - OTHER: 其他设备。

        :return: The terminal_type of this QosParticipantInfo.
        :rtype: str
        """
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, terminal_type):
        """Sets the terminal_type of this QosParticipantInfo.

        入会终端类型。 - PC: PC机。 - MOBILE: 手机。 - PAD：PAD设备。 - MAC：MAC设备。 - WEB：WEB方式入会，如通过WebRTC入会。 - ROOM: 会议室。 - 硬件终端：显示具体的硬件设备类型，如TE50, HUAWEI IDEAHUB, CISCO等。 - OTHER: 其他设备。

        :param terminal_type: The terminal_type of this QosParticipantInfo.
        :type: str
        """
        self._terminal_type = terminal_type

    @property
    def role(self):
        """Gets the role of this QosParticipantInfo.

        与会者角色。 - host：主持人。 - guest：来宾。 - audience：观众。

        :return: The role of this QosParticipantInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this QosParticipantInfo.

        与会者角色。 - host：主持人。 - guest：来宾。 - audience：观众。

        :param role: The role of this QosParticipantInfo.
        :type: str
        """
        self._role = role

    @property
    def ip_address(self):
        """Gets the ip_address of this QosParticipantInfo.

        与会者的IP地址。

        :return: The ip_address of this QosParticipantInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this QosParticipantInfo.

        与会者的IP地址。

        :param ip_address: The ip_address of this QosParticipantInfo.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def country(self):
        """Gets the country of this QosParticipantInfo.

        国家。

        :return: The country of this QosParticipantInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this QosParticipantInfo.

        国家。

        :param country: The country of this QosParticipantInfo.
        :type: str
        """
        self._country = country

    @property
    def province(self):
        """Gets the province of this QosParticipantInfo.

        省市（仅限中国）。

        :return: The province of this QosParticipantInfo.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this QosParticipantInfo.

        省市（仅限中国）。

        :param province: The province of this QosParticipantInfo.
        :type: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this QosParticipantInfo.

        城市（仅限中国）。

        :return: The city of this QosParticipantInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this QosParticipantInfo.

        城市（仅限中国）。

        :param city: The city of this QosParticipantInfo.
        :type: str
        """
        self._city = city

    @property
    def app_version(self):
        """Gets the app_version of this QosParticipantInfo.

        华为云会议APP版本。

        :return: The app_version of this QosParticipantInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this QosParticipantInfo.

        华为云会议APP版本。

        :param app_version: The app_version of this QosParticipantInfo.
        :type: str
        """
        self._app_version = app_version

    @property
    def join_time(self):
        """Gets the join_time of this QosParticipantInfo.

        入会时间(UTC时间), Unix时间戳（单位毫秒）。

        :return: The join_time of this QosParticipantInfo.
        :rtype: int
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this QosParticipantInfo.

        入会时间(UTC时间), Unix时间戳（单位毫秒）。

        :param join_time: The join_time of this QosParticipantInfo.
        :type: int
        """
        self._join_time = join_time

    @property
    def left_time(self):
        """Gets the left_time of this QosParticipantInfo.

        离会时间(UTC时间), Unix时间戳（单位毫秒）。 说明： * 与会者未离会：leftTime = 0。 * 与会者已离会：leftTime = 实际离会时间。

        :return: The left_time of this QosParticipantInfo.
        :rtype: int
        """
        return self._left_time

    @left_time.setter
    def left_time(self, left_time):
        """Sets the left_time of this QosParticipantInfo.

        离会时间(UTC时间), Unix时间戳（单位毫秒）。 说明： * 与会者未离会：leftTime = 0。 * 与会者已离会：leftTime = 实际离会时间。

        :param left_time: The left_time of this QosParticipantInfo.
        :type: int
        """
        self._left_time = left_time

    @property
    def system_info(self):
        """Gets the system_info of this QosParticipantInfo.

        系统信息。

        :return: The system_info of this QosParticipantInfo.
        :rtype: str
        """
        return self._system_info

    @system_info.setter
    def system_info(self, system_info):
        """Sets the system_info of this QosParticipantInfo.

        系统信息。

        :param system_info: The system_info of this QosParticipantInfo.
        :type: str
        """
        self._system_info = system_info

    @property
    def network_type(self):
        """Gets the network_type of this QosParticipantInfo.

        网络类型。

        :return: The network_type of this QosParticipantInfo.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this QosParticipantInfo.

        网络类型。

        :param network_type: The network_type of this QosParticipantInfo.
        :type: str
        """
        self._network_type = network_type

    @property
    def alarm(self):
        """Gets the alarm of this QosParticipantInfo.

        总体告警 YES/NO。 说明： * 音频（发送/接收），视频（发送/接收），屏幕共享（发送/接收），CPU任一项产生告警，总体告警状态即为 YES。

        :return: The alarm of this QosParticipantInfo.
        :rtype: str
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """Sets the alarm of this QosParticipantInfo.

        总体告警 YES/NO。 说明： * 音频（发送/接收），视频（发送/接收），屏幕共享（发送/接收），CPU任一项产生告警，总体告警状态即为 YES。

        :param alarm: The alarm of this QosParticipantInfo.
        :type: str
        """
        self._alarm = alarm

    @property
    def audio_alarm_send(self):
        """Gets the audio_alarm_send of this QosParticipantInfo.

        音频发送告警 YES / NO。 说明： * 发送音频的抖动，时延，丢包率任一项产生阈值告警，则音频发送告警状态为YES。

        :return: The audio_alarm_send of this QosParticipantInfo.
        :rtype: str
        """
        return self._audio_alarm_send

    @audio_alarm_send.setter
    def audio_alarm_send(self, audio_alarm_send):
        """Sets the audio_alarm_send of this QosParticipantInfo.

        音频发送告警 YES / NO。 说明： * 发送音频的抖动，时延，丢包率任一项产生阈值告警，则音频发送告警状态为YES。

        :param audio_alarm_send: The audio_alarm_send of this QosParticipantInfo.
        :type: str
        """
        self._audio_alarm_send = audio_alarm_send

    @property
    def video_alarm_send(self):
        """Gets the video_alarm_send of this QosParticipantInfo.

        视频发送告警 YES / NO。 说明： * 发送视频的抖动，时延，丢包率，分辨率任一项产生阈值告警，则视频发送告警状态为YES。

        :return: The video_alarm_send of this QosParticipantInfo.
        :rtype: str
        """
        return self._video_alarm_send

    @video_alarm_send.setter
    def video_alarm_send(self, video_alarm_send):
        """Sets the video_alarm_send of this QosParticipantInfo.

        视频发送告警 YES / NO。 说明： * 发送视频的抖动，时延，丢包率，分辨率任一项产生阈值告警，则视频发送告警状态为YES。

        :param video_alarm_send: The video_alarm_send of this QosParticipantInfo.
        :type: str
        """
        self._video_alarm_send = video_alarm_send

    @property
    def screen_alarm_send(self):
        """Gets the screen_alarm_send of this QosParticipantInfo.

        屏幕共享发送告警 YES / NO。 说明： * 发送屏幕共享的抖动，时延，丢包率任一项产生阈值告警，则屏幕共享发送告警状态为YES。

        :return: The screen_alarm_send of this QosParticipantInfo.
        :rtype: str
        """
        return self._screen_alarm_send

    @screen_alarm_send.setter
    def screen_alarm_send(self, screen_alarm_send):
        """Sets the screen_alarm_send of this QosParticipantInfo.

        屏幕共享发送告警 YES / NO。 说明： * 发送屏幕共享的抖动，时延，丢包率任一项产生阈值告警，则屏幕共享发送告警状态为YES。

        :param screen_alarm_send: The screen_alarm_send of this QosParticipantInfo.
        :type: str
        """
        self._screen_alarm_send = screen_alarm_send

    @property
    def audio_alarm_rec(self):
        """Gets the audio_alarm_rec of this QosParticipantInfo.

        音频接收告警 YES / NO。 说明： * 接收音频的抖动，时延，丢包率任一项产生阈值告警，则音频接收告警状态为YES。

        :return: The audio_alarm_rec of this QosParticipantInfo.
        :rtype: str
        """
        return self._audio_alarm_rec

    @audio_alarm_rec.setter
    def audio_alarm_rec(self, audio_alarm_rec):
        """Sets the audio_alarm_rec of this QosParticipantInfo.

        音频接收告警 YES / NO。 说明： * 接收音频的抖动，时延，丢包率任一项产生阈值告警，则音频接收告警状态为YES。

        :param audio_alarm_rec: The audio_alarm_rec of this QosParticipantInfo.
        :type: str
        """
        self._audio_alarm_rec = audio_alarm_rec

    @property
    def video_alarm_rec(self):
        """Gets the video_alarm_rec of this QosParticipantInfo.

        视频接收告警 YES / NO。 说明： * 接收视频的抖动，时延，丢包率任一项产生阈值告警，则视频接收告警状态为YES。

        :return: The video_alarm_rec of this QosParticipantInfo.
        :rtype: str
        """
        return self._video_alarm_rec

    @video_alarm_rec.setter
    def video_alarm_rec(self, video_alarm_rec):
        """Sets the video_alarm_rec of this QosParticipantInfo.

        视频接收告警 YES / NO。 说明： * 接收视频的抖动，时延，丢包率任一项产生阈值告警，则视频接收告警状态为YES。

        :param video_alarm_rec: The video_alarm_rec of this QosParticipantInfo.
        :type: str
        """
        self._video_alarm_rec = video_alarm_rec

    @property
    def screen_alarm_rec(self):
        """Gets the screen_alarm_rec of this QosParticipantInfo.

        屏幕共享接收告警 YES / NO。 说明： * 接收屏幕共享的抖动，时延，丢包率任一项产生阈值告警，则屏幕共享接收告警状态为YES。

        :return: The screen_alarm_rec of this QosParticipantInfo.
        :rtype: str
        """
        return self._screen_alarm_rec

    @screen_alarm_rec.setter
    def screen_alarm_rec(self, screen_alarm_rec):
        """Sets the screen_alarm_rec of this QosParticipantInfo.

        屏幕共享接收告警 YES / NO。 说明： * 接收屏幕共享的抖动，时延，丢包率任一项产生阈值告警，则屏幕共享接收告警状态为YES。

        :param screen_alarm_rec: The screen_alarm_rec of this QosParticipantInfo.
        :type: str
        """
        self._screen_alarm_rec = screen_alarm_rec

    @property
    def cpu_alarm(self):
        """Gets the cpu_alarm of this QosParticipantInfo.

        CPU告警 YES / NO。 说明： * 端侧的APP最大CPU使用率或系统最大CPU使用率任一项产生阈值告警，则CPU告警状态为YES。

        :return: The cpu_alarm of this QosParticipantInfo.
        :rtype: str
        """
        return self._cpu_alarm

    @cpu_alarm.setter
    def cpu_alarm(self, cpu_alarm):
        """Sets the cpu_alarm of this QosParticipantInfo.

        CPU告警 YES / NO。 说明： * 端侧的APP最大CPU使用率或系统最大CPU使用率任一项产生阈值告警，则CPU告警状态为YES。

        :param cpu_alarm: The cpu_alarm of this QosParticipantInfo.
        :type: str
        """
        self._cpu_alarm = cpu_alarm

    @property
    def microphone_info(self):
        """Gets the microphone_info of this QosParticipantInfo.

        麦克风。

        :return: The microphone_info of this QosParticipantInfo.
        :rtype: str
        """
        return self._microphone_info

    @microphone_info.setter
    def microphone_info(self, microphone_info):
        """Sets the microphone_info of this QosParticipantInfo.

        麦克风。

        :param microphone_info: The microphone_info of this QosParticipantInfo.
        :type: str
        """
        self._microphone_info = microphone_info

    @property
    def speaker_info(self):
        """Gets the speaker_info of this QosParticipantInfo.

        扬声器。

        :return: The speaker_info of this QosParticipantInfo.
        :rtype: str
        """
        return self._speaker_info

    @speaker_info.setter
    def speaker_info(self, speaker_info):
        """Sets the speaker_info of this QosParticipantInfo.

        扬声器。

        :param speaker_info: The speaker_info of this QosParticipantInfo.
        :type: str
        """
        self._speaker_info = speaker_info

    @property
    def camera_info(self):
        """Gets the camera_info of this QosParticipantInfo.

        摄像头。

        :return: The camera_info of this QosParticipantInfo.
        :rtype: str
        """
        return self._camera_info

    @camera_info.setter
    def camera_info(self, camera_info):
        """Sets the camera_info of this QosParticipantInfo.

        摄像头。

        :param camera_info: The camera_info of this QosParticipantInfo.
        :type: str
        """
        self._camera_info = camera_info

    @property
    def data_center(self):
        """Gets the data_center of this QosParticipantInfo.

        数据中心。

        :return: The data_center of this QosParticipantInfo.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this QosParticipantInfo.

        数据中心。

        :param data_center: The data_center of this QosParticipantInfo.
        :type: str
        """
        self._data_center = data_center

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
        if not isinstance(other, QosParticipantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
