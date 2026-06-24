import streamlit as st
import pandas as pd
import plotly.express as px

from services.api_client import (
    get_chart_data,
    get_risk_report
)

st.title("Reports Dashboard")

# ------------------------
# Risk Distribution Chart
# ------------------------

st.subheader("Risk Distribution")

chart_data = get_chart_data()

risk_distribution = chart_data["risk_distribution"]

df_chart = pd.DataFrame(
    {
        "Risk Level": list(
            risk_distribution.keys()
        ),
        "Count": list(
            risk_distribution.values()
        )
    }
)

fig = px.bar(
    df_chart,
    x="Risk Level",
    y="Count",
    title="Supplier Risk Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ------------------------
# Risk Report Table
# ------------------------

st.subheader("Risk Report")

risk_report = get_risk_report()

if len(risk_report) > 0:

    df_report = pd.DataFrame(
        risk_report
    )

    st.dataframe(
        df_report,
        use_container_width=True
    )

else:

    st.warning(
        "No Risk Report Available"
    )

st.divider()

# ------------------------
# CSV Export Links
# ------------------------

st.subheader("Export Reports")

supplier_csv = (
    "http://127.0.0.1:8000/reports/export/suppliers"
)

risk_csv = (
    "http://127.0.0.1:8000/reports/export/risk-report"
)

st.markdown(
    f"[Download Suppliers CSV]({supplier_csv})"
)

st.markdown(
    f"[Download Risk Report CSV]({risk_csv})"
)

