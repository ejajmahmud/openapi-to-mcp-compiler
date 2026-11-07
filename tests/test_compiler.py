"""Tests for openapi-to-mcp-compiler."""
import unittest
from openapi_to_mcp_compiler.compiler import OpenAPIToMCPCompiler


class TestOpenAPICompiler(unittest.TestCase):
    def test_compile_single_endpoint(self):
        spec = {
            "paths": {
                "/items": {
                    "get": {
                        "operationId": "listItems",
                        "parameters": [{"name": "limit", "schema": {"type": "integer"}}]
                    }
                }
            }
        }
        tools = OpenAPIToMCPCompiler.compile_spec(spec)
        self.assertEqual(len(tools), 1)
        self.assertEqual(tools[0]["name"], "listItems")
        self.assertIn("limit", tools[0]["inputSchema"]["properties"])
