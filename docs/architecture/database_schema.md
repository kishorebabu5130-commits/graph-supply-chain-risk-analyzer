# Database Schema

## Supplier Table

| Column | Type |
|----------|----------|
| id | Integer |
| supplier_name | String |
| country | String |
| category | String |
| reliability_score | Float |
| lead_time_days | Integer |
| is_active | Boolean |

## Dependency Table

| Column | Type |
|----------|----------|
| id | Integer |
| supplier_id | Integer |
| depends_on_supplier_id | Integer |
| dependency_weight | Float |
| dependency_type | String |