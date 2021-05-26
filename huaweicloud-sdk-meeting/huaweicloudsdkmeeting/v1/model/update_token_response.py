# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateTokenResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_token': 'str',
        'token_ip': 'str',
        'valid_period': 'int',
        'expire_time': 'int',
        'create_time': 'int',
        'user': 'UserInfo',
        'client_type': 'int',
        'force_login_ind': 'int',
        'first_login': 'bool',
        'pwd_expired': 'bool',
        'days_pwd_available': 'int',
        'proxy_token': 'ProxyTokenDTO',
        'delay_delete': 'bool',
        'token_type': 'int',
        'refresh_token': 'str',
        'refresh_valid_period': 'int',
        'refresh_expire_time': 'int',
        'refresh_create_time': 'int'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'token_ip': 'tokenIp',
        'valid_period': 'validPeriod',
        'expire_time': 'expireTime',
        'create_time': 'createTime',
        'user': 'user',
        'client_type': 'clientType',
        'force_login_ind': 'forceLoginInd',
        'first_login': 'firstLogin',
        'pwd_expired': 'pwdExpired',
        'days_pwd_available': 'daysPwdAvailable',
        'proxy_token': 'proxyToken',
        'delay_delete': 'delayDelete',
        'token_type': 'tokenType',
        'refresh_token': 'refreshToken',
        'refresh_valid_period': 'refreshValidPeriod',
        'refresh_expire_time': 'refreshExpireTime',
        'refresh_create_time': 'refreshCreateTime'
    }

    def __init__(self, access_token=None, token_ip=None, valid_period=None, expire_time=None, create_time=None, user=None, client_type=None, force_login_ind=None, first_login=None, pwd_expired=None, days_pwd_available=None, proxy_token=None, delay_delete=None, token_type=None, refresh_token=None, refresh_valid_period=None, refresh_expire_time=None, refresh_create_time=None):
        """UpdateTokenResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateTokenResponse, self).__init__()

        self._access_token = None
        self._token_ip = None
        self._valid_period = None
        self._expire_time = None
        self._create_time = None
        self._user = None
        self._client_type = None
        self._force_login_ind = None
        self._first_login = None
        self._pwd_expired = None
        self._days_pwd_available = None
        self._proxy_token = None
        self._delay_delete = None
        self._token_type = None
        self._refresh_token = None
        self._refresh_valid_period = None
        self._refresh_expire_time = None
        self._refresh_create_time = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if token_ip is not None:
            self.token_ip = token_ip
        if valid_period is not None:
            self.valid_period = valid_period
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time
        if user is not None:
            self.user = user
        if client_type is not None:
            self.client_type = client_type
        if force_login_ind is not None:
            self.force_login_ind = force_login_ind
        if first_login is not None:
            self.first_login = first_login
        if pwd_expired is not None:
            self.pwd_expired = pwd_expired
        if days_pwd_available is not None:
            self.days_pwd_available = days_pwd_available
        if proxy_token is not None:
            self.proxy_token = proxy_token
        if delay_delete is not None:
            self.delay_delete = delay_delete
        if token_type is not None:
            self.token_type = token_type
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if refresh_valid_period is not None:
            self.refresh_valid_period = refresh_valid_period
        if refresh_expire_time is not None:
            self.refresh_expire_time = refresh_expire_time
        if refresh_create_time is not None:
            self.refresh_create_time = refresh_create_time

    @property
    def access_token(self):
        """Gets the access_token of this UpdateTokenResponse.

        接入token字符串。

        :return: The access_token of this UpdateTokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this UpdateTokenResponse.

        接入token字符串。

        :param access_token: The access_token of this UpdateTokenResponse.
        :type: str
        """
        self._access_token = access_token

    @property
    def token_ip(self):
        """Gets the token_ip of this UpdateTokenResponse.

        用户IP。

        :return: The token_ip of this UpdateTokenResponse.
        :rtype: str
        """
        return self._token_ip

    @token_ip.setter
    def token_ip(self, token_ip):
        """Sets the token_ip of this UpdateTokenResponse.

        用户IP。

        :param token_ip: The token_ip of this UpdateTokenResponse.
        :type: str
        """
        self._token_ip = token_ip

    @property
    def valid_period(self):
        """Gets the valid_period of this UpdateTokenResponse.

        token有效时长，单位：秒。

        :return: The valid_period of this UpdateTokenResponse.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this UpdateTokenResponse.

        token有效时长，单位：秒。

        :param valid_period: The valid_period of this UpdateTokenResponse.
        :type: int
        """
        self._valid_period = valid_period

    @property
    def expire_time(self):
        """Gets the expire_time of this UpdateTokenResponse.

        token的失效时间戳，单位：秒。

        :return: The expire_time of this UpdateTokenResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UpdateTokenResponse.

        token的失效时间戳，单位：秒。

        :param expire_time: The expire_time of this UpdateTokenResponse.
        :type: int
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        """Gets the create_time of this UpdateTokenResponse.

        业务token的创建时间戳，单位：毫秒。

        :return: The create_time of this UpdateTokenResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateTokenResponse.

        业务token的创建时间戳，单位：毫秒。

        :param create_time: The create_time of this UpdateTokenResponse.
        :type: int
        """
        self._create_time = create_time

    @property
    def user(self):
        """Gets the user of this UpdateTokenResponse.


        :return: The user of this UpdateTokenResponse.
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UpdateTokenResponse.


        :param user: The user of this UpdateTokenResponse.
        :type: UserInfo
        """
        self._user = user

    @property
    def client_type(self):
        """Gets the client_type of this UpdateTokenResponse.

        登录帐号类型。 * 0：Web客户端类型； * 5：cloudlink pc； * 6：cloudlink mobile； * 15：硬终端; * 16：welink pc; * 17：cloudlink 大屏; * 18：welink mobile; * 20：welink 大屏; * 24：cloudlink/welink pad; * 26：智慧屏; * 50：手机客户端; * 51：PAD客户端; * 52：PC客户端; * 53：电视客户端; * 54：大屏客户端。 

        :return: The client_type of this UpdateTokenResponse.
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this UpdateTokenResponse.

        登录帐号类型。 * 0：Web客户端类型； * 5：cloudlink pc； * 6：cloudlink mobile； * 15：硬终端; * 16：welink pc; * 17：cloudlink 大屏; * 18：welink mobile; * 20：welink 大屏; * 24：cloudlink/welink pad; * 26：智慧屏; * 50：手机客户端; * 51：PAD客户端; * 52：PC客户端; * 53：电视客户端; * 54：大屏客户端。 

        :param client_type: The client_type of this UpdateTokenResponse.
        :type: int
        """
        self._client_type = client_type

    @property
    def force_login_ind(self):
        """Gets the force_login_ind of this UpdateTokenResponse.

        抢占登录标识 * 0：非抢占 * 1：抢占  未启用 

        :return: The force_login_ind of this UpdateTokenResponse.
        :rtype: int
        """
        return self._force_login_ind

    @force_login_ind.setter
    def force_login_ind(self, force_login_ind):
        """Sets the force_login_ind of this UpdateTokenResponse.

        抢占登录标识 * 0：非抢占 * 1：抢占  未启用 

        :param force_login_ind: The force_login_ind of this UpdateTokenResponse.
        :type: int
        """
        self._force_login_ind = force_login_ind

    @property
    def first_login(self):
        """Gets the first_login of this UpdateTokenResponse.

        是否首次登录（说明：首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码），默认值：false。

        :return: The first_login of this UpdateTokenResponse.
        :rtype: bool
        """
        return self._first_login

    @first_login.setter
    def first_login(self, first_login):
        """Sets the first_login of this UpdateTokenResponse.

        是否首次登录（说明：首次登录表示尚未修改过密码。首次登录时，系统会提醒用户需要修改密码），默认值：false。

        :param first_login: The first_login of this UpdateTokenResponse.
        :type: bool
        """
        self._first_login = first_login

    @property
    def pwd_expired(self):
        """Gets the pwd_expired of this UpdateTokenResponse.

        密码是否过期，默认值：false。

        :return: The pwd_expired of this UpdateTokenResponse.
        :rtype: bool
        """
        return self._pwd_expired

    @pwd_expired.setter
    def pwd_expired(self, pwd_expired):
        """Sets the pwd_expired of this UpdateTokenResponse.

        密码是否过期，默认值：false。

        :param pwd_expired: The pwd_expired of this UpdateTokenResponse.
        :type: bool
        """
        self._pwd_expired = pwd_expired

    @property
    def days_pwd_available(self):
        """Gets the days_pwd_available of this UpdateTokenResponse.

        密码有效天数

        :return: The days_pwd_available of this UpdateTokenResponse.
        :rtype: int
        """
        return self._days_pwd_available

    @days_pwd_available.setter
    def days_pwd_available(self, days_pwd_available):
        """Sets the days_pwd_available of this UpdateTokenResponse.

        密码有效天数

        :param days_pwd_available: The days_pwd_available of this UpdateTokenResponse.
        :type: int
        """
        self._days_pwd_available = days_pwd_available

    @property
    def proxy_token(self):
        """Gets the proxy_token of this UpdateTokenResponse.


        :return: The proxy_token of this UpdateTokenResponse.
        :rtype: ProxyTokenDTO
        """
        return self._proxy_token

    @proxy_token.setter
    def proxy_token(self, proxy_token):
        """Sets the proxy_token of this UpdateTokenResponse.


        :param proxy_token: The proxy_token of this UpdateTokenResponse.
        :type: ProxyTokenDTO
        """
        self._proxy_token = proxy_token

    @property
    def delay_delete(self):
        """Gets the delay_delete of this UpdateTokenResponse.

        是否延时删除状态

        :return: The delay_delete of this UpdateTokenResponse.
        :rtype: bool
        """
        return self._delay_delete

    @delay_delete.setter
    def delay_delete(self, delay_delete):
        """Sets the delay_delete of this UpdateTokenResponse.

        是否延时删除状态

        :param delay_delete: The delay_delete of this UpdateTokenResponse.
        :type: bool
        """
        self._delay_delete = delay_delete

    @property
    def token_type(self):
        """Gets the token_type of this UpdateTokenResponse.

        token类型 * 0：用户ACCESS TOKEN； * 1：会控TOKEN * 2：一次性TOKEN 

        :return: The token_type of this UpdateTokenResponse.
        :rtype: int
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this UpdateTokenResponse.

        token类型 * 0：用户ACCESS TOKEN； * 1：会控TOKEN * 2：一次性TOKEN 

        :param token_type: The token_type of this UpdateTokenResponse.
        :type: int
        """
        self._token_type = token_type

    @property
    def refresh_token(self):
        """Gets the refresh_token of this UpdateTokenResponse.

        刷新token字符串。

        :return: The refresh_token of this UpdateTokenResponse.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this UpdateTokenResponse.

        刷新token字符串。

        :param refresh_token: The refresh_token of this UpdateTokenResponse.
        :type: str
        """
        self._refresh_token = refresh_token

    @property
    def refresh_valid_period(self):
        """Gets the refresh_valid_period of this UpdateTokenResponse.

        刷新token有效时长，单位：秒。

        :return: The refresh_valid_period of this UpdateTokenResponse.
        :rtype: int
        """
        return self._refresh_valid_period

    @refresh_valid_period.setter
    def refresh_valid_period(self, refresh_valid_period):
        """Sets the refresh_valid_period of this UpdateTokenResponse.

        刷新token有效时长，单位：秒。

        :param refresh_valid_period: The refresh_valid_period of this UpdateTokenResponse.
        :type: int
        """
        self._refresh_valid_period = refresh_valid_period

    @property
    def refresh_expire_time(self):
        """Gets the refresh_expire_time of this UpdateTokenResponse.

        刷新token的失效时间戳，单位：秒。

        :return: The refresh_expire_time of this UpdateTokenResponse.
        :rtype: int
        """
        return self._refresh_expire_time

    @refresh_expire_time.setter
    def refresh_expire_time(self, refresh_expire_time):
        """Sets the refresh_expire_time of this UpdateTokenResponse.

        刷新token的失效时间戳，单位：秒。

        :param refresh_expire_time: The refresh_expire_time of this UpdateTokenResponse.
        :type: int
        """
        self._refresh_expire_time = refresh_expire_time

    @property
    def refresh_create_time(self):
        """Gets the refresh_create_time of this UpdateTokenResponse.

        刷新token的创建时间戳，单位：毫秒。

        :return: The refresh_create_time of this UpdateTokenResponse.
        :rtype: int
        """
        return self._refresh_create_time

    @refresh_create_time.setter
    def refresh_create_time(self, refresh_create_time):
        """Sets the refresh_create_time of this UpdateTokenResponse.

        刷新token的创建时间戳，单位：毫秒。

        :param refresh_create_time: The refresh_create_time of this UpdateTokenResponse.
        :type: int
        """
        self._refresh_create_time = refresh_create_time

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
        if not isinstance(other, UpdateTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
