import streamlit as st
import pandas as pd

from services.api_client import (
    get_risk_summary,
    get_high_risk_suppliers,
    get_top_risk_suppliers
)

st.title("Risk Analytics")

# Risk Summary
st.subheader("Risk Summary")

summary = get_risk_summary()

st.json(summary)

st.divider()

# High Risk Suppliers
st.subheader("High Risk Suppliers")

high_risk = get_high_risk_suppliers()

if len(high_risk) > 0:
    st.dataframe(
        pd.DataFrame(high_risk),
        use_container_width=True
    )
else:
    st.success(
        "No High Risk Suppliers Found"
    )

st.divider()

# Top Risk Suppliers
st.subheader("Top Risk Suppliers")

top_risk = get_top_risk_suppliers()

if len(top_risk) > 0:
    st.dataframe(
        pd.DataFrame(top_risk),
        use_container_width=True
    )
else:
    st.info(
        "No Suppliers Available"
    )