#!/usr/bin/env python3
"""
Download NREL DuraMAT PVDAQ dataset.
URL: https://datahub.duramat.org/dataset/a49bb656-7b36-437a-8089-1870a40c2a7d
"""

import requests

NREL_URL = "https://datahub.duramat.org/dataset/a49bb656-7b36-437a-8089-1870a40c2a7d/resource/xxx/download/pvdaq_system4.csv"

def download_nrel(output_file='pvdaq_system4.csv'):
    # Note: actual direct download link may require parsing the datahub page.
    # For reproducibility, the script uses a known static URL after manual retrieval.
    # Alternatively, use the DataHub API.
    print("Please download manually from DuraMAT DataHub or use provided sample.")
    # Placeholder for automated download if API available.
    pass

if __name__ == '__main__':
    download_nrel()