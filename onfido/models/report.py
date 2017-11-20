# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Report(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, created_at=None, href=None, name=None, status=None, result=None, sub_result=None, variant=None, options=None, breakdown=None, properties=None):
        """
        Report - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'created_at': 'datetime',
            'href': 'str',
            'name': 'str',
            'status': 'str',
            'result': 'str',
            'sub_result': 'str',
            'variant': 'str',
            'options': 'object',
            'breakdown': 'object',
            'properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'href': 'href',
            'name': 'name',
            'status': 'status',
            'result': 'result',
            'sub_result': 'sub_result',
            'variant': 'variant',
            'options': 'options',
            'breakdown': 'breakdown',
            'properties': 'properties'
        }

        self._id = id
        self._created_at = created_at
        self._href = href
        self._name = name
        self._status = status
        self._result = result
        self._sub_result = sub_result
        self._variant = variant
        self._options = options
        self._breakdown = breakdown
        self._properties = properties


    @property
    def id(self):
        """
        Gets the id of this Report.
        The unique identifier for the report.

        :return: The id of this Report.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Report.
        The unique identifier for the report.

        :param id: The id of this Report.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Report.
        The date and time at which the report was first initiated.

        :return: The created_at of this Report.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Report.
        The date and time at which the report was first initiated.

        :param created_at: The created_at of this Report.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def href(self):
        """
        Gets the href of this Report.
        The API endpoint to retrieve the report.

        :return: The href of this Report.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Report.
        The API endpoint to retrieve the report.

        :param href: The href of this Report.
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """
        Gets the name of this Report.
        Report type string identifier.

        :return: The name of this Report.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Report.
        Report type string identifier.

        :param name: The name of this Report.
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this Report.
        The current state of the report in the checking process.

        :return: The status of this Report.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Report.
        The current state of the report in the checking process.

        :param status: The status of this Report.
        :type: str
        """

        self._status = status

    @property
    def result(self):
        """
        Gets the result of this Report.
        The result of the report.

        :return: The result of this Report.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this Report.
        The result of the report.

        :param result: The result of this Report.
        :type: str
        """

        self._result = result

    @property
    def sub_result(self):
        """
        Gets the sub_result of this Report.
        The sub_result of the report. It gives a more detailed result for document reports only, and will be null otherwise.

        :return: The sub_result of this Report.
        :rtype: str
        """
        return self._sub_result

    @sub_result.setter
    def sub_result(self, sub_result):
        """
        Sets the sub_result of this Report.
        The sub_result of the report. It gives a more detailed result for document reports only, and will be null otherwise.

        :param sub_result: The sub_result of this Report.
        :type: str
        """

        self._sub_result = sub_result

    @property
    def variant(self):
        """
        Gets the variant of this Report.
        Report variant string identifier. Some reports e.g. criminal_history have sub-types, which are identified by this field.

        :return: The variant of this Report.
        :rtype: str
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """
        Sets the variant of this Report.
        Report variant string identifier. Some reports e.g. criminal_history have sub-types, which are identified by this field.

        :param variant: The variant of this Report.
        :type: str
        """

        self._variant = variant

    @property
    def options(self):
        """
        Gets the options of this Report.
        Report options. Some reports e.g. criminal_history expose additional options.

        :return: The options of this Report.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Report.
        Report options. Some reports e.g. criminal_history expose additional options.

        :param options: The options of this Report.
        :type: object
        """

        self._options = options

    @property
    def breakdown(self):
        """
        Gets the breakdown of this Report.
        The details of the report. This is specific to each type of report.

        :return: The breakdown of this Report.
        :rtype: object
        """
        return self._breakdown

    @breakdown.setter
    def breakdown(self, breakdown):
        """
        Sets the breakdown of this Report.
        The details of the report. This is specific to each type of report.

        :param breakdown: The breakdown of this Report.
        :type: object
        """

        self._breakdown = breakdown

    @property
    def properties(self):
        """
        Gets the properties of this Report.
        The properties associated with the report, if any.

        :return: The properties of this Report.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Report.
        The properties associated with the report, if any.

        :param properties: The properties of this Report.
        :type: object
        """

        self._properties = properties

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
