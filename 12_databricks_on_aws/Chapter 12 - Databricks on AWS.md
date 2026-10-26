---
type: chapter
status: written
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
  - "[[Hive Metastore Federation for AWS Glue]]"
  - "[[AWS Marketplace and Billing]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Customer-Managed Keys on AWS]]"
  - "[[Databricks on AWS GovCloud]]"
last_verified: 2026-10-25
tags:
  - chapter
---

# Chapter 12 - Databricks on AWS

> [!story] Context
> [[Chapter 11 - Azure Databricks]] ended with [[Customer-Managed Keys on Azure]], completing the Azure deployment model. This chapter covers Amazon Web Services, where Databricks is a separate vendor's product that reaches into your AWS account only through IAM roles you create.

**Databricks on Amazon Web Services, covering cross-account roles, customer-managed VPCs, PrivateLink, and S3.**

## The story of this chapter

### Era

AWS was the first cloud Databricks ran on (see [[The Founding of Databricks]]). Databricks on AWS is sold by Databricks, either directly (credit card or contract) or through AWS Marketplace, where Databricks introduced a pay-as-you-go offering in 2022. The account console is at `accounts.cloud.databricks.com`. See [[Databricks on AWS Overview]].

### Getting started

Express setup creates an account and a serverless workspace with only an email address. Serverless workspaces became generally available on AWS on January 29, 2026; they use serverless compute and Databricks-managed default storage, so they create nothing in your AWS account. Classic workspaces, which run compute in your account, are created with the AWS Quickstart (a CloudFormation stack), automated configuration, manual configuration, or the Account API and Terraform ([[Account Setup on AWS]]).

### Classic building blocks

A classic workspace is assembled from account-level configuration objects. A credential configuration holds the [[Cross-Account IAM Role]] that lets the control plane launch EC2 instances. A storage configuration holds the [[Workspace Storage Bucket]], an S3 bucket for workspace system data that should not hold production data. An optional network configuration places compute in a [[Customer-Managed VPC on AWS]] with at least two private subnets in different availability zones. [[AWS PrivateLink]] adds private front-end and back-end endpoints, controlled by private access settings, on the Enterprise plan.

### Data access

The legacy pattern attached [[Instance Profiles]] to clusters, which gave every user of a cluster the same S3 access. [[Unity Catalog]] replaced it with storage credentials backed by self-assuming IAM roles and external locations ([[S3 Access via Unity Catalog]]). Since January 20, 2025, Databricks blocks storage credentials whose roles are not self-assuming. Tables already registered in AWS Glue can be governed in place through catalog federation ([[Hive Metastore Federation for AWS Glue]]).

### Cost and compute

The Databricks charge (in DBUs) is billed by Databricks or through AWS Marketplace, while EC2, EBS, S3, and networking for classic compute appear on the AWS bill ([[AWS Marketplace and Billing]]). Instance choice, Arm-based Graviton types, fleet types, and spot with fallback are the main levers on classic cost ([[EC2 Instance Types and Graviton]]).

### Security and compliance

[[Customer-Managed Keys on AWS]] encrypt managed services, the workspace bucket, and EBS volumes with AWS KMS keys on the Enterprise tier. [[Databricks on AWS GovCloud]] is a separate environment in `us-gov-west-1` with FedRAMP High and DoD IL5 authorizations and the compliance security profile on every workspace.

### Next

[[Chapter 13 - Databricks on Google Cloud]] covers the same concepts on Google Cloud, where Databricks is bought through Google Cloud Marketplace and authenticates with Google service accounts.

## Notes in reading order

<!-- GENERATED:reading-order START (scripts/scaffold.py) -->

| # | Note | Depth | What it covers |
|---|---|---|---|
| 1 | [[Databricks on AWS Overview]] | 101 Beginner | How Databricks runs on AWS, sold by Databricks directly or through AWS Marketplace. |
| 2 | [[Account Setup on AWS]] | 101 Beginner | Signing up, then creating a serverless workspace or a classic workspace with Quickstart, manual setup, or Terraform. |
| 3 | [[Cross-Account IAM Role]] | 301 Advanced | The IAM role that lets the Databricks control plane launch and manage EC2 instances in your AWS account. |
| 4 | [[Workspace Storage Bucket]] | 201 Practitioner | The S3 bucket a classic AWS workspace uses for its own system data, and why production data belongs elsewhere. |
| 5 | [[Customer-Managed VPC on AWS]] | 301 Advanced | Running classic compute in a VPC you create and control, with subnet, security group, and egress requirements. |
| 6 | [[AWS PrivateLink]] | 401 Expert | Private front-end and back-end connectivity between your VPCs and Databricks using VPC interface endpoints. |
| 7 | [[Instance Profiles]] | 301 Advanced | The legacy way clusters got S3 access by attaching an IAM role to EC2 nodes, and why Unity Catalog replaced it. |
| 8 | [[S3 Access via Unity Catalog]] | 301 Advanced | Storage credentials backed by self-assuming IAM roles, plus external locations, for governed S3 access. |
| 9 | [[Hive Metastore Federation for AWS Glue]] | 401 Expert | Governing and reading tables registered in the AWS Glue Data Catalog from Unity Catalog through catalog federation. |
| 10 | [[AWS Marketplace and Billing]] | 201 Practitioner | Paying Databricks directly or through AWS Marketplace, and where the EC2, EBS, S3, and networking costs of classic compute appear. |
| 11 | [[EC2 Instance Types and Graviton]] | 301 Advanced | Picking EC2 node types, fleet types, spot instances, and Arm-based Graviton for classic compute price and performance. |
| 12 | [[Customer-Managed Keys on AWS]] | 401 Expert | Encrypting managed services, the workspace storage bucket, and EBS volumes with AWS KMS keys you control. |
| 13 | [[Databricks on AWS GovCloud]] | 401 Expert | The separate Databricks environment in AWS GovCloud (US) for FedRAMP High, DoD IL5, and other US public-sector workloads. |

<!-- GENERATED:reading-order END -->

> [!nextup] Up next
> [[Databricks on AWS Overview]]
