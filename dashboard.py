import streamlit as st
import pandas as pd
from github import Github
import os
from datetime import datetime

st.set_page_config(page_title="PR Quality Dashboard", layout="wide")
st.title("PR Quality Dashboard")

st.markdown("""
This dashboard helps track **meaningful** PR quality metrics instead of vanity metrics.
Focus: Business impact, low-friction contributions, and reducing post-merge issues.
""")

# Sidebar
token = st.sidebar.text_input("GitHub Token", type="password")
repo_name = st.sidebar.text_input("Repo (owner/repo)", "your-org/your-repo")

if st.sidebar.button("Fetch Data"):
    if token and repo_name:
        g = Github(token)
        repo = g.get_repo(repo_name)
        
        prs = []
        for pr in repo.get_pulls(state='closed', sort='updated', direction='desc')[:50]:  # Last 50 PRs
            # Basic metrics
            files_changed = pr.changed_files
            lines_added = pr.additions
            review_comments = pr.get_issue_comments().totalCount + pr.get_review_comments().totalCount
            
            pr_data = {
                'PR #': pr.number,
                'Title': pr.title,
                'Author': pr.user.login,
                'Created': pr.created_at,
                'Merged': pr.merged_at,
                'Files Changed': files_changed,
                'Lines Added': lines_added,
                'Review Comments': review_comments,
                'Review Cycles': 'TBD',  # Would need more detailed review history
                'Status': 'Merged' if pr.merged else 'Closed'
            }
            prs.append(pr_data)
        
        df = pd.DataFrame(prs)
        st.dataframe(df)
        
        # Simple charts
        st.subheader("Change Size Distribution")
        fig = px.histogram(df, x='Files Changed', title="PRs by Files Changed")
        st.plotly_chart(fig)
        
        st.info("Extend this with bug linking, test coverage, AI cost tracking, etc.")
    else:
        st.error("Provide token and repo")import plotly.express as px
