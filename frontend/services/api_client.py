import requests

BASE_URL = "http://127.0.0.1:8000"


def get_dashboard_overview():
    return requests.get(
        f"{BASE_URL}/dashboard/overview"
    ).json()


def get_network_health():
    return requests.get(
        f"{BASE_URL}/dashboard/network-health"
    ).json()


def get_network_resilience():
    return requests.get(
        f"{BASE_URL}/dashboard/network-resilience"
    ).json()


def get_executive_summary():
    return requests.get(
        f"{BASE_URL}/dashboard/executive-summary"
    ).json()


def get_risk_summary():
    return requests.get(
        f"{BASE_URL}/analytics/risk-summary"
    ).json()


def get_high_risk_suppliers():
    return requests.get(
        f"{BASE_URL}/analytics/high-risk-suppliers"
    ).json()


def get_top_risk_suppliers():
    return requests.get(
        f"{BASE_URL}/analytics/top-risk-suppliers"
    ).json()


def get_graph():
    return requests.get(
        f"{BASE_URL}/graph"
    ).json()


def get_centrality():
    return requests.get(
        f"{BASE_URL}/graph/centrality"
    ).json()


def get_chart_data():
    return requests.get(
        f"{BASE_URL}/reports/chart-data"
    ).json()


def get_risk_report():
    return requests.get(
        f"{BASE_URL}/reports/risk-report"
    ).json()

def get_graph_visualization():
    return requests.get(
        f"{BASE_URL}/reports/graph-visualization"
    ).json()