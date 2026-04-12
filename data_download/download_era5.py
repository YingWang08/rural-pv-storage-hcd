#!/usr/bin/env python3
"""
Download ERA5-Land hourly data for PV simulation.
Requires CDS API key (free registration at https://cds.climate.copernicus.eu/)
Dataset: Muñoz-Sabater, J. (2023) doi:10.24381/cds.e2161bac
"""

import cdsapi
import argparse

def download_era5(year: int, month: int, bbox: list, output_file: str):
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-land',
        {
            'variable': [
                'surface_solar_radiation_downwards',
                '2m_temperature',
            ],
            'year': str(year),
            'month': f'{month:02d}',
            'day': [f'{d:02d}' for d in range(1, 32)],
            'time': [f'{h:02d}:00' for h in range(24)],
            'area': bbox,  # [N, W, S, E]
            'format': 'netcdf',
        },
        output_file
    )
    print(f"Downloaded to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, default=2023)
    parser.add_argument('--month', type=int, default=1)
    parser.add_argument('--output', default='era5_data.nc')
    args = parser.parse_args()

    # Sichuan rural area bounding box [N, W, S, E]
    bbox = [33, 97, 26, 108]
    download_era5(args.year, args.month, bbox, args.output)