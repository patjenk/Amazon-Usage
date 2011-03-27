"""
A flat dictionary of amazon's usage rates organized by Service, UsageType, 
and Thresholds. All rates are in US Dollars per 1 unit. This can get crazy for gigabytes.

This is very incomplete but right now I just want a rough estimate.
"""
from decimal import Decimal
pricing = {
  'AmazonS3': {
    'DataTransfer-Out-Bytes': {
      'unit': 1073741824,
      'price': Decimal('0.15'),
    },
    'C3DataTransfer-Out-Bytes': { 
      'unit': 1073741824,
      'price': Decimal('0.15'),
    },
    'DataTransfer-In-Bytes': {
      'unit': 1073741824,
      'price': Decimal('0.10'),
    },
    'Requests-Tier1': {
      'unit': 1000, 
      'price': Decimal('0.01'),
    },
    'Requests-Tier2': {
      'unit': 10000, 
      'price': Decimal('0.01'),
    },
    'TimedStorage-ByteHrs': {
      'unit': 1,
      'price': Decimal('0'),
    },
    'StorageObjectCount': {
      'unit': 1,
      'price': Decimal('0'),
    },
    'Requests-NoCharge': {
      'unit': 1,
      'price': Decimal('0'),
    },
    'TimedStorage-RRS-ByteHrs': {
      'unit': 1,
      'price': Decimal('0'),
    },
  },
}
