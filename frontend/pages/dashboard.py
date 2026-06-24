import streamlit as st

from services.api_client import (
    get_dashboard_overview,
    get_network_health,
    get_network_resilience
)

st.title("Dashboard")

overview = get_dashboard_overview()
health = get_network_health()
resilience = get_network_resilience()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Suppliers",
        overview["total_suppliers"]
    )

with col2:
    st.metric(
        "Total Dependencies",
        overview["total_dependencies"]
    )

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Network Health",
        health["network_health_score"]
    )

with col4:
    st.metric(
        "Resilience Score",
        resilience["resilience_score"]
    )