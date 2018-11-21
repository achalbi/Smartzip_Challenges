# Kinesis Producer

## Problem Statement:
Currently We need building a system which will act as the Data Generator for the Kinesis Stream. Ultimately the Data is going to be loaded in Redshift. 

The data generator should be able to produce the volume of 10000 Records/sec.

An Amazon Kinesis Data Streams producer is any application that puts user data records into a Kinesis data stream (also called data ingestion). The Kinesis Producer Library (KPL) simplifies producer application development, allowing developers to achieve high write throughput to a Kinesis data stream.

Technologies used is Kinesis Stream, Kinesis Firehose, S3 and Redshift. The plugin that will be used is Kinesis Producer Library.

Note: we need to pull data out of the DB using the above data generator

## Solutions:


#### Installing AWS CLI

https://docs.aws.amazon.com/cli/latest/userguide/installing.html

```python
$ pip install awscli --upgrade --user
```

```python
$ aws configure
```

```
AWS Access Key ID [None]: AKIAJFSDE3HQDOOBIEQ
AWS Secret Access Key [None]: EaEoCgBHEvSxxxxxxx1bmvB1rQopNbvHzvxxxxxx
Default region name [None]: us-east-1
Default output format [None]: json
```

#### AWS SDK for Python (Boto3)

https://aws.amazon.com/sdk-for-python/

#### Install Boto

```
$ pip install boto3
```


## Solution 1: Kiner package

Set Kinesis stream name: (smartzip-challenge-5)

#### Run

```
python3 kiner_producer_kiner.py
```


## Solution 2: Kinesis Aggregator/Deaggregator package

#### Run
```python
python3 kiner_publisher.py <stream name> <region>
```


## References:

https://github.com/awslabs/kinesis-aggregation

