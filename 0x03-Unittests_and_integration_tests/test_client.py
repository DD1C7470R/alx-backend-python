#!/usr/bin/env python3
"""Test for utilities.py.
"""
import unittest
import utils
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test for TestGithubOrgClient.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("utils.get_json")
    def test_org(self, org_name, mock_get_json):
        mock_get_json.return_value = {"repos_url": "example_value"}
        with patch.object(
            GithubOrgClient, 'org',
            return_value={"repos_url": "example_value"}
        ):
            github_org_client = GithubOrgClient(org_name)
            result = github_org_client.org()

            self.assertEqual(dict(mock_get_json.return_value), dict(result))
            mock_get_json.assert_called_once()

            expected_result = {"repos_url": "example_value"}
            self.assertEqual(dict(result), expected_result)
