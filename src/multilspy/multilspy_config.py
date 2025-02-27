"""
Configuration parameters for Multilspy.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional

class Language(str, Enum):
    """
    Possible languages with Multilspy.
    """

    CSHARP = "csharp"
    PYTHON = "python"
    RUST = "rust"
    JAVA = "java"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"
    GO = "go"
    RUBY = "ruby"

    def __str__(self) -> str:
        return self.value

@dataclass
class MultilspyConfig:
    """
    Configuration parameters
    """
    code_language: Language
    trace_lsp_communication: bool = False

    # If the language server is already installed, set this to the fully qualified path of the executable
    # otherwise, the language server will be installed automatically
    preinstalled_executeable_path: Optional[str] = None

    @classmethod
    def from_dict(cls, env: dict):
        """
        Create a MultilspyConfig instance from a dictionary
        """
        import inspect
        return cls(**{
            k: v for k, v in env.items() 
            if k in inspect.signature(cls).parameters
        })