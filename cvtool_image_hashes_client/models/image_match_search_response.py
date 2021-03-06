# coding: utf-8

"""
    Kingpick ImageMatch API

    Image Perceptual Hash services. Search for images that look similar to each other.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImageMatchSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, method=None, error=None, status=None, results=None):
        """
        ImageMatchSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'method': 'str',
            'error': 'str',
            'status': 'str',
            'results': 'list[ImageMatchSearchItem]'
        }

        self.attribute_map = {
            'method': 'method',
            'error': 'error',
            'status': 'status',
            'results': 'results'
        }

        self._method = method
        self._error = error
        self._status = status
        self._results = results

    @property
    def method(self):
        """
        Gets the method of this ImageMatchSearchResponse.

        :return: The method of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this ImageMatchSearchResponse.

        :param method: The method of this ImageMatchSearchResponse.
        :type: str
        """

        self._method = method

    @property
    def error(self):
        """
        Gets the error of this ImageMatchSearchResponse.

        :return: The error of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ImageMatchSearchResponse.

        :param error: The error of this ImageMatchSearchResponse.
        :type: str
        """

        self._error = error

    @property
    def status(self):
        """
        Gets the status of this ImageMatchSearchResponse.

        :return: The status of this ImageMatchSearchResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ImageMatchSearchResponse.

        :param status: The status of this ImageMatchSearchResponse.
        :type: str
        """

        self._status = status

    @property
    def results(self):
        """
        Gets the results of this ImageMatchSearchResponse.

        :return: The results of this ImageMatchSearchResponse.
        :rtype: list[ImageMatchSearchItem]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this ImageMatchSearchResponse.

        :param results: The results of this ImageMatchSearchResponse.
        :type: list[ImageMatchSearchItem]
        """

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ImageMatchSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
