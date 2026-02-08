"""Public interface for oro-models.

This brick provides data models (dataclasses) and enums rather than
abstract interfaces. The models themselves ARE the public contract.

Core types:
    - Belief, Entity, Source, Tension -- knowledge substrate models
    - Session, Exchange, Pattern, SessionInsight -- conversation tracking models
    - TemporalValidity, SupersessionChain -- temporal utilities
    - calculate_freshness, freshness_label -- freshness scoring

All types are re-exported from the package root:

    from oro_models import Belief, TemporalValidity
"""
