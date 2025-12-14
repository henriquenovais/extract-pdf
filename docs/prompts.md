 "find_matching_sections" function needs improvement to find sections that contains similar names.

 @10_slides_amazon_s3.md was generated through running  with  as input file.

PROBLEM: sections 'Amazon S3 - Advanced' and 'Amazon S3 - Security' clearly exist within @10_slides_amazon_s3.md but they were ignored by the algorithm.



Here are the last script logs:

```
(.venv) burricolpj@pop-os:~/Documents/GitHub/extract-pdf$ python3 file-slicer.py slides.md -kf keywords.txt -o output/
Detected file format: markdown → output format: markdown
Loaded 31 keyword(s): Getting Started with AWS, AWS Identity and Access Management (AWS IAM), Amazon EC2 - Basics, Amazon EC2 - Associate, Amazon EC2 - Instance Storage, High Availability and Scalability, RDS, Aurora and ElastiCache, Amazon Route 53, Classic Solutions Architecture, Amazon S3, Amazon S3 - Advanced, Amazon S3 - Security, CloudFront and Global Accelerator, AWS Storage Extras, AWS Integration and Messaging, Containers on AWS, Serverless Overview, Serverless Architectures, Databases in AWS, Data and Analytics, Machine Learning, AWS Monitoring, Audit and Performance, Advanced Identity in AWS, AWS Security and Encryption, Amazon VPC, Disaster Recovery and Migrations, More Solutions Architecture, Other Services, White Papers and Architectures, Exam Preparation, Congratulations
Reading input file 'slides.md'...
Normalizing raw content...
Parsing content into pages ...
Total pages is 872
Found 872 pages.
Searching for keyword matches (case-insensitive)...
Analyzing 873 pages for keyword matches...
Keywords: Getting Started with AWS, AWS Identity and Access Management (AWS IAM), Amazon EC2 - Basics, Amazon EC2 - Associate, Amazon EC2 - Instance Storage, High Availability and Scalability, RDS, Aurora and ElastiCache, Amazon Route 53, Classic Solutions Architecture, Amazon S3, Amazon S3 - Advanced, Amazon S3 - Security, CloudFront and Global Accelerator, AWS Storage Extras, AWS Integration and Messaging, Containers on AWS, Serverless Overview, Serverless Architectures, Databases in AWS, Data and Analytics, Machine Learning, AWS Monitoring, Audit and Performance, Advanced Identity in AWS, AWS Security and Encryption, Amazon VPC, Disaster Recovery and Migrations, More Solutions Architecture, Other Services, White Papers and Architectures, Exam Preparation, Congratulations
  Page 2: REJECTED 'Exam Preparation' (too much extra content: 'disclaimertheseslide...')
  Page 3: MULTIPLE keywords found: Getting Started with AWS, AWS Identity and Access Management (AWS IAM), Amazon EC2 - Basics, Amazon EC2 - Associate, Amazon EC2 - Instance Storage, High Availability and Scalability, RDS, Aurora and ElastiCache, Amazon Route 53, Classic Solutions Architecture, Amazon S3
  Page 4: MULTIPLE keywords found: Amazon S3, Amazon S3 - Advanced, Amazon S3 - Security, CloudFront and Global Accelerator, AWS Storage Extras, AWS Integration and Messaging, Containers on AWS, Serverless Overview, Serverless Architectures, Databases in AWS, Data and Analytics
  Page 5: MULTIPLE keywords found: Machine Learning, AWS Monitoring, Audit and Performance, Advanced Identity in AWS, AWS Security and Encryption, Amazon VPC, Disaster Recovery and Migrations, More Solutions Architecture, Other Services, White Papers and Architectures, Exam Preparation, Congratulations
  Page 14: MATCH for 'Getting Started with AWS'
  Page 24: MATCH for 'AWS Identity and Access Management (AWS IAM)'
  Page 41: MATCH for 'Amazon EC2 - Basics'
  Page 48: REJECTED 'Machine Learning' (too much extra content: 'ec2instancetypescomp...')
  Page 78: MATCH for 'Amazon EC2 - Associate'
  Page 93: MATCH for 'Amazon EC2 - Instance Storage'
  Page 118: MATCH for 'High Availability and Scalability'
  Page 123: REJECTED 'High Availability and Scalability' (too much extra content: 'forec2verticalscalin...')
  Page 160: MATCH for 'RDS, Aurora and ElastiCache'
  Page 178: REJECTED 'Machine Learning' (too much extra content: 'auroraenablesyoutoad...')
  Page 182: REJECTED 'Amazon S3' (too much extra content: 'rdsandaurorarestoreo...')
  Page 193: MATCH for 'Amazon Route 53'
  Page 195: REJECTED 'Amazon Route 53' (too much extra content: 'dnsterminologieshttp...')
  Page 197: REJECTED 'Amazon Route 53' (too much extra content: 'ahighlyavailablescal...')
  Page 210: REJECTED 'Amazon Route 53' (too much extra content: 'route53healthchecksh...')
  Page 212: REJECTED 'Amazon Route 53' (too much extra content: 'route53calculatedhea...')
  Page 223: REJECTED 'Amazon Route 53' (too much extra content: '3rdpartyregistrarwit...')
  Page 227: MATCH for 'Classic Solutions Architecture'
  Page 267: MATCH for 'Amazon S3'
  Page 268: REJECTED 'Amazon S3' (too much extra content: 'sectionintroductioni...')
  Page 269: REJECTED 'Amazon S3' (too much extra content: 'usecasesbackupandsto...')
  Page 270: REJECTED 'Amazon S3' (too much extra content: 'bucketsallowspeoplet...')
  Page 271: REJECTED 'Amazon S3' (too much extra content: 'objectsobjectsfilesh...')
  Page 272: REJECTED 'Amazon S3' (too much extra content: 'objectscontobjectval...')
  Page 273: MULTIPLE keywords found: Amazon S3, Amazon S3 - Security
  Page 280: REJECTED 'Amazon S3' (too much extra content: 'staticwebsitehosting...')
  Page 281: REJECTED 'Amazon S3' (too much extra content: 'versioningyoucanvers...')
  Page 282: REJECTED 'Amazon S3' (too much extra content: 'replicationcrrandsrr...')
  Page 283: REJECTED 'Amazon S3' (too much extra content: 'replicationnotesafte...')
  Page 284: REJECTED 'Amazon S3' (too much extra content: 's3storageclassesstan...')
  Page 285: REJECTED 'Amazon S3' (too much extra content: 's3durabilityandavail...')
  Page 287: REJECTED 'Amazon S3' (too much extra content: 's3storageclassesinfr...')
  Page 288: REJECTED 'Amazon S3' (too much extra content: 'glacierstorageclasse...')
  Page 293: MULTIPLE keywords found: Amazon S3, Amazon S3 - Advanced
  Page 294: REJECTED 'Amazon S3' (too much extra content: 'movingbetweenstorage...')
  Page 295: REJECTED 'Amazon S3' (too much extra content: 'lifecyclerulestransi...')
  Page 296: REJECTED 'Amazon S3' (too much extra content: 'lifecyclerulesscenar...')
  Page 297: REJECTED 'Amazon S3' (too much extra content: 'lifecyclerulesscenar...')
  Page 298: REJECTED 'Amazon S3' (too much extra content: 'analyticsstorageclas...')
  Page 299: REJECTED 'Amazon S3' (too much extra content: 's3requesterpaysingen...')
  Page 300: REJECTED 'Amazon S3' (too much extra content: 's3eventnotifications...')
  Page 301: REJECTED 'Amazon S3' (too much extra content: 's3eventnotifications...')
  Page 302: REJECTED 'Amazon S3' (too much extra content: 's3eventnotifications...')
  Page 303: REJECTED 'Amazon S3' (too much extra content: 's3baselineperformanc...')
  Page 304: REJECTED 'Amazon S3' (too much extra content: 's3performancemultipa...')
  Page 308: REJECTED 'Amazon S3' (too much extra content: 'storagelensdefaultda...')
  Page 313: MULTIPLE keywords found: Amazon S3, Amazon S3 - Security
  Page 314: REJECTED 'Amazon S3' (too much extra content: 'objectencryptionyouc...')
  Page 315: REJECTED 'Amazon S3' (too much extra content: 'encryptionsses3encry...')
  Page 316: REJECTED 'Amazon S3' (too much extra content: 'encryptionssekmsencr...')
  Page 318: REJECTED 'Amazon S3' (too much extra content: 'encryptionssecserver...')
  Page 319: REJECTED 'Amazon S3' (too much extra content: 'encryptionclientside...')
  Page 320: REJECTED 'Amazon S3' (too much extra content: 'encryptionintransits...')
  Page 321: REJECTED 'Amazon S3' (too much extra content: 'forceencryptionintra...')
  Page 322: REJECTED 'Amazon S3' (too much extra content: 'defaultencryptionvsb...')
  Page 325: REJECTED 'Amazon S3' (too much extra content: 'corsifaclientmakesac...')
  Page 326: REJECTED 'Amazon S3' (too much extra content: 'mfadeletemfamultifac...')
  Page 329: REJECTED 'Amazon S3' (too much extra content: 'presignedurlsgenerat...')
  Page 335: MATCH for 'CloudFront and Global Accelerator'
  Page 353: MATCH for 'AWS Storage Extras'
  Page 356: REJECTED 'Amazon S3' (too much extra content: 'diagramsdirectupload...')
  Page 357: REJECTED 'Machine Learning' (too much extra content: 'whatisedgecomputingp...')
  Page 358: REJECTED 'Amazon S3' (too much extra content: 'solutionarchitecture...')
  Page 361: REJECTED 'Machine Learning' (too much extra content: 'amazonfsxforlustrelu...')
  Page 366: REJECTED 'Amazon S3' (too much extra content: 'awsstoragecloudnativ...')
  Page 368: REJECTED 'Amazon S3' (too much extra content: 'filegatewayconfigure...')
  Page 370: REJECTED 'Amazon S3' (too much extra content: 'tapegatewaysomecompa...')
  Page 371: REJECTED 'Amazon S3' (too much extra content: 'awsstoragegatewayonp...')
  Page 372: REJECTED 'Amazon S3' (too much extra content: 'awstransferfamilyafu...')
  Page 373: REJECTED 'Amazon S3' (too much extra content: 'awstransferfamilyaws...')
  Page 374: REJECTED 'Amazon S3' (too much extra content: 'awsdatasyncmovelarge...')
  Page 376: REJECTED 'Amazon S3' (too much extra content: 'awsdatasynctransferb...')
  Page 377: REJECTED 'Amazon S3' (too much extra content: 'storagecomparisons3o...')
  Page 378: REJECTED 'AWS Integration and Messaging' (too much extra content: 'sqssnsandkinesis...')
  Page 388: REJECTED 'Other Services' (too much extra content: 'amazonsqssecurityenc...')
  Page 401: REJECTED 'Other Services' (too much extra content: 'amazonsnssecurityenc...')
  Page 403: REJECTED 'Amazon S3' (too much extra content: 'applications3eventst...')
  Page 404: REJECTED 'Amazon S3' (too much extra content: 'applicationsnstothro...')
  Page 411: REJECTED 'Amazon S3' (too much extra content: 'amazondatafirehoseaw...')
  Page 412: REJECTED 'Amazon S3' (too much extra content: 'amazondatafirehoseno...')
  Page 417: MATCH for 'Containers on AWS'
  Page 424: REJECTED 'Containers on AWS' (too much extra content: 'amazonecsec2launchty...')
  Page 425: REJECTED 'Containers on AWS' (too much extra content: 'amazonecsfargatelaun...')
  Page 428: REJECTED 'Amazon S3' (too much extra content: 'amazonecsdatavolumes...')
  Page 433: REJECTED 'Amazon S3' (too much extra content: 'ecstasksinvokedbyeve...')
  Page 436: REJECTED 'Amazon S3' (too much extra content: 'amazonecrecrelasticc...')
  Page 444: MATCH for 'Serverless Overview'
  Page 446: REJECTED 'Amazon S3' (too much extra content: 'serverlessinawsawsla...')
  Page 479: REJECTED 'Amazon S3' (too much extra content: 'dynamodbstreamsappli...')
  Page 483: REJECTED 'Amazon S3' (too much extra content: 'dynamodbintegrationw...')
  Page 487: REJECTED 'Amazon S3' (too much extra content: 'apigatewayawsservice...')
  Page 497: MATCH for 'Serverless Architectures'
  Page 500: REJECTED 'Amazon S3' (too much extra content: 'mobileappgivingusers...')
  Page 501: REJECTED 'Amazon S3' (too much extra content: 'mobileapphighreadthr...')
  Page 502: REJECTED 'Amazon S3' (too much extra content: 'mobileappcachingatth...')
  Page 505: REJECTED 'Amazon S3' (too much extra content: 'servingstaticcontent...')
  Page 506: REJECTED 'Amazon S3' (too much extra content: 'servingstaticcontent...')
  Page 507: REJECTED 'Amazon S3' (too much extra content: 'addingapublicserverl...')
  Page 508: REJECTED 'Amazon S3' (too much extra content: 'leveragingdynamodbgl...')
  Page 509: REJECTED 'Amazon S3' (too much extra content: 'userwelcomeemailflow...')
  Page 510: REJECTED 'Amazon S3' (too much extra content: 'thumbnailgenerationf...')
  Page 513: REJECTED 'Amazon Route 53' (too much extra content: 'microservicesenviron...')
  Page 519: MATCH for 'Databases in AWS'
  Page 521: REJECTED 'Data and Analytics' (too much extra content: 'databasetypesrdbmssq...')
  Page 523: REJECTED 'Machine Learning' (too much extra content: 'compatibleapiforpost...')
  Page 526: REJECTED 'Amazon S3' (too much extra content: 'summarys3isakeyvalue...')
  Page 533: MATCH for 'Data and Analytics'
  Page 534: REJECTED 'Amazon S3' (too much extra content: 'amazonathenaserverle...')
  Page 536: REJECTED 'Amazon S3' (too much extra content: 'amazonathenafederate...')
  Page 541: REJECTED 'Amazon S3' (too much extra content: 'redshiftspectrumquer...')
  Page 546: REJECTED 'Machine Learning' (too much extra content: 'amazonemremrstandsfo...')
  Page 548: REJECTED 'Machine Learning' (too much extra content: 'amazonquicksightserv...')
  Page 553: REJECTED 'Amazon S3' (too much extra content: 'gluedatacatalogcatal...')
  Page 556: REJECTED 'Amazon S3' (too much extra content: 'awslakeformationdata...')
  Page 557: REJECTED 'Amazon S3' (too much extra content: 'awslakeformationcent...')
  Page 565: REJECTED 'Amazon S3' (too much extra content: 'bigdataingestionpipe...')
  Page 566: MATCH for 'Machine Learning'
  Page 574: REJECTED 'Machine Learning' (too much extra content: 'amazoncomprehendforn...')
  Page 575: REJECTED 'Amazon S3' (too much extra content: 'amazoncomprehendmedi...')
  Page 576: REJECTED 'Machine Learning' (too much extra content: 'amazonsagemakeraiful...')
  Page 577: MULTIPLE keywords found: Amazon S3, Machine Learning
  Page 578: REJECTED 'Amazon S3' (too much extra content: 'amazonpersonalizeful...')
  Page 580: REJECTED 'Machine Learning' (too much extra content: 'awssummaryrekognitio...')
  Page 581: REJECTED 'AWS Monitoring, Audit and Performance' (too much extra content: 'cloudwatchcloudtrail...')
  Page 583: REJECTED 'Amazon S3' (too much extra content: 'cloudwatchmetricstre...')
  Page 584: REJECTED 'Amazon S3' (too much extra content: 'cloudwatchlogsloggro...')
  Page 588: REJECTED 'Amazon S3' (too much extra content: 'cloudwatchlogss3expo...')
  Page 590: REJECTED 'Amazon S3' (too much extra content: 'cloudwatchlogsaggreg...')
  Page 612: REJECTED 'Amazon S3' (too much extra content: 'cloudtraileventsmana...')
  Page 613: REJECTED 'Amazon S3' (too much extra content: 'cloudtrailinsightsen...')
  Page 624: MATCH for 'Advanced Identity in AWS'
  Page 636: REJECTED 'Amazon S3' (too much extra content: 'iamrolesvsresourceba...')
  Page 637: REJECTED 'Amazon S3' (too much extra content: 'iamrolesvsresourceba...')
  Page 653: REJECTED 'AWS Security and Encryption' (too much extra content: 'kmsencryptionsdkssmp...')
  Page 667: REJECTED 'Amazon S3' (too much extra content: 's3replicationencrypt...')
  Page 685: REJECTED 'Amazon Route 53' (too much extra content: 'awsfirewallmanagerma...')
  Page 691: REJECTED 'Machine Learning' (too much extra content: 'amazonguarddutyintel...')
  Page 695: REJECTED 'Machine Learning' (too much extra content: 'awsmacieamazonmaciei...')
  Page 696: MATCH for 'Amazon VPC'
  Page 732: REJECTED 'Amazon S3' (too much extra content: 'privatesubnettypesof...')
  Page 733: REJECTED 'Amazon S3' (too much extra content: 'gatewayorinterfaceen...')
  Page 745: REJECTED 'Amazon S3' (too much extra content: 'directconnectdiagram...')
  Page 751: REJECTED 'Amazon VPC' (too much extra content: 'networktopologiescan...')
  Page 752: REJECTED 'Amazon VPC' (too much extra content: 'transitgatewayforhav...')
  Page 768: REJECTED 'Amazon S3' (too much extra content: 'privatesubnet2100102...')
  Page 769: REJECTED 'Amazon VPC' (too much extra content: 'networkprotectionona...')
  Page 770: REJECTED 'Amazon VPC' (too much extra content: 'awsnetworkfirewallpr...')
  Page 771: REJECTED 'Amazon S3' (too much extra content: 'networkfirewallfineg...')
  Page 772: MATCH for 'Disaster Recovery and Migrations'
  Page 776: REJECTED 'Amazon S3' (too much extra content: 'backupandrestorehigh...')
  Page 783: REJECTED 'Amazon S3' (too much extra content: 'dmssourcesandtargets...')
  Page 787: REJECTED 'Amazon S3' (too much extra content: 'rdsandauroramysqlmig...')
  Page 788: REJECTED 'Amazon S3' (too much extra content: 'rdsandaurorapostgres...')
  Page 790: REJECTED 'Amazon S3' (too much extra content: 'awsbackupfullymanage...')
  Page 792: REJECTED 'Amazon S3' (too much extra content: 'awsbackupawsbackupcr...')
  Page 798: MATCH for 'More Solutions Architecture'
  Page 801: REJECTED 'Amazon S3' (too much extra content: 's3eventnotifications...')
  Page 802: REJECTED 'Amazon S3' (too much extra content: 's3eventnotifications...')
  Page 804: REJECTED 'Amazon S3' (too much extra content: 'apigatewayawsservice...')
  Page 811: REJECTED 'Machine Learning' (too much extra content: 'highperformancecompu...')
  Page 815: REJECTED 'Amazon S3' (too much extra content: 'storageinstanceattac...')
  Page 820: REJECTED 'Other Services' (too much extra content: 'overviewofservicesth...')
  Page 829: REJECTED 'Amazon S3' (too much extra content: 'systemsmanagerruncom...')
  Page 838: REJECTED 'Machine Learning' (too much extra content: 'awscostanomalydetect...')
  Page 840: REJECTED 'Amazon S3' (too much extra content: 'awsoutpostsbenefitsl...')
  Page 842: REJECTED 'Amazon S3' (too much extra content: 'awsbatchsimplifiedex...')
  Page 844: REJECTED 'Amazon S3' (too much extra content: 'amazonappflowfullyma...')
  Page 846: REJECTED 'Amazon S3' (too much extra content: 'awsamplifywebandmobi...')
  Page 848: REJECTED 'White Papers and Architectures' (too much extra content: 'wellarchitectedframe...')
  Page 869: REJECTED 'Machine Learning' (too much extra content: 'awscertificationpath...')
  Page 870: REJECTED 'Machine Learning' (too much extra content: 'awscertificationpath...')
  Page 871: MATCH for 'Congratulations'
  Page 872: REJECTED 'Congratulations' (too much extra content: 'congratsonfinishingt...')

Matching Summary:
  Pages analyzed: 873
  Pages with matches: 23
  Pages with multiple keywords: 7
  Pages rejected (extra content): 147
  'Getting Started with AWS': 1 match(es) on pages 14
  'AWS Identity and Access Management (AWS IAM)': 1 match(es) on pages 24
  'Amazon EC2 - Basics': 1 match(es) on pages 41
  'Amazon EC2 - Associate': 1 match(es) on pages 78
  'Amazon EC2 - Instance Storage': 1 match(es) on pages 93
  'High Availability and Scalability': 1 match(es) on pages 118
  'RDS, Aurora and ElastiCache': 1 match(es) on pages 160
  'Amazon Route 53': 1 match(es) on pages 193
  'Classic Solutions Architecture': 1 match(es) on pages 227
  'Amazon S3': 1 match(es) on pages 267
  'Amazon S3 - Advanced': No matches found
  'Amazon S3 - Security': No matches found
  'CloudFront and Global Accelerator': 1 match(es) on pages 335
  'AWS Storage Extras': 1 match(es) on pages 353
  'AWS Integration and Messaging': No matches found
  'Containers on AWS': 1 match(es) on pages 417
  'Serverless Overview': 1 match(es) on pages 444
  'Serverless Architectures': 1 match(es) on pages 497
  'Databases in AWS': 1 match(es) on pages 519
  'Data and Analytics': 1 match(es) on pages 533
  'Machine Learning': 1 match(es) on pages 566
  'AWS Monitoring, Audit and Performance': No matches found
  'Advanced Identity in AWS': 1 match(es) on pages 624
  'AWS Security and Encryption': No matches found
  'Amazon VPC': 1 match(es) on pages 696
  'Disaster Recovery and Migrations': 1 match(es) on pages 772
  'More Solutions Architecture': 1 match(es) on pages 798
  'Other Services': No matches found
  'White Papers and Architectures': No matches found
  'Exam Preparation': No matches found
  'Congratulations': 1 match(es) on pages 871
Created 'output/1_slides_getting_started_with_aws.md' with 1 matching section(s)
Created 'output/2_slides_aws_identity_and_access_management_aws_iam.md' with 1 matching section(s)
Created 'output/3_slides_amazon_ec2_-_basics.md' with 1 matching section(s)
Created 'output/4_slides_amazon_ec2_-_associate.md' with 1 matching section(s)
Created 'output/5_slides_amazon_ec2_-_instance_storage.md' with 1 matching section(s)
Created 'output/6_slides_high_availability_and_scalability.md' with 1 matching section(s)
Created 'output/7_slides_rds_aurora_and_elasticache.md' with 1 matching section(s)
Created 'output/8_slides_amazon_route_53.md' with 1 matching section(s)
Created 'output/9_slides_classic_solutions_architecture.md' with 1 matching section(s)
Created 'output/10_slides_amazon_s3.md' with 1 matching section(s)
Skipping 'Amazon S3 - Advanced': only 0 match(es) found (minimum: 1)
Skipping 'Amazon S3 - Security': only 0 match(es) found (minimum: 1)
Created 'output/11_slides_cloudfront_and_global_accelerator.md' with 1 matching section(s)
Created 'output/12_slides_aws_storage_extras.md' with 1 matching section(s)
Skipping 'AWS Integration and Messaging': only 0 match(es) found (minimum: 1)
Created 'output/13_slides_containers_on_aws.md' with 1 matching section(s)
Created 'output/14_slides_serverless_overview.md' with 1 matching section(s)
Created 'output/15_slides_serverless_architectures.md' with 1 matching section(s)
Created 'output/16_slides_databases_in_aws.md' with 1 matching section(s)
Created 'output/17_slides_data_and_analytics.md' with 1 matching section(s)
Created 'output/18_slides_machine_learning.md' with 1 matching section(s)
Skipping 'AWS Monitoring, Audit and Performance': only 0 match(es) found (minimum: 1)
Created 'output/19_slides_advanced_identity_in_aws.md' with 1 matching section(s)
Skipping 'AWS Security and Encryption': only 0 match(es) found (minimum: 1)
Created 'output/20_slides_amazon_vpc.md' with 1 matching section(s)
Created 'output/21_slides_disaster_recovery_and_migrations.md' with 1 matching section(s)
Created 'output/22_slides_more_solutions_architecture.md' with 1 matching section(s)
Skipping 'Other Services': only 0 match(es) found (minimum: 1)
Skipping 'White Papers and Architectures': only 0 match(es) found (minimum: 1)
Skipping 'Exam Preparation': only 0 match(es) found (minimum: 1)
Created 'output/23_slides_congratulations.md' with 1 matching section(s)

Successfully created 23 file(s) with 23 total matching sections.
Output directory: /home/burricolpj/Documents/GitHub/extract-pdf/output
Output format: markdown (.md files)
```