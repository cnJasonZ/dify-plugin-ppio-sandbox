import os
from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from e2b_code_interpreter import Sandbox


class PPIOSandboxProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # Test API key by listing sandboxes
            running_sandboxes = Sandbox.list(api_key=credentials.get("api_key"))
            
            # Also test creating and destroying a sandbox to validate full access
            sbx = Sandbox(api_key=credentials.get("api_key"), domain="sandbox.ppio.cn")
            sbx.kill()

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e)) 