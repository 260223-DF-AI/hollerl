# Exercise: Data Classification Challenge

## Overview

In this exercise, you will analyze various datasets and classify them based on their structure and characteristics. You will then recommend appropriate storage and processing approaches for each dataset.

## Learning Objectives

- Identify structured, semi-structured, and unstructured data types
- Understand the 5 V's of Big Data in practical contexts
- Recommend appropriate file formats for different use cases
- Evaluate storage and processing trade-offs

## Exercise Mode: Conceptual (Design/Analysis)

This is a classification and analysis exercise. No coding is required.

## The Challenge

You are a data engineer at a healthcare analytics company. Your team has received data from multiple sources and needs to design an appropriate data architecture. Analyze each dataset and provide recommendations.

## Part 1: Dataset Classification (45 minutes)

For each dataset below, complete the classification table:

### Dataset A: Patient Records

- Format: Relational database export (PostgreSQL dump)
- Size: 50 GB
- Contents: Patient demographics, visit history, billing codes
- Update frequency: Real-time inserts, daily batch updates

### Dataset B: Medical Images

- Format: DICOM files
- Size: 5 TB
- Contents: X-rays, MRIs, CT scans
- Update frequency: Continuous (100+ images/hour)

### Dataset C: Doctor Notes

- Format: PDF and Word documents
- Size: 200 GB
- Contents: Free-text clinical notes, handwritten prescriptions
- Update frequency: Daily additions

### Dataset D: IoT Sensor Data

- Format: JSON from medical devices
- Size: 10 GB/day (streaming)
- Contents: Heart rate, blood pressure, temperature readings
- Update frequency: Real-time streaming (1000 events/second)

### Dataset E: Insurance Claims

- Format: XML files from external partners
- Size: 2 GB/week
- Contents: Claims, approvals, denials with nested structures
- Update frequency: Weekly batch

### Classification Table

| Dataset | Data Type       | Volume    | Velocity   | Variety | Veracity    |
|---------|-----------------|-----------|------------|---------|-------------|
| A       | Structured      | 50 GB     | Real-time  | Low     | Medium-High |
| B       | Unstructured    | 5 TB      | Continuous | Low     | High        |
| C       | Unstructured    | 200 GB    | Daily      | Low     | Low-Med     |
| D       | Semi-structured | 10 GB/day | Real-time  | Low     | Med-High    |
| E       | Semi-structured | 2 GB/week | Weekly     | High    | Med         |

## Part 2: Storage Recommendations (45 minutes)

For each dataset, recommend:

1. **Primary Storage Solution** (e.g., Data Lake, Data Warehouse, Object Storage)
2. **File Format** (e.g., Parquet, JSON, CSV, Avro)
3. **Justification** (2-3 sentences explaining your choice)

Use this template:

```
### Dataset [X]: [Name]

**Storage:** [Your recommendation]
**Format:** [Your recommendation]
**Justification:** [Your reasoning]
```


### Dataset [A]: Patient Records

**Storage:** Data Warehouse
**Format:** SQL
**Justification:** The data is structured and needs frequent updates.


### Dataset [B]: Medical Images

**Storage:** Object Storage
**Format:** DICOM
**Justification:** The data is large, but needs frequent updates.


### Dataset [C]: Doctor Notes

**Storage:** Object Storage
**Format:** PDF
**Justification:** The data is unstructured, but there's a large amount of it.


### Dataset [D]: IoT Sensor Data

**Storage:** Data Lake
**Format:** JSON
**Justification:** The data is large, but semi-structured.


### Dataset [E]: Insurance Claims

**Storage:** Data Lake
**Format:** XML
**Justification:** The data is large, but semi-structured.



## Part 3: Architecture Diagram (30 minutes)

Create a simple architecture diagram showing how all five datasets would flow into a unified analytics platform. Your diagram should include:

- Data sources (the 5 datasets)
- Ingestion layer
- Storage layer(s)
- Processing layer
- Analytics/consumption layer

You may use any diagramming tool or create an ASCII diagram in markdown.

## Definition of Done

- Classification table completed with all 25 cells filled
- Storage recommendations for all 5 datasets with justifications
- Architecture diagram showing data flow
- All recommendations are realistic and aligned with the written content

## Submission

Save your deliverables as:

- `classification-table.md` - The completed classification table
- `storage-recommendations.md` - Your storage and format recommendations
- `architecture-diagram.md` - Your data flow diagram

## Time Estimate

2-3 hours

## Resources

- Written Content: c165-c175 (Big Data, Data Types, File Formats)
- Reference materials on Parquet, Avro, and ORC

## Rubric

| Criteria | Points |
|----------|--------|
| Classification accuracy | 30 |
| Storage recommendations quality | 30 |
| Architecture diagram completeness | 25 |
| Justification quality | 15 |
| **Total** | **100** |
