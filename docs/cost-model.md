# Cost Model

## Purpose

The cost model translates engineering activity into directional cost visibility for CTO reviews, diligence discussions, and operating partner reporting.

## Inputs

- cycle time
- review cycles
- estimated engineering rate
- rework commits
- AI usage cost
- post-merge bug signal

## Estimated Engineering Cost

The demo data includes estimated engineering cost per pull request. In a live implementation, this can be calculated from:

```text
engineering cost = estimated engineering days * blended daily engineering cost
```

This is not intended for payroll analysis. It is intended to show where engineering capacity is being consumed.

## AI Usage Cost

AI usage cost tracks provider spend or estimated internal model cost by PR, team, product area, or business area.

Useful views:

- AI cost by team
- AI cost by feature area
- AI cost compared with rework rate
- AI cost compared with delivery speed

## Executive Use

Cost metrics should answer:

- Where is engineering capacity being consumed?
- Which teams or products have high rework cost?
- Is AI spend improving flow or increasing uncontrolled cost?
- Which technical risks are expensive to remediate?
