"""Executable primitives for the Force of Will formalism.

These classes are deliberately lightweight. They are not a finished measurement system.
They provide a clean object model for experiments, audits, and future tests.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
from typing import Mapping


@dataclass(frozen=True)
class Will:
    """Six-component structured agency object.

    Attributes map to W = <P, N, F, I, V, R>:

    - past: P, evidential trace of agency.
    - present: N, live verification / now-will.
    - future: F, attractor-structure.
    - invariant: I, conserved agency-structure.
    - variable: V, adaptive agency under changing conditions.
    - relational: R, coherence topology among components.
    """

    past: str
    present: str
    future: str
    invariant: str
    variable: str
    relational: str
    metadata: Mapping[str, str] = field(default_factory=dict)

    def as_tuple(self) -> tuple[str, str, str, str, str, str]:
        """Return the will object in canonical component order."""

        return (
            self.past,
            self.present,
            self.future,
            self.invariant,
            self.variable,
            self.relational,
        )

    def symbolic(self) -> str:
        """Return the symbolic form."""

        return "W = <P, N, F, I, V, R>"


@dataclass(frozen=True)
class CoherenceAssessment:
    """Early scalar approximation of the coherence functional C(W).

    Scores should be normalized from 0.0 to 1.0.
    This is an experimental scaffold, not a final definition of Force of Will.
    """

    will: Will
    non_contradiction: float | None = None
    mutual_reinforcement: float | None = None
    repair_capacity: float | None = None
    resistance_to_coercive_collapse: float | None = None
    adaptation_without_identity_loss: float | None = None
    future_orientation_without_delusion: float | None = None
    past_integration_without_domination: float | None = None
    present_verification_without_naivety: float | None = None
    notes: str = ""

    @classmethod
    def from_notes(cls, will: Will, notes: str = "") -> "CoherenceAssessment":
        """Create an unscored assessment from qualitative notes."""

        return cls(will=will, notes=notes)

    def scores(self) -> dict[str, float]:
        """Return only dimensions that have been scored."""

        raw = {
            "non_contradiction": self.non_contradiction,
            "mutual_reinforcement": self.mutual_reinforcement,
            "repair_capacity": self.repair_capacity,
            "resistance_to_coercive_collapse": self.resistance_to_coercive_collapse,
            "adaptation_without_identity_loss": self.adaptation_without_identity_loss,
            "future_orientation_without_delusion": self.future_orientation_without_delusion,
            "past_integration_without_domination": self.past_integration_without_domination,
            "present_verification_without_naivety": self.present_verification_without_naivety,
        }
        return {key: _validate_score(key, value) for key, value in raw.items() if value is not None}

    def coherence_score(self) -> float | None:
        """Return the mean of scored dimensions, or None if nothing is scored."""

        scored = list(self.scores().values())
        if not scored:
            return None
        return mean(scored)

    def force_of_will_summary(self) -> str:
        """Return a compact textual summary."""

        score = self.coherence_score()
        score_text = "unscored" if score is None else f"{score:.3f}"
        return (
            f"{self.will.symbolic()} | FoW ≈ C(W) = {score_text}. "
            "Interpret this as an experimental coherence assessment, not a final proof."
        )


def _validate_score(name: str, value: float | None) -> float:
    if value is None:
        raise ValueError(f"{name} cannot be None when validating a score")
    numeric = float(value)
    if not 0.0 <= numeric <= 1.0:
        raise ValueError(f"{name} must be between 0.0 and 1.0, got {numeric}")
    return numeric
