"""Shared test fixtures for oro-models."""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

import pytest


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "unit: Unit tests (no external dependencies)")
    config.addinivalue_line("markers", "integration: Integration tests (require external services)")
    config.addinivalue_line("markers", "slow: Slow tests (>5s)")


# ============================================================================
# Model Row Factory Fixtures
# ============================================================================


@pytest.fixture
def belief_row_factory() -> Any:
    """Factory for creating belief database rows."""

    def factory(
        id: UUID | None = None,
        content: str = "Test belief content",
        confidence: dict[str, Any] | None = None,
        domain_path: list[str] | None = None,
        status: str = "active",
        **kwargs: Any,
    ) -> dict[str, Any]:
        now = datetime.now()
        return {
            "id": id or uuid4(),
            "content": content,
            "confidence": json.dumps(confidence or {"overall": 0.7}),
            "domain_path": domain_path or ["test", "domain"],
            "valid_from": kwargs.get("valid_from"),
            "valid_until": kwargs.get("valid_until"),
            "created_at": kwargs.get("created_at", now),
            "modified_at": kwargs.get("modified_at", now),
            "source_id": kwargs.get("source_id"),
            "extraction_method": kwargs.get("extraction_method"),
            "supersedes_id": kwargs.get("supersedes_id"),
            "superseded_by_id": kwargs.get("superseded_by_id"),
            "status": status,
        }

    return factory


@pytest.fixture
def entity_row_factory() -> Any:
    """Factory for creating entity database rows."""

    def factory(
        id: UUID | None = None,
        name: str = "Test Entity",
        type: str = "concept",
        **kwargs: Any,
    ) -> dict[str, Any]:
        now = datetime.now()
        return {
            "id": id or uuid4(),
            "name": name,
            "type": type,
            "description": kwargs.get("description"),
            "aliases": kwargs.get("aliases", []),
            "canonical_id": kwargs.get("canonical_id"),
            "created_at": kwargs.get("created_at", now),
            "modified_at": kwargs.get("modified_at", now),
        }

    return factory


@pytest.fixture
def session_row_factory() -> Any:
    """Factory for creating session database rows."""

    def factory(
        id: UUID | None = None,
        platform: str = "claude-code",
        status: str = "active",
        **kwargs: Any,
    ) -> dict[str, Any]:
        now = datetime.now()
        return {
            "id": id or uuid4(),
            "platform": platform,
            "project_context": kwargs.get("project_context"),
            "status": status,
            "summary": kwargs.get("summary"),
            "themes": kwargs.get("themes", []),
            "started_at": kwargs.get("started_at", now),
            "ended_at": kwargs.get("ended_at"),
            "claude_session_id": kwargs.get("claude_session_id"),
            "external_room_id": kwargs.get("external_room_id"),
            "metadata": kwargs.get("metadata", {}),
            "exchange_count": kwargs.get("exchange_count"),
            "insight_count": kwargs.get("insight_count"),
        }

    return factory


@pytest.fixture
def exchange_row_factory() -> Any:
    """Factory for creating exchange database rows."""

    def factory(
        id: UUID | None = None,
        session_id: UUID | None = None,
        sequence: int = 1,
        role: str = "user",
        content: str = "Test message",
        **kwargs: Any,
    ) -> dict[str, Any]:
        return {
            "id": id or uuid4(),
            "session_id": session_id or uuid4(),
            "sequence": sequence,
            "role": role,
            "content": content,
            "created_at": kwargs.get("created_at", datetime.now()),
            "tokens_approx": kwargs.get("tokens_approx"),
            "tool_uses": kwargs.get("tool_uses", []),
        }

    return factory


@pytest.fixture
def pattern_row_factory() -> Any:
    """Factory for creating pattern database rows."""

    def factory(
        id: UUID | None = None,
        type: str = "topic_recurrence",
        description: str = "Test pattern",
        **kwargs: Any,
    ) -> dict[str, Any]:
        now = datetime.now()
        return {
            "id": id or uuid4(),
            "type": type,
            "description": description,
            "evidence": kwargs.get("evidence", []),
            "occurrence_count": kwargs.get("occurrence_count", 1),
            "confidence": kwargs.get("confidence", 0.5),
            "status": kwargs.get("status", "emerging"),
            "first_observed": kwargs.get("first_observed", now),
            "last_observed": kwargs.get("last_observed", now),
        }

    return factory


@pytest.fixture
def tension_row_factory() -> Any:
    """Factory for creating tension database rows."""

    def factory(
        id: UUID | None = None,
        belief_a_id: UUID | None = None,
        belief_b_id: UUID | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        now = datetime.now()
        return {
            "id": id or uuid4(),
            "belief_a_id": belief_a_id or uuid4(),
            "belief_b_id": belief_b_id or uuid4(),
            "type": kwargs.get("type", "contradiction"),
            "description": kwargs.get("description"),
            "severity": kwargs.get("severity", "medium"),
            "status": kwargs.get("status", "detected"),
            "resolution": kwargs.get("resolution"),
            "resolved_at": kwargs.get("resolved_at"),
            "detected_at": kwargs.get("detected_at", now),
        }

    return factory


@pytest.fixture
def source_row_factory() -> Any:
    """Factory for creating source database rows."""

    def factory(id: UUID | None = None, type: str = "conversation", **kwargs: Any) -> dict[str, Any]:
        return {
            "id": id or uuid4(),
            "type": type,
            "title": kwargs.get("title"),
            "url": kwargs.get("url"),
            "content_hash": kwargs.get("content_hash"),
            "session_id": kwargs.get("session_id"),
            "metadata": kwargs.get("metadata", {}),
            "created_at": kwargs.get("created_at", datetime.now()),
        }

    return factory
