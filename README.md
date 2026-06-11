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

## Related Projects

- [CTO Operating System](https://github.com/serewicz/cto-operating-system): CTO frameworks, operating models, and governance templates.
- [Executive AI Advisor](https://github.com/serewicz/Executive-AI-Advisor): document ingestion, diligence analysis, cited executive outputs, and 100-day plans.
- [K8s Platform Blueprint](https://github.com/serewicz/k8s-platform-blueprint): implementation patterns for platform governance, FinOps, observability, and Kubernetes controls.

## Repository Status

Engineering Operating Metrics is a lightweight executive analytics prototype. It intentionally avoids enterprise authentication, heavy data pipelines, and large frameworks so the operating model remains easy to inspect and extend.

## License

Apache 2.0. See [LICENSE](LICENSE).
