# Coherence Functional `C`

`C` is the open mathematical heart of the Force of Will formalism.

```txt
FoW_a(t) = C(W_a(t))
```

Where:

```txt
W_a(t) = <P_a(t), N_a(t), F_a(t), I_a(t), V_a(t), R_a(t)>
```

## Purpose

`C` should describe or measure achieved coherence across six will components:

```txt
P = trace
N = live verification
F = attractor
I = conservation
V = adaptation
R = relation
```

The function should not reward raw intensity, stubbornness, charisma, domination, or social approval by default. It should reward coherence across distinction.

## Candidate dimensions

A practical early version of `C` can evaluate the following dimensions.

### 1. Non-contradiction

Do the six components directly contradict one another?

Examples:

```txt
Past evidence says the path repeatedly fails.
Present will refuses to verify that evidence.
Future will still insists the path is guaranteed.
```

This lowers coherence.

### 2. Mutual reinforcement

Do the components strengthen one another without collapsing into sameness?

Examples:

```txt
Past evidence informs present verification.
Present verification updates future trajectory.
Future attractor motivates adaptive change.
Invariant will constrains adaptation.
Relational will keeps the system repairable.
```

This raises coherence.

### 3. Repair capacity

Can the agent detect breaks, acknowledge mismatch, and restore coherence?

Repair capacity matters because a strong will is not a will that never breaks. A strong will is one that can recompose without falsifying evidence.

### 4. Resistance to coercive collapse

Can the system preserve refusal, consent, verification, and invariant structure under pressure?

Coercive collapse occurs when outside pressure forces one component to dominate or falsify the others.

### 5. Adaptation without identity-loss

Can variable will change with state, embodiment, information, or social condition without being mistaken for invariant will?

This is especially important for high-variance agents.

### 6. Future orientation without delusion

Can future will guide becoming while remaining constrained by evidence, verification, invariant structure, adaptation, and relation?

### 7. Past integration without domination

Can past will inform risk and trust without becoming destiny, authority, or identity-prison?

### 8. Present verification without naivety

Can present will correct stale assumptions without erasing useful evidence?

## Sketch: scalar scoring version

A first operational score can use normalized sub-scores from `0.0` to `1.0`:

```txt
C(W) = mean(
  non_contradiction,
  mutual_reinforcement,
  repair_capacity,
  resistance_to_coercive_collapse,
  adaptation_without_identity_loss,
  future_orientation_without_delusion,
  past_integration_without_domination,
  present_verification_without_naivety
)
```

This is useful for early self-audit or system-audit tooling, but it is not the final philosophical definition.

## Sketch: relational graph version

Represent the will-object as a directed graph:

```txt
nodes = {P, N, F, I, V, R}
edges = constraints, reinforcements, distortions, repairs
```

Then evaluate:

```txt
coherence = positive cross-component reinforcement - unresolved destructive contradiction
```

Possible edge types:

```txt
supports
constrains
verifies
updates
repairs
distorts
dominates
ignores
captures
```

## Sketch: failure-mode penalty version

Start from an ideal maximum and subtract penalties:

```txt
C(W) = 1 - penalty(W)
```

Where penalties may include:

```txt
past_authority_without_reverification
present_naivety
future_fantasy
invariant_rigidity
variable_chaos
relational_domination
identity_capture
coercive_collapse
```

## Open questions

1. Should `C` be scalar, vector-valued, graph-valued, or multi-layered?
2. Should moral legitimacy be part of `C`, or a separate function applied to coherent systems?
3. Can an evil or coercive agent have high internal coherence but low legitimacy?
4. How should consent boundaries appear in the formalism?
5. How should uncertainty be represented when evidence is incomplete?
6. What is the difference between coherence, resonance, capability improvement, and emergent capability discovery?

## Current working stance

The safest current stance is:

```txt
C measures internal will-coherence.
M measures moral legitimacy / non-degradation constraints.
Capability improvement and emergent capability discovery require both coherence and legitimacy.
```

So a fuller model may become:

```txt
FoW_a(t) = C(W_a(t))
Legitimacy_a(t) = M(W_a(t), environment, affected_beings)
```

This prevents internal coherence from being mistaken for moral worth.
