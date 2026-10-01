# Serverless Automated Resource Auditor & Cost Optimizer

## Project Description
An event-driven serverless FinOps solution built on AWS using Python. The application automatically audits cloud infrastructure to locate idle development resources (EC2 instances) and safely stops them based on a scheduled timer to optimize cloud spending and prevent budget overruns.

## Technical Skills Used
* AWS Lambda
* Amazon EventBridge (Scheduler)
* AWS Systems Manager (SSM)
* AWS IAM (Security Roles)
* Python (Boto3 SDK)

## Key Implementation Highlights
1. **Serverless Execution:** Utilized AWS Lambda written in Python to perform completely automated infrastructure discovery without server overhead.
2. **Resource Filtering:** Implemented smart filters using the AWS Boto3 SDK to automatically capture running `Dev` instances across target regions.
3. **Cost Optimization Logic:** Triggered autonomous environment state changes via integration rules, saving non-production resource expenses outside of business hours.
