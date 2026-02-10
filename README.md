# our-models

Data models with temporal validity, dimensional confidence, and conversation tracking for the ourochronos ecosystem.

## Overview

our-models provides the Python dataclasses and enums that represent the Valence knowledge substrate. It bridges the PostgreSQL schema and application code with structured types for beliefs, entities, sessions, exchanges, patterns, and tensions. Key features include time-bounded validity on knowledge claims, exponential freshness decay, and supersession chains that track belief evolution.

## Install

```bash
pip install our-models
```

Requires `our-confidence>=0.1.0`.

## Usage

### Beliefs

```python
from uuid import uuid4
from datetime import datetime
from our_models import Belief, BeliefStatus
from our_confidence import DimensionalConfidence

belief = Belief(
    id=uuid4(),
    content="Python 3.12 adds incremental GC",
    confidence=DimensionalConfidence(overall=0.9),
    domain_path=["tech", "python"],
    valid_from=datetime.now(),
    status=BeliefStatus.ACTIVE,
)
```

### Temporal Validity

```python
from our_models import TemporalValidity

# Valid for a specific range
tv = TemporalValidity.range(start, end)
tv.is_valid_at(some_date)  # True/False
tv.is_expired()
tv.remaining()  # timedelta or None

# Always valid
tv = TemporalValidity.always_valid()

# Valid from now for 30 days
tv = TemporalValidity.for_duration(timedelta(days=30))
```

### Freshness Scoring

```python
from our_models import calculate_freshness, freshness_label

score = calculate_freshness(belief.created_at, half_life_days=30)
# 1.0 = just created, decays exponentially

label = freshness_label(score)
# "very fresh" | "fresh" | "aging" | "stale" | "very stale"
```

### Supersession Chains

```python
from our_models import SupersessionChain

chain = SupersessionChain(entries=[...])
chain.original_id    # first belief in the chain
chain.current_id     # latest belief
chain.revision_count
chain.get_at_time(some_date)  # belief that was current at that time
```

### Sessions and Exchanges

```python
from our_models import Session, Exchange, Platform, ExchangeRole

session = Session(
    id=uuid4(),
    platform=Platform.CLAUDE_CODE,
    project_context="valence",
    themes=["refactoring", "testing"],
)

exchange = Exchange(
    session_id=session.id,
    sequence=1,
    role=ExchangeRole.USER,
    content="How do I add a new MCP tool?",
)
```

### Serialization

```python
# All models support database round-tripping
d = belief.to_dict()        # JSON-serializable dict
belief = Belief.from_row(db_row)  # Reconstruct from database row
```

## API

### Knowledge Models

| Class | Description |
|-------|-------------|
| `Belief` | Knowledge claim with confidence, domain path, and temporal validity |
| `Entity` | Person, tool, concept, etc. that beliefs reference |
| `Source` | Provenance information (type, URL, content hash) |
| `Tension` | Contradiction between beliefs with severity and resolution status |
| `BeliefEntity` | Junction linking a belief to an entity with a role |

### Conversation Models

| Class | Description |
|-------|-------------|
| `Session` | A conversation session with platform, themes, metadata |
| `Exchange` | A single turn (user/assistant/system) |
| `Pattern` | Behavioral pattern observed across sessions |
| `SessionInsight` | Link between a session and an extracted belief |

### Temporal

| Symbol | Description |
|--------|-------------|
| `TemporalValidity` | Time-bounded validity with factory methods and queries |
| `SupersessionChain` | Tracks belief evolution through supersessions |
| `calculate_freshness()` | Exponential decay scoring (configurable half-life) |
| `freshness_label()` | Human-readable freshness labels |

### Enums

`BeliefStatus`, `EntityType`, `EntityRole`, `SessionStatus`, `Platform`, `ExchangeRole`, `PatternStatus`, `TensionType`, `TensionSeverity`, `TensionStatus`

## Development

```bash
# Install with dev dependencies
make dev

# Run linters
make lint

# Run tests
make test

# Run tests with coverage
make test-cov

# Auto-format
make format
```

## State Ownership

None directly. This package defines data shapes — state is owned by the database layer (`our-db`) and the substrate that persists these models.

## Part of Valence

This brick is part of the [Valence](https://github.com/ourochronos/valence) knowledge substrate. See [our-infra](https://github.com/ourochronos/our-infra) for ourochronos conventions.

## License

MIT
