---
type: concept
status: written
level: 2
section: The Big Data Era
depth: 301
summary: Hadoop's resource manager, which decides which job gets which machines.
personas:
  - engineer
  - admin
chapter: "[[Chapter 02 - The Big Data Era]]"
prev: "[[MapReduce]]"
next: "[[Apache Hive]]"
evolved_from:
  - "[[MapReduce]]"
evolved_into:
  - "[[Serverless Compute]]"
  - "[[Kubernetes]]"
cloud_equivalent: []
related:
  - "[[Apache Hadoop]]"
  - "[[HDFS]]"
  - "[[Cluster]]"
  - "[[Container]]"
  - "[[Driver and Executors]]"
  - "[[Compute Types]]"
  - "[[Autoscaling]]"
  - "[[Compute Policies]]"
  - "[[Apache Spark]]"
aliases:
  - Yet Another Resource Negotiator
  - Hadoop YARN
  - ResourceManager
  - NodeManager
prereqs:
  - "[[MapReduce]]"
  - "[[Distributed Systems]]"
unlocks:
  - "[[Apache Spark]]"
  - "[[Driver and Executors]]"
  - "[[Compute Types]]"
clouds:
  - aws
  - azure
  - gcp
mastery: new
last_verified: 2026-10-25
tags:
  - concept
  - flashcards
---

# YARN

Mastery: `INPUT[inlineSelect(option(new), option(learning), option(solid)):mastery]`

> [!story] Context
> [[MapReduce]] provided batch processing on Hadoop. In Hadoop 1, one component, the JobTracker, both managed cluster resources and ran MapReduce jobs, so a cluster could run only MapReduce. Hadoop 2 moved resource management into a separate layer, YARN (Yet Another Resource Negotiator).

> [!eli5] Summary
> YARN allocates the computing power and memory of a shared group of computers. Programs request resources, and YARN decides which program receives which machines and when, so many different programs can share the same cluster.

> [!analogy]- Analogy: a shared office with bookable desks
> | Shared office | YARN |
> |---|---|
> | Office manager holding the booking calendar | ResourceManager |
> | Caretaker on each floor | NodeManager |
> | A desk with fixed space and power | Container: a slice of one machine's memory and CPU |
> | Project lead who books desks for one project | ApplicationMaster |
> | Department desk budgets | Scheduler queues |

## Background

The Hadoop 1 JobTracker had three responsibilities: tracking free capacity on every machine, scheduling every map and reduce task, and monitoring and restarting tasks. At large cluster sizes this made it a bottleneck and a single point of failure. It also supported only MapReduce, so other processing frameworks required separate clusters.

YARN separates these responsibilities. A global ResourceManager allocates resources, and each application runs its own ApplicationMaster to schedule and monitor its work. MapReduce becomes one application type among many.

YARN became generally available in **Hadoop 2.2.0** on **October 15, 2013**. The release announcement describes it as a general-purpose resource management system that allows MapReduce and other data processing frameworks and services to run on Hadoop.

## Overview

| Component | Location | Function |
|---|---|---|
| **ResourceManager (RM)** | One per cluster; Active/Standby pair for high availability | Allocates cluster resources. Contains the **Scheduler**, which allocates resources subject to capacities and queues, and the **ApplicationsManager**, which accepts job submissions, starts each application's ApplicationMaster, and restarts it on failure. |
| **NodeManager (NM)** | One per worker machine | Launches containers, monitors their CPU, memory, disk, and network usage, and reports to the RM. |
| **ApplicationMaster (AM)** | One per application, in a container | Negotiates containers from the RM, works with NodeManagers to run tasks, and monitors progress. Framework-specific. |
| **Container** | On a NodeManager | An allocation of resources (memory, virtual cores) on one machine in which a task runs. |

The Scheduler is pluggable. The YARN documentation names the CapacityScheduler and the FairScheduler as examples:

| Scheduler | Allocation model |
|---|---|
| **CapacityScheduler** | Hierarchical queues, each guaranteed a share of cluster capacity, with the ability to use idle capacity |
| **FairScheduler** | Resources divided so that, over time, applications or queues receive equal or weighted shares |

## How it works

```mermaid
sequenceDiagram
  participant C as Client
  participant RM as ResourceManager
  participant NM1 as NodeManager 1
  participant AM as ApplicationMaster
  participant NM2 as NodeManager 2
  C->>RM: submit application
  RM->>NM1: launch container for the AM
  NM1->>AM: start ApplicationMaster
  AM->>RM: request containers (memory, vcores)
  RM-->>AM: containers granted
  AM->>NM2: launch task in container
  NM2-->>AM: task status
  AM-->>RM: unregister; release containers
```

Application lifecycle:

1. A client submits an application to the ResourceManager, for example through `YarnClient`.
2. The RM allocates a container and launches the application's ApplicationMaster in it.
3. The AM requests containers from the RM, optionally preferring nodes that hold its HDFS input.
4. The Scheduler grants containers according to queue capacities and policies.
5. The AM instructs NodeManagers to launch tasks in the granted containers and monitors them.
6. On completion, the AM unregisters and its containers are released.

Common commands:

```bash
yarn application -list                                  # running applications
yarn application -kill application_1700000000000_0042   # stop an application
yarn node -list -all                                    # NodeManagers and states
yarn logs -applicationId application_1700000000000_0042 # aggregated logs
yarn queue -status analytics                            # queue capacity and usage
```

Two CapacityScheduler queues splitting a cluster 70/30 (`capacity-scheduler.xml`):

```xml
<property>
  <name>yarn.scheduler.capacity.root.queues</name>
  <value>etl,analytics</value>
</property>
<property>
  <name>yarn.scheduler.capacity.root.etl.capacity</name>
  <value>70</value>
</property>
<property>
  <name>yarn.scheduler.capacity.root.analytics.capacity</name>
  <value>30</value>
</property>
```

Submitting a Spark application to a YARN cluster:

```bash
spark-submit --master yarn --deploy-mode cluster \
  --num-executors 20 --executor-memory 8g --executor-cores 4 \
  daily_sales.py
```

In cluster deploy mode, the Spark driver runs inside the ApplicationMaster's container and each executor runs in a YARN container. Compare [[Driver and Executors]].

## Small-business considerations

> [!smallbiz] Small-business considerations
> YARN addresses contention for a fixed, shared, owned cluster. In the cloud, each workload can receive its own compute, sized for that workload and stopped when idle, so queue management is rarely necessary. Use [[Serverless Compute]] or [[Jobs Compute|job compute]] with [[Auto Termination|auto termination]], and apply a [[Compute Policies|compute policy]] to cap cluster sizes.

> [!bridge]- In Databricks today
> Databricks does not use YARN. Its responsibilities are divided as follows:
>
> | YARN responsibility | Databricks equivalent |
> |---|---|
> | ResourceManager allocating machines | The Databricks [[Control Plane and Compute Plane\|control plane]] provisions cloud VMs per cluster, or runs [[Serverless Compute]] |
> | Queues guaranteeing team capacity | Separate clusters or SQL warehouses per team, constrained by [[Compute Policies]] and budgets |
> | NodeManagers and containers | Worker VMs running Spark executors (see [[Driver and Executors]]) |
> | ApplicationMaster per job | The Spark driver per cluster; [[Lakeflow Jobs]] for multi-task workflows |
> | Resizing capacity | [[Autoscaling]] and serverless scaling |
>
> YARN shares a fixed pool of machines, so scheduling is zero-sum. Databricks provisions elastic cloud machines, so the constraint becomes cost rather than capacity. See [[Compute Types]].

## Cloud differences

> [!azure]- Azure Databricks
> No YARN. Classic clusters run on Azure VMs provisioned by Databricks, and serverless compute runs in the Databricks serverless compute plane. Azure subscription quotas limit the size of classic clusters.

> [!aws]- Databricks on AWS
> No YARN. Classic clusters run on EC2 instances, and AWS account quotas limit their size. See [[EC2 Instance Types and Graviton]]. Amazon EMR, AWS's managed Hadoop service, uses YARN.

> [!gcp]- Databricks on Google Cloud
> No YARN. Classic clusters run on Compute Engine VMs, and project quotas limit their size. See [[Compute on Google Cloud]]. Managed Service for Apache Spark (formerly Dataproc) clusters use YARN.

## Advanced topics

> [!deepdive]- Advanced topics (301–401)
> - **ResourceManager high availability:** Before Hadoop 2.4, the ResourceManager was a single point of failure. RM high availability adds an Active/Standby ResourceManager pair.
> - **Memory-based sizing:** Containers are sized primarily by memory. Processes that exceed their container's memory limit are terminated by the NodeManager, a common failure for Spark executors with large off-heap usage.
> - **Preemption:** Schedulers can reclaim containers from queues using more than their share when another queue needs its guaranteed capacity. Applications must tolerate killed tasks.
> - **Locality versus wait time:** Schedulers can delay a task briefly to obtain a container on a node holding its data. On cloud object storage, data locality has little effect, so this tuning no longer applies.
> - **General-purpose successors:** Outside Databricks, [[Kubernetes]] is a common general-purpose scheduler for data workloads. Databricks serverless compute is a managed scheduling layer that is not exposed to users.

## Common misconceptions

> [!confusion] A YARN container is not a Docker container
> A YARN container is a resource allocation (memory and virtual cores) on one machine in which a process runs. YARN can launch Docker containers, but the term originally refers only to the allocation.

> [!confusion] YARN does not process data
> YARN allocates resources. MapReduce, Spark, or another framework performs the processing inside the allocated containers.

## Recall

What does YARN stand for?::Yet Another Resource Negotiator.
Which release made YARN generally available, and when?::Hadoop 2.2.0, October 15, 2013.
Which Hadoop 1 component's responsibilities did YARN separate?::The JobTracker, which both managed cluster resources and scheduled and monitored MapReduce tasks.
What are the two components of the ResourceManager?::The Scheduler and the ApplicationsManager.
What does the ApplicationMaster do?::Negotiates containers from the ResourceManager for one application and works with NodeManagers to run and monitor its tasks.
What is a YARN container?::An allocation of memory and virtual cores on one machine in which a task runs.
Name two YARN schedulers.::The CapacityScheduler and the FairScheduler.
In which Hadoop version did ResourceManager high availability arrive?::Hadoop 2.4.
What replaces YARN's resource management on Databricks?::The Databricks control plane provisioning cloud VMs per cluster, autoscaling, and serverless compute.

## Next steps

> [!path] Learning path
> **Needs first:** [[MapReduce]], [[Distributed Systems]]
> **Unlocks next:** [[Apache Spark]], [[Driver and Executors]], [[Compute Types]]

> [!nextup] Next
> [[Apache Hive]] covers the SQL layer that let analysts query Hadoop data without writing Java.

> [!sources]- Sources (last verified: 2026-10-25)
> - [Apache Hadoop YARN architecture (stable docs)](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html)
> - [Writing YARN applications (Apache Hadoop 3.5.0)](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/WritingYarnApplications.html)
> - [ResourceManager High Availability (Apache Hadoop)](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/ResourceManagerHA.html)
> - [Release 2.2.0 available (Apache Hadoop)](https://hadoop.apache.org/release/2.2.0.html)
> - [Hadoop 2.2.0 changelog (Apache Hadoop)](https://hadoop.apache.org/docs/r2.10.0/hadoop-project-dist/hadoop-common/release/2.2.0/CHANGES.2.2.0.html)
> - [Apache Hadoop on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop.html)
> - [Managed Service for Apache Spark on clusters overview (Google Cloud)](https://docs.cloud.google.com/dataproc/docs/concepts/overview)
> - [Migrate data applications to Databricks (AWS)](https://docs.databricks.com/aws/en/migration/)
