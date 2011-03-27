"""
A flat dictionary of amazon's usage rates organized by Service, UsageType, 
and Thresholds. All rates are in US Dollars per 1 unit. This can get crazy for gigabytes.

This is very incomplete but right now I just want a rough estimate.
"""
from decimal import Decimal
pricing = {
  'AmazonS3': {
    'DataTransfer-Out-Bytes': Decimal('0.000000000139698386'),
    'C3DataTransfer-Out-Bytes': Decimal('0.000000000139698386'),
    'DataTransfer-In-Bytes': Decimal('0.0000000000931322575'),
    'Requests-Tier1': Decimal('0.00001'),
    'Requests-Tier2': Decimal('0.000001'),
    'TimedStorage-ByteHrs': Decimal('0'),
    'StorageObjectCount': Decimal('0'),
    'Requests-NoCharge': Decimal('0'),
    'TimedStorage-RRS-ByteHrs': Decimal('0'),
  },
}
