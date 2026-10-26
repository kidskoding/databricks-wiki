---
type: glossary
status: written
level: 90
section: Glossary
depth: 101
summary: "A network interface with a private IP address in your own virtual network that connects to a cloud service without using the public internet."
related:
  - "[[Azure Private Link]]"
  - "[[AWS PrivateLink]]"
  - "[[Private Service Connect]]"
  - "[[VNet Injection]]"
  - "[[Network Security Overview]]"
  - "[[Public vs Private IP]]"
aliases:
  - "Azure private endpoint"
  - "VPC endpoint"
  - "interface endpoint"
  - "PSC endpoint"
last_verified: 2026-10-26
tags:
  - glossary
  - flashcards
---

# Private Endpoint

> [!eli5] Summary
> A private endpoint puts a service's front door inside your own private network. Your traffic reaches the service without crossing the public internet.

**In data work:** A private endpoint is a network interface with a private IP address from one of your [[Subnet|subnets]]. Traffic to that address travels over the cloud provider's backbone to the target service. Private DNS makes the service's normal hostname resolve to the private IP, so applications need no changes. Combined with disabling public access, it keeps sensitive traffic off the internet, which many security reviews require.

**In Databricks:** Each cloud uses its own name for the same idea.
- **Azure ([[Azure Private Link]]):** Azure Databricks private endpoints use the `databricks_ui_api` sub-resource for UI and REST API traffic and `browser_authentication` for browser single sign-on. Only one `browser_authentication` endpoint can exist per region and private DNS zone, so Microsoft recommends hosting it in a dedicated workspace. The private DNS zone is `privatelink.azuredatabricks.net` in commercial regions.
- **AWS ([[AWS PrivateLink]]):** The endpoints are interface VPC endpoints for the workspace front end and the secure cluster connectivity relay.
- **Google Cloud ([[Private Service Connect]]):** The endpoints are Private Service Connect endpoints.

Private endpoints are optional. A small business with no regulatory requirement usually relies on [[Secure Cluster Connectivity|secure cluster connectivity]] and [[IP Access Lists|IP access lists]] instead, and adds private connectivity when a customer contract or auditor asks for it.

Seen in: [[Azure Private Link]], [[AWS PrivateLink]], [[Private Service Connect]], [[Network Security Overview]]

## Recall

Private endpoint::A private-IP network interface in your virtual network that connects privately to a cloud service.
Which Azure Databricks sub-resource supports browser SSO over Private Link?::browser_authentication (one per region and private DNS zone).

> [!sources]- Sources (last verified: 2026-10-26)
> - [Configure inbound Private Link for workspaces (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/network/front-end/front-end-private-connect)
> - [Private Link concepts (Azure Databricks)](https://learn.microsoft.com/en-us/azure/databricks/security/network/concepts/private-link)
> - [Azure Private Endpoint private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns)
> - [Configure classic private connectivity to Databricks (AWS)](https://docs.databricks.com/aws/en/security/network/classic/privatelink)
> - [Configure Inbound Private Service Connect (GCP)](https://docs.databricks.com/gcp/en/security/network/front-end/front-end-private-connect)
