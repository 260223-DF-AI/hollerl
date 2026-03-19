# Exercise: Cloud Provider Research and Comparison

## Overview

In this exercise, you will research and compare the three major cloud providers (AWS, Azure, GCP) with a focus on their data services. This exercise reinforces the cloud computing concepts covered in today's written content.

## Learning Objectives

- Compare cloud provider offerings for data services
- Evaluate trade-offs between different cloud platforms
- Practice structured technical analysis and documentation
- Develop decision-making skills for cloud platform selection

## Exercise Mode: Conceptual (Design/Analysis)

This is a research and analysis exercise. No coding is required.

## The Scenario

Your company is a mid-sized e-commerce retailer planning to migrate their on-premises data infrastructure to the cloud. They need to:

1. Store transactional data from their PostgreSQL database
2. Build a data warehouse for business analytics
3. Process daily batch jobs for inventory management
4. Store product images and customer documents
5. Eventually implement real-time analytics for fraud detection

Leadership has asked you to evaluate AWS, Azure, and GCP and provide a recommendation.

## Deliverables

### Part 1: Service Mapping Matrix (30 minutes)

Create a comparison table mapping the company's needs to specific services from each provider.

| Requirement                                  | AWS Service               | Azure Service                 | GCP Service                  |
|----------------------------------------------|---------------------------|-------------------------------|------------------------------|
| Managed PostgreSQL                           | Amazon RDS for PostgreSQL | Azure Database for PostgreSQL | Cloud SQL for PostgreSQL     |
| Data Warehouse                               | Amazon Redshift           | Azure Data Warehouse          | Google Cloud BigQuery        |
| Batch Processing                             | AWS Batch                 | Azure Batch                   | Google Cloud Batch           |
| Object Storage                               | Amazon S3                 | Azure Blob Storage            | Google Cloud Storage         |
| Stream Processing                            | Amazon Kinesis            | Azure Stream Analytics        | Streaming analytics solutions|

### Part 2: Cost Analysis (30 minutes)

Using each provider's pricing calculator, estimate monthly costs for:

- 500 GB of data warehouse storage
- 10 TB of object storage
- 1000 compute hours per month

AWS
500 GB   - 19,038.40, https://calculator.aws/#/estimate
10 TB    - 230, https://aws.amazon.com/s3/pricing/
1000 hrs - 17992, https://aws.amazon.com/ec2/pricing/on-demand/

Azure
500 GB   - 2.5, https://azure.microsoft.com/en-us/pricing/details/synapse-analytics/#pricing
10 TB    - 1500, https://azure.microsoft.com/en-us/pricing/details/storage/blobs/
1000 hrs - 971.63, https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/#pricing

GCP
500 GB   - 11.5, https://cloud.google.com/bigquery/pricing#storage-pricing
10 TB    - 102.4, https://cloud.google.com/storage/pricing-examples#detailed
1000 hrs - 62.5, https://cloud.google.com/bigquery/pricing#on-demand-compute-pricing

Document your findings with links to the pricing pages you used.

### Part 3: Recommendation Report (1 hour)

Write a 1-2 page recommendation report that includes:

1. **Executive Summary** (2-3 sentences)
2. **Evaluation Criteria** (list 5 factors you considered)
3. **Provider Comparison** (strengths/weaknesses of each)
4. **Recommendation** (which provider and why)
5. **Migration Considerations** (3 potential challenges)

## Definition of Done

- Completed service mapping matrix with all 15 cells filled
- Cost estimates with documented sources
- Recommendation report with all 5 sections
- Clear, professional writing without jargon overload

## Submission

Save your deliverables as:

- `service-mapping.md` - The comparison table
- `cost-analysis.md` - Cost estimates with sources
- `recommendation-report.md` - Your final recommendation

## Time Estimate

2-3 hours

## Resources

- AWS Pricing Calculator: <https://calculator.aws/>
- Azure Pricing Calculator: <https://azure.microsoft.com/en-us/pricing/calculator/>
- GCP Pricing Calculator: <https://cloud.google.com/products/calculator>
- Written Content: c153-c164 (Cloud Computing)

## Rubric

| Criteria | Points |
|----------|--------|
| Service mapping accuracy | 25 |
| Cost analysis completeness | 25 |
| Recommendation reasoning | 30 |
| Professional presentation | 20 |
| **Total** | **100** |
