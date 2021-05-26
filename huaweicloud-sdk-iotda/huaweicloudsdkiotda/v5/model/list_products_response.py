# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListProductsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'products': 'list[ProductSummary]',
        'page': 'Page'
    }

    attribute_map = {
        'products': 'products',
        'page': 'page'
    }

    def __init__(self, products=None, page=None):
        """ListProductsResponse - a model defined in huaweicloud sdk"""
        
        super(ListProductsResponse, self).__init__()

        self._products = None
        self._page = None
        self.discriminator = None

        if products is not None:
            self.products = products
        if page is not None:
            self.page = page

    @property
    def products(self):
        """Gets the products of this ListProductsResponse.

        产品信息列表。

        :return: The products of this ListProductsResponse.
        :rtype: list[ProductSummary]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ListProductsResponse.

        产品信息列表。

        :param products: The products of this ListProductsResponse.
        :type: list[ProductSummary]
        """
        self._products = products

    @property
    def page(self):
        """Gets the page of this ListProductsResponse.


        :return: The page of this ListProductsResponse.
        :rtype: Page
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListProductsResponse.


        :param page: The page of this ListProductsResponse.
        :type: Page
        """
        self._page = page

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
        if not isinstance(other, ListProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
