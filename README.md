# Engineering Operating Metrics

Engineering Operating Metrics helps CTOs, engineering leaders, operating partners, and technology investors understand engineering effectiveness beyond vanity metrics.

The platform measures:

- Delivery Flow
- Review Quality
- Rework
- Engineering Cost
- AI Usage Cost
- Technical Risk
- Governance

## Why This Exists

Most engineering dashboards focus on activity.

Engineering Operating Metrics focuses on outcomes.

Pull request counts, lines of code, and comment volume do not tell a CTO whether engineering is improving delivery predictability, quality, cost discipline, or technical risk. This project provides an executive-facing operating view that connects engineering work to business outcomes.

## Who It Is For

- CTOs
- VP Engineering
- Engineering Managers
- Operating Partners
- Technology Due Diligence
- Boards

## Core Metrics

### Flow

- median cycle time
- review cycles
- deployment and merge throughput
- blocked or aging work

### Quality

- review quality score
- rework rate
- post-merge bug signal
- test and validation discipline

### Cost

- estimated engineering cost
- cost by team or business area
- AI usage cost
- cost of rework

### Risk

- technical risk score
- large change risk
- architectural impact
- high-risk service changes

### Governance

- missing ownership
- missing linked issue or decision record
- risky changes without review
- policy and operating exceptions

## AI Cost Governance

Engineering Operating Metrics can be extended to track AI-related operating metrics such as external provider spend, local inference cost, retrieval usage, adoption trends, and AI-assisted delivery cost.

Metrics may include:

- external LLM provider spend
- local inference cost
- retrieval/search usage
- AI-assisted PR or workflow cost
- adoption trends by team or workflow

## Demo Mode

Demo Mode uses fictional PR data from `data/sample-prs.json`. It works without a GitHub token and is intended for executive demos, portfolio reviews, and product development.

Run:

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

Then select `Demo Mode`.

## Live GitHub Mode

Live GitHub Mode uses GitHub API data from a repository you provide.

Set a token through the Streamlit sidebar or environment:

```bash
export GITHUB_TOKEN=your_token_here
streamlit run dashboard.py
```

Tokens are used only for the local session. Do not commit tokens or `.env` files.

## Documentation

- [Metrics Model](docs/metrics-model.md)
- [Cost Model](docs/cost-model.md)
- [Executive Dashboard](docs/executive-dashboard.md)
- [Sample Report](docs/sample-report.md)
- [Governance Use Cases](docs/governance-use-cases.md)

## Technology Leadership Portfolio

This repository is part of a broader Technology Leadership Portfolio: a practical system for assessing, operating, governing, implementing, and measuring technology organizations.

| Layer | Repository | Purpose |
|---|---|---|
| Methodology | [CTO Operating System](https://github.com/serewicz/cto-operating-system) | Defines CTO, diligence, governance, board reporting, and operating partner frameworks |
| Assessment | [Executive AI Advisor](https://github.com/serewicz/Executive-AI-Advisor) | Converts company documents into diligence reports, board briefs, CRA readiness assessments, AI governance assessments, and 100-day technology plans |
| Implementation | [K8s Platform Blueprint](https://github.com/serewicz/k8s-platform-blueprint) | Provides implementation patterns for platform governance, FinOps, observability, policy controls, and compliance evidence |
| Measurement | [Engineering Operating Metrics](https://github.com/serewicz/engineering-operating-metrics) | Measures delivery flow, review quality, rework, engineering cost, AI usage cost, risk, and engineering governance |

This repository provides the measurement layer. See [Technology Leadership Portfolio](docs/Technology-Leadership-Portfolio.md).

## Repository Status

Engineering Operating Metrics is a lightweight executive analytics prototype. It intentionally avoids enterprise authentication, heavy data pipelines, and large frameworks so the operating model remains easy to inspect and extend.

## License

Apache 2.0. See [LICENSE](LICENSE).
