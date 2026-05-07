from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Check:
    name: str
    passed: bool
    message: str = ""
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class ValidationResult:
    task_id: str
    checks: list[Check] = field(default_factory=list)

    def add(self, name: str, passed: bool, message: str = "", **details: Any) -> None:
        self.checks.append(Check(name=name, passed=passed, message=message, details=details))

    @property
    def passed(self) -> bool:
        return bool(self.checks) and all(check.passed for check in self.checks)

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "passed": self.passed,
            "checks": [
                {
                    "name": check.name,
                    "passed": check.passed,
                    "message": check.message,
                    "details": check.details,
                }
                for check in self.checks
            ],
        }
