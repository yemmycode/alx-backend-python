#!/usr/bin/env python3
"""Module for testing the `client` module functionality."""

import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict, mocked_get_json: MagicMock) -> None:
        """Verifies the `org` method's behavior."""
        mocked_get_json.return_value = response
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), response)
        mocked_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property behavior."""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {'repos_url': "https://api.github.com/users/google/repos"}
            gh_org_client = GithubOrgClient("google")
            self.assertEqual(gh_org_client._public_repos_url, "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock) -> None:
        """Verifies the `public_repos` method's functionality."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {"id": 7697149, "name": "episodes.dart", "private": False, "owner": {"login": "google", "id": 1342004}, "fork": False, "url": "https://api.github.com/repos/google/episodes.dart", "created_at": "2013-01-19T00:31:37Z", "updated_at": "2019-09-23T11:53:58Z", "has_issues": True, "forks": 22, "default_branch": "master"},
                {"id": 8566972, "name": "kratu", "private": False, "owner": {"login": "google", "id": 1342004}, "fork": False, "url": "https://api.github.com/repos/google/kratu", "created_at": "2013-03-04T22:52:33Z", "updated_at": "2019-11-15T22:22:16Z", "has_issues": True, "forks": 32, "default_branch": "master"},
            ]
        }
        mocked_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            gh_org_client = GithubOrgClient("google")
            self.assertEqual(gh_org_client.public_repos(), ["episodes.dart", "kratu"])
            mock_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Verifies the `has_license` method's behavior."""
        gh_org_client = GithubOrgClient("google")
        self.assertEqual(gh_org_client.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test suite for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up resources before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method functionality."""
        gh_org_client = GithubOrgClient("google")
        self.assertEqual(gh_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with license filtering."""
        gh_org_client = GithubOrgClient("google")
        self.assertEqual(gh_org_client.public_repos(license="apache-2.0"), self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleans up resources after running all tests."""
        cls.get_patcher.stop()

