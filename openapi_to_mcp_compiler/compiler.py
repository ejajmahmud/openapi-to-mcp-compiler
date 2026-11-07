"""Core OpenAPI to MCP Compiler implementation."""
from typing import Dict, Any, List


class OpenAPIToMCPCompiler:
    @staticmethod
    def compile_spec(openapi_spec: Dict[str, Any]) -> List[Dict[str, Any]]:
        tools = []
        paths = openapi_spec.get("paths", {})

        for path, path_item in paths.items():
            for method, operation in path_item.items():
                if method.lower() not in ["get", "post", "put", "delete", "patch"]:
                    continue

                op_id = operation.get("operationId") or f"{method.lower()}_{path.replace('/', '_').strip('_')}"
                summary = operation.get("summary") or operation.get("description") or f"{method.upper()} {path}"

                properties = {}
                required = []

                # Extract parameters
                for param in operation.get("parameters", []):
                    p_name = param["name"]
                    p_schema = param.get("schema", {"type": "string"})
                    properties[p_name] = {
                        "type": p_schema.get("type", "string"),
                        "description": param.get("description", f"Parameter {p_name}")
                    }
                    if param.get("required", False):
                        required.append(p_name)

                tools.append({
                    "name": op_id,
                    "description": summary,
                    "inputSchema": {
                        "type": "object",
                        "properties": properties,
                        "required": required
                    }
                })

        return tools
