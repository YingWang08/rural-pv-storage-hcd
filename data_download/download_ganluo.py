#!/usr/bin/env python3
"""
Download Ganluo County electricity data from Liangshan Public Data Platform.
URL: http://data.lsz.gov.cn/oportal/catalog/9a8377dfedc049968840fd147ac2b532
"""

import requests

GANLUO_URL = "http://data.lszdsjzx.cn/oportal/catalog/9a8377dfedc049968840fd147ac2b532/download"

def download_ganluo(output_file='ganluo_electricity.csv'):
    r = requests.get(GANLUO_URL)
    if r.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(r.content)
        print(f"Downloaded to {output_file}")
    else:
        print(f"Download failed: {r.status_code}")

if __name__ == '__main__':
    download_ganluo()