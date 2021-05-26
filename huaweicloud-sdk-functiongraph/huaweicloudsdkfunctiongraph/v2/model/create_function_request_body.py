# coding: utf-8

import pprint
import re

import six





class CreateFunctionRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'func_name': 'str',
        'package': 'str',
        'runtime': 'str',
        'timeout': 'int',
        'handler': 'str',
        'memory_size': 'int',
        'code_type': 'str',
        'code_url': 'str',
        'code_filename': 'str',
        'user_data': 'str',
        'xrole': 'str',
        'app_xrole': 'str',
        'description': 'str',
        'func_code': 'FuncCode',
        'initializer_handler': 'str',
        'initializer_timeout': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'func_name': 'func_name',
        'package': 'package',
        'runtime': 'runtime',
        'timeout': 'timeout',
        'handler': 'handler',
        'memory_size': 'memory_size',
        'code_type': 'code_type',
        'code_url': 'code_url',
        'code_filename': 'code_filename',
        'user_data': 'user_data',
        'xrole': 'xrole',
        'app_xrole': 'app_xrole',
        'description': 'description',
        'func_code': 'func_code',
        'initializer_handler': 'initializer_handler',
        'initializer_timeout': 'initializer_timeout',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, func_name=None, package=None, runtime=None, timeout=None, handler=None, memory_size=None, code_type=None, code_url=None, code_filename=None, user_data=None, xrole=None, app_xrole=None, description=None, func_code=None, initializer_handler=None, initializer_timeout=None, enterprise_project_id=None):
        """CreateFunctionRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._func_name = None
        self._package = None
        self._runtime = None
        self._timeout = None
        self._handler = None
        self._memory_size = None
        self._code_type = None
        self._code_url = None
        self._code_filename = None
        self._user_data = None
        self._xrole = None
        self._app_xrole = None
        self._description = None
        self._func_code = None
        self._initializer_handler = None
        self._initializer_timeout = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.func_name = func_name
        self.package = package
        self.runtime = runtime
        self.timeout = timeout
        self.handler = handler
        self.memory_size = memory_size
        self.code_type = code_type
        if code_url is not None:
            self.code_url = code_url
        if code_filename is not None:
            self.code_filename = code_filename
        if user_data is not None:
            self.user_data = user_data
        if xrole is not None:
            self.xrole = xrole
        if app_xrole is not None:
            self.app_xrole = app_xrole
        if description is not None:
            self.description = description
        if func_code is not None:
            self.func_code = func_code
        if initializer_handler is not None:
            self.initializer_handler = initializer_handler
        if initializer_timeout is not None:
            self.initializer_timeout = initializer_timeout
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def func_name(self):
        """Gets the func_name of this CreateFunctionRequestBody.

        函数名称。

        :return: The func_name of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this CreateFunctionRequestBody.

        函数名称。

        :param func_name: The func_name of this CreateFunctionRequestBody.
        :type: str
        """
        self._func_name = func_name

    @property
    def package(self):
        """Gets the package of this CreateFunctionRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :return: The package of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this CreateFunctionRequestBody.

        函数所属的分组Package，用于用户针对函数的自定义分组。

        :param package: The package of this CreateFunctionRequestBody.
        :type: str
        """
        self._package = package

    @property
    def runtime(self):
        """Gets the runtime of this CreateFunctionRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :return: The runtime of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this CreateFunctionRequestBody.

        FunctionGraph函数的执行环境 支持Node.js6.10、Python2.7、Python3.6、Java8、Go1.8、Node.js 8.10、C#.NET Core 2.0、C#.NET Core 2.1、PHP7.3。 Python2.7: Python语言2.7版本。 Python3.6: Pyton语言3.6版本。 Go1.8: Go语言1.8版本。 Java8: Java语言8版本。 Node.js6.10: Nodejs语言6.10版本。 Node.js8.10: Nodejs语言8.10版本。 C#(.NET Core 2.0): C#语言2.0版本。 C#(.NET Core 2.1): C#语言2.1版本。 C#(.NET Core 3.1): C#语言3.1版本。 Custom: 自定义运行时。 PHP7.3: Php语言7.3版本。

        :param runtime: The runtime of this CreateFunctionRequestBody.
        :type: str
        """
        self._runtime = runtime

    @property
    def timeout(self):
        """Gets the timeout of this CreateFunctionRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :return: The timeout of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateFunctionRequestBody.

        函数执行超时时间，超时函数将被强行停止，范围3～900秒

        :param timeout: The timeout of this CreateFunctionRequestBody.
        :type: int
        """
        self._timeout = timeout

    @property
    def handler(self):
        """Gets the handler of this CreateFunctionRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :return: The handler of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this CreateFunctionRequestBody.

        函数执行入口 规则：xx.xx，必须包含“. ” 举例：对于node.js函数：myfunction.handler，则表示函数的文件名为myfunction.js，执行的入口函数名为handler。

        :param handler: The handler of this CreateFunctionRequestBody.
        :type: str
        """
        self._handler = handler

    @property
    def memory_size(self):
        """Gets the memory_size of this CreateFunctionRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :return: The memory_size of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this CreateFunctionRequestBody.

        函数消耗的内存。 单位M。 取值范围为：128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096。 最小值为128，最大值为4096。

        :param memory_size: The memory_size of this CreateFunctionRequestBody.
        :type: int
        """
        self._memory_size = memory_size

    @property
    def code_type(self):
        """Gets the code_type of this CreateFunctionRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :return: The code_type of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this CreateFunctionRequestBody.

        函数代码类型，取值有4种。 inline: UI在线编辑代码。 zip: 函数代码为zip包。 obs: 函数代码来源于obs存储。 jar: 函数代码为jar包，主要针对Java函数。

        :param code_type: The code_type of this CreateFunctionRequestBody.
        :type: str
        """
        self._code_type = code_type

    @property
    def code_url(self):
        """Gets the code_url of this CreateFunctionRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :return: The code_url of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        """Sets the code_url of this CreateFunctionRequestBody.

        当CodeType为obs时，该值为函数代码包在OBS上的地址，CodeType为其他值时，该字段为空。

        :param code_url: The code_url of this CreateFunctionRequestBody.
        :type: str
        """
        self._code_url = code_url

    @property
    def code_filename(self):
        """Gets the code_filename of this CreateFunctionRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :return: The code_filename of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._code_filename

    @code_filename.setter
    def code_filename(self, code_filename):
        """Sets the code_filename of this CreateFunctionRequestBody.

        函数的文件名，当CodeType为jar/zip时必须提供该字段，inline和obs不需要提供。

        :param code_filename: The code_filename of this CreateFunctionRequestBody.
        :type: str
        """
        self._code_filename = code_filename

    @property
    def user_data(self):
        """Gets the user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :return: The user_data of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this CreateFunctionRequestBody.

        用户自定义的name/value信息。 在函数中使用的参数。 举例：如函数要访问某个主机，可以设置自定义参数：Host={host_ip}，最多定义20个，总长度不超过4KB。

        :param user_data: The user_data of this CreateFunctionRequestBody.
        :type: str
        """
        self._user_data = user_data

    @property
    def xrole(self):
        """Gets the xrole of this CreateFunctionRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The xrole of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._xrole

    @xrole.setter
    def xrole(self, xrole):
        """Sets the xrole of this CreateFunctionRequestBody.

        函数使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param xrole: The xrole of this CreateFunctionRequestBody.
        :type: str
        """
        self._xrole = xrole

    @property
    def app_xrole(self):
        """Gets the app_xrole of this CreateFunctionRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :return: The app_xrole of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._app_xrole

    @app_xrole.setter
    def app_xrole(self, app_xrole):
        """Sets the app_xrole of this CreateFunctionRequestBody.

        函数app使用的权限委托名称，需要IAM支持，并在IAM界面创建委托，当函数需要访问其他服务时，必须提供该字段。

        :param app_xrole: The app_xrole of this CreateFunctionRequestBody.
        :type: str
        """
        self._app_xrole = app_xrole

    @property
    def description(self):
        """Gets the description of this CreateFunctionRequestBody.

        函数描述。

        :return: The description of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFunctionRequestBody.

        函数描述。

        :param description: The description of this CreateFunctionRequestBody.
        :type: str
        """
        self._description = description

    @property
    def func_code(self):
        """Gets the func_code of this CreateFunctionRequestBody.


        :return: The func_code of this CreateFunctionRequestBody.
        :rtype: FuncCode
        """
        return self._func_code

    @func_code.setter
    def func_code(self, func_code):
        """Sets the func_code of this CreateFunctionRequestBody.


        :param func_code: The func_code of this CreateFunctionRequestBody.
        :type: FuncCode
        """
        self._func_code = func_code

    @property
    def initializer_handler(self):
        """Gets the initializer_handler of this CreateFunctionRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :return: The initializer_handler of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._initializer_handler

    @initializer_handler.setter
    def initializer_handler(self, initializer_handler):
        """Sets the initializer_handler of this CreateFunctionRequestBody.

        函数初始化入口，规则：xx.xx，必须包含“. ”。 举例：对于node.js函数：myfunction.initializer，则表示函数的文件名为myfunction.js，初始化的入口函数名为initializer。

        :param initializer_handler: The initializer_handler of this CreateFunctionRequestBody.
        :type: str
        """
        self._initializer_handler = initializer_handler

    @property
    def initializer_timeout(self):
        """Gets the initializer_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :return: The initializer_timeout of this CreateFunctionRequestBody.
        :rtype: int
        """
        return self._initializer_timeout

    @initializer_timeout.setter
    def initializer_timeout(self, initializer_timeout):
        """Sets the initializer_timeout of this CreateFunctionRequestBody.

        初始化超时时间，超时函数将被强行停止，范围1～300秒。

        :param initializer_timeout: The initializer_timeout of this CreateFunctionRequestBody.
        :type: int
        """
        self._initializer_timeout = initializer_timeout

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateFunctionRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :return: The enterprise_project_id of this CreateFunctionRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateFunctionRequestBody.

        企业项目ID，在企业用户创建函数时必填。

        :param enterprise_project_id: The enterprise_project_id of this CreateFunctionRequestBody.
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
        if not isinstance(other, CreateFunctionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
