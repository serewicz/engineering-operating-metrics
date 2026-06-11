from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from statistics import median
from typing import Any

import pandas as pd
import plotly.express as px
import streamlit as st
from github import Github


ROOT = Path(__file__).resolve().parent
SAMPLE_DATA_PATH = ROOT / "data" / "sample-prs.json"


st.set_page_config(page_title="Engineering Operating Metrics", layout="wide")
st.title("Engineering Operating Metrics")

st.markdown(
    """
Engineering Operating Metrics helps CTOs, engineering leaders, operating partners,
and technology investors understand engineering effectiveness beyond vanity metrics.
"""
)


def _load_sample_data() -> pd.DataFrame:
    with SAMPLE_DATA_PATH.open("r", encoding="utf-8") as file:
        return pd.DataFrame(json.load(file))


def _fetch_github_data(token: str, repo_name: str, limit: int = 50) -> pd.DataFrame:
    github = Github(token)
    repo = github.get_repo(repo_name)
    rows = []

    for pr in repo.get_pulls(state="closed", sort="updated", direction="desc")[:limit]:
        if not pr.merged_at:
            continue

        created_at = pr.created_at.replace(tzinfo=None)
        merged_at = pr.merged_at.replace(tzinfo=None)
        cycle_time_hours = max((merged_at - created_at).total_seconds() / 3600, 0)
        review_comments = pr.get_issue_comments().totalCount + pr.get_review_comments().totalCount

        rows.append(
            {
                "pr_number": pr.number,
                "title": pr.title,
                "team": "unknown",
                "author": pr.user.login,
                "created_at": created_at.isoformat(),
                "merged_at": merged_at.isoformat(),
                "cycle_time_hours": round(cycle_time_hours, 1),
                "review_comments": review_comments,
                "review_cycles": max(1, min(review_comments // 3 + 1, 5)),
                "files_changed": pr.changed_files,
                "lines_changed": pr.additions + pr.deletions,
                "rework_commits": 0,
                "post_merge_bug": False,
                "estimated_engineering_cost": round((cycle_time_hours / 8) * 900, 2),
                "ai_usage_cost": 0.0,
                "risk_score": _estimate_pr_risk(pr.changed_files, pr.additions + pr.deletions, review_comments),
                "governance_flags": [],
                "business_area": "unknown",
            }
        )

    return pd.DataFrame(rows)


def _estimate_pr_risk(files_changed: int, lines_changed: int, review_comments: int) -> int:
    score = 20
    if files_changed > 10:
        score += 20
    if lines_changed > 500:
        score += 20
    if review_comments > 12:
        score += 15
    return min(score, 100)


def _review_quality_score(df: pd.DataFrame) -> int:
    if df.empty:
        return 0
    cycle_penalty = min(df["review_cycles"].mean() * 8, 35)
    bug_penalty = df["post_merge_bug"].mean() * 35
    rework_penalty = min(df["rework_commits"].mean() * 5, 20)
    return max(0, round(100 - cycle_penalty - bug_penalty - rework_penalty))


def _recommended_actions(df: pd.DataFrame) -> list[str]:
    if df.empty:
        return ["Load demo data or connect a GitHub repository."]

    actions = []
    if df["cycle_time_hours"].median() > 36:
        actions.append("Reduce review queue time by assigning explicit reviewers and daily review windows.")
    if df["post_merge_bug"].mean() > 0.15:
        actions.append("Strengthen pre-merge test expectations for high-risk services.")
    if df["rework_commits"].mean() > 2:
        actions.append("Clarify acceptance criteria before implementation starts to reduce rework.")
    if df["risk_score"].mean() > 55:
        actions.append("Review large or high-risk changes in architecture review before merge.")
    if df["ai_usage_cost"].sum() > 100:
        actions.append("Track AI-assisted development cost by team and business area.")

    return actions or ["Maintain current operating cadence and monitor trend changes."]


def _executive_summary(df: pd.DataFrame) -> dict[str, Any]:
    if df.empty:
        return {
            "median_cycle_time": 0,
            "review_quality_score": 0,
            "rework_rate": 0,
            "engineering_cost": 0,
            "ai_usage_cost": 0,
            "risk_score": 0,
            "recommended_actions": _recommended_actions(df),
        }

    return {
        "median_cycle_time": round(float(median(df["cycle_time_hours"])), 1),
        "review_quality_score": _review_quality_score(df),
        "rework_rate": round(float((df["rework_commits"] > 0).mean() * 100), 1),
        "engineering_cost": round(float(df["estimated_engineering_cost"].sum()), 2),
        "ai_usage_cost": round(float(df["ai_usage_cost"].sum()), 2),
        "risk_score": round(float(df["risk_score"].mean()), 1),
        "recommended_actions": _recommended_actions(df),
    }


def _render_summary(df: pd.DataFrame) -> None:
    summary = _executive_summary(df)

    st.subheader("Executive Summary")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Median Cycle Time", f"{summary['median_cycle_time']} hrs")
    col2.metric("Review Quality", f"{summary['review_quality_score']}/100")
    col3.metric("Rework Rate", f"{summary['rework_rate']}%")
    col4.metric("Engineering Cost", f"${summary['engineering_cost']:,.0f}")
    col5.metric("AI Usage Cost", f"${summary['ai_usage_cost']:,.2f}")
    col6.metric("Risk Score", f"{summary['risk_score']}/100")

    st.markdown("#### Recommended Actions")
    for action in summary["recommended_actions"]:
        st.markdown(f"- {action}")


def _render_charts(df: pd.DataFrame) -> None:
    st.subheader("Operating Views")

    tab_flow, tab_quality, tab_cost, tab_risk, tab_governance = st.tabs(
        ["Flow", "Quality", "Cost", "Risk", "Governance"]
    )

    with tab_flow:
        st.plotly_chart(px.box(df, x="team", y="cycle_time_hours", title="Cycle Time by Team"), use_container_width=True)
        st.dataframe(df[["pr_number", "title", "team", "cycle_time_hours", "review_cycles"]])

    with tab_quality:
        st.plotly_chart(px.scatter(df, x="review_comments", y="rework_commits", color="post_merge_bug"), use_container_width=True)
        st.dataframe(df[["pr_number", "title", "review_comments", "rework_commits", "post_merge_bug"]])

    with tab_cost:
        cost_by_team = df.groupby("team", as_index=False)[["estimated_engineering_cost", "ai_usage_cost"]].sum()
        st.plotly_chart(px.bar(cost_by_team, x="team", y=["estimated_engineering_cost", "ai_usage_cost"]), use_container_width=True)
        st.dataframe(cost_by_team)

    with tab_risk:
        st.plotly_chart(px.bar(df, x="pr_number", y="risk_score", color="business_area"), use_container_width=True)
        st.dataframe(df[["pr_number", "title", "business_area", "risk_score", "files_changed", "lines_changed"]])

    with tab_governance:
        governance_rows = df[["pr_number", "title", "team", "governance_flags"]].copy()
        governance_rows["governance_flags"] = governance_rows["governance_flags"].apply(
            lambda flags: ", ".join(flags) if isinstance(flags, list) and flags else "None"
        )
        st.dataframe(governance_rows)


st.sidebar.header("Mode")
mode = st.sidebar.radio("Dashboard Mode", ["Demo Mode", "Live GitHub Mode"])

if mode == "Demo Mode":
    dataframe = _load_sample_data()
    st.caption("Demo Mode uses fictional synthetic PR data. No GitHub token is required.")
else:
    st.sidebar.caption("Live GitHub Mode uses the GitHub API. Tokens are read from this session only.")
    token = st.sidebar.text_input("GitHub Token", value=os.getenv("GITHUB_TOKEN", ""), type="password")
    repo_name = st.sidebar.text_input("Repository", "owner/repo")
    limit = st.sidebar.slider("Closed PRs to fetch", min_value=10, max_value=100, value=50, step=10)
    if st.sidebar.button("Fetch GitHub Data"):
        if not token or repo_name == "owner/repo":
            st.error("Provide a GitHub token and repository name.")
            st.stop()
        dataframe = _fetch_github_data(token, repo_name, limit)
    else:
        st.info("Enter a GitHub token and repository, then select Fetch GitHub Data. Demo Mode works without a token.")
        st.stop()

if dataframe.empty:
    st.warning("No pull request data available.")
else:
    dataframe["created_at"] = pd.to_datetime(dataframe["created_at"])
    dataframe["merged_at"] = pd.to_datetime(dataframe["merged_at"])
    _render_summary(dataframe)
    _render_charts(dataframe)

    st.subheader("Raw Operating Data")
    st.dataframe(dataframe)

    st.caption(f"Generated at {datetime.utcnow().isoformat(timespec='seconds')} UTC")
