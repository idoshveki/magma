#!/usr/bin/env python3

from gql import gql


gql(
    """
{
  id
}
"""
)  # GQL101: Cannot query field "id" on type "Query".
