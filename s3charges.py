"""Print out the charges for s3 for the last 24 hours by hour."""
from amazonPrices import pricing
from check_aws_usage import get_report, PERIODS, FORMATS
from csv import DictReader
from datetime import date
from decimal import Decimal
from optparse import OptionParser
from StringIO import StringIO
from time import strptime

def organize_buckets_and_operations(csv_dictreader):
  """
  Take in a csv dictreader object and conslidate the s3 buckets into a 
  dictionary of time ordered elements with each dict of operations and 
  values.
  """
  result = dict()
  for row in csv_dictreader:
    if row['Operation'] != 'GetObject': # Honestly, i don't care what other things costs me.
      if not row['Resource'] in result:
        result[row['Resource']] = {}
      if not row['StartTime'] in result[row['Resource']]:
        result[row['Resource']][row['StartTime']] = {}
      result[row['Resource']][row['StartTime']][row['UsageType']] = row['UsageValue']
  return result

def sum_usage(organized_results):
  """
  go over the results output from organize_buckets_and_operations and sum the costs.
  """
  for bucket, report_slice in organized_results.items():
    print "%s:" % bucket
    for date_str, usage in report_slice.items():
      print "\t%s: " % date_str
      for usage_name, usage_value in usage.items():
        print "\t\t%s: $%.6f" % (usage_name, (Decimal(usage_value)/pricing['AmazonS3'][usage_name]['unit']) * pricing['AmazonS3'][usage_name]['price'])
 
if __name__ == "__main__":
  USAGE = (
      "Usage: %prog [options] -s SERVICE DATE_FROM DATE_TO\n\n"
      "DATE_FROM and DATE_TO should be in YYYY-MM-DD format (eg. 2009-01-31)\n"
      "Username and Password can also be specified via AWS_USERNAME and AWS_PASSWORD environment variables.\n"
      "\n"
  )
  parser = OptionParser(usage=USAGE)
  parser.add_option('-p', '--period', dest="period", type="choice", choices=PERIODS, default='hours', metavar="PERIOD", help="Period of report entries")
  parser.add_option('-f', '--format', dest="format", type="choice", choices=FORMATS, default='csv', metavar="FORMAT", help="Format of report")
  parser.add_option('-U', '--username', dest="username", metavar="USERNAME", help="Email address for your AWS account")
  parser.add_option('-P', '--password', dest="password", metavar="PASSWORD")
  parser.add_option('-d', '--debug', action="store_true", dest="debug", default=False)
  parser.add_option('-c', '--current', action="store_true", dest="current", default=False)    
  
  opts, args = parser.parse_args()
  
  if not opts.username and not os.environ.get('AWS_USERNAME'):
      parser.error("Must specify username option or set AWS_USERNAME")
  if not opts.password and not os.environ.get('AWS_PASSWORD'):
      parser.error("Must specify password option or set AWS_PASSWORD")
      
  if opts.current:
      kwopts = {
        'username': opts.username or os.environ.get('AWS_USERNAME'),
        'password': opts.password or os.environ.get('AWS_PASSWORD'),
        'debug': opts.debug,
      }    
      get_current(**kwopts)
  
  else:
  
    if len(args) < 2:
        parser.error("Missing date range")
    date_range = [date(*strptime(args[i], '%Y-%m-%d')[0:3]) for i in range(2)]
    if date_range[1] < date_range[0]:
        parser.error("End date < start date")
    
  kwopts = {
      'service': 'AmazonS3' ,
      'date_from': date_range[0],
      'date_to': date_range[1],
      'format': opts.format,
      'period': opts.period,
      'username': opts.username or os.environ.get('AWS_USERNAME'),
      'password': opts.password or os.environ.get('AWS_PASSWORD'),
      'debug': opts.debug,
  }
  
  csv_report = get_report(**kwopts)
  csv_dictreader = DictReader(StringIO(csv_report), delimiter=',', lineterminator="\n", skipinitialspace=True)
  organized_report = organize_buckets_and_operations(csv_dictreader)
  sum_usage(organized_report)  
