# Lab: BigQuery Hands-On

## Overview

In this hands-on lab, you will work directly with Google BigQuery to create datasets, load data, and run analytical queries. This lab reinforces the BigQuery concepts from today's written content.

## Learning Objectives

- Create and configure BigQuery datasets
- Load data from various sources
- Write SQL queries using BigQuery syntax
- Apply partitioning and clustering strategies
- Understand query cost estimation

## Exercise Mode: Implementation (Code Lab)

This is a hands-on coding lab. You will work directly in BigQuery.

## Prerequisites

- Google Cloud account with BigQuery access
- Basic SQL knowledge
- Familiarity with the BigQuery console or bq CLI

## Lab Setup

1. Navigate to the BigQuery console: <https://console.cloud.google.com/bigquery>
2. Ensure you have a project selected
3. You will use public datasets for this lab (no data upload required)

## Part 1: Dataset and Table Creation (30 minutes)

### Task 1.1: Create a Dataset

Create a new dataset with the following specifications:

- Name: `analytics_lab`
- Location: US (multi-region)
- Default table expiration: 7 days

**Deliverable:** Screenshot or DDL statement used

### Task 1.2: Create a Partitioned Table

Create a table from the public dataset with partitioning:

```sql
-- Use this as a starting point
CREATE TABLE `your-project.analytics_lab.sales_partitioned`
PARTITION BY DATE(transaction_date)
CLUSTER BY customer_id
AS
SELECT *
FROM `bigquery-public-data.thelook_ecommerce.order_items`
WHERE created_at >= '2023-01-01';
```

**Deliverable:** The DDL statement you used

### Task 1.3: Create an External Table

Create an external table pointing to a GCS bucket (use public sample data):

```sql
CREATE EXTERNAL TABLE `your-project.analytics_lab.external_example`
OPTIONS (
  format = 'CSV',
  uris = ['gs://cloud-samples-data/bigquery/us-states/us-states.csv'],
  skip_leading_rows = 1
);
```

**Deliverable:** Query the external table and capture the results

## Part 2: SQL Queries (1 hour)

Using the `bigquery-public-data.thelook_ecommerce` dataset, write queries for each task.

### Task 2.1: Basic Aggregation

Write a query that shows:

- Total orders per month for 2023
- Total revenue per month
- Average order value per month

**Deliverable:** Your SQL query and results

### Task 2.2: Window Functions

Write a query that calculates:

- Running total of revenue by day
- 7-day moving average of order count
- Rank of products by total sales within each category

**Deliverable:** Your SQL query demonstrating window functions

### Task 2.3: ARRAY and STRUCT

Write a query that groups order items into an array per order:

```sql
SELECT 
    order_id,
    ARRAY_AGG(STRUCT(product_id, sale_price)) AS items
FROM `bigquery-public-data.thelook_ecommerce.order_items`
GROUP BY order_id
LIMIT 10;
```

Then write a query that UNNESTs this structure back to rows.

**Deliverable:** Both queries and their results

## Part 3: Query Optimization (30 minutes)

### Task 3.1: Cost Estimation

For the following query, use the "Dry Run" feature to estimate bytes processed:

```sql
SELECT *
FROM `bigquery-public-data.thelook_ecommerce.order_items`
WHERE created_at >= '2023-01-01';
```

Now optimize the query by selecting only needed columns:

```sql
SELECT order_id, product_id, sale_price, created_at
FROM `bigquery-public-data.thelook_ecommerce.order_items`
WHERE created_at >= '2023-01-01';
```

**Deliverable:** Compare bytes processed for both queries

### Task 3.2: Partition Pruning

Query your partitioned table with and without a partition filter:

```sql
-- Without filter (scans all partitions)
SELECT COUNT(*) FROM `analytics_lab.sales_partitioned`;

-- With filter (partition pruning)
SELECT COUNT(*) FROM `analytics_lab.sales_partitioned`
WHERE transaction_date = '2023-06-15';
```

**Deliverable:** Execution details showing partition pruning in action

## Part 4: Cleanup

Delete the resources you created:

```sql
DROP TABLE IF EXISTS `analytics_lab.sales_partitioned`;
DROP TABLE IF EXISTS `analytics_lab.external_example`;
-- Optionally delete the dataset
```

## Definition of Done

- Dataset created with proper configuration
- Partitioned and external tables created
- All 6 SQL queries written and executed
- Query optimization comparison documented
- Resources cleaned up

## Submission

Create a document `bigquery-lab-results.md` containing:

- All DDL statements used
- All SQL queries written
- Screenshots or query results for each task
- Cost comparison from Part 3

## Time Estimate

3-4 hours

## Resources

- Written Content: c176-c191 (Data Warehousing, BigQuery)
- BigQuery Public Datasets: <https://cloud.google.com/bigquery/public-data>
- BigQuery Documentation: <https://cloud.google.com/bigquery/docs>

## Rubric

| Criteria | Points |
|----------|--------|
| Dataset/table creation | 20 |
| Basic aggregation query | 15 |
| Window functions query | 20 |
| ARRAY/STRUCT handling | 15 |
| Optimization analysis | 20 |
| Documentation quality | 10 |
| **Total** | **100** |
