# AWS Solutions Architect Associate - Study Notes

*Formatted from course slides*

---

# Disclaimer: These slides are copyrighted and strictly for personal use only

# Table of Contents

## Table of Contents

## Table of Contents

# AWS Certified Solutions Architect Associate CourseSAA-C03

# Welcome! We’re starting in 5 minutes

# My SAA-C03 certification: 96.1%

# About me

# What’s AWS?

# What we’ll learn in this course (and more!)

## Elastic Load BalancingAWS Elastic BeanstalkAWSLambdaAmazonS3AmazonRDSAmazonDynamoDBAmazon ElastiCache

## Amazon CloudFrontAmazonRoute 53Amazon CloudWatchAWSCloudFormationAWSCloudTrailIAMAWS KMS

## Amazon KinesisAmazon API GatewayAWS Step FunctionsAuto Scaling

## AmazonSQSAmazonSNSAmazonSES

Amazon Aurora

---

# Navigating the AWS spaghetti bowl

# Udemy Tips

# Getting started with AWS

- AWS Cloud Number Facts
- In 2023, AWS had $90 billion in annual revenue
- AWS accounts for 31% of the market in Q1 2024 (Microsoft is 2nd with 25%)
- Pioneer and Leader of the AWS Cloud Market for the 13th consecutive year
- Over 1,000,000 active usersGartner Magic Quadrant
## AWS Cloud Use Cases

# AWS Global Infrastructure

## AWS Regions

# How to choose an AWS Region?

## AWS Availability Zones

# AWS Points of Presence (Edge Locations)

# To u r o f th e AW S Co n s o l e

# AWS Identity and Access Management (AWS IAM)

# IAM: Users & Groups

EdwardGroup: DevelopersGroup: OperationsGroup Audit Team
## IAM: Permissions

# IAM Policies inheritance

EdwardDevelopersOperationsAudit Team
inline
- IAM Policies Structure
- Consists of
- **Version**: policy language version, always include “2012-10-17”
- **Id**: an identifier for the policy (optional)
- **Statement**: one or more individual statements (required)
- Statements consists of
- **Sid**: an identifier for the statement (optional)
- **Effect**: whether the statement allows or denies access (Allow, Deny)
- **Principal**: account/user/role to which this policy applied to
- **Action**: list of actions this policy allows or denies
- **Resource**: list of resources to which the actions applied to
- **Condition**: conditions for when this policy is in effect (optional)
## IAM – Password Policy

## Multi Factor Authentication - MFA

### Alice+Password

=> Successful login

---

# MFA devices options in AWSVirtual MFA device

### Authy(phone only)Universal 2nd Factor (U2F) Security Key

### YubiKey by Yubico (3rd party)

Support for multiple tokens on a single device.Support for multiple root and IAM users using a single security key
## MFA devices options in AWS

### Provided by Gemalto (3rd party)

## Hardware Key Fob MFA Device forAWS GovCloud (US)

Provided by SurePassID (3rd party)

---

# How can users access AWS ?

# Example (Fake) Access Keys

# What’s the AWS CLI?

- What’s the AWS SDK?
- AWS Software Development Kit (AWS SDK)
- Language-specific APIs (set of libraries)
- Enables you to access and manage AWS services programmatically
- Embedded within your application
- Supports
- SDKs (JavaScript, Python, PHP , .NET, Ruby, Java, Go, Node.js, C++)
- Mobile SDKs (Android, iOS, …)
- IoT Device SDKs (Embedded C, Arduino, …)
- **Example**: AWS CLI is built on AWS SDK for PythonAWS SDKYour Application

---

# IAM Roles for Services

## IAM Role

Access AWS
## IAM Security T ools

# IAM Guidelines & Best Practices

## IAM Section – Summary

## Amazon EC2 – Basics

# Amazon EC2

# EC2 sizing & configuration options

## EC2 User Data

# Hands-On:Launching an EC2 Instance running Linux

## EC2 Instance Types - Overview

## EC2 Instance Types – General Purpose

## EC2 Instance Types – Compute Optimized

## EC2 Instance Types – Memory Optimized

## EC2 Instance Types – Storage Optimized

# Introduction to Security Groups

## Security GroupsDeeper Dive

## Security GroupsDiagram

## Security GroupsGood to know

# Referencing other security groupsDiagram

# Classic Ports to know

# SSH Summary TableMacLinuxWindows < 10Windows >= 10SSHPuttyEC2 Instance Connect

# Which Lectures to watch

# SSH troubleshooting

# How to SSH into your EC2 InstanceLinux / Mac OS X

## How to SSH into your EC2 InstanceWindows

## EC2 Instance Connect

## EC2 Instances Purchasing Options

## EC2 On Demand

## EC2 Reserved Instances

## EC2 Savings Plans

## EC2 Spot Instances

## EC2 Dedicated Hosts

## EC2 Dedicated Instances

## EC2 Capacity Reservations

# Which purchasing option is right for me?

# EC2 Spot Instance Requests

# EC2 Spot Instances Pricing

# How to terminate Spot Instances?

You can only cancel Spot Instance requests that areopen,active, ordisabled. Cancelling a Spot Request does not terminate instancesYou must first cancel a Spot Request, and then terminate the associated Spot Instances
## Spot Fleets

## Amazon EC2 – Associate

# Private vs Public IP (IPv4)

# Company BPrivate Network192.168.0.1/22Company APrivate Network192.168.0.1/22Private vs Public IP (IPv4)Example

## Private vs Public IP (IPv4)Fundamental Differences

# Elastic IPs

## Elastic IP

## Private vs Public IP (IPv4)In AWS EC2 – Hands On

# Placement Groups

# Same AZPlacement GroupsCluster

# Us-east-1aHardware 1Placement GroupsSpread

## Hardware 4EC2Us-east-1cHardware 5EC2

Hardware 6EC2

---

# Placements GroupsPartition

# Elastic Network Interfaces (ENI)

### Eth0 – primary ENI192.168.0.31

Eth1 – secondary ENI192.168.0.42
### Eth0 – primary ENI

Can be movedAvailability Zone

---

# EC2 Hibernate

- EC2 Hibernate
- **Introducing EC2 Hibernate**: 
- The in-memory (RAM) state is preserved
- The instance boot is much faster! (the OS is not stopped / restarted)
- **Under the hood**: the RAM state is written to a file in the root EBS volume
- The root EBS volume must be encrypted
- **Use cases**: 
- Long-running processing
- Saving the RAM state
- Services that take time to initializeRAM
EC2 InstanceRoot EBS Volume(Encrypted)
RunningStoppingStoppedRunningHibernateShutdownStartHibernation
## EC2 Hibernate – Good to know

## Amazon EC2 – Instance Storage

# What’s an EBS Volume?

## EBS Volume

## US-EAST-1BUS-EAST-1AEBS Volume - Example

## EBS(100 GB)

## EBS(50 GB)

## EBS(50 GB)

EBS(10 GB)unattached
## EBS – Delete on Termination attribute

## EBS Snapshots

## EBS(50 GB)

EBS Snapshotsnapshotrestore

---

# EBS Snapshots Features

## EBS SnapshotArchive

archive
EBS SnapshotRecycle Bindelete

---

# AMI Overview

# AMI Process (from an EC2 instance)

### Custom AMI

Create AMILaunch from AMI
## EC2 Instance Store

## Local EC2 Instance Store

# EBS Volume Types

# EBS Volume Types Use casesGeneral Purpose SSD

# EBS Volume Types Use casesProvisioned IOPS (PIOPS) SSD

## EBS Volume Types Use casesHard Disk Drives (HDD)

## EBS – Volume Types Summar y

## EBS Multi-Attach – io1/io2 family

## EBS Encryption

## Encryption: encrypt an unencrypted EBS volume

## Amazon EFS – Elastic File System

## EC2 Instancesus-east-1c

## EC2 InstancesSecurity Group

EFS FileSystem
## Amazon EFS – Elastic File System

## EFS – Performance & Storage Classes

## EFS – Storage Classes

## EFS Standard

## EFS IALifecycle Policy

no access for 60 daysmove
## EBS vs EFS – Elastic Block Storage

restoreAvailability Zone 1
EBS SnapshotAvailability Zone 2EBSEBS
## EBS vs EFS – Elastic File System

## EFSAvailability Zone 2

LinuxLinuxEFSMountTarget

---

# High Availability & Scalability

## Scalability & High Availability

## Ver tical Scalability

## Horizontal Scalability

# second building in San Franciscofirst building in New YorkHigh Availability

## High Availability & Scalability For EC2

# What is load balancing?

## EC2 Instance

## EC2 Instance

## EC2 Instance

- Load Balances are servers that forward traffic to multiple servers (e.g., EC2 instances) downstream

---

# Why use a load balancer?

# Why use an Elastic Load Balancer?

# Health Checks

Health ChecksProtocol: HTTPPort: 4567Endpoint: /health

---

# Types of load balancer on AWS

# Load Balancer Security GroupsUsersHTTPS / HTTPFrom anywhereHTTP Restricted to Load balancerLOAD BALANCER

Application Security Group: Allow traffic only from Load Balancer
## Classic Load Balancers (v1)

## Application Load Balancer (v2)

## Application Load Balancer (v2)

## Target Group for Users applicationApplication Load Balancer (v2)HTTP Based Traffic

### Target Group for Search applicationHTTPWWWRoute /search

Health CheckHealth Check
## Application Load Balancer (v2)Tar get Groups

## Target Group 1AWS – EC2 basedApplication Load Balancer (v2)Query Strings/Parameters Routing

## Application Load Balancer (v2)Good to Know

## Network Load Balancer (v2)

## Network Load Balancer (v2)TCP (Layer 4) Based Traffic

### Target Group for Search applicationHTTPWWWTCP + Rules

Health CheckHealth Check
## Network Load Balancer – Tar get Groups

i-1234567890abcdef0
i-1234567890abcdef0NetworkLoad Balancer
### Target Group (IP Addresses)

192.168.1.11810.0.4.21NetworkLoad Balancer
Target Group (Application Load Balancer)NetworkLoad Balancer
## Gateway Load Balancer

### GatewayLoad Balancer

### Application(destination)

### Target Group

3rd Party SecurityVirtual Appliancestraffictraffic
## Gateway Load Balancer – Tar get Groups

i-1234567890abcdef0
i-1234567890abcdef0GatewayLoad Balancer
### Target Group (IP Addresses)

192.168.1.11810.0.4.21GatewayLoad Balancer

---

# Sticky Sessions (Session Affinity)

## EC2 Instance

Client 1Client 2Client 3
## Sticky Sessions – Cookie Names

# Cross-Zone Load Balancing

### Availability Zone 2

10101010101010101010
### Availability Zone 1

### Availability Zone 2

25256.256.256.256.256.256.256.256.25
With Cross Zone Load Balancing:each load balancer instance distributes evenly across all registered instances in all AZWithout Cross Zone Load Balancing:Requests are distributed in the instances of the node of the Elastic Load Balancer50505050
## Cross-Zone Load Balancing

## SSL/TLS - Basics

## Load Balancer - SSL Certificates

## SSL – Server Name Indication (SNI)

## SSL Cert:Domain1.example.com

SSL Cert:www.mycorp.com
I would likewww.mycorp.comTarget group forwww.mycorp.comTarget group forDomain1.example.com
….Use the correctSSL cert
## Elastic Load Balancers – SSL Certificates

# Connection Draining

## EC2 Instance

EC2 Instance

---

# What’s an Auto Scaling Group?

## Auto Scaling Group in AWS

## EC2Instance

## EC2Instance

## EC2InstanceEC2InstanceEC2InstanceEC2InstanceAuto Scaling Group

Minimum CapacityDesired CapacityMaximum CapacityScale Out as Needed
## Auto Scaling Group in AWS With Load BalancerElastic Load Balancer

## ELB can check the health of your EC2 instances!

## EC2Instance

## EC2Instance

## EC2Instance

EC2InstanceEC2InstanceEC2InstanceEC2InstanceAuto Scaling Group
## Auto Scaling Group Attributes

## EBS VolumesSecurity Groups

SSH Key Pair

## IAM Role

## VPC + Subnets…

## Auto Scaling - CloudWatch Alarms & Scaling

## EC2Instance

## EC2InstanceEC2InstanceEC2InstanceAuto Scaling Group

CloudWatchAlarmtrigger Scaling
## Auto Scaling Groups – Scaling Policies

## Auto Scaling Groups – Scaling Policies

# Good metrics to scale on

### UsersApplicationLoad Balancer

RequestCountPerTargetTarget Value: 3
## Auto Scaling Groups - Scaling Cooldowns

# RDS, Aurora & ElastiCache

# Amazon RDS Overview

# Advantage over using RDS versus deploying DB on EC2

## RDS – Storage Auto Scaling

## RDS Read Replicas for read scalability

## RDS DB instance read replica

- Application writesreadsreadsreadsASYNC replicationASYNC replication
- Up to 15 Read Replicas
- Within AZ, Cross AZ or Cross Region
- Replication is ASYNC, so reads are eventually consistent
- Replicas can be promoted to their own DB
- Applications must update the connection string to leverage read replicas
## RDS Read Replicas – Use Cases

## RDS DB instance read replica

readsreadsASYNC replicationReporting Application
## RDS Read Replicas – Network Cost

- ASYNC ReplicationCross-Region$$$Region/AZus-east-1aRegion/AZeu-west-1b
- In AWS there’s a network cost when data goes from one AZ to another
- For RDS Read Replicas within the same region, you don’t pay that fee

## RDS DB instanceRDS DB instance read replica

ASYNC ReplicationSame Region FreeSame Region / Different AZus-east-1a us-east-1b
## RDS Multi AZ (Disaster Recovery)

- SYNCreplication
- SYNC replication
- One DNS name – automatic app failover to standby
- Increase availability
- Failover in case of loss of AZ, loss of network, instance or storage failure
- No manual intervention in apps
- Not used for scaling
- **Note**: The Read Replicas be setup as Multi AZ for Disaster Recovery (DR)RDS DB instance standby (AZ B)
One DNS name – automatic failover
## RDS – From Single-AZ to Multi-AZ

### Standby DB

snapshotrestoreDB snapshot
## RDS Custom

# Amazon Aurora

## Aurora High Availability and Read Scaling

# Auto ScalingAurora DB Cluster

WRRRRRReader EndpointConnection Load BalancingWriter EndpointPointing to the master
client

---

# Features of Aurora

## Replicas Auto ScalingAurora Replicas - Auto Scaling

Shared Storage VolumeWRRRR
CPUUsageCPUUsageMany RequestsEndpoint Extended
## Aurora – Custom Endpoints

### Writer EndpointReader Endpoint

### Shared Storage VolumeWRRRR

### ClientQueriesCustom Endpointdb.r3.largedb.r3.large

db.r5.2xlargeAnalytical Queries
## Aurora Serverless

- Automated database instantiation and auto-scaling based on actual usage
- Good for infrequent, intermittent or unpredictable workloads
- No capacity planning needed
- Pay per second, can be more cost-effective
us-east-1 - PRIMARY region
### ApplicationsRead / Write

eu-west-1 - SECONDARY region
ApplicationsRead OnlyreplicationGlobal Aurora
## Aurora Machine Learning

SQL query(Recommended products?)data(user’s profile, shopping history, …)predictions(red shirt, blue pants, …)query results(red shirt, blue …)

---

# Babelfish for Aurora PostgreSQL

### ApplicationSQL Server Client Driver

## T-SQLPostgreSQL

### ApplicationPostgreSQL DriverPL/pgSQL

migrateT-SQL

---

# RDS Backups

# Aurora Backups

# RDS & Aurora Restore options

## Aurora Database Cloning

## RDS & Aurora Security

## Amazon RDS Proxy

…Lambda functions

## RDS Proxy

RDS DBInstance

---

# Amazon ElastiCache Overview

## ElastiCache Solution Architecture - DB Cache

## ElastiCache Solution Architecture – User Session Store

## ElastiCache – Redis vs MemcachedREDIS

+Replicationsharding
## ElastiCache – Cache Security

### Redis Security groupSSL encryptionRedis AUTH

EC2 Security group
## Patterns for ElastiCache

Lazy Loading illustrated
## ElastiCache – Redis Use Case

## ElastiCache for RedisElastiCache for RedisElastiCache for Redis

3Real-time Leaderboard
## Amazon Route 53

# What is DNS?

# DNS Terminologieshttp://api.www.example.com.

### How DNS Works

Web BrowserLocal DNS ServerYou want to access example.comAssigned and Managed by your company or assigned by your ISP dynamicallyexample.com?Root DNS Serverexample.com?TLD DNS Server(.com)SLD DNS Server (example.com).com NS 1.2.3.4example.com?example.com NS 5.6.7.8example.com IP 9.10.11.12Managed by ICANN
Managed by Domain Registrar(e.g., Amazon Registrar, Inc.)Managed by IANA (Branch of ICANN)9.10.11.12Web Server (example.com) (IP: 9.10.11.12)
example.com?

---

# Amazon Route 53

## AmazonRoute 53

## EC2 InstanceAWS Cloud

Public IP54.22.33.44
## Route 53 – Records

## Route 53 – Record Types

## Route 53 – Hosted Zones

## Route 53 – Public vs. Private Hosted Zones

## EC2 Instance(Public IP)ApplicationLoad Balancer

### Public Hosted ZoneClient

## S3 BucketAmazonCloudFrontexample.com?54.22.33.44VPC

## EC2 Instance(webapp.example.internal)(Private IP)Private Hosted Zone

EC2 Instance(api.example.internal)(Private IP)DB Instance(db.example.internal)(Private IP)api.example.internal?10.0.0.10db.example.internal?10.0.0.35Public Hosted ZonePrivate Hosted Zone
## Route 53 – Records TTL (Time T o Live)

- AmazonRoute 53A 12.34.56.78(with TTL)HTTP RequestHTTP ResponseWill cache the result for The TTL of the record
- High TTL – e.g., 24 hr
- Less traffic on Route 53
- Possibly outdated records
- Low TTL – e.g., 60 sec.
- More traffic on Route 53 ($$)
- Records are outdated for less time
- Easy to change records
- Except for Alias records, TTL is mandatory for each DNS record

---

# CNAME vs Alias

## Route 53 – Alias Records

ApplicationLoad BalancerAlias Record (Enabled)Record NameTypeValueexample.comAMyALB-123456789.us-east-1.elb.amazonaws.comAWS-Managed(IP Addresses might change)
## Route 53 – Alias Records Targets

## Route 53 – Routing Policies

## Routing Policies – Simple

foo.example.comA 11.22.33.44A 55.66.77.88A 99.11.22.33Client

## AmazonRoute 53Multiple Value

chooses a random value
## Routing Policies – Weighted

## Routing Policies – Latency-based

ALB(ap-southeast-1)
## Route 53 – Health Checks

## EC2 InstanceHealth Check

Health Check
us-east-1
### ALBAuto Scaling group

EC2 Instanceeu-west-1
## eu-west-1Health Checker(us-east-1)Health Checks – Monitor an Endpoint

## EC2 Instance

### Health Checker(us-west-1)

### Health Checker(sa-east-1)

200 codeMust allow incomingrequests from Route 53Health Checkers IP address range
[https://ip-ranges.amazonaws.com/ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json)
## Amazon Route 53Route 53 – Calculated Health Checks

### Health Check(Child)

### Health Check(Child)

## EC2 Instance

## EC2 Instance

EC2 Instancemonitormonitormonitor
## Private subnetHealth Checks – Private Hosted Zones

### Health Checker(us-east-1)

monitormonitor
## Routing Policies – Failover (Active-Passive)EC2 Instance(Primary)Health Check(mandatory)Failover

## AmazonRoute 53EC2 Instance(Secondary – Disaster Recovery)

DNS Requests
## Routing Policies – Geolocation

A 55.66.77.88DefaultA 99.11.22.33
## Routing Policies – Geoproximity

## Routing Policies – Geoproximity

us-west-1
Bias: 0Bias: 0
## Routing Policies – Geoproximity

us-west-1
Bias: 0Bias: 50Higher bias in us-east-1
## Routing Policies – IP-based Routing

## Record NameValueIP-basedexample.com1.2.3.4location-1example.com5.6.7.8location-2RecordsEC2 Instance(1.2.3.4)

## EC2 Instance(5.6.7.8)

### User A(203.0.113.56)

User B(200.5.4.100)
## Routing Policies – Multi-Value

# Domain Registar vs. DNS Service

# GoDaddy as Registrar & Route 53 as DNS Service

## AmazonRoute 53

Public Hosted Zonestephanetheteacher.com
## 3rd Party Registrar with Amazon Route 53

## Route 53 – Hybrid DNS

## EC2 Instance(ec2-192-0-2-44.compute-1.amazonaws.com)

Private Hosted ZoneRoute 53ResolverPublic Name Server
## Route 53 – Resolver Endpoints

### DNS Resolvers(onpremise.private)

### Server(web.onpremise.private)ResolverInbound Endpoint

## Route 53Resolver

## Private Hosted Zone(aws.private)EC2 Instance(app.aws.private)DNS Queryapp.aws.private?DNS Queryapp.aws.private?

VPN or DX connectionlookup
## Route 53 – Resolver Endpoints

### DNS Resolvers(onpremise.private)

### Server(web.onpremise.private)ResolverOutbound Endpoint

## Route 53Resolver

## Private Hosted Zone(aws.private)EC2 Instance(app.aws.private)DNS Queryweb.onpremise.private?

VPN or DX connectionDNS Queryweb.onpremise.private?

---

# Classic Solutions Architecture

# Section Introduction

# Stateless Web App: WhatIsTheTime.com

## Stateless web app: What time is it?Starting simple

## Elastic IP Address

UserWhat time is it?5:30 pm!
## Stateless web app: What time is it?Scaling vertically

## Public EC2

## Elastic IP Address

UserWhat time is it?5:30 pm!
What time is it?6:30 pm!
What time is it?7:30 pm!
Downtime while upgrading to M5
## Stateless web app: What time is it?Scaling horizontally

## Stateless web app: What time is it?Scaling horizontallyWhat time is it?5:30 pm!What time is it?6:30 pm!What time is it?7:30 pm!

# Public EC2 instance,No Elastic IPDNS QueryFor api.whatisthetime.comA RecordTTL 1 hourINSTANCE IS GONE!

# Stateless web app: What time is it?Scaling horizontally, with a load balancerWhat time is it?

### DNS QueryFor api.whatisthetime.comAlias Record

### Availability zone 1Availability zone 1

ELB +Health ChecksRestrictedSecurity groups rules
## Stateless web app: What time is it?Scaling horizontally, with an auto-scaling groupWhat time is it?

### DNS QueryFor api.whatisthetime.comAlias Record

### Availability zone 1Availability zone 1

ELB +Health ChecksAuto Scaling group
## Stateless web app: What time is it?Making our app multi-AZWhat time is it?

### Availability zone 1 to 3Availability zone 1

### ELB +Health Checks+ Multi AZAuto Scaling group

### Availability zone 2

Availability zone 3

---

# Minimum 2 AZ => Let’s reserve capacity

### Availability zone 1 to 3Availability zone 1

### ELB +Health Checks+ Multi AZAuto Scaling group

### Availability zone 2

Minimum capacity= reserved instances = cost savings

---

# In this lecture we’ve discussed…

# Stateful Web App: MyClothes.com

## Stateful Web App: MyClothes.com

### Auto Scaling group

Availability zone 2Availability zone 3
## Stateful Web App: MyClothes.comIntroduce Stickiness (Session Affinity)

### Auto Scaling group

### Availability zone 2Availability zone 3

ELB Stickiness
## Stateful Web App: MyClothes.comIntroduce User Cookies

### Auto Scaling group

### Availability zone 2Availability zone 3

Send shopping cart content in Web CookiesStatelessHTTP requests are heavierSecurity risk (cookies can be altered)Cookies must be validatedCookies must be less than 4KB
## Stateful Web App: MyClothes.comIntroduce Server Session

### Auto Scaling group

### Availability zone 2Availability zone 3

### Send session_id inWeb Cookies

## ElastiCacheStore / retrieve session data

Amazon DynamoDB(alternative)
## Stateful Web App: MyClothes.comStoring User Data in a database

### Auto Scaling group

### Availability zone 2Availability zone 3

## Amazon RDS

Store / retrieve user data(address, name, etc)
## Stateful Web App: MyClothes.comScaling Reads

### Auto Scaling group

### Availability zone 2Availability zone 3

RDSRead ReplicasRDSMaster(writes)replication
## Stateful Web App: MyClothes.comScaling Reads (Alternative) – Lazy Loading

### Auto Scaling group

### Availability zone 2Availability zone 3

RDSRead/writecacheRead from cachehit
## Stateful Web App: MyClothes.comMulti AZ – Survive disasters

### Auto Scaling group

### Availability zone 2Availability zone 3

## ElastiCacheMulti AZ

RDSMulti AZ
## Stateful Web App: MyClothes.comSecurity Groups

### Auto Scaling group

### Availability zone 2Availability zone 3

RDSRestrict traffic to EC2Security group from the LBRestrict traffic to RDSSecurity group from theEC2 security groupRestrict traffic to ElastiCacheSecurity group from theEC2 security groupOpen HTTP / HTTPS to 0.0.0.0/0

---

# In this lecture we’ve discussed…3-tier architectures for web applications

# Stateful Web App: MyWordPress.com

## Stateful Web App: MyWordPress.comRDS layer

### Auto Scaling group

### Availability zone 2Availability zone 3

RDSMulti AZ
## Stateful Web App: MyWordPress.comScaling with Aurora: Multi AZ & Read Replicas

### Auto Scaling group

### Availability zone 2Availability zone 3

Aurora MySQLMulti AZRead Replicas
## Stateful Web App: MyWordPress.comStoring images with EBS

## Amazon EBS Volume

Availability zone 1Send image
## Stateful Web App: MyWordPress.comStoring images with EBS

## Amazon EBS Volume

## Amazon EBS Volume

### Availability zone 1

Availability zone 2Send image
## Stateful Web App: MyWordPress.comStoring images with EFS

### Availability zone 1

Availability zone 2
ENISend image

---

# In this lecture we’ve discussed…

# Instantiating Applications quickly

## Instantiating Applications quickly

# Typical architecture: Web App 3-tier

### Auto Scaling group

### Availability zone 2Availability zone 3

## ElastiCacheStore / retrieve session data+ Cached data

## PUBLIC SUBNETPRIVATE SUBNETDATA SUBNET

Amazon RDSRead / write dataELBRoute 53

---

# Developer problems on AWS

## Elastic Beanstalk – Overview

## Elastic Beanstalk – Components

## Elastic Beanstalk – Supported Platforms

# Web Ser ver Tier vs. Worker Tier

### Web Environment(myapp.us-east-1.elasticbeanstalk.com)

### Security Group

### Availability Zone 1

### Availability Zone 2

## EC2 Instance(Web Server)ELB

### Security Group

## EC2 Instance(Web Server)Auto Scaling group

Worker EnvironmentAvailability Zone 1Availability Zone 2

## SQS Queue

## SQS messageSQS messagepullmessages

## EC2 Instance(Worker)

- EC2 Instance(Worker)
- Scale based on the number of SQS messages
- Can push messages to SQS queue from another Web Server Tier

---

# RDS Master

## RDS StandbyEC2 Instance

## EC2 Instance

### ALBAvailability Zone 1

## RDS MasterEC2 Instance

Elastic IP

---

# Amazon S3

# Section introduction

# Amazon S3 Use cases

## Amazon S3 - Buckets

## Amazon S3 - Objects

## Amazon S3 – Objects (cont.)

## Amazon S3 – Security

## S3 Bucket Policies

## Example: Public Access - Use Bucket Policy

### Anonymous www website visitor

S3 Bucket PolicyAllows Public Access
## Example: User Access to S3 – IAM permissions

IAM Policy IAM User
## Example: EC2 instance access - Use IAM Roles

## EC2 Instance Role

IAM permissionsEC2 Instance
## Advanced: Cross-Account Access – Use Bucket Policy

S3 Bucket PolicyAllows Cross-Account

---

# Bucket settings for Block Public Access

## Amazon S3 – Static Website Hosting

User[http://demo-bucket.s3-website-us-west-2.amazonaws.comhttp://demo-bucket.s3-website.us-west-2.amazonaws.com](http://demo-bucket.s3-website-us-west-2.amazonaws.comhttp://demo-bucket.s3-website.us-west-2.amazonaws.com)
## Amazon S3 - Versioning

s3://my-bucket/my-file.docx
uploadVersion 1Version 2Version 3
## Amazon S3 – Replication (CRR & SRR)

S3 Bucket(us-east-2)asynchronousreplication
## Amazon S3 – Replication (Notes)

# S3 Storage Classes

# S3 Durability and Availability

## S3 Standard – General Purpose

## S3 Storage Classes – Infrequent Access

# Amazon S3 Glacier Storage Classes

## S3 Intelligent-Tiering

## S3 Storage Classes Comparison

## S3 Storage Classes – Price ComparisonExample: us-east-1

## S3 Express One Zone

Availability Zone (AZ 4)
## Amazon S3 – Advanced

## Amazon S3 – Moving between Storage Classes

## Intelligent TieringOne-Zone IA

### Glacier Instant RetrievalGlacier Flexible Retrieval

Glacier Deep Archive
## Amazon S3 – Lifecycle Rules

## Amazon S3 – Lifecycle Rules (Scenario 1)

## Amazon S3 – Lifecycle Rules (Scenario 2)

## Amazon S3 Analytics – Storage Class Analysis

## S3 – Requester Pays

### Owner$$ Networking Cost

downloadRequester
Owner$$ Storage CostRequester$$ Networking Cost
download
Requester Pays BucketStandard Bucket
## S3 Event Notifications

## Lambda Function

- SNS
- **S3**: ObjectCreated, S3:ObjectRemoved, S3:ObjectRestore, S3:Replication…
- Object name filtering possible (*.jpg)
- **Use case**: generate thumbnails of images uploaded to S3
- Can create as many “S3 events” as desired
- S3 event notifications typically deliver events in seconds but can sometimes take a minute or longer
## S3 Event Notifications – IAM Permissions

## Lambda Function

## Lambda Resource Policy

## SNS Resource (Access) Policy

SQS Resource (Access) Policy

---

# S3 Event Notifications with Amazon EventBridge

- AmazonEventBridgerulesOver 18 AWS servicesas destinations
- Advanced filtering options with JSON rules (metadata, object size, name...)
- Multiple Destinations – ex Step Functions, Kinesis Streams / Firehose…
- EventBridge Capabilities – Archive, Replay Events, Reliable delivery
## S3 – Baseline Performance

## S3 Performance

### DivideIn partsBIG file

## S3 BucketAustralia

### Edge LocationUSA

Fast (public www)Fast (private AWS)File in USA
## S3 Performance – S3 Byte-Range Fetches

## S3 Batch Operations

filterS3 Batch Operations
operation+parametersUser
Processed Objects
## S3 – Storage Lens

## Storage Lens – Default Dashboard

## Storage Lens – Metrics

## Storage Lens – Metrics

## Storage Lens – Metrics

## Storage Lens – Free vs. Paid

## Amazon S3 – Security

## Amazon S3 – Object Encryption

## Amazon S3 Encryption – SSE-S3

uploadHTTP(S) + Header

## S3 Bucket

+ObjectS3 Owned KeyEncryption
## Amazon S3 Encryption – SSE-KMS

uploadHTTP(S) + Header

## S3 Bucket

+ObjectKMS Key
AWS KMSEncryption

---

# SSE-KMS Limitation

UsersUpload / downloadSSE-KMSAPI call
## Amazon S3 Encryption – SSE-C

uploadHTTPS ONLY+ Key in Header

## S3 Bucket

+Object

## Client-Provided Key

+Encryption
## Amazon S3 Encryption – Client-Side Encryption

- S3 Bucket
- Use client libraries such as Amazon S3 Client-Side Encryption Library
- Clients must encrypt data themselves before sending to Amazon S3
- Clients must decrypt data themselves when retrieving from Amazon S3
- Customer fully manages the keys and encryption cycle+File
### Client Key

File(encrypted)uploadHTTP(S)Encryption
## Amazon S3 – Encryption in transit (SSL/TLS)

## Amazon S3 – Force Encryption in Transitaws:SecureTransport

## S3 Bucket(my-bucket)

Bucket Policy
httphttps
## Amazon S3 – Default Encryption vs. Bucket Policies

# What is CORS?

## What is CORS?

## Web Server(Cross-Origin)https://www.other.com

Web BrowserHTTPS RequestOPTIONS /Host: www.other.comOrigin: [https://www.example.comPreflight](https://www.example.comPreflight) RequestAccess-Control-Allow-Origin: [https://www.example.comAccess-Control-Allow-Methods](https://www.example.comAccess-Control-Allow-Methods) GET, PUT, DELETEPreflight ResponseGET /Host: www.other.comOrigin: [https://www.example.comCORS](https://www.example.comCORS) Headers received already by the OriginThe Web Browser can make requests
## Amazon S3 – CORS

## S3 Bucket(my-bucket-html)(Static Website Enabled)

S3 Bucket(my-bucket-assets)(Static Website Enabled)GET /index.htmlHost: [http://my-bucket-html.s3-website.us-west-2.amazonaws.com](http://my-bucket-html.s3-website.us-west-2.amazonaws.com)
index.htmlGET /images/coffee.jpgHost: [http://my-bucket-assets.s3-website.us-west-2.amazonaws.comOrigin](http://my-bucket-assets.s3-website.us-west-2.amazonaws.comOrigin) [http://my-bucket-html.s3-website.us-west-2.amazonaws.comAccess-Control-Allow-Origin](http://my-bucket-html.s3-website.us-west-2.amazonaws.comAccess-Control-Allow-Origin) [http://my-bucket-html.s3-website.us-west-2.amazonaws.com](http://my-bucket-html.s3-website.us-west-2.amazonaws.com)
## Amazon S3 – MFA Delete

MFA Hardware Device

---

# S3 Access Logs

Log all requests

---

# S3 Access Logs: Warning

PutObjectDo not try this at home J
## Amazon S3 – Pre-Signed URLs

Usergeneratepre-signed URL
## S3 Glacier Vault Lock

# S3 Object Lock (versioning must be enabled)

## S3 – Access Points

/finance/…
/sales/…
### Simple BucketPolicy

### FinanceAccess Point

### SalesAccess Point

### AnalyticsAccess Point

### PolicyGrant R/W to/finance prefix

### PolicyGrant R/W to/sales prefix

### PolicyGrant R toentire bucket

- Users(Finance)Users(Sales)Users(Analytics)
- Access Points simplify security management for S3 Buckets
- **Each Access Point has**: 
- its own DNS name (Internet Origin or VPC Origin)
- an access point policy (similar to bucket policy) – manage security at scale
## S3 – Access Points – VPC Origin

## EC2 InstanceAccess PointVPC Origin

## VPC Endpoint

Endpoint PolicyAccess Point PolicyBucketPolicy
## S3 Object Lambda

### AnalyticsApplication

### MarketingApplication

## S3 BucketSupportingS3 Access Point

Customer LoyaltyDatabaseRedactingLambda FunctionEnrichingLambda FunctionS3 Object LambdaAccess PointS3 Object LambdaAccess PointOriginalObjectRedactedObjectEnrichedObject

---

# CloudFront & Global Accelerator

## Amazon CloudFront

## CloudFront – Origins

## CloudFront at a high level

### Local Cache

## S3HTTPorOrigin

ClientGET /beach.jpg?size=300x300 HTTP/1.1User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)Host: www.example.comAccept-Encoding: gzip, deflate
## CloudFront – S3 as an Origin

## Origin (S3 bucket)

### Public www

## Public wwwEdgeSão PauloOrigin Access Control+ S3 bucket policy

OACPrivate AWSPrivate AWSPrivate AWSPrivate AWSAWS Cloud
## CloudFront vs S3 Cross Region Replication

## CloudFront – ALB or EC2 as an originUsing VPC Origins

Edge LocationPrivate Subnet
Application Load BalancerNetwork Load BalancerEC2 Instance
## CloudFront – ALB or EC2 as an originUsing Public Networkhttp://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips

### Application Load BalancerMust be Public

EC2 InstancesCan be PrivateAllow Security Group of Load BalancerAllow Public IP of Edge LocationsSecurity groupSecurity group

## Edge LocationEC2 InstancesMust be Public

Allow Public IP of Edge LocationsSecurity group
## CloudFront Geo Restriction

## CloudFront - Pricing

## CloudFront – Price Classes

## CloudFront - Price Class

## CloudFront – Cache Invalidations

index.html/images/Cache
### Edge Location

### Invalidate- /index.html- /images/*invalidate

## S3 Bucket(origin)

index.html/images/Cache
### GET /index.html

update files
## Global users for our application

Public ALB
hops

---

# Unicast IP vs Anycast IP

12.34.56.7812.34.56.78Client

---

# AWS Global Accelerator

### IndiaPublic ALB

Edge locationPrivate AWS

---

# AWS Global Accelerator

# AWS Global Accelerator vs CloudFront

## AWS Storage Extras

## AWS Snowball

# Diagrams

# What is Edge Computing?

# Solution Architecture: Snowball into Glacier

## Amazon S3

Amazon GlacierS3 lifecycle policyimport
## Amazon FSx – Overview

# Amazon FSx for Windows (File Server)

## Amazon FSx for Lustre

## FSx Lustre - File System Deployment Options

Compute instancesCompute instancesS3 bucket(optional data repository)FSx For Lustre(Scratch file system)RegionAvailability Zone 1
### Availability Zone 2

Compute instancesCompute instancesS3 bucket(optional data repository)FSx For Lustre(Persistent file system)
## Amazon FSx for NetApp ONTAP

## VMware Cloudon AWS

## AmazonAppStream 2.0AmazonWorkSpaces

On-premisesServerNFS, SMB, iSCSI
## Amazon FSx for OpenZFS

## VMware Cloudon AWS

## AmazonAppStream 2.0AmazonWorkSpaces

On-premisesServerNFS (v3, v4, v4.1, v4.2)
## Hybrid Cloud for Storage

# AWS Storage Cloud Native OptionsBlock

## AWS Storage Gateway

# Amazon S3 File Gateway

## HTTPSApplicationServerS3 FileGatewayS3 StandardS3 Standard-IAS3 One Zone-IAS3 Intelligent-TieringS3 GlacierNFS or SMB

Lifecycle policy
## Volume Gateway

## S3 Bucket

## Amazon EBSSnapshots

### ApplicationServeriSCSI

Volume GatewayHTTPS
## Tape Gateway

## Virtual Tapesstored inAmazon S3

## Archived Tapesstored inAmazon Glacier

### BackupServeriSCSIHTTPS

TapeGatewayMedia ChangerTape Drive
## AWS Storage Gateway

File Gatewaylocal cacheVolume Gatewaylocal cacheTape Gatewaylocal cache
### Application ServerBackup Application

## User/group file sharesAWS Cloud

## NFS/SMBiSCSIiSCSI VTLGateway Deployment OptionsVM(VMware, Hyper-V, KVM)

Amazon S3excluding Glacier &Glacier Deep Archive Amazon S3Amazon S3Tape LibraryAny S3 Storage ClassIncluding GlacierAWS EBSTape ArchiveGlacier &Glacier Deep ArchiveEject from backup applicationStorage GatewayEncryption in TransitInternet or Direct Connect

---

# AWS Transfer Family

# AWS Transfer Family

## AWS Transfer for SFTPAWS Transfer for FTPSAWS Transfer for FTP(only within VPC)Amazon S3

## Amazon EFS

authenticateMS Active DirectoryLDAP …Route 53(optional)Users(FTP client)
IAM Role
## AWS DataSync

# AWS DataSyncNFS / SMB to AWS (S3, EFS, FSx…)

### NFS or SMB

## RegionAWSDataSyncAWS Storage Resources

## S3 Standard

## S3 Intelligent-TieringS3 Standard-IAS3 OneZone-IAS3 GlacierS3 GlacierDeep ArchiveAWS EFS

## Amazon FSxTLS

AWS Snowcone(agent pre-installed)

---

# AWS DataSyncTransfer between AWS storage ser vices

## Amazon FSxAmazon EFS

## Amazon S3

## Amazon FSxAmazon EFS

Amazon S3

---

# Storage Comparison

# AWS Integration & MessagingSQS, SNS & Kinesis

# Section Introduction

## Section Introduction

# Amazon SQSWhat’s a queue?ProducerProducerProducerSQS QueueConsumerConsumerConsumerConsumerSend messagesPoll messages

## Amazon SQS – Standard Queue

## SQS – Producing Messages

## SQS – Consuming Messages

## SQS – Multiple EC2 Instances ConsumersSQS Queue

# SQS with Auto Scaling Group (ASG)SQS Queue

## EC2 InstancesPoll for messages

CloudWatch AlarmscaleAlarm for breach
## SQS to decouple between application tiers

## Auto-Scaling

### Back-end processingapplication

### Front-end web apprequestsSendMessage

Auto-ScalingReceiveMessages
## Amazon SQS - Security

## SQS – Message Visibility Timeout

Message returned (again)
## SQS – Message Visibility Timeout

Visibility timeoutMessage returnedReceiveMessageRequestNot returnedReceiveMessageRequestNot returnedReceiveMessageRequest
- Message returned (again)
- If a message is not processed within the visibility timeout, it will be processed twice
- A consumer could call the ChangeMessageVisibility API to get more time
- If visibility timeout is high (hours), and consumer crashes, re-processing will take time
- If visibility timeout is too low (seconds), we may get duplicates
## Amazon SQS - Long Polling

message
## Amazon SQS – FIFO Queue

# SQS with Auto Scaling Group (ASG)SQS Queue

## EC2 InstancesPoll for messages

CloudWatch AlarmscaleAlarm for breach

---

# If the load is too big, some transactions may be lost

## Auto-ScalingInsert transactions

Amazon RDSAmazon AuroraAmazon DynamoDB

---

# SQS as a buffer to database writes

## Auto-Scaling

### Dequeue message

### Enqueue messagerequestsSendMessage

## Auto-ScalingReceiveMessages

insert

---

# SQS to decouple between application tiers

## Auto-Scaling

### Back-end processingapplication

### Front-end web apprequestsSendMessage

Auto-ScalingReceiveMessages

---

# Amazon SNS

## Amazon SNS

## SNSSubscriberspublish

## SQSLambdaKinesis DataFirehoseHTTP(S)EndpointsSMS &Mobile Notifications

# SNS integrates with a lot of AWS services

## CloudWatch AlarmsS3 Bucket(Events)Auto Scaling Group(Notifications)CloudFormation(State Changes)

## AWS Budgets

## AWS DMS(New Replic)

RDS Eventspublish………
## Amazon SNS – How to publish

## Amazon SNS – Security

## SNS + SQS: Fan Out

# Application: S3 Events to multiple queues

## Amazon S3eventsS3 Object created…

Lambda FunctionFan-out
## Application: SNS to Amazon S3 through Kinesis Data Firehose

## Kinesis DataFirehose

- Amazon S3
- **SNS can send to Kinesis and therefore we can have the following solutions architecture**: Any supported KDFDestination
## Amazon SNS – FIFO T opic

# SNS FIFO + SQS FIFO: Fan Out

## SNS – Message Filtering

New transactionOrder: 1036Product: PencilQty: 4State: PlacedSQS Queue(Placed orders)Email Subscription(Cancelled orders)SQS Queue(Declined orders)

## State: PlacedFilter Policy

## State: DeclinedFilter PolicyState: CancelledFilter Policy

## SQS Queue(All)

SQS Queue(Cancelled orders)

---

# Amazon Kinesis Data Streams

### Metrics & Logs

## Amazon KinesisData StreamsReal-time dataConsumers

## ProducersApplicationsKinesis Agent

## AmazonData Firehose

Managed Service for Apache Flink
## Kinesis Data Streams

## Kinesis Data Streams – Capacity Modes

## Amazon Data Firehose

## Amazon S3Amazon RedshiftAmazon OpenSearchHTTP Endpoint

## ProducersApplicationsClientKinesis Agent

## KinesisData StreamsAmazon CloudWatch(Logs & Events)AWS IoTAmazonData Firehose

## Data transformationLambdafunctionUp to 1 MBRecordBatch writes

## S3 backup bucketAll or Failed dataCustom Destinations

3rd-party Partner Destinations
## Amazon Data Firehose

## Kinesis Data Streams vs Amazon Data Firehose

# SQS vs SNS vs KinesisSQS:

# Amazon MQ

## Amazon MQ – High Availability

### Availability Zone(us-east-1b)ACTIVESTANDBY

## Amazon EFS(storage)

## Amazon MQ BrokerAmazon MQ Broker

# Containers on AWS

# What is Docker?

# Docker on an OSServer (e.g., EC2 instance)

## Where are Docker images stored?

## Docker vs. Virtual Machines

## Getting Started with Docker

imageBuildRuncontainer
### Docker Repository

## Docker Containers Management on AWS

## AWS Fargate

## Amazon EKS

Amazon ECR
## Amazon ECS - EC2 Launch Type

## EC2 Instance

## EC2 Instance

## ECS Agent

## ECS Agent

ECS Agent
## Amazon ECS – Fargate Launch Type

## Amazon ECS – IAM Roles for ECS

### Task ATask B

## ECSECRCloudWatchLogs

## EC2 Instance Profile

S3DynamoDBECS Task A RoleECS Task B Role
## Amazon ECS – Load Balancer Integrations

### ApplicationLoad Balancer

UsersECS TaskECS TaskECS TaskECS Task80/443
## Amazon ECS – Data Volumes (EFS)

Amazon EFSFile Systemmountmount

---

# ECS Service Auto Scaling

## EC2 Launch Type – Auto Scaling EC2 Instances

## ECS Scaling – Service CPU Usage Example

### Auto Scaling Group

## Scale ECS Capacity Providers(optional)Auto Scaling

### Task 1Task 2CPU Usage

## CloudWatch Metric(ECS Service CPU Usage)

## CloudWatch AlarmTriggerScale

Task 3(new)

---

# ECS tasks invoked by Event Bridge

### Upload object

## AmazonEventBridgeVPCRegion

## Amazon ECS Cluster

## AWS FargateTask (new)S3 BucketEventRule: Run ECS Task

## AmazonDynamoDBSave result

ECS Task Role(Access S3 & DynamoDB)Get object

---

# ECS tasks invoked by Event Bridge Schedule

## AWS FargateTask (new)Rule: Run ECS TaskAmazon S3Batch Processing

### Every 1 hour

ECS Task RoleAccess S3
## ECS – SQS Queue Example

## ECS Service Auto Scaling

Task 1Task 2
### Task 3

SQS QueueMessagesPoll for messages
## ECS – Intercept Stopped Tasks using EventBridge

## ECS Task

exited
event
### Event Pattern

SNStriggerAdministratoremail

---

# Amazon ECR

### ECR Repository

### DockerImage ADockerImage B

IAM Rolepullpull
## Amazon EKS Overview

## Private subnet 3Private subnet 1Private subnet 2Amazon EKS - Diagram

Availability Zone 1Availability Zone 2Availability Zone 3Public subnet 1
### Public subnet 2

Public subnet 3

## EKSPublicService LBELB

## Auto Scaling GroupEKS node

## EKS PodsEKS node

## EKS PodsEKS node

EKS PodsEKS Worker NodesEKSPrivateService LB
## Amazon EKS – Node Types

## Amazon EKS – Data Volumes

# AWS App Runner

# AWS App2Container (A2C)

# AWS App2Container (A2C)

## CloudFormationTemplate

## Amazon ECR(store image)

Amazon ECS(deploy)Amazon EKS(deploy)App Runner(deploy)

---

# Serverless Overview

# What’s serverless?

# Serverless in AWS

## Why AWS Lambda

# Benefits of AWS Lambda

# AWS Lambda language support

# AWS Lambda IntegrationsMain ones

## S3KinesisAPI GatewayDynamoDB

CloudFrontCloudWatch EventsEventBridge

---

# Example: Serverless Thumbnail creation

Metadata in DynamoDBpushImage nameImage sizeCreation dateetc…
## Example: Serverless CRON Job

# AWS Lambda Pricing: example

## AWS Lambda Limits to Know - per region

## Lambda Concurrency and Throttling

## Lambda Concurrency Issue

1000 concurrent executions
### THROTTLE!

THROTTLE!Many usersFew users

---

# Concurrency and Asynchronous Invocations

### New file event

### New file event

- New file event
- If the function doesn't have enough concurrency available to process all events, additional requests are throttled.
- For throttling errors (429) and system errors (500-series), Lambda returns the event to the queue and attempts to run the function again for up to 6 hours.
- The retry interval increases exponentially from 1 second after the first attempt to a maximum of 5 minutes.
## Cold Starts & Provisioned Concurrency

## Reserved and Provisioned Concurrency

# Lambda SnapStart

### SnapStartenabledinvoke

InvokeShutdownfunction ispre-initializedLambdaLambda

---

# Customization At The Edge

# CloudFront Functions & Lambda@Edge Use Cases

## CloudFront Functions

### ClientViewerRequest ViewerResponse

OriginRequest OriginResponse
## Lambda@Edge

### ClientViewerRequest ViewerResponse

OriginRequest OriginResponse
## CloudFront Functions vs. Lambda@Edge - Use CasesCloudFront Functions

# Lambda by default

## AWS Cloud

## Private RDS

## Not workingDefault Lambda Deployment

- Public www works
- By default, your Lambda function is launched outside your own VPC (in an AWS-owned VPC)
- Therefore, it cannot access resources in your VPC (RDS, ElastiCache, internal ELB…)

---

# Private subnetLambda in VPC

## Amazon RDS In VPC

## Lambda Security group

## RDS Security group

Elastic Network Interface (ENI)

---

# Lambda with RDS Proxy

…Lambda functions

## RDS Proxy

RDS DBInstance

---

# Invoking Lambda from RDS & Aurora

## Amazon SESLambdafunction

### Userregister(INSERT)invokesend Email

## RDS Event Notifications

SQSQueue…

---

# Amazon DynamoDB

## DynamoDB - Basics

## DynamoDB – Table example

## DynamoDB – Read/Write Capacity Modes

## DynamoDB Accelerator (DAX)

## Amazon DynamoDB

…DAX Cluster
…Nodes
## DynamoDB Accelerator (DAX) vs. ElastiCache

- Individual objects cache- Query & Scan cacheStore Aggregation ResultApplication
## DynamoDB – Stream Processing

## DynamoDB Streams

## TableDynamoDBStreams

## Kinesis DataStreams

### Processing Layer

## DynamoDBKCL AdapterLambda

## Amazon SNSmessaging, notifications

### DDB Tablefiltering, transforming, …

## Kinesis DataFirehose

## AmazonRedshiftanalytics

## Amazon S3archiving

AmazonOpenSearchindexingcreate/update/delete
## DynamoDB Global Tables

## DynamoDB – Time T o Live (TTL)

Friday, September 10, 2021, 11:56:11 AM(Epoch timestamp: 1631274971)Current Timescan &expire items
Deletion Processscan &delete items
## DynamoDB – Backups for disaster recovery

## DynamoDB – Integration with Amazon S3

S3(.csv, .json, .ion)DynamoDBimportexportquery

---

# Example: Building a Serverless API

API GatewayClientLambda DynamoDB
## AWS API Gateway

## API Gateway – Integrations High Level

## API Gateway – AWS Service IntegrationKinesis Data Streams example

## API Gateway - Endpoint Types

## API Gateway – Security

# AWS Step Functions

# Amazon Cognito

## Cognito User Pools (CUP) – User Features

## Cognito User Pools (CUP) - Integrations

## Cognito User Pools

## Cognito User Pools

### Application Load Balancer+ Listeners & RulesAuthenticate

### Target GroupBackend

API Gatewaybackend
## Cognito Identity Pools (Federated Identities)

## Cognito Identity Pools – Diagram

### Web & Mobile Applications

### Social Identity Provider

## Login and Get TokenExchange token for temporaryAWS credentialsvalidate

## Private S3 Bucket DynamoDB TableDirect access to AWS

CognitoUser Pools
## Cognito Identity PoolsRow Level Security in DynamoDB

# Serverless Architectures

# Mobile application: MyT odoList

## Mobile app: REST API layer

## Amazon Cognito

## AWS LambdaAmazon DynamoDB

Mobile clientREST HTTPSinvokequeryauthenticateVerify authentication
## Mobile app: giving users access to S3

## Amazon Cognito

## AWS LambdaAmazon DynamoDB

## Amazon S3

### Mobile clientStore/retrieve filesPermissions

authenticate
## Mobile app: high read throughput, static data

## Amazon Cognito

## AWS LambdaDynamoDB

## Amazon S3

### Mobile clientStore/retrieve filesPermissions

### REST HTTPSinvokeQuery / readauthenticateVerify authentication

DAXCaching layer
## Mobile app: caching at the API Gateway

## Amazon Cognito

## AWS LambdaDynamoDB

## Amazon S3

### Mobile clientStore/retrieve filesPermissions

### REST HTTPSinvokeQuery / readauthenticateVerify authentication

DAXCaching layerCACHING OF RESPONSES

---

# In this lecture

# Serverless hosted website: MyBlog.com

# Serving static content, globallyAmazon CloudFrontGlobal distribution

Interaction with edge locations
## Serving static content, globally, securelyAmazon CloudFrontGlobal distribution

## Interaction with edge locationsOAC: Origin Access Control

Bucket policyOnly authorize fromCloudFront Distribution

---

# Adding a public serverless REST APIAmazon CloudFrontGlobal distribution

## Interaction with edge locationsOAC: Origin Access Control

## Bucket policyOnly authorize fromCloudFront Distribution

## Amazon API Gateway

## AWS LambdaDynamoDB

### REST HTTPSinvokeQuery / read

DAXCaching layer
## Leveraging DynamoDB Global TablesAmazon CloudFrontGlobal distribution

## Interaction with edge locationsOAC: Origin Access Control

## Bucket policyOnly authorize fromCloudFront Distribution

## Amazon API Gateway

## AWS LambdaDynamoDBGlobal Tables

### REST HTTPSinvokeQuery / read

DAXCaching layer
## User Welcome email flowAmazon CloudFrontGlobal distribution

## Interaction with edge locationsOAC: Origin Access Control

## Bucket policyOnly authorize fromCloudFront Distribution

## Amazon API Gateway

## AWS LambdaDynamoDB

### REST HTTPSinvokeQuery / read

### DAXCaching layer

## DynamoDBStreamStream changes

## AWS LambdaInvoke lambda

Amazon Simple Email Service (SES)SDK to send emailIAM Role
## Thumbnail Generation flowAmazon CloudFrontGlobal distribution

## Interaction with edge locationsOAC: Origin Access Control

## Bucket policyOnly authorize fromCloudFront Distribution

## Amazon API Gateway

## AWS LambdaDynamoDB

### REST HTTPSinvokeQuery / read

### DAXCaching layer

## Amazon CloudFrontGlobal distribution

## Amazon S3OACUpload photosTransfer accelerationtrigger

## Amazon S3thumbnailAWS Lambda

optional

---

# AWS Hosted Website Summary

# Micro Services architecture

## Micro Services Environment

## AWS LambdaElastiCache

## Elastic Load Balancing

## Amazon EC2 Auto ScalingAmazon RDS

## Elastic Load Balancing

## Amazon Route 53

service1.example.comservice2.example.comservice3.example.com
UsersDNS QueryHTTPS

---

# Discussions on Micro Services

# Software updates offloading

# Our application current state

### Auto Scaling group

### Availability zone 2

### Availability zone 3

Amazon Elastic File System

---

# Easy way to fix things!

### Auto Scaling group

### Availability zone 2

### Availability zone 3

## Amazon Elastic File System

Amazon CloudFront

---

# Why CloudFront?

# Databases in AWS

# Choosing the Right Database

## Database Types

## Amazon RDS – Summary

## Amazon ElastiCache – Summary

## Amazon DynamoDB – Summary

## Amazon S3 – Summary

# DocumentDB

# Amazon Neptune

## Amazon Neptune – Streams

Neptune StreamsStreams API HTTP Get Request
ElastiCache…Streams reader applicationwrites
## Amazon Keyspaces (for Apache Cassandra)

## Amazon Timestream

## Amazon Timestream – Architecture

## Kinesis DataStreams

## Amazon MSK

## Kinesis Data AnalyticsFor Apache Flink

## Kinesis DataStreams

Any JDBC connection

---

# Data & Analytics

# Amazon Athena

load data

## AmazonAthenaQuery & Analyze

AmazonQuickSightReporting & Dashboards
## Amazon Athena – Performance Improvement

## Amazon Athena – Federated Query

## Database(On-Premises)S3 BucketLambda(Data SourceConnector)ElastiCacheDocumentDBDynamoDBRedshiftHBase in EMR

MySQLAuroraSQL Server

---

# Redshift Overview

## Redshift Cluster

## Amazon Redshift Cluster

JDBC/ODBCLeader NodeCompute Nodes
## Redshift – Snapshots & DR

## Redshift Cluster(Original)Cluster SnapshotTake Snapshot

### Region(eu-west-1)

Redshift Cluster(New)Copied SnapshotRestoreAutomated/ ManualCopy

---

# Loading data into Redshift: Large inserts are MUCH betterAmazon Kinesis Data FirehoseS3 using COPY command

## Amazon RedshiftCluster(through S3 copy)

Amazon RedshiftClusterS3 Bucket(mybucket)copy customerfrom 's3://mybucket/mydata’ iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole';

## InternetWithout Enhanced VPC RoutingWith Enhanced VPC RoutingThrough VPCEC2 InstanceJDBC driver

Amazon RedshiftClusterEC2 InstanceBetter to write Data in batches

---

# Redshift Spectrum

JDBC/ODBCLeader NodeCompute Nodes
12….N
Redshift SpectrumAmazon S3

---

# Amazon OpenSearch Service

## OpenSearch patternsDynamoDB

## Lambda Function

Amazon OpenSearchAPI to retrieve itemsAPI to search items
## OpenSearch patternsCloudWatch LogsCloudWatch LogsSubscription FilterLambda Function(managed by AWS)

## CloudWatch LogsSubscription FilterKinesis Data FirehoseAmazon OpenSearch

### Real time

Near Real Time
## OpenSearch patternsKinesis Data Streams & Kinesis Data Firehose

## AmazonOpenSearchLambdaFunction(real time)

Kinesis DataStreams
## Amazon EMR

## Amazon EMR – Node types & purchasing

## Amazon QuickSight

# QuickSight Integrations

### ELF & CLF(Log Format)

## TimestreamData Sources (AWS Services)

### Data Sources (SaaS)Data Sources (Imports)

On-PremisesDatabases (JDBC)
## QuickSight – Dashboard & Analysis

# AWS Glue

## Amazon RDS

## ExtractTransformGlue ETL

RedshiftData WarehouseLoad
## AWS Glue – Convert data into Parquet format

### Import CSVParquet

## OutputS3 BucketGlue ETL

Event notificationsOn S3 PUTLambda Function(EventBridge works as an alternative)Trigger Glue ETL JobS3 Put
## Glue Data Catalog: catalog of datasets

### Tables(Metadata)Database

### Tables(Metadata)

## Amazon AthenaAmazonRedshiftSpectrumAmazon EMR

## AWS GlueData Crawler

Glue Jobs (ETL)Data discovery
## Glue – things to know at a high-level

# AWS Lake Formation

# AWS Lake Formation

## Source CrawlersETL and Data Prep.Data CatalogSecurity SettingsAccess ControlData Lake(stored in S3)AthenaRedshiftEMR

ingest

---

# AWS Lake Formation Centralized Permissions Example

## Access ControlColumn-level securityData Lake(stored in S3)Athena

# Amazon Managed Service for Apache Flink

## Amazon Managed Servicefor Apache Flink

Kinesis DataStreams
## Amazon Managed Streaming for Apache Kafka (Amazon MSK)

## Apache Kafka at a high level

MSK Cluster
Etc…
### Broker 2

Broker 3Broker 1Producers(your code)Consumers(your code)EMRS3SageMakerKinesisRDSWrite to topicPoll from topicreplicationreplication
## Kinesis Data Streams vs. Amazon MSK

Amazon MSK
## Amazon MSK Consumers

## Kinesis Data Analytics for Apache Flink

AWS GlueStreaming ETL JobsPowered by Apache Spark StreamingLambdaAmazon EC2Applications Running onECSEKS

---

# Big Data Ingestion Pipeline

# Big Data Ingestion Pipeline

## Amazon Kinesis Data Firehose

## AWS Lambda

## Amazon Simple Storage Service (S3)Amazon Simple Queue Service

## AWS Lambda

## Amazon Athena

## Amazon Simple Storage Service (S3)Reporting Bucket

IoT DevicesIngestion Bucket(optional)Every 1 minuteReal-timetriggerPull data

## Amazon QuickSight

Amazon RedshiftServerless

---

# Big Data Ingestion Pipeline discussion

# Machine Learning

# Amazon Rekognition

## Amazon Rekognition – Content Moderation

## Amazon Transcribe

## Amazon Polly

## Amazon Polly – Lexicon & SSML

## Amazon Translate

## Amazon Lex & Connect

LexIntent recognized
CRMcallstreaminvokeschedule
## Amazon Comprehend

## Amazon Comprehend Medical

## Amazon SageMaker AI

670890934build
### ML model

### Train and Tune

New dataApply modelPredictionPASS WITH 906score
## Amazon Kendra

## Amazon S3Amazon RDSGoogle DriveMS SharePointMS OneDrive3rd party, APNs, Custom

## Knowledge Index(powered by ML)Amazon Kendra

indexing
UserWhere is the IT support desk?
1st floor
## Amazon Personalize

Customized personalized APIWebsites & AppsMobile AppsSMSEmails
- Amazon Textract
- Automatically extracts text, handwriting, and data from any scanned documents using AI and ML
- Extract data from forms and tables
- Read and process any type of document (PDFs, images, …)
- **Use cases**: 
- Financial Services (e.g., invoices, financial reports)
- Healthcare (e.g., medical records, insurance claims)
- Public Sector (e.g., tax forms, ID documents, passports)
Amazon Textract{ “Document ID”: “123456789-005”, “Name”: “”, “SEX”: “F”, “DOB”: “23.05.1997”, …}analyzeresult
## AWS Machine Learning - Summary

# AWS Monitoring, Audit and PerformanceCloudWatch, CloudTrail & AWS Config

# Amazon CloudWatch Metrics

## CloudWatch Metric Streams

## Amazon S3AmazonRedshiftAmazon OpenSearch

## Kinesis Data Firehose

AthenaStream near-real-time
## CloudWatch Logs

## CloudWatch Logs - Sources

## CloudWatch Logs Insights

## CloudWatch Logs Insights

## CloudWatch Logs – S3 Export

## CloudWatch Logs Subscriptions

KDFKDAEC2Lambda…
## CloudWatch Logs AggregationMulti-Account & Multi Region

## CloudWatch LogsSubscription Filter

## CloudWatch LogsSubscription Filter

## Kinesis Data StreamsKinesis Data FirehoseNear Real Time

Amazon S3ACCOUNT AREGION 1ACCOUNT BREGION 2ACCOUNT BREGION 3
- CloudWatch Logs Subscriptions
- Cross-Account Subscription – send log events to resources in a different AWS account (KDS, KDF)Account – Sender(111111111111)
### CloudWatchLogsSubscriptionFilterlogsAccount – Recipient(999999999999)

### Kinesis Data Streams(RecipientStream)

### SubscriptionDestination

### DestinationAccess PolicyIAM RoleIAM Role(Cross-Account)

### DestinationAccess Policylogs

Can be assumedallow PutRecord
## CloudWatch Logs for EC2

## CloudWatch Logs Agent & Unified Agent

## CloudWatch Unified Agent – Metrics

## CloudWatch Alarms

## CloudWatch Alarm Targets

## CloudWatch Alarms – Composite Alarms

## EC2 Instance

## CW Alarm - Bmonitor CPUmonitor IOPSComposite Alarm

## Amazon SNS

# EC2 Instance Recovery

- SNS Topicalert
- **Recovery**: Same Private, Public, Elastic IP , metadata, placement group

---

# CloudWatch Alarm: good to know

## CW AlarmAlertAmazon SNS

Metric Filter

---

# Amazon EventBridge (formerly CloudWatch Events)

Schedule Every hourTrigger script on Lambda function
## Amazon EventBridge Rules

Filter events(optional)Example Destinations{ "version": "0", "id": "6a7e8feb-b491", "detail-type": "EC2 Instance State-change Notification", ….}JSON

## LambdaAWS BatchECS Task

## SQSSNSKinesis DataStreams

### StepFunctionsCodePipelineCodeBuild

SSMEC2 ActionsComputeIntegrationOrchestrationMaintenance
## Amazon EventBridge

## Default Event BusPartner Event BusCustom Event BusAWS SaaS Partners

Custom Apps
## Amazon EventBridge – Schema Registry

## Amazon EventBridge – Resource-based Policy

## AWS Account(111122223333)

### EventBridge Bus(central-event-bus)

Lambda functionPutEvents
## CloudWatch Container Insights

EKS ContainerMetrics and logsCloudWatch Container Insights
## CloudWatch Lambda Insights

## CloudWatch Contributor Insights

## CloudWatch LogsCloudWatch Contributor Insights

Top-10 IP addresses
## CloudWatch Application Insights

## CloudWatch Insights and Operational Visibility

# AWS CloudTrail

## CloudTrail Diagram

## ConsoleCloudTrail Console

### Inspect & Audit

## CloudWatch Logs

## S3 Bucket

IAM Users &IAM Roles
## CloudTrail Events

## CloudTrail Insights

generate

## CloudTrail Console

## S3 Bucket

EventBridge event
## CloudTrail Events Retention

## S3 BucketLong-term retention

### Data Events

### Management EventsInsights Events

log90 days retention
analyzeAthena
## Amazon EventBridge – Intercept API Calls

## SNSeventDynamoDBLog API call

UseralertDeleteTable API Call

---

# Amazon EventBridge + CloudTrail

## IAMIAM Role

UserAssumeRoleAPI Call logs
event

## CloudTrailEC2

UserAuthorizeSecurityGroupIngressAPI Call logs
event
### Security Groupedit SGInbound Rules

# AWS Config

## Config Rules

# AWS Config Resource

## Config Rules – Remediations

expired
AWS ConfigmonitorAuto-Remediation Action(SSM Document: AWSConfigRemediation-RevokeUnusedIAMUserCredentials)triggerRetries: 5deactivate
## Config Rules – Notifications

## Security group…monitorAWS ConfigEventBridge

## NON_COMPLIANT

trigger

## LambdaSNSSQS…

monitorAWS ConfigSNS
trigger

## AdminAll events (configuration changes,compliance state…)AWS Resources

Security group…notification

---

# CloudWatch vs CloudTrail vs Config

# For an Elastic Load Balancer

# Advanced Identity in AWS

## AWS Organizations

# AWS OrganizationsRoot Organizational Unit (OU)

Member Accounts
OU (Prod)
### OU (HR)

OU (Finance)
## Organizational Units (OU) - ExamplesBusiness Unit

Management AccountProd OUDev OUTest OUProdAccount 1ProdAccount 2DevAccount 1DevAccount 2TestAccount 1TestAccount 2Project-Based
Management AccountProject 1 OUProject 2 OUProject 3 OUProject 1Account 1Project 1Account 2Project 2Account 1Project 2Account 2Project 3Account 1Project 3Account 2
## AWS Organizations

# SCP HierarchyOU (Root)

OU (Sandbox)
### OU (Test)

- Account AAccount DFullAWSAccessDeny AthenaFullAWSAccess + Deny S3FullAWSAccess + Deny EC2
- Management Account
- Can do anything (no SCP apply)
- Account A
- Can do anything
- EXCEPT S3 (explicit Deny from Sandbox OU)
- EXCEPT EC2 (explicit Deny)
- Account B & C
- Can do anything
- EXCEPT S3 (explicit Deny from Sandbox OU)
- Account D
- Can access EC2
- Prod OU & Account E & F
- Can do anything
### Account B

Account COU (Workloads)
OU (Prod)
Account E
### Account F

FullAWSAccessAllow EC2FullAWSAccess

---

# SCP ExamplesBlocklist and Allowlist strategies

## AWS Organizations – Tag Policies

# IAM Conditionsaws:SourceIprestrict the client IP from which the API calls are being made

# IAM Conditionsec2:ResourceTagrestrict based on tagsaws:MultiFactorAuthPresentto force MFA

- IAM for S3
- **s3**: ListBucket permission applies toarn:aws:s3:::test
- => bucket level permission
- **s3**: GetObject, s3:PutObject, s3:DeleteObject applies toarn:awn:s3:::test/*
- => object level permission

---

# Resource Policies & aws:PrincipalOrgID

…Member Accounts
User outside Organization
## IAM Roles vs Resource Based Policies

Amazon S3S3 Bucket Policy
## IAM Roles vs Resource-Based Policies

- Amazon EventBridge – Security
- When a rule runs, it needs permissions on the target
- **Resource-based policy**: Lambda, SNS, SQS, S3 buckets, API Gateway…
- **IAM role**: EC2 Auto Scaling, Systems Manager Run Command, ECS task…
### Lambda with Resource based Policye.g. Allow EventBridge

IAM RoleEC2 Auto ScalingEventBridgeRule

---

# IAM Permission Boundaries

=No PermissionsExample:

---

# IAM Permission Boundaries

# IAM Policy Evaluation Logic

## Example IAM Policy

# AWS IAM Identity Center(successor to AWS Single Sign-On)

## AWS IAM Identity Center – Login Flow

## AWS IAM Identity Center

### Business Cloud Apps

## Custom SAML2.0-enabled AppsAWS IAM Identity CenterPermission Sets

### Browser Interface

## Windows EC2loginStore / retrieveUser identitiesSSO

### Active DirectoryUsers & groups(On-premises, cloud)

IAM Identity CenterBuilt-in Identity StoreAWS Cloud
## IAM Identity CenterAWS Organization

### OU (Development)

### Dev Account A

### Dev Account B

### OU (Production)

### Prod Account A

### Prod Account B

## IAM Identity Center(in Management account)Group (Developers)

### Permission SetReadOnlyAccess

Permission SetFullAccessassignassign

---

# AWS IAM Identity CenterFine-grained Permissions and Assignments

## DatabaseAdminsAurora

## IAM RoleIAM Roleassume

Permission Sets(DB Admins)

---

# What is Microsoft Active Directory (AD)?

## AWS Directory Services

### On-prem ADAD Connectorproxy

Simple ADauthauthauth
## IAM Identity Center – Active Directory Setup

## AWS ManagedMicrosoft ADconnect

## IAM IdentityCenter

## AWS ManagedMicrosoft ADtwo-way trust relationship

### AD Connectorproxy

connectconnect

---

# AWS Control Tower

## AWS Control Tower – Guardrails

## Guardrail(Detective)SNSLambda

monitor un-taggedresourcestrigger(NON_COMPLIANT)Adminnotifyinvokeremediate(add tags)
AWS Config

---

# AWS Security & EncryptionKMS, Encryption SDK, SSM Parameter Store

# Why encryption?Encryption in flight (TLS / SSL)

TLS EncryptionTLS DecryptionUsername: adminPassword: supersecretUsername: adminPassword: supersecretaGVsbG8gd29ybGQgZWh…ClientServerClient
- Why encryption?Server-side encryption at rest
- Data is encrypted after being received by the server
- Data is decrypted before being sent
- It is stored in an encrypted form thanks to a key (usually a data key)
- The encryption / decryption keys must be managed somewhere, and the server must have access to it
### AWS Service (e.g., S3)

+HTTP(S)HTTP(S)ObjectData keyObject
+Data key
## Why encryption?Client-side encryption

+Data key(client-side)
storeEncrypted object
Data key(client-side)

---

# AWS KMS (Key Management Service)

## KMS Keys Types

# AWS KMS (Key Management Service)

# Copying Snapshots across regions

### KMS Key ARegion eu-west-2

## EBS VolumeEncryptedWith KMSEBS SnapshotEncryptedWith KMSKMS Key BKMS Key BRegion ap-southeast-2

KMS ReEncrypt with KMS Key B

---

# KMS Key Policies

KMS Key Policy

---

# KMS Multi-Region KeysAWS KMS

multi-Region Primary keyarn:aws:kms:us-east-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890abus-west-2
multi-Region Replica keyarn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890abeu-west-1
multi-Region Replica keyarn:aws:kms:eu-west-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890abap-southeast-2
multi-Region Replica keyarn:aws:kms:ap-southeast-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890absync
## KMS Multi-Region Keys

# DynamoDB Global Tables and KMS Multi-Region Keys Client-Side encryption

Client App1. Encrypt attribute with primary MRK2. Put encryptedattributeap-southeast-2
### DDB TableKMSMRK

Client App5. Decrypt attribute with replica MRK4. Get encryptedattribute3. Global TableReplicationAttr(SSN)
Attr(SSN)replication
## Global Aurora and KMS Multi-Region Keys Client-Side encryption

Client App1. Encrypt attribute with primary MRK2. Put encryptedcolumnap-southeast-2
Client App5. Decrypt attribute with replica MRK4. Get encryptedcolumn3. Global DBReplicationCol(SSN)
Col(SSN)replication

---

# S3 Replication Encryption Considerations

AMIAccount - A
AMIAccount - B
share
EC2 Instancelaunchshare

---

# SSM Parameter Store

# SSM Parameter Store Hierarchy

# Parameters Policies (for advanced parameters)

NoChangeNotification (EventBridge)

---

# AWS Secrets Manager

## AWS Secrets Manager – Multi-Region Secrets

## MySecret-A(primary)us-west-2 (Secondary)

SecretsManagerMySecret-A(replica)replicate

---

# AWS Certificate Manager (ACM)

EC2 InstanceEC2 InstanceAWS Certificate ManagerApplicationLoadBalancerHTTPSHTTPprovision andmaintain TLS certs
## ACM – Requesting Public Certificates1.List domain names to be included in the certificate

## ACM – Importing Public Certificates

## Rule events:Non-compliance

ACMACM Events:Daily Certificate ExpiryRule check
## ACM – Integration with ALB

EC2 InstanceEC2 InstanceAWS Certificate ManagerApplication Load BalancerWith HTTP -> HTTPS redirect ruleHTTPprovision andmaintain TLS certsRedirect to HTTPSHTTPS
## API Gateway - Endpoint Types

## ACM – Integration with API Gateway

## CloudFrontACMlinkedcertificateAPI GatewayEdge-Optimized

ap-southeast-2
ACMlinkedcertificateAPI GatewayRegional
## AWS WAF – Web Application Firewall

## AWS WAF – Web Application Firewall

## WAF – Fixed IP while using WAF with a Load Balancer

us-east-1
### Application LoadBalancer

## AWS WAFWebACLattached

EC2 InstancesWebACL must be in the sameAWS Region as ALB

---

# AWS Shield: protect from DDoS attack

## AWS Firewall Manager

# WAF vs. Firewall Manager vs. Shield

AWS Shield

---

# AWS Best Practices for DDoS ResiliencyEdge Location Mitigation (BP1, BP3)

## AWS Best Practices for DDoS ResiliencyBest pratices for DDoS mitigation

## AWS Best Practices for DDoS ResiliencyApplication Layer Defense

## AWS Best Practices for DDoS ResiliencyAttack surface reduction

# Amazon GuardDuty

## Amazon GuardDuty

## CloudTrail Logs

## DNS Logs (AWS DNS)GuardDutyEventBridge

### Optional Features

## EKS Audit Logs &Runtime Monitoring

## RDS & AuroraLogin Activity

## S3 Logs

## EBS Volumes

Lambda NetworkActivity
- Amazon Inspector
- Automated Security Assessments
- For EC2 instances
- Leveraging the AWS System Manager (SSM) agent
- Analyze against unintended network accessibility
- Analyze the running OS against known vulnerabilities
- For Container Images push to Amazon ECR
- Assessment of Container Images as they are pushed
- For Lambda Functions
- Identifies software vulnerabilities in function code and package dependencies
- Assessment of functions as they are deployed
- Reporting & integration with AWS Security Hub
- Send findings to Amazon Event Bridge
### SSM AgentAmazonInspector

### EventBridgeassessment run state& findings

### Security Hub

Amazon ECRContainer Image

---

# What does Amazon Inspector evaluate?

# AWS Macie

## S3 Buckets

### MacieDiscover Sensitive Data (PII)

AmazonEventBridgeanalyzenotifyintegrations

---

# Amazon VPC

# VPC Components Diagram

## Availability ZoneVPC

## VPC PeeringConnectionsPrivate SubnetPublic Subnet

### InternetGatewayRouterRouteTable

### NAT GatewaySecurity Group

## Public EC2 Instance

### NACLSecurity Group

## Private EC2 InstanceSecurity Group

## Private EC2 Instance

## VPC Flow Logs

InternetwwwCorporate Data Center
### S2S VPNConnection

## CloudWatchS3VPCEndpoint

### DX Location

## Direct ConnectConnection

## Understanding CIDR – IPv4

## Understanding CIDR – IPv4

## Understanding CIDR – Subnet Mask

## Understanding CIDR – Little Exercise

# Public vs. Private IP (IPv4)

# Default VPC Walkthrough

## VPC in AWS – IPv4

# State of Hands-on

# Adding Subnets

Availability ZonePrivate SubnetPublic Subnet
## VPC – Subnet (IPv4)

# Internet Gateway (IGW)

# Adding Internet Gateway

### Availability ZonePrivate SubnetPublic Subnet

# Editing Route Tables

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

# Bastion Hosts

### Private SubnetPublic Subnet

## EC2 Instance(Bastion Host)

## Security Group (BastionHost-SG)

Security Group (LinuxInstance-SG)UsersSSH

---

# NAT Instance (outdated, but still at the exam)

### Private SubnetPublic Subnet

### NAT Instance

## Security Group (NATInstance-SG)

## EIP(IP: 12.34.56.78)

## IP: 10.0.0.10IP: 10.0.0.20

Server(IP: 50.60.4.10)
Src.: 10.0.0.20Dest.: 50.60.4.10Src.: 12.34.56.78Dest.: 50.60.4.10Src.: 50.60.4.10Dest.: 12.34.56.78
Src.: 50.60.4.10Dest.: 10.0.0.20
## NAT Instance

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### InternetwwwSecurity Group

### NAT InstanceSecurity Group

## Private EC2 Instance

## NAT Instance – Comments

## NAT Gateway

## NAT Gateway

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### NAT GatewaySecurity Group

## Private EC2 Instance

## NAT Gateway with High Availability

## AZ - BAZ - APublic Subnet

### Private Subnet

### NAT Gateway

## EC2 Instance

### Public Subnet

### Private Subnet

### NAT Gateway

EC2 Instance
More at: [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html)

---

# SubnetSecurity Groups & NACLs

## EC2 InstanceNACL

### NACL InboundRules

### SG InboundRules Outbound Allowed(Stateful)

### NACL OutboundRules (Stateless)Incoming RequestSubnetSecurity Group

## EC2 InstanceNACL

### NACL OutboundRules

### SG OutboundRules Inbound Allowed(Stateful)

NACL InboundRules (Stateless)Outgoing Request123123

---

# Network Access Control List (NACL)

# NACLs

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### NAT GatewaySecurity Group

## Private EC2 Instance

# Default NACL

# ResponseEphemeral Ports

# NACL with Ephemeral PortsVPC

### Web TierDatabase Tier

DB InstancePort 3306

## Web-NACL

## DB-NACL

### Allow Outbound TCPOn port 3306To DB Subnet CIDR

### Allow Inbound TCPOn port 3306From Web Subnet CIDR

Allow Inbound TCPOn port 1024-65535From DB Subnet CIDRAllow Outbound TCPOn port 1024-65535To Web Subnet CIDR[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-portsClientEphemeral](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-portsClientEphemeral) Port

---

# Create NACL rules for each target subnets CIDRVPC

## Web Subnet - B (Public)

## DB Subnet – B (Private)

Web TierDatabase TierDB InstanceDB Instance

## Web-NACL

DB-NACL

---

# VPC Peering

## VPC - B

## VPC - C

VPC Peering(A – B)VPC Peering(B – C)VPC Peering(A – C)
## VPC Peering – Good to know

# VPC Peering

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### NAT GatewaySecurity Group

## Private EC2 Instance

VPC PeeringConnections

---

# VPC Endpoints

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### NAT GatewaySecurity Group

## Private EC2 Instance

## VPC PeeringConnections

## CloudWatchS3VPCEndpoint

# VPC Endpoints (AWS PrivateLink)

### Public Subnet

### InternetGatewayRegion

## VPC Endpoint

## EC2 InstancewwwNATGateway

## EC2 InstanceAmazon SNSOption 1Option 2

Amazon SNS

---

# Private SubnetTypes of Endpoints

## EC2 Instance

## VPC Endpoint(Interface)ENI (PrivateLink)

## Amazon SNS

Private SubnetRegion

## EC2 InstanceAmazon S3

## VPC Endpoint(Gateway)

# Gateway or Interface Endpoint for S3?

## Direct ConnectS2S VPN

## Amazon S3InterfaceEndpointIn-VPCApps

GatewayEndpointPrivateLink

---

# Private subnetLambda in VPC accessing DynamoDBAWS Cloud

Public subnet
- VPC Gateway EndpointFor DynamoDB
- DynamoDB is a public service from AWS
- **Option 1**: Access from the public internet
- Because Lambda is in a VPC, it needs a NAT Gateway in a public subnet and an internet gateway
- **Option 2 (better & free)**: Access from the private VPC network
- Deploy a VPC Gateway endpoint for DynamoDB
- Change the Route Tables
## VPC Flow Logs

## VPC Flow Logs

### Availability ZonePrivate SubnetPublic Subnet

### RouterRouteTableSecurity Group

## Public EC2 Instance

### NAT GatewaySecurity Group

## Private EC2 Instance

## VPC PeeringConnections

## CloudWatchS3VPCEndpoint

VPC Flow Logs
## VPC Flow Logs Syntax

## VPC Flow Logs – Troubleshoot SG & NACL issues

## EC2 InstanceNACL

### NACL InboundRules

### SG InboundRules Outbound Allowed(Stateful)

### NACL OutboundRules (Stateless)SubnetSecurity Group

## EC2 InstanceNACL

### NACL OutboundRules

### SG OutboundRules Inbound Allowed(Stateful)

- NACL InboundRules (Stateless)Incoming Requests
- Inbound REJECT => NACL or SG
- Inbound ACCEPT, Outbound REJECT => NACLOutgoing Requests
- Outbound REJECT => NACL or SG
- Outbound ACCEPT, Inbound REJECT => NACLLook at the “ACTION” field
## VPC Flow Logs – Architectures

## CloudWatch LogsCloudWatch Contributor Insights

### Top-10 IP addresses

## CW AlarmAlertAmazon SNS

### Metric Filter

## VPC Flow Logs

## CloudWatch Logs

## VPC Flow Logs

## S3 Bucket

AmazonQuickSightSSH, RDP…

---

# AWS Site-to-Site VPN

## Availability ZoneVPC

## VPC PeeringConnectionsPrivate SubnetPublic Subnet

### InternetGatewayRouterRouteTable

### NAT GatewaySecurity Group

## Public EC2 Instance

### NACLSecurity Group

## Private EC2 InstanceSecurity Group

## Private EC2 Instance

## VPC Flow Logs

InternetwwwCorporate Data Center
### S2S VPNConnection

CloudWatchS3VPCEndpoints

---

# AWS Site-to-Site VPN

# Private SubnetSite-to-Site VPN Connections

Corporate Data Center
### Virtual PrivateGatewayCustomerGateway(Public IP)

### Route Table(Route Propagation enabled)

### NAT Device(Public IP)

CustomerGateway(Private IP)
## AWS VPN CloudHub

### Private Subnet 2

### Availability Zone

## EC2 Instances

## EC2 InstancesCustomer Network

### Customer Network

### Customer Network

VirtualPrivateGateway(VGW)CustomerGatewayCustomerGatewayCustomerGateway

---

# Direct Connect (DX)

## Direct Connect Diagram

### Private Subnet

## EC2 Instances

### Virtual Private Gateway

## Amazon S3Amazon Glacier

## AWS Direct Connect LocationAWS CageCustomer orpartner cageAWS DirectConnect EndpointCustomer orpartner router

### Corporatedata center

### Customer NetworkCustomerrouter/firewallVLAN 1VLAN 2

Private virtual interfacePublic virtual interface
## Direct Connect Gateway

### Region(us-west-1)

## VPC10.0.0.0/16172.16.0.0/16Direct Connect Gateway

### Customer network

AWS DirectConnectconnectionPrivate virtualinterfacePrivate virtualinterfacePrivate virtualinterface
## Direct Connect – Connection Types

## Direct Connect – Encryption

## VPCAvailability Zone(us-east-1a)

### Availability Zone(us-east-1b)

### Private Subnet 1

### Private Subnet 2

## EC2 Instances

## EC2 Instances

## AWS DirectConnect LocationAWS DirectConnect Endpoint

### Customer NetworkCustomerrouter/firewall

### Corporatedata center

VPN Connection
## Direct Connect - ResiliencyHigh Resiliency for Critical Workloads

Maximum resilience is achieved by separate connections terminating on separate devices in more than one location.

## AWS DirectConnect Location - 1

### Corporatedata center

## AWS DirectConnect Location - 2

Corporatedata center

## AWS DirectConnect Location - 1

### Corporatedata center

## AWS DirectConnect Location - 2

Corporatedata center

---

# Site-to-Site VPN connection as a backup

Corporate DCVPC

---

# Network topologies can become complicated

## Amazon VPC

VPN Connection

## Amazon VPC

## VPC PeeringConnection

## Amazon VPC

## VPC PeeringConnection

## Amazon VPC

## VPC PeeringConnection

## VPC PeeringConnection

## VPC PeeringConnection

### VPN Connection

### VPN Connection

Direct ConnectGateway

---

# Transit Gateway

## Amazon VPC

## Amazon VPC

## Amazon VPC

Amazon VPCVPN ConnectionCustomer GatewayTransit Gateway
## Transit Gateway: Site-to-Site VPN ECMP

## AWS Transit GatewayVPC attachmentVPC attachmentVPC attachmentVPC attachment

### Corporate data center172.16.0.0/16

VPN attachment
## Transit Gateway: throughput with ECMPVPN to virtual private gateway

1x=1.25 Gbps
VPN connection(2 tunnels)VPN to transit gateway
1x=1xVPC
1x=2.5 Gbps (ECMP) – 2 tunnels used
2x=5.0 Gbps (ECMP)
3x=7.5 Gbps (ECMP)
per GB of TGWprocessed data
## Transit Gateway – Share Direct Connect between multiple accounts

Corporatedata center

## AWS DirectConnect endpointCustomer router/firewallTransit VIFVLANAccount 1DirectConnectGateway

## AWS CloudRegion

TransitGatewayAccount 2
VPCYou can use AWS Resource Access Manager to share Transit Gateway with other accounts.
## VPC – Traffic Mirroring

### Source A

### Auto Scaling groupNetwork LoadBalancer

Inbound &Outbound trafficInbound &Outbound trafficTraffic Mirroring(filter traffic, optional)
EC2 instances with Security Appliances

---

# What is IPv6?

# IPv6 in VPC

InternetGatewayIPv4 & IPv6Internet

---

# IPv4 Troubleshooting

192.168.0.10192.168.0.1510.0.0.35

---

# Egress-only Internet Gateway

InternetGatewayPublic Subnet
IPv6: 2001:db8::b1c2
IPv6: 2001:db8::e1c3
### Egress-onlyInternet Gatewayinitiate connectionsfrom both sides

can’t initiateconnections fromInternet
Private Subnet

---

# Private Subnet(IPv4: 10.0.1.0/24)(IPv6: 2001:db8:1234:1a02::/64)Public Subnet(IPv4: 10.0.0.0/24)(IPv6: 2001:db8:1234:1a00::/64)IPv6 RoutingRegion

Web serverPrivate IPv4: 10.0.0.5EIP: 198.51.100.1IPv6: 2001:db8:1234:1a00::123ServerPrivate IPv4: 10.0.1.5IPv6: 2001:db8:1234:1a02::456
NAT Gateway(IPv4)EIP: 198.51.100.1
### InternetGateway(IPv4 & IPv6)Egress-onlyInternet Gateway(IPv6)

Route Table(Public Subnet)DestinationTarget10.0.0.0/16local2001:db8:1234:1a00::/56local0.0.0.0/0igw-id::/0igw-id
DestinationTarget10.0.0.0/16local2001:db8:1234:1a00::/56local0.0.0.0/0nat-gateway-id::/0eigw-idInternet
Route Table(Private Subnet)

---

# VPC Section Summary (1/3)

# VPC Section Summary (2/3)

# VPC Section Summary (3/3)

## Networking Costs in AWS per GB - SimplifiedRegion

## Availability Zone$0.02Inter-region$0.02 if usingPublic IP / Elastic IP

### Free if using private IP$0.01 if Using private IP

- Use Private IP instead of Public IP for good savings and better network performance
- Use same AZ for maximum savings (at the cost of high availability)Free for traffic in

---

# Minimizing egress traffic network cost

## AWS Cloud

DatabaseApplicationEgress cost is minimizedCorporate data center

## AWS Cloud

### DB Query100 MB

### DatabaseApplicationQuery Results50 KB

DB Query100 MBQuery Results50 KBEgress cost is high
## S3 Data Transfer Pricing – Analysis for USA

### Edge location

### Transfer acceleration +$0.04

internet$0.09$0.00CloudFront
$0.085

---

# Private subnet 2(10.0.1.0/24)Public subnetPricing: NAT Gateway vs Gateway VPC EndpointRegion(us-east-1)

### Private subnet 1(10.0.0.0/24)

## EC2 Instance

### NAT GatewayInternetGateway

## VPC Endpoint

## InternetS3 Bucket

EC2 InstanceDestinationTarget10.0.0.0/16Local0.0.0.0/0igw-idDestinationTarget10.0.0.0/16Localpl-id for Amazon S3vpce-idSubnet 1 route tableSubnet 2 route table$0.045 NAT Gateway / hour$0.045 NAT Gateway data processed / GB$0.09 Data transfer out to S3 (cross-region)$0.00 Data transfer out to S3 (same-region)
No cost for using Gateway Endpoint.$0.01 Data transfer in/out (same-region)

---

# Network Protection on AWS

## AWS Network Firewall

## Peered VPC

### VPN connection

## Direct Connect

Corporate DCAWS Network Firewallinternet
## Network Firewall – Fine Grained Controls

# Disaster Recovery & Migrations

## Disaster Recovery Overview

# RPO and RTO

# Disaster Recovery Strategies

# Backup and Restore (High RPO)Corporate data center

## AWS Cloud

## AWS Storage Gateway

## GlacierAmazon S3AWS Snowball

lifecycleAWS Cloud

## Amazon EC2

## Amazon RDS

AMIScheduled regularsnapshots
## Disaster Recovery – Pilot Light

## RDS (running)

## Data ReplicationEC2 (not running)

Route 53

---

# Warm Standby

## RDS Secondary (running)

## Data ReplicationRoute 53

## EC2 Auto Scaling(minimum)

Reverse proxyApp ServerPrimaryDBfailover

---

# Multi Site / Hot Site Approach

## RDS secondary (running)

## Data ReplicationRoute 53

## EC2 Auto Scaling(production)

Reverse proxyApp ServerPrimaryDBfailoveractiveactive
## All AWS Multi RegionAWS Cloud

## EC2 Auto Scaling(production)

failoveractiveactiveAWS Cloud

## EC2 Auto Scaling(production)ELB

## Aurora Global (primary)

Aurora Global (secondary)

---

# Disaster Recovery Tips

## DMS – Database Migration Service

Target DB

---

# DMS Sources and TargetsSOURCES:

# AWS Schema Conversion Tool (SCT)

Target DB (different engine)
## DMS - Continuous ReplicationCorporate data center

### RegionPublic Subnet

## AWS DMS Replication Instance

## Private SubnetAmazon RDS for MySQL DB(target)Full load +CDCSchema conversionData migration

Server withAWS SCT installed
## AWS DMS – Multi-AZ DeploymentAWS RegionAvailability Zone - A

- DMS ReplicationInstance(Standby Replica)synchronousreplication
- When Multi-AZ Enabled, DMS provisions and maintains a synchronously stand replica in a different AZ
- **Advantages**: 
- Provides Data Redundancy
- Eliminates I/O freezes
- Minimizes latency spikes

---

# RDS & Aurora MySQL Migrations

import
mysqldump

---

# RDS & Aurora PostgreSQL Migrations

import

---

# On-Premise strategy with AWS

## AWS Backup

## AWS Backup

## AWS Backup

## EC2EBSDynamoDBRDSEFS

## Amazon S3Automaticallybacked up to

## AWS Backup Vault Lock

# AWS Application Discovery Service

# AWS Application Migration Service (MGN)

## AWS Cloud

## AWS ReplicationAgentStaging

cutoverLow-cost EC2 instances& EBS volumesTarget EC2 instances& EBS volumescontinuous replication
Application Migration Service
- VMware Cloud on AWS
- Some customers use VMware Cloud to manage their on-premises Data Center
- They want to extend the Data Center capacity to AWS, but keep using the VMware Cloud software
- …Enter VMware Cloud on AWS
- Use cases
- Migrate your VMware vSphere-based workloads to AWS
- Run your production workloads across VMware vSphere-based private, public, and hybrid cloud environments
- Have a disaster recover strategy
Customer Data Center
### AWS Cloud

### On-Premises vCentervSphere-basedenvironment

vSphereVMware Cloudon AWSAWS Services
AmazonEC2AmazonS3DirectConnectAmazonFSxAmazonRDSAmazonRedshift

---

# Transferring large amount of data into AWS

# More Solutions Architecture

# Lambda, SNS & SQS

DLQTry, retry

## SQS FIFO

## DLQTry, retryblockingDLQasynchronous(poll)SQS + Lambda

SQS FIFO + LambdaSNS + Lambda

---

# Fan Out Pattern: deliver to multiple SQS

### PUT #1PUT #2PUT #3Option 1SDK

## Option 2 – Fan Out

SNSSQSSQSPUTsubscribe

---

# S3 Event Notifications

## Lambda Function

- SNS
- **S3**: ObjectCreated, S3:ObjectRemoved, S3:ObjectRestore, S3:Replication…
- Object name filtering possible (*.jpg)
- **Use case**: generate thumbnails of images uploaded to S3
- Can create as many “S3 events” as desired
- S3 event notifications typically deliver events in seconds but can sometimes take a minute or longer

---

# S3 Event Notifications with Amazon EventBridge

- AmazonEventBridgerulesOver 18 AWS servicesas destinations
- Advanced filtering options with JSON rules (metadata, object size, name...)
- Multiple Destinations – ex Step Functions, Kinesis Streams / Firehose…
- EventBridge Capabilities – Archive, Replay Events, Reliable delivery
## Amazon EventBridge – Intercept API Calls

## SNSeventDynamoDBLog API call

UseralertDeleteTable API Call
## API Gateway – AWS Service IntegrationKinesis Data Streams example

# Caching Strategies

## CloudFront (edge)

## Redis Memcached DAXS3

### Caching, TTL, Network, Computation, Cost, LatencyClient

## App logicEC2 / Lambda

# Blocking an IP address

### Public Subnet

### Security Group (allow rules)

## EC2 Instancepublic IP + Firewall Software (optional)

NACLDeny + Allow rules
## Blocking an IP address – with an ALB

### Public Subnet

## EC2 Security Group

## EC2 InstancePrivate IP

### Private Subnet

### ALB Security Group

Application Load BalancerConnection TerminationNACL
## Blocking an IP address – with an NLB

### Public Subnet

## EC2 Security Group

## EC2 InstancePrivate IP

### NACLPrivate Subnet

NLB Security GroupNetwork Load Balancer
## Blocking an IP address – ALB + WAF

### Public Subnet

## EC2 Security Group

## EC2 InstancePrivate IP

### NACLPrivate Subnet

### ALB Security Group

### Application Load Balancer

AWS WAFIP Address Filtering
## Blocking an IP address – ALB, CloudFront & WAF

### Public Subnet

## EC2 Security Group

## EC2 InstancePrivate IP

### NACLPrivate Subnet

### ALB Security Group

### Application Load BalancerPublic

## CloudFront(Geo Restriction)

AWS WAF(IP Address Filtering)CloudFrontPublic IPsNOT helpful

---

# High Performance Computing (HPC)

# Data Management & Transfer

# Compute and Networking

## Compute and Networking

# Storage

# Automation and Orchestration

# Creating a highly available EC2 instance

## Elastic IP Address

What time is it?5:30 pm!

## Standby EC2 instance

## CloudWatch Event(or Alarm based on metric)

Start the instanceAttach the Elastic IPmonitor
## Creating a highly available EC2 instanceWith an Auto Scaling Group

## Elastic IP Address

What time is it?5:30 pm!

## Replacement EC2 instance

### Auto Scaling group

## EC2 User DataAttachmentBased on TagAvailability Zone 1

Availability Zone 2ASG Settings1 min1 max1 desired>= 2 AZEC2 user data to attachThe Elastic IPEC2 instance role to Allow API calls to attachThe Elastic IP
## Creating a highly available EC2 instanceWith ASG + EBS

## Elastic IP Address

What time is it?5:30 pm!

## Replacement EC2 instance

### Auto Scaling group

## EC2 User DataAttachmentBased on TagAvailability Zone 1

Availability Zone 2

## EBS Volume

## EBS Snapshot+ tagsEBS SnapshotOn ASG Terminate lifecycle hook

EBS Volume created + attachedOn ASG Launch lifecycle hook

---

# Other ServicesOverview of Services that might come up in a few questions

# What is CloudFormation

# Benefits of AWS CloudFormation (1/2)

## Benefits of AWS CloudFormation (2/2)

## CloudFormation + Infrastructure Composer

## CloudFormation – Service Role

- s3:*BucketService RoleUserTemplateCloudFormation
S3 bucket

---

# Amazon Simple Email Service (Amazon SES)

APIsor SMTPbulk emails
## Amazon Pinpoint

## Systems Manager – SSM Session Manager

Execute commandsSession Manager
## Systems Manager – Run Command

## Amazon SNSnotification

## EC2 Instances(with SSM Agent)

EC2 Instances(with SSM Agent)
## Systems Manager – Patch Manager

## Run CommandrunAWS-RunBatchBaseline

## EC2 Instances(with SSM Agent)

EC2 Instances(with SSM Agent)
## Systems Manager – Maintenance Windows

## EC2 Instances(with SSM Agent)Maintenance WindowsRun Command

trigger every 24 hourupdate
## Systems Manager - Automation

## AmazonEventBridgeSSM AutomationRunbooks(automation documents)execute automation(AWS-RestartEC2Instance)

## EC2 InstancesAWS Resources

## RDS…execute

AWS ConfigRemediation

---

# Cost Explorer

## Cost Explorer – Monthly Cost by AWS Service

## Cost Explorer– Hourly & Resource Level

## Cost Explorer – Savings PlanAlternative to Reserved Instances

## Cost Explorer – Forecast Usage

# AWS Cost Anomaly Detection

## AWS Outposts

## On-prem serversOutpostsRacks

Extension of AWS services
## AWS Outposts

## AWS Batch

## AWS Batch – Simplified Example

## EC2 Instance

Spot InstanceAmazon S3Insert processed objectAmazon S3

---

# Batch vs Lambda

# Amazon AppFlow

## Amazon AppFlow

## AWS Amplify - web and mobile applications

configure backendusing Amplify CLI

## Amazon S3Amazon CognitoAWS AppSyncAPIGatewayDynamoDBLambdaAmazonSageMakerAmazon Lex

…connect frontend to backendusingAmplify Frontend Libraries……
AmplifyConsoleAmazon CloudFrontbuild using Amplify Console & deploy

---

# Instance Scheduler on AWS

# White Papers & ArchitecturesWell Architected Framework, Disaster Recover y, etc…

# Section Overview

# Well Architected Framework General Guiding Principles

## Well Architected Framework 6 Pillars

# AWS Well-Architected T ool

# Tr usted Advisor

# More Architecture Examples

# Exam Review & Tips

# State of learning checkpoint

# Practice makes perfect

# Proceed by elimination

# Skim the AWS Whitepapers

# Read each service’s FAQ

# Get into the AWS Community

## How will the exam work?

Dive Deep
### Dive Deep

[https://d1.awsstatic.com/training-and-certification/docs/AWS_certification_paths.pdf](https://d1.awsstatic.com/training-and-certification/docs/AWS_certification_paths.pdf) optional for IT/cloud professionalsrecommended for IT/cloudprofessionals to leverage AI
recommended for IT/cloudprofessionals to leverage AIoptional for IT/cloud professionals
Dive Deep
### Dive Deep

optional for IT/cloud professionals
optional for IT/cloud professionals
AWS Certification Paths – DevOpsDevOpsTest EngineerEmbed testing and qualitybest practices for softwaredevelopment from design to release,throughout the product life cycleDevOpsCloud DevOps EngineerDesign, deployment, and operationsof large-scale global hybridcloud computing environment,advocating for end-to-endautomated CI/CD DevOps pipelines
OptionalDive DeepDevOpsDevSecOps EngineerAccelerate enterprise cloud adoptionwhile enabling rapid and stable deliveryof capabilities using CI/CD principles,methodologies, and technologies
optional for IT/cloud professionals
recommended for IT/cloudprofessionals working onAI/ML projectsoptional for IT/cloud professionals
optional for IT/cloud professionalsrecommended for IT/cloudprofessionals working onAI/ML projects
Dive Deep
### Dive Deep

optional for IT/cloud professionalsrecommended for IT/cloudprofessionals to secureAI/ML systems
optional for IT/cloud professionalsrecommended for IT/cloudprofessionals to secureAI/ML systems
recommended for IT/cloudprofessionals to leverage AIoptional for IT/cloud professionalsNetworkingNetwork EngineerDesign and implement computerand information networks, such aslocal area networks (LAN),wide area networks (WAN), intranets, extranets, etc.
### Dive Deep

optional for IT/cloud professionals
### Dive Deep

optional for IT/cloud professionalsrecommended for IT/cloudprofessionals working onAI/ML projectsAI/MLMachine Learning EngineerResearch, build, and design artificialintelligence (AI) systems to automatepredictive models, and design machinelearning systems, models, and schemes
optional for IT/cloud professionalsoptional for AI/MLprofessionals
Dive Deep
AWS Certification Paths – AI/MLAI/MLPrompt EngineerDesign, test, and refine textprompts to optimize theperformance of AI language modelsAI/MLMachine Learning Ops EngineerBuild and maintain AI and ML platformsand infrastructure. Design, implement,and operationally support AI/ML modelactivity and deployment infrastructure
AI/MLData ScientistDevelop and maintain AI/ML modelsto solve business problems. Train andfine tune models and evaluatetheir performance
optional for IT/cloud professionals
optional for IT/cloud professionals
optional for IT/cloud professionals
### Dive Deep

optional for AI/MLprofessionals
optional for AI/MLprofessionals

---

# Congratulations!

## Congratulations!
