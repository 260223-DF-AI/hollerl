# Collaborative Project: Dimensional Model Design

## Overview

This is a **collaborative project** where you will work with a partner to design a complete dimensional model for a real-world business scenario. This project synthesizes the entire week's topics including data warehousing, dimensional modeling, star schema design, and slowly changing dimensions.

## Learning Objectives

- Apply dimensional modeling methodology to a business problem
- Design fact and dimension tables following best practices
- Implement slowly changing dimension strategies
- Practice collaborative design and peer review
- Create professional technical documentation

## Exercise Mode: Collaborative (Hybrid - Design then Implement)

This is a pair exercise using the **Architect/Critic** format. One partner designs while the other reviews and challenges.

## Team Roles

- **Architect**: Leads the design, creates diagrams, defines schemas
- **Critic**: Reviews for completeness, identifies gaps, suggests improvements

Roles should swap halfway through the project.

## The Business Scenario

**Company:** StreamFlix - A video streaming service

**Business Requirements:**
StreamFlix needs a data warehouse to analyze:

1. **User Viewing Behavior**: What content is being watched, when, and for how long
2. **Content Performance**: Which shows/movies perform best by various dimensions
3. **Subscription Analytics**: User acquisition, churn, and revenue analysis
4. **Device Analytics**: Which devices are used, streaming quality metrics

**Source Systems:**

- User database (PostgreSQL)
- Content catalog (MongoDB)
- Streaming events (Kafka)
- Billing system (Stripe API)
- Device telemetry (IoT platform)

## Deliverables

### Part 1: Business Process Selection

Identify 2-3 key business processes to model. For each:

- Business process name
- Business questions it will answer
- Potential grain of the fact table
- Source systems involved

User Viewing Behavior
What is popular, how long do people watch, what are the most common times to watch?
One row per content watched by user.
Device telemetry, Kafka, content catalog, MongoDB.

Subscription Analytics
User growth, money being made, when users join
One row per subscription
PostgreSQL, Stripe API

### Part 2: Dimensional Model Design

For each business process, create:

#### 2.1 Fact Table Design

Document for each fact table:

- Table name
- Grain statement (one specific sentence)
- List of foreign keys to dimensions
- List of measures with type (additive/semi-additive/non-additive)
- Fact table type (transaction/periodic snapshot/accumulating)

#### 2.2 Dimension Table Design

Document for each dimension:

- Table name
- Surrogate key name
- Natural key(s)
- Key attributes (at least 10 per major dimension)
- Hierarchies
- SCD Type for each attribute (0, 1, 2, or 3)

#### 2.3 Star Schema Diagram

Create a diagram showing:

- Fact tables in the center
- Dimension tables surrounding facts
- Foreign key relationships
- Cardinalities

Use Mermaid, draw.io, or another diagramming tool.

### Part 3: Physical Design Considerations

Document:

- Partitioning strategy for each fact table
    Date Ranges
- Clustering columns for each table
    Content/Watch time
    Subscription type and pricing/user/duration
- Estimated table sizes and growth rates
    A lot real time
    Set amount daily
- Recommended load frequency
    Real-time
    Daily

### Part 4: SCD Implementation Example

Write SQL DDL for one dimension with SCD Type 2:

CREATE TABLE user (user_id int PRIMARY KEY, gender string, age int, ssn string, region string, date_updated DATE);
UPDATE user SET col1 = val1,... WHERE user_id = whatever;

- Table structure with effective/end dates
- Sample MERGE statement for handling updates

MERGE dataset.oldusers
USING dataset.newusers
ON dataset.oldusers.user_id = dataset.newusers.user_id

WHEN MATCHED THEN
  UPDATE SET col = dataset.newusers.col

WHEN NOT MATCHED THEN
  INSERT (user_id, cols)
  VALUES (val1, val2, etc.);

### Part 5: Peer Review

Swap designs with your partner and complete a review checklist:

| Criterion | Y/N | Comments |
|-----------|-----|----------|
| Grain clearly defined | | |
| Surrogate keys used | | |
| Dimensions fully denormalized | | |
| SCD types appropriate | | |
| Date dimension included | | |
| Conformed dimensions identified | | |
| Partitioning makes sense | | |
| Documentation complete | | |

## Definition of Done

- Business process matrix completed
- At least 2 fact tables fully designed
- At least 5 dimension tables fully designed
- Star schema diagram created
- SCD Type 2 SQL implementation written
- Peer review checklist completed by partner
- All documentation is clear and professional

## Submission

Create a folder `streamflix-dimensional-model/` containing:

- `README.md` - Project overview and team members
- `business-processes.md` - Part 1 deliverable
- `fact-tables.md` - Fact table definitions
- `dimension-tables.md` - Dimension table definitions
- `schema-diagram.md` - Star schema diagram (embedded or linked)
- `physical-design.md` - Partitioning and clustering strategy
- `scd-implementation.sql` - SCD Type 2 SQL code
- `peer-review.md` - Completed review checklist

## Resources

- Written Content: c192-c201 (Dimensional Modeling)
- Kimball Dimensional Modeling Techniques: <https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/>

## Collaboration Tips

1. Start with a 15-minute planning session to align on approach
2. Use screen sharing or a collaborative whiteboard
3. The Critic should ask "why" questions, not just approve
4. Document disagreements and how you resolved them
5. Both partners should understand every design decision
