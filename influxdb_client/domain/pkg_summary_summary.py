# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PkgSummarySummary(object):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'buckets': 'list[Bucket]',
        'labels': 'list[Label]',
        'dashboards': 'list[PkgSummarySummaryDashboards]',
        'label_mappings': 'list[PkgSummarySummaryLabelMappings]',
        'variables': 'list[Variable]'
    }

    attribute_map = {
        'buckets': 'buckets',
        'labels': 'labels',
        'dashboards': 'dashboards',
        'label_mappings': 'labelMappings',
        'variables': 'variables'
    }

    def __init__(self, buckets=None, labels=None, dashboards=None, label_mappings=None, variables=None):  # noqa: E501,D401,D403
        """PkgSummarySummary - a model defined in OpenAPI."""  # noqa: E501
        self._buckets = None
        self._labels = None
        self._dashboards = None
        self._label_mappings = None
        self._variables = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets
        if labels is not None:
            self.labels = labels
        if dashboards is not None:
            self.dashboards = dashboards
        if label_mappings is not None:
            self.label_mappings = label_mappings
        if variables is not None:
            self.variables = variables

    @property
    def buckets(self):
        """Get the buckets of this PkgSummarySummary.

        :return: The buckets of this PkgSummarySummary.
        :rtype: list[Bucket]
        """  # noqa: E501
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Set the buckets of this PkgSummarySummary.

        :param buckets: The buckets of this PkgSummarySummary.
        :type: list[Bucket]
        """  # noqa: E501
        self._buckets = buckets

    @property
    def labels(self):
        """Get the labels of this PkgSummarySummary.

        :return: The labels of this PkgSummarySummary.
        :rtype: list[Label]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this PkgSummarySummary.

        :param labels: The labels of this PkgSummarySummary.
        :type: list[Label]
        """  # noqa: E501
        self._labels = labels

    @property
    def dashboards(self):
        """Get the dashboards of this PkgSummarySummary.

        :return: The dashboards of this PkgSummarySummary.
        :rtype: list[PkgSummarySummaryDashboards]
        """  # noqa: E501
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Set the dashboards of this PkgSummarySummary.

        :param dashboards: The dashboards of this PkgSummarySummary.
        :type: list[PkgSummarySummaryDashboards]
        """  # noqa: E501
        self._dashboards = dashboards

    @property
    def label_mappings(self):
        """Get the label_mappings of this PkgSummarySummary.

        :return: The label_mappings of this PkgSummarySummary.
        :rtype: list[PkgSummarySummaryLabelMappings]
        """  # noqa: E501
        return self._label_mappings

    @label_mappings.setter
    def label_mappings(self, label_mappings):
        """Set the label_mappings of this PkgSummarySummary.

        :param label_mappings: The label_mappings of this PkgSummarySummary.
        :type: list[PkgSummarySummaryLabelMappings]
        """  # noqa: E501
        self._label_mappings = label_mappings

    @property
    def variables(self):
        """Get the variables of this PkgSummarySummary.

        :return: The variables of this PkgSummarySummary.
        :rtype: list[Variable]
        """  # noqa: E501
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Set the variables of this PkgSummarySummary.

        :param variables: The variables of this PkgSummarySummary.
        :type: list[Variable]
        """  # noqa: E501
        self._variables = variables

    def to_dict(self):
        """Return the model properties as a dict."""
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
                result[attr] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, PkgSummarySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
