# Challenge 4

## Description
Identify and correct all the contacts that has non-unicode characters in the first_name or last_name

Input: id, first_name, last_name
id: bigint(20)
first_name, last_name : string

Output: id, first_name, last_name, Flag

Data volume: 110 millions

Business Rules while Analyzing Data:

It should take care of the following Rules and Flag for any Erroneous Records.

 - Names should not contain non ASCII characters like Tabs, New Line or Any special Characters
 - Names may contain single quote, hyphan, semicolon or
 - Names may contain different numeric or space characters Like Victor-2

Sample Input file: https://drive.google.com/open?id=1x9iNyziXSEu_suyl16EGk4M0Pe7WrKd1

Row count: 2 million rows. 
Actual input would be of 24 millions


## Ticket
https://smartzip.atlassian.net/browse/ST5S-9404

## Frameworks

The challenge is attempted in three different frameworks
  - Nodejs
  - Python
  - Spark in Python


## Observations

Time taken for excecution of test data with 200000 records is as follows
  - Nodejs:  < 8secs
  - Python: ~30secs
  - Spark in Python: 
    -- partioned files: < 13 secs
    -- single file: ~ 25 secs