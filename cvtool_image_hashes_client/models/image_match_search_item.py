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


class ImageMatchSearchItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, score=None, filepath=None, metadata=None):
        """
        ImageMatchSearchItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'score': 'float',
            'filepath': 'str',
            'metadata': 'Metadata'
        }

        self.attribute_map = {
            'score': 'score',
            'filepath': 'filepath',
            'metadata': 'metadata'
        }

        self._score = score
        self._filepath = filepath
        self._metadata = metadata

    @property
    def score(self):
        """
        Gets the score of this ImageMatchSearchItem.

        :return: The score of this ImageMatchSearchItem.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this ImageMatchSearchItem.

        :param score: The score of this ImageMatchSearchItem.
        :type: float
        """

        self._score = score

    @property
    def filepath(self):
        """
        Gets the filepath of this ImageMatchSearchItem.

        :return: The filepath of this ImageMatchSearchItem.
        :rtype: str
        """
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        """
        Sets the filepath of this ImageMatchSearchItem.

        :param filepath: The filepath of this ImageMatchSearchItem.
        :type: str
        """

        self._filepath = filepath

    @property
    def metadata(self):
        """
        Gets the metadata of this ImageMatchSearchItem.

        :return: The metadata of this ImageMatchSearchItem.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ImageMatchSearchItem.

        :param metadata: The metadata of this ImageMatchSearchItem.
        :type: Metadata
        """

        self._metadata = metadata

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
        if not isinstance(other, ImageMatchSearchItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other