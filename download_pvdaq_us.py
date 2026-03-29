# -*- coding: utf-8 -*-
"""
NREL DuraMAT PVDAQ System4 Data Download
Public dataset for PV output validation
"""
import os
import requests


def download_pvdaq_system4():
    os.makedirs("./data", exist_ok=True)
    url = "https://datahub.duramat.org/dataset/a49bb656-7b36-437a-8089-1870a40c2a7d/resource/8f9d8f7c-1b1a-4d0d-9f7c-0f7a7d1e3c4e/download/pvdaq_system4_2010_2016.csv"

    print("Downloading NREL PVDAQ System4...")
    resp = requests.get(url, timeout=300)
    with open("./data/pvdaq_system4.csv", "wb") as f:
        f.write(resp.content)
    print("✅ PVDAQ 美国光伏数据下载完成")


if __name__ == "__main__":
    download_pvdaq_system4()