#!/usr/bin/env python3
"""
Download Norwegian rural load dataset from Zenodo.
DOI: 10.5281/zenodo.14528192
"""

import requests
import zipfile
import io
import os

ZENODO_URL = "https://zenodo.org/record/14528192/files/rural_load_norway.zip"

def download_norwegian_dataset(output_dir='.'):
    print(f"Downloading from {ZENODO_URL}")
    r = requests.get(ZENODO_URL)
    if r.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(output_dir)
        print(f"Extracted to {output_dir}")
    else:
        print(f"Download failed: {r.status_code}")

if __name__ == '__main__':
    download_norwegian_dataset()