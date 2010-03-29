#!/usr/bin/python
# -*- coding: utf-8 -*-
# req_log/tests.py
""" Reqest log tests """

from tddspry.django import DatabaseTestCase, HttpTestCase
from models import RequestLog


class TestRequestLog(DatabaseTestCase, HttpTestCase):
    """Methods for testing request log"""
    def test_count_logs(self):
        """Go for two URL's and count request logs"""
        self.go("/something")
        self.go("/nonsence_url")

        self.assert_count(RequestLog, 2)
