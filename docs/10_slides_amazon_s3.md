# Amazon S3 - Content Breakdown

*Extracted from: slides.md*

*Keyword: Amazon S3*

*Matching sections: 1*

*Total pages included: 68*

*Page ranges: 267-334*

---

## Page 267 of 872
*Page 267*

Amazon S3



---



---

## Page 268 of 872
*Page 268*

Section introduction*Amazon S3 is one of the main building blocks of AWS*It's advertised as "infinitely scaling" storage *Many websites use Amazon S3 as a backbone*Many AWS services use Amazon S3 as an integration as well*We'll have a step-by-step approach to S3



---



---

## Page 269 of 872
*Page 269*

Amazon S3 Use cases*Backup and storage*Disaster Recovery*Archive*Hybrid Cloud storage*Application hosting*Media hosting*Data lakes and big data analytics*Software delivery*Static website
Nasdaq stores 7 years of data into S3 GlacierSysco runs analytics on its data and gain business insights



---



---

## Page 270 of 872
*Page 270*

Amazon S3 - Buckets*Amazon S3 allows people to store objects (files) in "buckets" (directories)*Buckets must have a globally unique name (across all regions all accounts)*Buckets are defined at the region level *S3 looks like a global service but buckets are created in a region*Naming convention*No uppercase, No underscore*3-63 characters long*Not an IP*Must start with lowercase letter or number*Must NOT start with the prefix xn--*Must NOT end with the suffix -s3alias
S3 Bucket



---



---

## Page 271 of 872
*Page 271*

Amazon S3 - Objects*Objects (files) have a Key*The key is the FULL path:*s3://my-bucket/my_file.txt*s3://my-bucket/my_folder1/another_folder/my_file.txt*The key is composed of prefix + object name*s3://my-bucket/my_folder1/another_folder/my_file.txt*There's no concept of "directories" within buckets(although the UI will trick you to think otherwise)*Just keys with very long names that contain slashes ("/")
S3 Bucketwith Objects
Object



---



---

## Page 272 of 872
*Page 272*

Amazon S3 - Objects (cont.)*Object values are the content of the body:*Max. Object Size is 5TB (5000GB)*If uploading more than 5GB, must use "multi-part upload"*Metadata (list of text key / value pairs - system or user metadata)*Tags (Unicode key / value pair - up to 10) - useful for security / lifecycle*Version ID (if versioning is enabled)



---



---

## Page 273 of 872
*Page 273*

Amazon S3 - Security*User-Based*IAM Policies - which API calls should be allowed for a specific user from IAM*Resource-Based*Bucket Policies - bucket wide rules from the S3 console - allows cross account*Object Access Control List (ACL) - finer grain (can be disabled)*Bucket Access Control List (ACL) - less common (can be disabled)*Note: an IAM principal can access an S3 object if*The user IAM permissions ALLOW it OR the resource policy ALLOWS it*AND there's no explicit DENY*Encryption: encrypt objects in Amazon S3 using encryption keys



---



---

## Page 274 of 872
*Page 274*

S3 Bucket Policies*JSON based policies*Resources: buckets and objects*Effect: Allow / Deny*Actions: Set of API to Allow or Deny*Principal: The account or user to apply the policy to*Use S3 bucket for policy to:*Grant public access to the bucket*Force objects to be encrypted at upload*Grant access to another account (Cross Account)



---



---

## Page 275 of 872
*Page 275*

Example: Public Access - Use Bucket Policy
S3 Bucket
Anonymous www website visitor
S3 Bucket PolicyAllows Public Access



---



---

## Page 276 of 872
*Page 276*

Example: User Access to S3 - IAM permissions
S3 Bucket
IAM Policy IAM User



---



---

## Page 277 of 872
*Page 277*

Example: EC2 instance access - Use IAM Roles
S3 Bucket
EC2 Instance Role
IAM permissionsEC2 Instance



---



---

## Page 278 of 872
*Page 278*

Advanced: Cross-Account Access - Use Bucket Policy
S3 BucketIAM UserOther AWS account
S3 Bucket PolicyAllows Cross-Account



---



---

## Page 279 of 872
*Page 279*

Bucket settings for Block Public Access
*These settings were created to prevent company data leaks*If you know your bucket should never be public, leave these on*Can be set at the account level



---



---

## Page 280 of 872
*Page 280*

Amazon S3 - Static Website Hosting*S3 can host static websites and have them accessible on the Internet*The website URL will be (depending on the region)*http://bucket-name.s3-website-aws-region.amazonaws.comOR*http://bucket-name.s3-website.aws-region.amazonaws.com*If you get a 403 Forbidden error, make sure the bucket policy allows public reads!
S3 Bucket(demo-bucket)us-west-2
Userhttp://demo-bucket.s3-website-us-west-2.amazonaws.comhttp://demo-bucket.s3-website.us-west-2.amazonaws.com



---



---

## Page 281 of 872
*Page 281*

Amazon S3 - Versioning*Yo u  c a n  ve r s i o n  yo u r  fi l e s  i n  A m a zo n  S 3*It is enabled at the bucket level*Same key overwrite will change the "version": 1, 2, 3....*It is best practice to version your buckets*Protect against unintended deletes (ability to restore a version)*Easy roll back to previous version *Notes:*Any file that is not versioned prior to enabling versioning will have version "null"*Suspending versioning does not delete the previous versions
S3 Bucket(my-bucket)
s3://my-bucket/my-file.docx
User
uploadVersion 1Version 2Version 3



---



---

## Page 282 of 872
*Page 282*

Amazon S3 - Replication (CRR and SRR)*Must enable Versioning in source and destination buckets*Cross-Region Replication (CRR)*Same-Region Replication (SRR)*Buckets can be in different AWS accounts*Copying is asynchronous*Must give proper IAM permissions to S3*Use cases:*CRR - compliance, lower latency access, replication across accounts*SRR - log aggregation, live replication between production and test accounts
S3 Bucket(eu-west-1)
S3 Bucket(us-east-2)asynchronousreplication



---



---

## Page 283 of 872
*Page 283*

Amazon S3 - Replication (Notes)*After you enable Replication, only new objects are replicated*Optionally, you can replicate existing objects using S3 Batch Replication*Replicates existing objects and objects that failed replication*For DELETE operations*Can replicate delete markers from source to target (optional setting)*Deletions with a version ID are not replicated (to avoid malicious deletes)*There is no "chaining" of replication*If bucket 1 has replication into bucket 2, which has replication into bucket 3*Then objects created in bucket 1 are not replicated to bucket 3



---



---

## Page 284 of 872
*Page 284*

S3 Storage Classes*Amazon S3 Standard - General Purpose*Amazon S3 Standard-Infrequent Access (IA)*Amazon S3 One Zone-Infrequent Access*Amazon S3 Glacier Instant Retrieval*Amazon S3 Glacier Flexible Retrieval*Amazon S3 Glacier Deep Archive*Amazon S3 Intelligent Tiering*Can move between classes manually or using S3 Lifecycle configurations



---



---

## Page 285 of 872
*Page 285*

S3 Durability and Availability*Durability:*High durability (99.999999999%, 11 9's) of objects across multiple AZ*If you store 10,000,000 objects with Amazon S3, you can on average expect to incur a loss of a single object once every 10,000 years*Same for all storage classes*Availability:*Measures how readily available a service is*Varies depending on storage class*Example: S3 standard has 99.99% availability = not available 53 minutes a year



---



---

## Page 286 of 872
*Page 286*

S3 Standard - General Purpose*99.99% Availability*Used for frequently accessed data*Low latency and high throughput*Sustain 2 concurrent facility failures*Use Cases: Big Data analytics, mobile and gaming applications, content distribution...



---



---

## Page 287 of 872
*Page 287*

S3 Storage Classes - Infrequent Access*For data that is less frequently accessed, but requires rapid access when needed*Lower cost than S3 Standard*Amazon S3 Standard-Infrequent Access (S3 Standard-IA)*99.9% Availability*Use cases: Disaster Recovery, backups*Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)*High durability (99.999999999%) in a single AZ; data lost when AZ is destroyed*99.5% Availability*Use Cases: Storing secondary backup copies of on-premises data, or data you can recreate



---



---

## Page 288 of 872
*Page 288*

Amazon S3 Glacier Storage Classes*Low-cost object storage meant for archiving / backup*Pricing: price for storage + object retrieval cost*Amazon S3 Glacier Instant Retrieval*Millisecond retrieval, great for data accessed once a quarter*Minimum storage duration of 90 days*Amazon S3 Glacier Flexible Retrieval (formerly Amazon S3 Glacier):*Expedited (1 to 5 minutes), Standard (3 to 5 hours), Bulk (5 to 12 hours) - free*Minimum storage duration of 90 days*Amazon S3 Glacier Deep Archive - for long term storage:*Standard (12 hours), Bulk (48 hours)*Minimum storage duration of 180 days



---



---

## Page 289 of 872
*Page 289*

S3 Intelligent-Tiering*Small monthly monitoring and auto-tiering fee*Moves objects automatically between Access Tiers based on usage*There are no retrieval charges in S3 Intelligent-Tiering*Frequent Access tier (automatic): default tier*Infrequent Access tier (automatic): objects not accessed for 30 days*Archive Instant Access tier (automatic): objects not accessed for 90 days*Archive Access tier (optional): configurable from 90 days to 700+ days*Deep Archive Access tier (optional): config. from 180 days to 700+ days



---



---

## Page 290 of 872
*Page 290*

S3 Storage Classes Comparison
https://aws.amazon.com/s3/storage-classes/StandardIntelligent-TieringStandard-IAOne Zone-IAGlacier Instant RetrievalGlacier Flexible RetrievalGlacier Deep ArchiveDurability99.999999999% == (11 9's)Availability99.99%99.9%99.9%99.5%99.9%99.99%99.99%Availability SLA99.9%99%99%99%99%99.9%99.9%Availability Zones>= 3>= 3>= 31>= 3>= 3>= 3Min. Storage Duration ChargeNoneNone30 Days30 Days90 Days90 Days180 DaysMin. Billable Object SizeNoneNone128 KB128 KB128 KB40 KB40 KBRetrieval FeeNoneNonePer GB retrievedPer GB retrievedPer GB retrievedPer GB retrievedPer GB retrieved



---



---

## Page 291 of 872
*Page 291*

S3 Storage Classes - Price ComparisonExample: us-east-1
https://aws.amazon.com/s3/pricing/StandardIntelligent-TieringStandard-IAOne Zone-IAGlacier Instant RetrievalGlacier Flexible RetrievalGlacier Deep ArchiveStorage Cost(per GB per month)$0.023$0.0025 - $0.023$0.0125$0.01$0.004$0.0036$0.00099Retrieval Cost(per 1000 request)GET: $0.0004POST: $0.005GET: $0.0004POST: $0.005GET: $0.001POST: $0.01GET: $0.001POST: $0.01GET: $0.01POST: $0.02GET: $0.0004POST: $0.03Expedited: $10Standard: $0.05Bulk: freeGET: $0.0004POST: $0.05Standard: $0.10Bulk: $0.025Retrieval TimeInstantaneousExpedited (1 - 5 mins)Standard (3 - 5 hours)Bulk (5 - 12 hours)Standard (12 hours)Bulk (48 hours)Monitoring Cost (per 1000 objects)$0.0025



---



---

## Page 292 of 872
*Page 292*

S3 Express One Zone*High performance, single Availability Zone storage class*Objects stored in a Directory Bucket (bucket in a single AZ)*Handle 100,000s requests per second with single-digit millisecond latency*Up to 10x better performance than S3 Standard (50% lower costs)*High Durability (99.999999999%) and Availability (99.95%)*Co-locate your storage and compute resources in the same AZ (reduces latency)*Use cases: latency-sensitive apps, data-intensive apps, AI and ML training, financial modeling, media processing, HPC...*Best integrated with SageMaker Model Training, Athena, EMR, Glue...
stephane--use1-az4--x-s3Region (us-east-1)
Availability Zone (AZ 4)



---



---

## Page 293 of 872
*Page 293*

Amazon S3 - Advanced



---



---

## Page 294 of 872
*Page 294*

Amazon S3 - Moving between Storage Classes*Yo u  c a n  t r a n s i t i o n  o b j e c t s  b e t we e n  storage classes *For infrequently accessed object, move them to Standard IA*For archive objects that you don't need fast access to, move them to Glacier or Glacier Deep Archive*Moving objects can be automated using a Lifecycle Rules
StandardStandard IA
Intelligent TieringOne-Zone IA
Glacier Instant RetrievalGlacier Flexible Retrieval
Glacier Deep Archive



---



---

## Page 295 of 872
*Page 295*

Amazon S3 - Lifecycle Rules*Transition Actions - configure objects to transition to another storage class*Move objects to Standard IA class 60 days after creation*Move to Glacier for archiving after 6 months*Expiration actions - configure objects to expire (delete) after some time*Access log files can be set to delete after a 365 days*Can be used to delete old versions of files (if versioning is enabled)*Can be used to delete incomplete Multi-Part uploads*Rules can be created for a certain prefix (example: s3://mybucket/mp3/*)*Rules can be created for certain objects Tags (example: Department: Finance)



---



---

## Page 296 of 872
*Page 296*

Amazon S3 - Lifecycle Rules (Scenario 1)*Yo u r  a p p l i c a t i o n  o n  E C 2 c r e a t e s  i m a g e s  t h u m b n a i l s  a f t e r  p r o fi l e  photos are uploaded to Amazon S3. These thumbnails can be easily recreated, and only need to be kept for 60 days. The source images should be able to be immediately retrieved for these 60 days, and afterwards, the user can wait up to 6 hours. How would you design this?*S3 source images can be on Standard, with a lifecycle configuration to transition them to Glacier after 60 days*S3 thumbnails can be on One-Zone IA, with a lifecycle configuration to expire them (delete them) after 60 days



---



---

## Page 297 of 872
*Page 297*

Amazon S3 - Lifecycle Rules (Scenario 2)*A rule in your company states that you should be able to recover your deleted S3 objects immediately for 30 days, although this may happen rarely. After this time, and for up to 365 days, deleted objects should be recoverable within 48 hours.*Enable S3 Versioning in order to have object versions, so that "deleted objects" are in fact hidden by a "delete marker" and can be recovered*Transition the "noncurrent ver sions" of the object to Standard IA*Transition afterwards the "noncurrent ver sions" to Glacier Deep Archive



---



---

## Page 298 of 872
*Page 298*

Amazon S3 Analytics - Storage Class Analysis*Help you decide when to transition objects to the right storage class*Recommendations for Standard and Standard IA*Does NOT work for One-Zone IA or Glacier*Report is updated daily*24 to 48 hours to start seeing data analysis*Good first step to put together Lifecycle Rules (or improve them)!
S3 BucketS3 AnalyticsDateStorageClassObjectAge8/22/2022STANDARD000-0148/25/2022STANDARD030-0449/6/2022STANDARD120-149.csv report



---



---

## Page 299 of 872
*Page 299*

S3 - Requester Pays*In general, bucket owners pay for all Amazon S3 storage and data transfer costs associated with their bucket*With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket*Helpful when you want to share large datasets with other accounts*The requester must be authenticated in AWS (cannot be anonymous)
Owner$$ Storage Cost
Owner$$ Networking Cost
downloadRequester
Owner$$ Storage CostRequester$$ Networking Cost
download
Requester Pays BucketStandard Bucket



---



---

## Page 300 of 872
*Page 300*

S3 Event Notifications
Amazon S3events
Lambda Function
SQS
SNS*S3:ObjectCreated, S3:ObjectRemoved, S3:ObjectRestore, S3:Replication...*Object name filtering possible (*.jpg)*Use case: generate thumbnails of images uploaded to S3*Can create as many "S3 events" as desired*S3 event notifications typically deliver events in seconds but can sometimes take a minute or longer



---



---

## Page 301 of 872
*Page 301*

S3 Event Notifications - IAM Permissions
Amazon S3events
Lambda Function
SQS
SNS
Lambda Resource Policy
SNS Resource (Access) Policy
SQS Resource (Access) Policy



---



---

## Page 302 of 872
*Page 302*

S3 Event Notifications with Amazon EventBridge
Amazon S3bucketeventsAll events
AmazonEventBridgerulesOver 18 AWS servicesas destinations*Advanced filtering options with JSON rules (metadata, object size, name...)*Multiple Destinations - ex Step Functions, Kinesis Streams / Firehose...*EventBridge Capabilities - Archive, Replay Events, Reliable delivery



---



---

## Page 303 of 872
*Page 303*

S3 - Baseline Performance*Amazon S3 automatically scales to high request rates, latency 100-200 ms*Yo u r  a p p l i c a t i o n  c a n  a c h i e ve  a t  l e a s t  3,500 PUT/COPY/POST/DELETE or 5,500 GET/HEAD requests per second per prefix in a bucket. *There are no limits to the number of prefixes in a bucket. *Example (object path => prefix):*bucket/folder1/sub1/file  => /folder1/sub1/*bucket/folder1/sub2/file  => /folder1/sub2/*bucket/1/file                  => /1/*bucket/2/file                  => /2/*If you spread reads across all four prefixes evenly, you can achieve 22,000 requests per second for GET and HEAD



---



---

## Page 304 of 872
*Page 304*

S3 Performance*Multi-Part upload: *recommended for files > 100MB, must use for files > 5GB*Can help parallelize uploads (speed up transfers)*S3 Transfer Acceleration *Increase transfer speed by transferring file to an AWS edge location which will forward the data to the S3 bucket in the target region*Compatible with multi-part upload
Amazon S3Parallel uploads
DivideIn partsBIG file
S3 BucketAustralia
Edge LocationUSA
Fast (public www)Fast (private AWS)File in USA



---



---

## Page 305 of 872
*Page 305*

S3 Performance - S3 Byte-Range Fetches*Parallelize GETs by requesting specific byte ranges*Better resilience in case of failuresCan be used to speed up downloadsFile in S3Byte-range request for header(first XX bytes)headerFile in S3Part 1Part 2Part N...Can be used to retrieve only partial data (for example the head of a file)
Requests in parallel



---



---

## Page 306 of 872
*Page 306*

S3 Batch Operations*Perform bulk operations on existing S3 objects with a single request, example:*Modify object metadata and properties*Copy objects between S3 buckets*Encrypt un-encrypted objects*Modify ACLs, tags*Restore objects from S3 Glacier*Invoke Lambda function to perform custom action on each object*A job consists of a list of objects, the action to perform, and optional parameters*S3 Batch Operations manages retries, tracks progress, sends completion notifications, generate reports ...*Yo u  c a n  u s e  S 3  I nve n t o r y  t o  g e t  o b j e c t  l i s t  a n d  u s e  Athena to query and filter your objectsS3 InventoryObjects List Report
filtered list
filterS3 Batch Operations
operation+parametersUser
Processed Objects
...
Athena



---



---

## Page 307 of 872
*Page 307*

S3 - Storage Lens*Understand, analyze, and optimize storage across entire AWS Organization*Discover anomalies, identify cost efficiencies, and apply data protection best practices across entire AWS Organization (30 days usage and activity metrics)*Aggregate data for Organization, specific accounts, regions, buckets, or prefixes*Default dashboard or create your own dashboards*Can be configured to export metrics daily to an S3 bucket (CSV, Parquet)
S3 Storage LensOrganizationAccountsRegionsBucketsAggregateAnalyze(Dashboard)Summary InsightsData ProtectionCost EfficiencyConfigureOptimize



---



---

## Page 308 of 872
*Page 308*

Storage Lens - Default Dashboard*Visualize summarized insights and trends for both free and advanced metrics*Default dashboard shows Multi-Region and Multi-Account data*Preconfigured by Amazon S3*Can't be deleted, but can be disabled
https://aws.amazon.com/blogs/aws/s3-storage-lens/https://aws.amazon.com/blogs/aws/s3-storage-lens/



---



---

## Page 309 of 872
*Page 309*

Storage Lens - Metrics*Summary Metrics*General insights about your S3 storage*StorageBytes, ObjectCount...*Use cases: identify the fastest-growing (or not used) buckets and prefixes*Cost-Optimization Metrics*Provide insights to manage and optimize your storage costs*NonCurrentVersionStorageBytes, IncompleteMultipartUploadStorageBytes...*Use cases: identify buckets with incomplete multipart uploaded older than 7 days, Identify which objects could be transitioned to lower-cost storage class



---



---

## Page 310 of 872
*Page 310*

Storage Lens - Metrics*Data-Protection Metrics*Provide insights for data protection features*VersioningEnabledBucketCount, MFADeleteEnabledBucketCount, SSEKMSEnabledBucketCount, CrossRegionReplicationRuleCount...*Use cases: identify buckets that aren't following data-protection best practices*Access-management Metrics*Provide insights for S3 Object Ownership*ObjectOwnershipBucketOwnerEnforcedBucketCount...*Use cases: identify which Object Ownership settings your buckets use*Event Metrics*Provide insights for S3 Event Notifications*EventNotificationEnabledBucketCount (identify which buckets have S3 Event Notifications configured)



---



---

## Page 311 of 872
*Page 311*

Storage Lens - Metrics*Performance Metrics*Provide insights for S3 Transfer Acceleration*TransferAccelerationEnabledBucketCount (identify which buckets have S3 Transfer Acceleration enabled)*Activity Metrics*Provide insights about how your storage is requested*AllRequests, GetRequests, PutRequests, ListRequests, BytesDownloaded...*Detailed Status Code Metrics*Provide insights for HTTP status codes*200OKStatusCount, 403ForbiddenErrorCount, 404NotFoundErrorCount...



---



---

## Page 312 of 872
*Page 312*

Storage Lens - Free vs. Paid*Free Metrics*Automatically available for all customers*Contains around 28 usage metrics*Data is available for queries for 14 days*Advanced Metrics and Recommendations*Additional paid metrics and features*Advanced Metrics - Activity, Advanced Cost Optimization, Advanced Data Protection, Status Code*CloudWatch Publishing - Access metrics in CloudWatch without additional charges*Prefix Aggregation - Collect metrics at the prefix level*Data is available for queries for 15 months



---



---

## Page 313 of 872
*Page 313*

Amazon S3 - Security



---



---

## Page 314 of 872
*Page 314*

Amazon S3 - Object Encryption*Y ou can encrypt objects in S3 buckets using one of 4 methods*Server-Side Encryption (SSE)*Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) -Enabled by Default*Encrypts S3 objects using keys handled, managed, and owned by AWS*Server-Side Encryption with KMS Keys stored in AWS KMS (SSE-KMS)*Leverage AWS Key Management Service (AWS KMS) to manage encryption keys*Server-Side Encryption with Customer-Provided Keys (SSE-C)*When you want to manage your own encryption keys*Client-Side Encryption *It's important to understand which ones are for which situation for the exam



---



---

## Page 315 of 872
*Page 315*

Amazon S3 Encryption - SSE-S3*Encryption using keys handled, managed, and owned by AWS*Object is encrypted server-side*Encryption type is AES-256*Must set header "x-amz-server-side-encryption": "AES256"*Enabled by default for new buckets and new objectsAmazon S3
User
uploadHTTP(S) + Header
S3 Bucket
+ObjectS3 Owned KeyEncryption



---



---

## Page 316 of 872
*Page 316*

Amazon S3 Encryption - SSE-KMS*Encryption using keys handled and managed by AWS KMS (Key Management Service)*KMS advantages: user control + audit key usage using CloudTrail*Object is encrypted server side*Must set header "x-amz-server-side-encryption": "aws:kms"Amazon S3
User
uploadHTTP(S) + Header
S3 Bucket
+ObjectKMS Key
AWS KMSEncryption



---



---

## Page 317 of 872
*Page 317*

SSE-KMS Limitation*If you use SSE-KMS, you may be impacted by the KMS limits *When you upload, it calls the GenerateDataKey KMS API*When you download, it calls the Decrypt KMS API*Count towards the KMS quota per second (5500, 10000, 30000 req/s based on region)*Yo u  c a n  r e q u e s t  a  q u o t a  i n c r e a s e  u s i n g  t h e  Service Quotas Console
KMS KeyS3 Bucket
UsersUpload / downloadSSE-KMSAPI call



---



---

## Page 318 of 872
*Page 318*

Amazon S3 Encryption - SSE-C*Server-Side Encryption using keys fully managed by the customer outside of AWS*Amazon S3 does NOT store the encryption key you provide*HTTPS must be used*Encryption key must provided in HTTP headers, for every HTTP request madeAmazon S3
User
uploadHTTPS ONLY+ Key in Header
S3 Bucket
+Object
Client-Provided Key
+Encryption



---



---

## Page 319 of 872
*Page 319*

Amazon S3 Encryption - Client-Side Encryption
Amazon S3
S3 Bucket*Use client libraries such as Amazon S3 Client-Side Encryption Library*Clients must encrypt data themselves before sending to Amazon S3*Clients must decrypt data themselves when retrieving from Amazon S3*Customer fully manages the keys and encryption cycle+File
Client Key
File(encrypted)uploadHTTP(S)Encryption



---



---

## Page 320 of 872
*Page 320*

Amazon S3 - Encryption in transit (SSL/TLS)*Encryption in flight is also called SSL/TLS *Amazon S3 exposes two endpoints:*HTTP Endpoint - non encrypted*HTTPS Endpoint - encryption in flight*HTTPS is recommended*HTTPS is mandatory for SSE-C*Most clients would use the HTTPS endpoint by default



---



---

## Page 321 of 872
*Page 321*

Amazon S3 - Force Encryption in Transitaws:SecureTransport
Account B
S3 Bucket(my-bucket)
Bucket Policy
User
User
httphttps



---



---

## Page 322 of 872
*Page 322*

Amazon S3 - Default Encryption vs. Bucket Policies*SSE-S3 encryption is automatically applied to new objects stored in S3 bucket*Optionally, you can "force encryption" using a bucket policy and refuse any API call to PUT an S3 object without encryption headers (SSE-KMS or SSE-C)
*Note: Bucket Policies are evaluated before "Default Encryption"



---



---

## Page 323 of 872
*Page 323*

What is CORS?*Cross-Origin Resource Sharing (CORS)*Origin = scheme (protocol) + host (domain) + port*example: https://www.example.com (implied port is 443 for HTTPS, 80 for HTTP)*Web Browser based mechanism to allow requests to other origins while visiting the main origin*Same origin: http://example.com/app1 and http://example.com/app2 *Different origins: http://www.example.com and http://other.example.com *The requests won't be fulfilled unless the other origin allows for the requests, using CORS Headers (example: Access-Control-Allow-Origin)



---



---

## Page 324 of 872
*Page 324*

What is CORS?
Web Server(Origin)https://www.example.com
Web Server(Cross-Origin)https://www.other.com
Web BrowserHTTPS RequestOPTIONS /Host: www.other.comOrigin: https://www.example.comPreflight RequestAccess-Control-Allow-Origin: https://www.example.comAccess-Control-Allow-Methods: GET, PUT, DELETEPreflight ResponseGET /Host: www.other.comOrigin: https://www.example.comCORS Headers received already by the OriginThe Web Browser can make requests



---



---

## Page 325 of 872
*Page 325*

Amazon S3 - CORS *If a client makes a cross-origin request on our S3 bucket, we need to enable the correct CORS headers*It's a popular exam question*Yo u  c a n  a l l ow  fo r  a  s p e c i fi c  o r i g i n  o r  fo r  *  ( a l l  o r i g i n s )
Web Browser
S3 Bucket(my-bucket-html)(Static Website Enabled)
S3 Bucket(my-bucket-assets)(Static Website Enabled)GET /index.htmlHost: http://my-bucket-html.s3-website.us-west-2.amazonaws.com
index.htmlGET /images/coffee.jpgHost: http://my-bucket-assets.s3-website.us-west-2.amazonaws.comOrigin: http://my-bucket-html.s3-website.us-west-2.amazonaws.comAccess-Control-Allow-Origin: http://my-bucket-html.s3-website.us-west-2.amazonaws.com



---



---

## Page 326 of 872
*Page 326*

Amazon S3 - MFA Delete*MFA (Multi-Factor Authentication) - force users to generate a code on a device (usually a mobile phone or hardware) before doing important operations on S3*MFA will be required to:*Permanently delete an object version*Suspend Versioning on the bucket*MFA won't be required to:*Enable Versioning*List deleted versions*To  u s e  M FA  D e l e t e , Versioning must be enabled on the bucket*Only the bucket owner (root account) can enable/disable MFA Delete
Google Authenticator
MFA Hardware Device



---



---

## Page 327 of 872
*Page 327*

S3 Access Logs*For audit purpose, you may want to log all access to S3 buckets*Any request made to S3, from any account, authorized or denied, will be logged into another S3 bucket*That data can be analyzed using data analysis tools...*The target logging bucket must be in the same AWS region*The log format is at: https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html My-bucket
Logging Bucketrequests
Log all requests



---



---

## Page 328 of 872
*Page 328*

S3 Access Logs: Warning*Do not set your logging bucket to be the monitored bucket*It will create a logging loop, and your bucket will grow exponentially
App Bucket andLogging BucketLogging loop
PutObjectDo not try this at home J



---



---

## Page 329 of 872
*Page 329*

Amazon S3 - Pre-Signed URLs*Generate pre-signed URLs using the S3 Console, AWS CLI or SDK*URL Expiration*S3 Console - 1 min up to 720 mins (12 hours)*AWS CLI - configure expiration with --expires-in parameter in seconds (default 3600 secs, max. 604800 secs ~ 168 hours)*Users given a pre-signed URL inherit the permissions of the user that generated the URL for GET / PUT*Examples: *Allow only logged-in users to download a premium video from your S3 bucket*Allow an ever-changing list of users to download files by generating URLs dynamically*Allow temporarily a user to upload a file to a precise location in your S3 bucket
S3 Bucket(Private)
Owner
Usergeneratepre-signed URL
URL
URL
URL



---



---

## Page 330 of 872
*Page 330*

S3 Glacier Vault Lock*Adopt a WORM (Write Once Read Many) model*Create a Vault Lock Policy*Lock the policy for future edits (can no longer be changed or deleted)*Helpful for compliance and data retention
ObjectVault Lock PolicyObject can't be deleted



---



---

## Page 331 of 872
*Page 331*

S3 Object Lock (versioning must be enabled)*Adopt a WORM (Write Once Read Many) model*Block an object version deletion for a specified amount of time*Retention mode - Compliance:*Object versions can't be overwritten or deleted by any user, including the root user*Objects retention modes can't be changed, and retention periods can't be shortened*Retention mode - Governance: *Most users can't overwrite or delete an object version or alter its lock settings *Some users have special permissions to change the retention or delete the object*Retention Period: protect the object for a fixed period, it can be extended *Legal Hold: *protect the object indefinitely, independent from retention period*can be freely placed and removed using the s3:PutObjectLegalHold IAM permission



---



---

## Page 332 of 872
*Page 332*

S3 - Access Points
S3 Bucket
/finance/...
/sales/...
Simple BucketPolicy
FinanceAccess Point
SalesAccess Point
AnalyticsAccess Point
PolicyGrant R/W to/finance prefix
PolicyGrant R/W to/sales prefix
PolicyGrant R toentire bucket
Users(Finance)Users(Sales)Users(Analytics)*Access Points simplify security management for S3 Buckets*Each Access Point has:*its own DNS name (Internet Origin or VPC Origin)*an access point policy (similar to bucket policy) - manage security at scale



---



---

## Page 333 of 872
*Page 333*

S3 - Access Points - VPC Origin*We can define the access point to be accessible only from within the VPC*You  mu st  cr ea t e a  VPC  Endpoint to access the Access Point (Gateway or Interface Endpoint)*The VPC Endpoint Policy must allow access to the target bucket and Access Point
S3 Bucket
EC2 InstanceAccess PointVPC Origin
VPC Endpoint
VPC
Endpoint PolicyAccess Point PolicyBucketPolicy



---



---

## Page 334 of 872
*Page 334*

S3 Object Lambda*Use AWS Lambda Functions to change the object before it is retrieved by the caller application*Only one S3 bucket is needed, on top of which we create S3 Access Point and S3 Object Lambda Access Points. *Use Cases:*Redacting personally identifiable information for analytics or non-production environments.*Converting across data formats, such as converting XML to JSON.*Resizing and watermarking images on the fly using caller-specific details, such as the user who requested the object.AWS Cloud
E-CommerceApplication
AnalyticsApplication
MarketingApplication
S3 BucketSupportingS3 Access Point
Customer LoyaltyDatabaseRedactingLambda FunctionEnrichingLambda FunctionS3 Object LambdaAccess PointS3 Object LambdaAccess PointOriginalObjectRedactedObjectEnrichedObject



---

