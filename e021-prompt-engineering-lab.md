# Exercise: Prompt Engineering Lab

## Exercise ID: e021

## Overview

In this hands-on lab, you will practice prompt engineering techniques learned today. You will work through progressively complex challenges, applying zero-shot, few-shot, and chain-of-thought prompting patterns to solve data engineering tasks.

## Learning Objectives

- Apply zero-shot prompting for simple, well-defined tasks
- Use few-shot prompting to teach the model domain-specific patterns
- Implement chain-of-thought prompting for multi-step reasoning
- Apply prompt constraints to control output quality

## Prerequisites

- Access to an LLM (ChatGPT, Claude, Gemini, or similar)
- Completed Monday written content on prompt engineering

## Time Estimate

45-60 minutes

---

## Part 1: Zero-Shot Prompting (15 minutes)

### Challenge 1.1: SQL Generation

Using only zero-shot prompting (no examples), write a prompt that generates a BigQuery SQL query to:

- Find the top 5 departments by average salary
- Include the department name, average salary, and employee count
- Only include departments with more than 10 employees
- Order by average salary descending

**Your Task:**

1. Write your prompt
2. Submit it to the LLM
3. Evaluate the output -- does it produce valid BigQuery SQL?
4. If not, refine your prompt and try again
5. Document your original prompt, your refined prompt (if needed), and the final output


Write a BigQuery SQL query to find the top 5 departments by average salary. Select only the department name, average salary, and employee count. Only include departments where there are more than 10 employees. Order by average salary descending.

SELECT
  department_name,
  AVG(salary) AS avg_salary,
  COUNT(*) AS employee_count
FROM
  `your_project.your_dataset.your_table`
GROUP BY
  department_name
HAVING
  COUNT(*) > 10
ORDER BY
  avg_salary DESC
LIMIT 5;

### Challenge 1.2: Error Explanation

Write a zero-shot prompt that asks the LLM to explain this error message in plain English and suggest a fix:

```
google.api_core.exceptions.BadRequest: 400 Syntax error: 
Expected end of input but got keyword SELECT at [3:1]
```

**Your Task:**

1. Craft a prompt that provides enough context for a useful explanation
2. Evaluate whether the explanation is accurate
3. Rate the quality of the fix suggestion (1-5 scale)

Explain this error message and how to fix it: google.api_core.exceptions.BadRequest: 400 Syntax error: Expected end of input but got keyword SELECT at [3:1]

This error is coming from Google Cloud BigQuery, and it means your SQL query has extra or improperly structured content—specifically, a SELECT statement where BigQuery didn’t expect one.

🔍 What the error means

“Expected end of input but got keyword SELECT at [3:1]”

“Expected end of input” → BigQuery thought your query was already complete.
“but got keyword SELECT” → it then encountered another SELECT statement.
[3:1] → the issue starts at line 3, column 1.

👉 In plain English:
You likely have two SELECT statements back-to-back (or something structurally similar), and BigQuery doesn’t know how to handle the second one.

🧠 Common causes
1. Multiple SELECT statements without separation

❌ Invalid:

SELECT * FROM table1
SELECT * FROM table2

✅ Fix:

Combine with UNION ALL:
SELECT * FROM table1
UNION ALL
SELECT * FROM table2
2. Missing semicolon (in multi-statement scripts)

If you're running multiple queries:

❌

SELECT * FROM table1
SELECT * FROM table2

✅

SELECT * FROM table1;
SELECT * FROM table2;
3. Incorrect subquery syntax

❌

SELECT *
FROM table1
SELECT col FROM table2

✅ (use a subquery properly):

SELECT *
FROM (
  SELECT col FROM table2
)
4. Misplaced WITH (CTE) usage

❌

WITH t AS (SELECT * FROM table1)
SELECT * FROM t
SELECT * FROM table2

✅

WITH t AS (SELECT * FROM table1)
SELECT * FROM t;

Or combine:

WITH t AS (SELECT * FROM table1)
SELECT * FROM t
UNION ALL
SELECT * FROM table2
5. Trailing query fragments

Sometimes happens when dynamically building queries in Python:

query = """
SELECT * FROM table1
"""
query += "SELECT * FROM table2"

👉 This silently creates invalid SQL.

🛠️ How to fix it (quick checklist)
Go to line 3 in your query.
Look for an unexpected SELECT.
Ask:
Should this be a separate query? → add ;
Should it be combined? → use UNION ALL
Should it be a subquery? → wrap in parentheses
✅ Rule of thumb

BigQuery expects:

One complete query, OR
Multiple queries separated by semicolons

Anything else → this exact error.

If you paste your query here, I can point to the exact line and fix it precisely.

### Challenge 1.3: Data Dictionary Entry

Write a zero-shot prompt to generate a data dictionary entry for a column called `customer_lifetime_value` in a `dim_customer` table. The entry should include: data type, description, business definition, calculation method, and example values.

**Your Task:**

1. Write the prompt
2. Evaluate whether the output would be useful for a new team member
3. Note what additional context you would need to add to make it more accurate

---

Generate a data dictionary entry for a column called customer_lifetime_value in a dim_customer table. The entry should include: data type, description, business definition, calculation method, and example values. 

Column Name: customer_lifetime_value
Table: dim_customer
Data Type: DECIMAL(12,2) (or FLOAT/NUMERIC depending on your warehouse)
Description:

Represents the total estimated revenue a customer is expected to generate over the entire duration of their relationship with the business.

Business Definition:

Customer Lifetime Value (CLV) is a key business metric used to quantify the long-term value of a customer. It helps the organization understand customer profitability, guide marketing spend, and inform retention strategies.

Calculation Method:

CLV is typically calculated using one of the following approaches:

Simple historical model:

customer_lifetime_value = total_revenue_from_customer

Predictive / modeled approach:

customer_lifetime_value = average_order_value 
                          × purchase_frequency 
                          × average_customer_lifespan

Where:

average_order_value = total revenue / number of orders
purchase_frequency = number of orders / time period
average_customer_lifespan = estimated duration of customer relationship

Optional enhancements may include:

Discounting future cash flows (net present value)
Adjusting for churn probability
Segment-based modeling
Example Values:
customer_id	customer_lifetime_value
1001	1250.50
1002	320.00
1003	5875.75
1004	0.00
1005	142.99

If you want, I can tailor this to a specific warehouse (Snowflake, BigQuery, etc.) or align it with a dbt schema.yml format.

## Part 2: Few-Shot Prompting (15 minutes)

### Challenge 2.1: Column Name Standardization

You need the LLM to convert column names from various formats to snake_case following your team's convention.

**Provide these examples in your prompt:**

- `CustomerFirstName` -> `customer_first_name`
- `order-total-amount` -> `order_total_amount`
- `PRODUCT ID` -> `product_id`

**Then ask it to convert:**

- `ShippingAddress Line1`
- `total_Revenue_YTD`
- `customerEmailAddress`
- `ORDER__STATUS__CODE`

**Your Task:**

1. Write the few-shot prompt with the 3 examples
2. Submit and evaluate: did it follow the pattern correctly for all 4 inputs?
3. Were there any the model struggled with? Why?

Convert these to snake_case: - ShippingAddress Line1 - total_Revenue_YTD - customerEmailAddress - ORDER__STATUS__CODE Here are examples of how to do so: - CustomerFirstName -> customer_first_name - order-total-amount -> order_total_amount - PRODUCT ID -> product_id

ShippingAddress Line1 → shipping_address_line1
total_Revenue_YTD → total_revenue_ytd
customerEmailAddress → customer_email_address
ORDER__STATUS__CODE → order_status_code

### Challenge 2.2: SQL to Documentation

Teach the model to generate documentation from SQL using examples.

**Provide this example:**

Input:

```sql
SELECT customer_id, COUNT(*) as order_count 
FROM orders GROUP BY customer_id
```

Output:

```
Query: Customer Order Count
Purpose: Counts the total number of orders per customer
Tables Used: orders
Output Columns: customer_id, order_count
Aggregation: COUNT grouped by customer_id
```

**Then ask it to document this query:**

```sql
SELECT p.category, 
       DATE_TRUNC(o.order_date, MONTH) as month,
       SUM(o.quantity * p.unit_price) as revenue,
       COUNT(DISTINCT o.customer_id) as unique_customers
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date >= '2024-01-01'
GROUP BY 1, 2
ORDER BY 1, 2
```

**Your Task:**

1. Write the prompt with the example
2. Evaluate: did the model follow the documentation format?
3. Is the documentation accurate?


Document this SQL query: SELECT p.category, DATE_TRUNC(o.order_date, MONTH) as month, SUM(o.quantity * p.unit_price) as revenue, COUNT(DISTINCT o.customer_id) as unique_customers FROM orders o JOIN products p ON o.product_id = p.product_id WHERE o.order_date >= '2024-01-01' GROUP BY 1, 2 ORDER BY 1, 2 Here is an example of how to do so: Input:
sql
SELECT customer_id, COUNT(*) as order_count 
FROM orders GROUP BY customer_id
Output:
Query: Customer Order Count
Purpose: Counts the total number of orders per customer
Tables Used: orders
Output Columns: customer_id, order_count
Aggregation: COUNT grouped by customer_id


Query: Monthly Revenue and Customer Count by Product Category
Purpose: Calculates total revenue and the number of unique customers per product category for each month starting from January 1, 2024
Tables Used: orders (o), products (p)
Joins: INNER JOIN on o.product_id = p.product_id
Output Columns: 
  - category
  - month (truncated from order_date to month)
  - revenue (SUM of quantity * unit_price)
  - unique_customers (COUNT DISTINCT of customer_id)
Filters: order_date >= '2024-01-01'
Aggregation: GROUP BY category and month
Ordering: Sorted by category, then month

---

## Part 3: Chain-of-Thought Prompting (15 minutes)

### Challenge 3.1: Cost Estimation

Use chain-of-thought prompting to have the LLM estimate BigQuery costs:

**Scenario:**

- You have a table with 500 million rows, each row is approximately 500 bytes
- You run a query that scans 3 columns (out of 20 total columns)
- The query runs 4 times per day
- BigQuery charges $6.25 per TB scanned
- Assume columnar storage distributes data evenly across columns

**Your Task:**

1. Write a prompt that includes "Think through this step by step"
2. Verify each step of the model's calculation
3. Is the final answer reasonable?
4. Did chain-of-thought improve accuracy compared to a direct question?


Think through this step by step: - You have a table with 500 million rows, each row is approximately 500 bytes - You run a query that scans 3 columns (out of 20 total columns) - The query runs 4 times per day - BigQuery charges $6.25 per TB scanned - Assume columnar storage distributes data evenly across columns Estimate BigQuery total costs.

Let’s break it down cleanly.

1. Size per column
Total row size = 500 bytes
Total columns = 20

So per column:

500
/
20
=
25
 bytes per column
500/20=25 bytes per column
2. Data scanned per query
Query scans 3 columns

Per row scanned:

3
×
25
=
75
 bytes
3×25=75 bytes

Total rows = 500 million

500,000,000
×
75
=
37,500,000,000
 bytes
500,000,000×75=37,500,000,000 bytes

Convert to GB:

37.5
 GB
37.5 GB

Convert to TB:

37.5
/
1024
≈
0.0366
 TB
37.5/1024≈0.0366 TB
3. Cost per query

BigQuery pricing = $6.25 per TB

0.0366
×
6.25
≈
0.229
 dollars
0.0366×6.25≈0.229 dollars

👉 ≈ $0.23 per query

4. Daily cost

Query runs 4 times/day

0.23
×
4
=
0.92
0.23×4=0.92

👉 ≈ $0.92 per day

5. Monthly estimate (30 days)
0.92
×
30
≈
27.6
0.92×30≈27.6

👉 ≈ $27–28 per month

✅ Final Answer
Per query: ~$0.23
Per day: ~$0.92
Per month: ~$28

### Challenge 3.2: Pipeline Debugging

Use chain-of-thought prompting to diagnose this pipeline issue:

**Scenario:**
An ETL pipeline extracts data from a REST API, transforms it with Python, and loads it into BigQuery. The pipeline ran successfully for 30 days, then suddenly started failing with this error:

```
google.api_core.exceptions.Forbidden: 403 Access Denied: 
BigQuery BigQuery: Permission bigquery.tables.create denied
```

Nothing in the pipeline code changed. The GCP project and service account are the same.

**Your Task:**

1. Write a chain-of-thought prompt asking the LLM to reason through possible causes
2. Evaluate the reasoning: are the steps logical?
3. Which root cause does the model identify as most likely?
4. Do you agree? What would you check first?

---


An ETL pipeline extracts data from a REST API, transforms it with Python, and loads it into BigQuery. The pipeline ran successfully for 30 days, then suddenly started failing with this error:

 
google.api_core.exceptions.Forbidden: 403 Access Denied: 
BigQuery BigQuery: Permission bigquery.tables.create denied
 

Nothing in the pipeline code changed. The GCP project and service account are the same. Reason through possible causes.


If nothing in your code or architecture changed, then this is almost certainly a permissions or environment drift issue. Think of it as: something external to your pipeline changed state after 30 days. Let’s reason through the most likely causes in order of probability.

1. IAM Role Change (Most Common)

Even if you didn’t change anything, someone (or something automated) may have.

The service account likely lost a role that includes:
bigquery.tables.create (e.g., BigQuery Data Editor, BigQuery Admin)
Possible triggers:
Manual IAM cleanup by a teammate
Terraform / IaC re-apply overwriting permissions
Org policy enforcement resetting roles

👉 Key insight:
Your pipeline worked before → it definitely had permission at some point → so something revoked it.

2. Dataset-Level Permissions Changed

BigQuery permissions can be granted at:

Project level
Dataset level

If:

The dataset was recreated, or
Access controls were modified at the dataset level

Then your service account might:

Still have project permissions
But lack access to that specific dataset

👉 This often happens if:

Someone deleted/recreated the dataset
A script replaced it
Access entries were reset
3. Table Creation Path Changed Implicitly

Even if your code didn’t change, the behavior of the pipeline might have due to data:

Maybe previously:
Tables already existed → no create needed
Now:
Pipeline is trying to create a new table or partition

Common triggers:

New date partition (e.g., daily tables like events_20260323)
New schema variation → triggers table recreation
Write disposition like WRITE_TRUNCATE on a missing table

👉 So the failure only appears when a create operation is required

4. Service Account Changed Indirectly

Even if you think it's the same, check:

Are you using:
Default service account (e.g., from Cloud Run / Composer / VM)?
Those can change behavior if:
Resource was redeployed
Underlying compute instance changed
Workload Identity mapping changed

👉 You might now be running as a different identity without realizing it.

5. Organization Policy Enforcement

A new Org Policy could block table creation:

Examples:

Restricting dataset creation locations
Disallowing certain actions unless explicitly granted
VPC Service Controls tightening access

👉 These can silently break previously working pipelines.

6. Credential Expiry / Key Rotation Edge Case

If using:

A service account key file

Possible issues:

Key was deleted or rotated
Pipeline falls back to a different identity with fewer permissions
7. Billing or Project State Issues (Less Likely)

Rare, but worth checking:

Project billing got disabled temporarily
Quota/project restrictions triggered unusual behavior
How to Debug This Quickly

Here’s the fastest way to pinpoint it:

Step 1: Confirm Identity

Log or print:

from google.auth import default
creds, project = default()
print(creds.service_account_email)
Step 2: Check IAM Roles

Look for missing roles like:

roles/bigquery.dataEditor
roles/bigquery.admin
Step 3: Check Dataset Permissions

In BigQuery UI:

Go to dataset → “Share”
Verify service account is listed
Step 4: Check If Table Exists

Ask:

Is the pipeline now trying to create a new table?
Did naming or partitioning change?
Most Likely Root Cause (Based on Pattern)

If I had to bet:

The pipeline started needing to create a table (or partition) after 30 days, and the service account does not actually have tables.create permission, even though it never needed it before.

Quick Fix

Grant one of:

BigQuery Data Editor (recommended minimum)
or explicitly add bigquery.tables.create

If you want, I can help you pinpoint the exact failure mode if you share:

Your load job config (write disposition, table naming)
Whether you're using partitioned tables or daily tables

## Part 4: Constraint Application (Optional, 10 minutes)

### Challenge 4.1: Constrained Output

Write a prompt that generates a Python function with ALL of these constraints:

- Function name: `validate_order_data`
- Input: pandas DataFrame
- Must check for: null values, negative amounts, future dates, duplicate IDs
- Output: a dictionary with check results
- Maximum 30 lines of code
- Must include type hints
- Must include a docstring
- No external libraries beyond pandas and datetime

**Your Task:**

1. Write the prompt with all constraints
2. Did the model satisfy ALL constraints?
3. Which constraints were hardest for the model to follow?

---

## Submission

For each challenge, document:

1. Your prompt (original and refined versions)
2. The LLM's output
3. Your evaluation of the output quality (1-5 scale)
4. What you learned about prompting from that challenge

## Reflection Questions

1. Which prompting technique (zero-shot, few-shot, chain-of-thought) produced the best results for data engineering tasks?
2. What made the biggest difference in output quality: specificity, examples, or constraints?
3. When would you choose each technique in your daily work?
