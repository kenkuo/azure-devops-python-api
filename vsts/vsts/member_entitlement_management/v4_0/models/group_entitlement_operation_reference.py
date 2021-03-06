# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .operation_reference import OperationReference


class GroupEntitlementOperationReference(OperationReference):
    """GroupEntitlementOperationReference.

    :param id: The identifier for this operation.
    :type id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: Url to get the full object.
    :type url: str
    :param completed: Operation completed with success or failure
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful
    :type have_results_succeeded: bool
    :param results: List of results for each operation
    :type results: list of :class:`GroupOperationResult <member-entitlement-management.v4_0.models.GroupOperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[GroupOperationResult]'}
    }

    def __init__(self, id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(GroupEntitlementOperationReference, self).__init__(id=id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results
