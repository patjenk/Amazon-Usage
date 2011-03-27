"""
A flat dictionary of amazon's usage rates organized by Service, UsageType, 
and Thresholds. All rates are in US Dollars per 1 unit. This can get crazy for gigabytes.

This is very incomplete but right now I just want a rough estimate.
"""
from decimal import Decimal
pricing = {
  'AmazonS3': {
    'DataTransfer-Out-bytes': Decimal('0.000000000139698386'),
    'Requests-Tier2': Decimal('0.000001'),
  },
}
