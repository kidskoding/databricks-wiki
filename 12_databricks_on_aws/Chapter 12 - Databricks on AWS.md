---
type: chapter
status: stub
part: 2
level: 12
section: Databricks on AWS
summary: Databricks on Amazon Web Services, covering cross-account roles, customer-managed VPCs, PrivateLink, and S3.
prev: "[[Customer-Managed Keys on Azure]]"
next: "[[Databricks on AWS Overview]]"
notes:
  - "[[Databricks on AWS Overview]]"
  - "[[Account Setup on AWS]]"
  - "[[Cross-Account IAM Role]]"
  - "[[Workspace Storage Bucket]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[AWS PrivateLink]]"
  - "[[Instance Profiles]]"
  - "[[S3 Access via Unity Catalog]]"
  - "[[AWS Glue and Lake Formation Federation]]"
  - "[[AWS Marketplace and Billing]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Customer-Managed Keys on AWS]]"
  - "[[Databricks on AWS GovCloud]]"
last_verified:
tags:
  - chapter
---

# Chapter 12 - Databricks on AWS

> [!story] Previously
> (to write)

**Databricks on Amazon Web Services, covering cross-account roles, customer-managed VPCs, PrivateLink, and S3.**

## The story of this chapter

(to write)

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Databricks on AWS Overview]] | 101 Beginner | How Databricks runs on AWS, sold by Databricks directly or through AWS Marketplace. |
| 2 | [[Account Setup on AWS]] | 101 Beginner | Signing up, creating a workspace, and quick setup versus manual setup. |
| 3 | [[Cross-Account IAM Role]] | 301 Advanced | The IAM role that lets Databricks launch EC2 instances in your account. |
| 4 | [[Workspace Storage Bucket]] | 201 Practitioner | The S3 bucket each workspace uses for its own system data. |
| 5 | [[Customer-Managed VPC on AWS]] | 301 Advanced | Running classic compute in a VPC you create and control. |
| 6 | [[AWS PrivateLink]] | 401 Expert | Private front-end and back-end connectivity between your VPC and Databricks. |
| 7 | [[Instance Profiles]] | 301 Advanced | The legacy way clusters got S3 access, and why Unity Catalog replaced it. |
| 8 | [[S3 Access via Unity Catalog]] | 301 Advanced | Storage credentials backed by IAM roles for governed S3 access. |
| 9 | [[AWS Glue and Lake Formation Federation]] | 401 Expert | Reading tables registered in AWS Glue from Unity Catalog. |
| 10 | [[AWS Marketplace and Billing]] | 201 Practitioner | Paying Databricks directly or through the AWS bill, plus EC2 costs. |
| 11 | [[EC2 Instance Types and Graviton]] | 301 Advanced | Picking node types, spot instances, and ARM-based Graviton for price and performance. |
| 12 | [[Customer-Managed Keys on AWS]] | 401 Expert | Encrypting managed services and workspace storage with AWS KMS keys. |
| 13 | [[Databricks on AWS GovCloud]] | 401 Expert | Databricks for US public-sector and regulated workloads. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Databricks on AWS Overview]]
