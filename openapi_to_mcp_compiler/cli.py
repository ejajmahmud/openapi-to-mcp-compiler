"""CLI for openapi-to-mcp-compiler."""
import sys
import argparse
import json
from .compiler import OpenAPIToMCPCompiler


def main():
    parser = argparse.ArgumentParser(description="OpenAPI to MCP Compiler")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        sample_spec = {
            "openapi": "3.0.0",
            "paths": {
                "/users/{userId}": {
                    "get": {
                        "operationId": "getUserById",
                        "summary": "Retrieve user details by ID",
                        "parameters": [
                            {"name": "userId", "in": "path", "required": True, "schema": {"type": "integer"}}
                        ]
                    }
                }
            }
        }
        tools = OpenAPIToMCPCompiler.compile_spec(sample_spec)
        print("Compiled MCP Tools:")
        print(json.dumps(tools, indent=2))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
