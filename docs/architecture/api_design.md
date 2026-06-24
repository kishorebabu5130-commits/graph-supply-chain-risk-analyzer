# API Design Document

## Base URL

```text
http://127.0.0.1:8000
```

---

# 1. Health API

## GET /health

### URL

```http
GET /health
```

### Response

```json
{
  "status": "ok"
}
```

---

# 2. Create Supplier

## POST /suppliers

### Request

```json
{
  "supplier_name": "ABC Electronics",
  "country": "India",
  "category": "Semiconductor",
  "reliability_score": 0.95,
  "lead_time_days": 12,
  "is_active": true
}
```

### Response

```json
{
  "id": 1,
  "supplier_name": "ABC Electronics",
  "country": "India",
  "category": "Semiconductor",
  "reliability_score": 0.95,
  "lead_time_days": 12,
  "is_active": true
}
```

---

# 3. Get All Suppliers

## GET /suppliers

### Response

```json
[
  {
    "id": 1,
    "supplier_name": "ABC Electronics",
    "country": "India",
    "category": "Semiconductor",
    "reliability_score": 0.95,
    "lead_time_days": 12,
    "is_active": true
  }
]
```

---

# 4. Get Supplier By ID

## GET /suppliers/{id}

### Example

```http
GET /suppliers/1
```

### Response

```json
{
  "id": 1,
  "supplier_name": "ABC Electronics",
  "country": "India",
  "category": "Semiconductor",
  "reliability_score": 0.95,
  "lead_time_days": 12,
  "is_active": true
}
```

---

# 5. Update Supplier

## PATCH /suppliers/{id}

### Request

```json
{
  "reliability_score": 0.82
}
```

### Response

```json
{
  "message": "Supplier updated successfully"
}
```

---

# 6. Delete Supplier

## DELETE /suppliers/{id}

### Response

```json
{
  "message": "Supplier deleted successfully"
}
```

---

# 7. Create Dependency

## POST /dependencies

### Request

```json
{
  "supplier_id": 1,
  "depends_on_supplier_id": 2,
  "dependency_weight": 0.85,
  "dependency_type": "shipping"
}
```

### Response

```json
{
  "id": 1,
  "supplier_id": 1,
  "depends_on_supplier_id": 2,
  "dependency_weight": 0.85,
  "dependency_type": "shipping"
}
```

---

# 8. Get Dependencies

## GET /dependencies

### Response

```json
[
  {
    "id": 1,
    "supplier_id": 1,
    "depends_on_supplier_id": 2,
    "dependency_weight": 0.85,
    "dependency_type": "shipping"
  }
]
```

---

# 9. Graph Data

## GET /graph

### Response

```json
{
  "nodes": [
    {
      "id": 1,
      "name": "ABC Electronics"
    },
    {
      "id": 2,
      "name": "XYZ Logistics"
    }
  ],
  "edges": [
    {
      "source": 1,
      "target": 2,
      "weight": 0.85
    }
  ],
  "metadata": {
    "node_count": 2,
    "edge_count": 1
  }
}
```

---

# 10. Graph Centrality

## GET /graph/centrality

### Response

```json
{
  "degree_centrality": {
    "1": 1.0,
    "2": 1.0
  },
  "betweenness_centrality": {
    "1": 0.0,
    "2": 0.0
  },
  "pagerank": {
    "1": 0.35,
    "2": 0.65
  }
}
```

---

# 11. Train ML Model

## POST /predict/train

### Response

```json
{
  "message": "Model trained successfully"
}
```

---

# 12. Predict Risk

## POST /predict

### Request

```json
{
  "reliability_score": 0.85,
  "lead_time_days": 12
}
```

### Response

```json
{
  "predicted_risk": "LOW"
}
```

---

# 13. Risk Summary

## GET /analytics/risk-summary

### Response

```json
{
  "LOW": 1,
  "MEDIUM": 1,
  "HIGH": 0,
  "CRITICAL": 0
}
```

---

# 14. High Risk Suppliers

## GET /analytics/high-risk-suppliers

### Response

```json
[]
```

---

# 15. Top Risk Suppliers

## GET /analytics/top-risk-suppliers

### Response

```json
[
  {
    "supplier_id": 1,
    "supplier_name": "ABC Electronics",
    "risk_score": 34.0,
    "risk_level": "MEDIUM"
  }
]
```

---

# 16. Dashboard Overview

## GET /dashboard/overview

### Response

```json
{
  "total_suppliers": 2,
  "total_dependencies": 1
}
```

---

# 17. Network Health

## GET /dashboard/network-health

### Response

```json
{
  "network_health_score": 90.0
}
```

---

# 18. Network Resilience

## GET /dashboard/network-resilience

### Response

```json
{
  "resilience_score": 50.0
}
```

---

# 19. Executive Summary

## GET /dashboard/executive-summary

### Response

```json
{
  "overview": {
    "total_suppliers": 2,
    "total_dependencies": 1
  },
  "network_health": {
    "network_health_score": 90.0
  },
  "network_resilience": {
    "resilience_score": 50.0
  }
}
```

---

# 20. Risk Report

## GET /reports/risk-report

### Response

```json
[
  {
    "supplier_id": 1,
    "supplier_name": "ABC Electronics",
    "risk_level": "MEDIUM"
  }
]
```

---

# 21. Chart Data

## GET /reports/chart-data

### Response

```json
{
  "risk_distribution": {
    "LOW": 1,
    "MEDIUM": 1,
    "HIGH": 0,
    "CRITICAL": 0
  }
}
```

---

# 22. Graph Visualization

## GET /reports/graph-visualization

### Response

```json
{
  "nodes": [
    {
      "id": 1,
      "name": "ABC Electronics"
    }
  ],
  "edges": [
    {
      "source": 1,
      "target": 2,
      "weight": 0.85
    }
  ]
}
```

---

# 23. Export Suppliers CSV

## GET /reports/export/suppliers

### Response

```text
suppliers.csv downloaded
```

---

# 24. Export Risk Report CSV

## GET /reports/export/risk-report

### Response

```text
risk_report.csv downloaded
```

---

# Total APIs

| Module       | Count |
| ------------ | ----- |
| Health       | 1     |
| Suppliers    | 5     |
| Dependencies | 2     |
| Graph        | 2     |
| Prediction   | 2     |
| Analytics    | 3     |
| Dashboard    | 4     |
| Reports      | 5     |
| Total        | 24    |

```
```
