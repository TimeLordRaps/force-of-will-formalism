from force_of_will import CoherenceAssessment, Will


def make_will() -> Will:
    return Will(
        past="trace",
        present="verification",
        future="attractor",
        invariant="conservation",
        variable="adaptation",
        relational="relation",
    )


def test_will_tuple_order() -> None:
    will = make_will()
    assert will.as_tuple() == (
        "trace",
        "verification",
        "attractor",
        "conservation",
        "adaptation",
        "relation",
    )


def test_unscored_assessment() -> None:
    assessment = CoherenceAssessment.from_notes(make_will(), notes="qualitative only")
    assert assessment.coherence_score() is None
    assert "unscored" in assessment.force_of_will_summary()


def test_scored_assessment_mean() -> None:
    assessment = CoherenceAssessment(
        will=make_will(),
        non_contradiction=1.0,
        mutual_reinforcement=0.5,
        repair_capacity=0.0,
    )
    assert assessment.coherence_score() == 0.5


def test_score_validation() -> None:
    assessment = CoherenceAssessment(will=make_will(), non_contradiction=1.2)
    try:
        assessment.coherence_score()
    except ValueError as error:
        assert "non_contradiction" in str(error)
    else:
        raise AssertionError("Expected invalid score to raise ValueError")
