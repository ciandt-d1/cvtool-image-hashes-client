# coding: utf-8

"""
    Kingpick ImageMatch API

    Image Perceptual Hash services. Search for images that look similar to each other.

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.image_match_search_item import ImageMatchSearchItem


class TestImageMatchSearchItem(unittest.TestCase):
    """ ImageMatchSearchItem unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImageMatchSearchItem(self):
        """
        Test ImageMatchSearchItem
        """
        model = swagger_client.models.image_match_search_item.ImageMatchSearchItem()


if __name__ == '__main__':
    unittest.main()
