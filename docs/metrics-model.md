# Metrics Model

## Purpose

Engineering Operating Metrics measures delivery, quality, cost, risk, and governance signals that matter to CTOs and executive stakeholders.

## Metric Categories

| Category | Metric | Executive Question |
|---|---|---|
| Flow | Median cycle time | Is engineering work moving predictably? |
| Flow | Review cycles | Are changes clear enough to review efficiently? |
| Quality | Review quality score | Are reviews preventing defects and rework? |
| Quality | Rework rate | How much effort is spent correcting unclear or unstable work? |
| Cost | Estimated engineering cost | What is the labor cost of delivery and rework? |
| Cost | AI usage cost | How much AI-assisted development spend is being used? |
| Risk | Technical risk score | Which changes create elevated operational or architectural risk? |
| Governance | Governance flags | Where are ownership, process, or evidence gaps appearing? |

## Review Quality Score

The current prototype calculates a simple score from review cycles, post-merge bug signal, and rework commits. This is intentionally deterministic and explainable.

## Risk Score

Risk score considers:

- files changed
- lines changed
- review friction
- governance flags
- business area

## Expected Outcome

Leadership can distinguish activity from outcomes and discuss engineering performance in terms of flow, quality, cost, risk, and governance.
