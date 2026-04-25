# Force of Will Formalism

Force of Will Formalism models will as a six-component structure of agency.

For an agent `a` at time `t`, will is represented as:

```txt
W_a(t) = <P_a(t), N_a(t), F_a(t), I_a(t), V_a(t), R_a(t)>
```

Where:

```txt
P = past will
N = present / now-will
F = future will
I = invariant will
V = variable will
R = relational will
```

Force of Will is the achieved coherence of this structure:

```txt
FoW_a(t) = C(W_a(t))
```

The goal is not dominance by any one component, but coherence and resonance across distinction toward capability improvement and emergent capability.

## Core doctrine

```txt
Past will is evidence.
Present will is verification.
Future will is attractor.
Invariant will is conserved structure.
Variable will is adaptation.
Relational will is coherence topology.

Force of Will is achieved coherence across all six.
```

Tighter:

```txt
P = trace
N = live verification
F = attractor
I = conservation
V = adaptation
R = relation
FoW = coherence functional
```

Force of Will is not intensity, stubbornness, domination, mere desire, social approval, or doing whatever one wants. It is the degree to which an agent's trace, present action, future attractor, conserved structure, adaptive changes, and relational topology become mutually coherent without collapsing their differences.

## Components

| Symbol | Component | Short definition | Failure mode when unbalanced |
|---|---|---|---|
| `P` | Past will | Evidential trace of agency | Authority without re-verification |
| `N` | Present will | Live agency under current verification | Naivety when past evidence is erased |
| `F` | Future will | Attractor-structure of agency | Fantasy, coercive vision, or aesthetic drift |
| `I` | Invariant will | Conserved agency-structure across change | Rigidity, vagueness, or misrepresentation |
| `V` | Variable will | Adaptive agency under changing conditions | Temporary state falsely canonized as identity |
| `R` | Relational will | Coherence topology among will components | Dominance, capture, isolation, or fragmentation |

## Hyperstratum bridge

This repository is downstream of [Hyperstratum](https://github.com/TimeLordRaps/hyperstratum), the upstream recursive-form ontology for terms such as `hypernode`, `person-hypernode`, `recursive-graph`, `self-graph`, `mira-graph`, `self-mira-recursive-graph`, and `social-mira-graph`.

In this repository, `hypernode` only means:

```txt
A local recursive agency-node that can be modeled through the six-will structure.
```

The full hyper-ontology belongs in Hyperstratum, not Force of Will. See [`docs/hyperstratum-bridge.md`](docs/hyperstratum-bridge.md).

## Repository map

```txt
.
├── README.md
├── docs/
│   ├── formalism.md
│   ├── glossary.md
│   ├── coherence-functional.md
│   └── hyperstratum-bridge.md
├── examples/
│   ├── self-audit-template.md
│   └── agent-assessment.md
├── force_of_will/
│   ├── __init__.py
│   └── model.py
├── tests/
│   └── test_model.py
├── pyproject.toml
└── .gitignore
```

## Moral and design principle

```txt
Coherence and resonance toward capability improvement and discovery of emergent capability.
```

That means the formalism does not flatten distinct wills into sameness. It composes distinct wills so beings can live, speak, grow, refuse, repair, belong, create, and discover without unjust degradation.

## Status

This repository is an initial formalization scaffold. The mathematical object is stable enough to write against, but the coherence functional `C` is still open for refinement.

Current open work:

1. Define measurable subcomponents of `C`.
2. Distinguish descriptive coherence from moral legitimacy.
3. Build examples for persons, institutions, AI systems, projects, and ecosystems.
4. Add diagrams for the six-will topology.
5. Add tests for operational self-audit and agent-assessment workflows.

## Quick use

Install locally for experiments:

```bash
pip install -e .
```

Then:

```python
from force_of_will import Will, CoherenceAssessment

will = Will(
    past="prior evidence and traces",
    present="current verification and action",
    future="protected attractor",
    invariant="conserved structure",
    variable="adaptive state",
    relational="coherence topology",
)

assessment = CoherenceAssessment.from_notes(will)
print(assessment.force_of_will_summary())
```

## License

No license has been selected yet. Until one is added, this repository remains under default copyright restrictions.
