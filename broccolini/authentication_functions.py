"""Authentication functions.

Functions such as Hashicorp Vault for authentication.
"""
import logging
import os
from typing import Any, Dict, Tuple

import hvac
from hvac.v1 import Client

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")


class VaultFunctions:
    """Hashicorp Vault authentication functions.

    input: vault server
    input type: str
    input: github token
    input type: str
    output: return client
    """

    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        """Init class - vars are called in the function as needed."""

    def __repr__(self) -> str:  # pragma: no cover
        """Display function name using repr."""
        class_name = self.__class__.__name__
        return f"{class_name}"

    def __str__(self) -> str:  # pragma: no cover
        """Display function name using str."""
        return str(self)

    def unseal_vault(self, **kwargs: str) -> bool:
        """Unseal vault."""
        try:
            _vault_url: str = kwargs["vault_url"]
            _vault_token: str = kwargs["vault_token"]
            client = self.get_vault_credentials(vault_url=_vault_url, vault_token=_vault_token)
            try:
                if client.sys.is_sealed():
                    vault_unseal_token: str = os.environ[kwargs["vault_unseal_token"]]
                    client.sys.submit_unseal_key(vault_unseal_token)
                    # return True
                else:
                    print("Vault is sealed")
                return True
            except (hvac.exceptions.Forbidden) as _error:
                # pragma: no cover
                raise ValueError("Bad unseal token") from _error
        except (hvac.exceptions.Forbidden) as _error:  # pragma: no cover
            raise ValueError("Permission Denied, please check your permissions and the path to the secret") from _error

    @staticmethod
    def get_vault_credentials(**kwargs: str) -> Client:
        """Login to vault using credentials and return client."""
        try:
            _vault_url: str = kwargs["vault_url"]
            _vault_token: str = kwargs["vault_token"]
            vault_url = os.environ[_vault_url]
            vault_token = os.environ[_vault_token]
            # return vault_url, vault_token
            client = hvac.Client(url=vault_url, token=vault_token)
            return client

        # raise ValueError(f"Missing environment variables {errinfo}")
        except KeyError as _error:
            raise ValueError("Missing environment variables!") from _error

    def query_vault_data(self, **kwargs: str) -> Client:
        """Query vault data."""
        try:
            _vault_url: str = kwargs["vault_url"]
            _vault_token: str = kwargs["vault_token"]
            _secret_path: str = kwargs["secret_path"]
            client = self.get_vault_credentials(vault_url=_vault_url, vault_token=_vault_token)
            read_response = client.secrets.kv.v2.read_secret_version(path=_secret_path)
            return read_response
        except (hvac.exceptions.Forbidden) as _error:  # pragma: no cover
            raise ValueError("Permission Denied, please check your permissions and the path to the secret") from _error

    def add_to_vault(self, **kwargs: str) -> Tuple[bool, str]:
        """Add to vault data.

        input: vault_url: str
        input: vault_token: str
        input: secret_path: str
        input: secret: str
        input: calls other functions
        output: (success, result): type Tuple[bool, str]
        """
        try:
            _vault_url: str = kwargs["vault_url"]
            _vault_token: str = kwargs["vault_token"]
            _secret_path: str = kwargs["secret_path"]
            _secret: str = kwargs["secret"]
            client = self.get_vault_credentials(vault_url=_vault_url, vault_token=_vault_token)
            result = client.secrets.kv.v2.create_or_update_secret(path=_secret_path, secret=_secret)
            return True, result
        except (hvac.exceptions.Forbidden) as _error:  # pragma: no cover
            raise ValueError("Permission Denied, please check your permissions and the path to the secret!") from _error

    def initialized_vault(self, **kwargs: str) -> bool:
        """Confirm vault is initialized.

        input : vault_url
        input : vault_token
        output: is_initialized: bool
        """
        try:
            _vault_url: str = kwargs["vault_url"]
            _vault_token: str = kwargs["vault_token"]
            client = self.get_vault_credentials(vault_url=_vault_url, vault_token=_vault_token)
            if not client.sys.is_initialized():  # pragma: no cover
                return False  # pragma: no cover
            return True
        except (hvac.exceptions.Forbidden) as _error:  # pragma: no cover
            raise ValueError("Vault not ready!") from _error
