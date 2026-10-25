---
type: path
status: written
level: 80
section: Learning Paths
depth: 301
summary: Every AWS-specific rabbit hole in order.
personas:
  - admin
chapter: "[[Chapter 80 - Learning Paths]]"
prev: "[[Path - Azure Deep Dive]]"
next: "[[Path - Google Cloud Deep Dive]]"
evolved_from: []
evolved_into: []
cloud_equivalent:
  - "[[Path - Azure Deep Dive]]"
  - "[[Path - Google Cloud Deep Dive]]"
related:
  - "[[Databricks on AWS Overview]]"
  - "[[Account Setup on AWS]]"
  - "[[Cross-Account IAM Role]]"
  - "[[Workspace Storage Bucket]]"
  - "[[S3 Access via Unity Catalog]]"
  - "[[Instance Profiles]]"
  - "[[Customer-Managed VPC on AWS]]"
  - "[[AWS PrivateLink]]"
  - "[[EC2 Instance Types and Graviton]]"
  - "[[Customer-Managed Keys on AWS]]"
  - "[[Hive Metastore Federation for AWS Glue]]"
  - "[[AWS Marketplace and Billing]]"
  - "[[Unity Catalog]]"
  - "[[Path - Platform Admin]]"
  - "[[Cloud Comparison - Azure vs AWS vs GCP]]"
aliases:
  - AWS Path
  - Databricks on AWS Path
prereqs:
  - "[[Path - Platform Admin]]"
unlocks: []
clouds:
  - aws
mastery: new
last_verified: 2026-10-25
tags:
  - path
---

# Path - AWS Deep Dive

> [!persona] Who this is for
> **Who:** an AWS admin, cloud architect, or security lead running Databricks on Amazon Web Services, plus engineers who need to know how clusters reach S3.
> **Goal:** understand everything AWS-specific: how you buy it, the cross-account role, the workspace bucket, customer-managed VPCs, PrivateLink, S3 access through Unity Catalog, instance choices, and KMS keys.
> **Outcome:** you can deploy a production workspace in your own VPC with PrivateLink, governed S3 access through IAM roles, customer-managed keys, and sensible instance and cost choices.

## Before you start

Read [[Path - Platform Admin]] first, or at least its Stages 1 to 3. You need an AWS account where you can create IAM roles and policies, S3 buckets, VPCs, and KMS keys, and a Databricks account where you are an account admin. Free Edition does not help here.

## The route

### Stage 1: How Databricks runs on AWS (101 to 201)

**Goal:** know what lives in Databricks' account, what lives in yours, and how you pay.

1. [[Databricks on AWS Overview]]: the model, bought from Databricks or through AWS Marketplace.
2. [[Account Setup on AWS]]: sign-up, the first workspace, quick setup versus manual.
3. [[AWS Marketplace and Billing]] (201): one bill or two, plus EC2 and S3 costs.
4. [[Control Plane and Compute Plane]] (201): the split, seen through AWS resources.
5. [[Workspace Storage Bucket]] (201): the S3 bucket each workspace keeps for itself.
6. [[Amazon S3]]: where your data lives.

> [!check] Checkpoint
> Create a workspace with quick setup (the CloudFormation-based flow) in a test AWS account. Open CloudFormation and IAM and list what was created: the cross-account role, the workspace bucket, and the network. Note which resources are in your account and which are not.

### Stage 2: IAM and data access (201 to 301)

**Goal:** understand every role Databricks uses and give Unity Catalog governed S3 access.

1. [[Cross-Account IAM Role]] (301): the role that lets Databricks launch EC2 in your account.
2. [[IAM]]: the glossary entry for AWS identity and access.
3. [[Instance Profiles]] (301): the legacy way clusters reached S3, and why to move off it.
4. [[S3 Access via Unity Catalog]] (301): storage credentials backed by IAM roles.
5. [[Storage Credentials and External Locations]] (301): the Unity Catalog objects on top.
6. [[Metastore]] (201): one per region.
7. [[Users Groups and Service Principals]] (201): Databricks identities.
8. [[Single Sign-On]] (201) and [[SCIM Provisioning]] (301): connecting your IdP, such as Okta or Entra ID.

> [!check] Checkpoint
> Create an IAM role with a trust policy for Unity Catalog and an S3 policy for one bucket, register it as a storage credential (Catalog Explorer shows the external ID and trust policy to paste back into IAM), and create an external location on `s3://<bucket>/raw`. Run `LIST 's3://<bucket>/raw'` and create an external table there. Confirm that a cluster without any instance profile can still read it.

### Stage 3: Private networking (301 to 401)

**Goal:** run compute in your VPC and keep traffic on the AWS backbone.

1. [[Network Security Overview]] (301): the full map of controls.
2. [[Customer-Managed VPC on AWS]] (301): your VPC, subnets, and security groups.
3. [[AWS PrivateLink]] (401): private front-end and back-end connections.
4. [[Serverless Network Security]] (401): network connectivity configurations and egress control for serverless.
5. [[IP Access Lists]] (301): restricting the front door.
6. [[VPC and VNet]], [[Subnet]], and [[Public vs Private IP]]: the glossary entries behind it.

> [!check] Checkpoint
> Create a VPC with two private subnets in different availability zones and a security group that meets the Databricks requirements, register it as a network configuration in the account console, and deploy a workspace with it. Start a cluster and confirm its EC2 instances have no public IPs. Sketch where the PrivateLink VPC endpoints for the workspace and the secure cluster connectivity relay would go.

### Stage 4: Compute, keys, and integrations (301 to 401)

**Goal:** choose instances wisely, own your keys, and connect to the AWS data estate.

1. [[EC2 Instance Types and Graviton]] (301): node types, spot, and Graviton.
2. [[Spot Instances]]: the glossary entry for cheap, interruptible capacity.
3. [[Encryption]] (301): defaults, and where your keys fit.
4. [[Customer-Managed Keys on AWS]] (401): KMS keys for managed services and workspace storage.
5. [[Compliance Security Profile]] (401): hardened settings for HIPAA, PCI-DSS, and more.
6. [[Databricks on AWS GovCloud]] (401): US public-sector and regulated workloads.
7. [[Hive Metastore Federation for AWS Glue]] (401): reading Glue-registered tables from Unity Catalog.
8. [[Audit Logs]] (301): log delivery and system tables.
9. [[Terraform Provider]] (301): the usual way to automate all of the above.
10. [[Disaster Recovery]] (401): multi-region plans on AWS.

> [!check] Checkpoint
> Create a compute policy that allows only Graviton instance types with spot workers and an on-demand driver, and run a job with it; compare its cost in `system.billing.usage` with the same job on x86 on-demand. If you have a Glue catalog, create a federated catalog for it and query one table. Write down which KMS keys you would create for managed services and for workspace storage.

## Rabbit holes

- **The same ideas elsewhere:** [[Path - Azure Deep Dive]], [[Path - Google Cloud Deep Dive]], and [[Cloud Comparison - Azure vs AWS vs GCP]].
- **Migrating from AWS services:** [[Amazon Redshift]] and [[Migrating from Amazon Redshift]].
- **Cost:** [[Compute Policies]], [[Cost Optimization Checklist]], [[Tagging for Chargeback]].
- **Automation:** [[Declarative Automation Bundles]] and [[Databricks SDKs and REST API]].
- **Governance extras:** [[Row Filters and Column Masks]], [[Attribute-Based Access Control]].

## You are done when

- You can name every IAM role Databricks uses on AWS and what each is for.
- Unity Catalog reaches S3 through IAM-role storage credentials, and instance profiles are retired.
- Production compute runs in your own VPC with no public IPs, with a PrivateLink design.
- You can choose instance types, spot, and Graviton for a workload and justify the cost.
- You know which KMS keys protect what, and when GovCloud or the compliance profile is needed.

> [!nextup] Up next
> The same journey on Google: [[Path - Google Cloud Deep Dive]].

> [!sources]- Sources (last verified: 2026-10-25)
> - Route assembled on 2026-10-25 from chapter 12 (Databricks on AWS), chapter 14, and chapter 07 of the vault index (`llms.txt`). Product facts and official documentation links live in each linked note's `[!sources]` callout; [[Unity Catalog]] cites the AWS Unity Catalog documentation.
> - Exact VPC, security group, and IAM trust-policy requirements in the checkpoints were not re-checked for this path; confirm them in [[Customer-Managed VPC on AWS]] and [[S3 Access via Unity Catalog]] before deploying.
