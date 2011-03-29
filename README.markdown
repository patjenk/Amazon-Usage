# Amazon Usage

## Introduction
This python library allows you to pull down usage stats and calculate charges for Amazon cloud services such as S3 and EC2. It is very rough and the charges calculates are not correct. Right now they only aim to be "close." 

I wrote this library because I could only find piece of python code to access the information I wanted and it was a gist (https://gist.github.com/812303). I took that gist and added some very crude calculations.

## Dependencies
- Mechanize

## Example
To get started simply clone this repo. To calculate your charges on S3 for a given time frame use this command:

python s3charges.py 2011-03-27 2011-03-28 -U username -P password

## Thoughts
I wrote this library to quickly calculate what we were spending on S3. I think it could evolve into a useful library and since I wasn't able to find anything like it I decided to post it on github. I think a good next step would be to take into account the usage tiers for amazon pricing and use those while calculating charges. After that adding support for EC2 would be smart.
