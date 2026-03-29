# -*- coding: utf-8 -*-
"""
ERA5-Land Meteorological Data Download Script
For Rural PV-Storage System Simulation
Dataset: Copernicus ERA5-Land (Hourly)
Variables: Surface solar radiation downwards, 2m temperature
Region: Ganluo County, Sichuan
Time: January 2024
"""
import os

# CDS Official API Configuration
os.environ["CDSAPI_URL"] = "https://cds.climate.copernicus.eu/api"
os.environ["CDSAPI_KEY"] = "d0cdda65-f867-479e-aea4-04ad8da9220e"

import cdsapi


def download_era5_data():
    # Create data folder automatically
    os.makedirs("./data", exist_ok=True)

    print("=" * 60)
    print("ERA5-Land Meteorological Data Download")
    print("Time Range: 2024-01-01 ~ 2024-01-31")
    print("Region: Ganluo County, Sichuan Province")
    print("Output Path: ./data/era5_land.nc")
    print("=" * 60)

    # Initialize CDS client
    client = cdsapi.Client()

    # Download request
    client.retrieve(
        "reanalysis-era5-land",
        {
            "variable": [
                "surface_solar_radiation_downwards",
                "2m_temperature"
            ],
            "year": "2024",
            "month": "01",
            "day": [f"{i:02d}" for i in range(1, 32)],
            "time": [f"{i:02d}:00" for i in range(24)],
            "area": "29.5/102.0/28.0/103.5",
            "format": "netcdf",
        },
        "./data/era5_land.nc"
    )

    print("\n✅ Download completed successfully!")


if __name__ == "__main__":
    download_era5_data()