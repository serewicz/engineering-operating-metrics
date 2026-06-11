# PR Quality Dashboard

A tool to measure and visualize Pull Request quality based on meaningful metrics (not vanity metrics like LOC or PR count).

## Metrics Tracked
- Review cycles and time
- Change size (files changed, lines)
- Review comments per PR
- Post-merge bug rate (via linked bug tickets)
- Test coverage delta
- Architectural impact (new dependencies, tech debt signals)
- AI usage cost per PR (if applicable)

## Features
- GitHub API integration to fetch PR data
- Dashboard (Streamlit or HTML)
- Reports and charts
- Focus on business value and low-friction contributions

## Setup
1. `pip install -r requirements.txt`
2. Set `GITHUB_TOKEN` env var
3. Run `streamlit run dashboard.py`

## Usage
See `docs/` for detailed metrics definitions and how to link bugs to PRs.