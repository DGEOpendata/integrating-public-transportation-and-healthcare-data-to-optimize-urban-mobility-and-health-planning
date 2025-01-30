# Integrating Public Transportation and Healthcare Data

This project demonstrates how to integrate public transportation data with healthcare facilities data in Abu Dhabi to optimize urban mobility and health planning.

## Requirements
- Python 3.x
- Pandas library
- Geopandas library

## Setup
1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   bash
   pip install pandas geopandas
   
3. Download the datasets:
   - `PublicTransportData_AbuDhabi.csv`
   - `HealthcareFacilities_AbuDhabi.geojson`

## Running the Script
1. Save the provided Python script in a file named `integrate_data.py`.
2. Run the script using Python:
   bash
   python integrate_data.py
   
3. The script will generate `CombinedTransportHealthcareData.csv`, which contains the nearest healthcare facility for each public transport stop.

## Explanation
- The script loads the public transportation and healthcare datasets.
- It then finds the nearest healthcare facility for each public transport stop using geometric operations.
- Finally, it saves the combined data with the nearest healthcare facility information.

## Use Cases
- Urban planners can use the combined data to optimize transportation routes linking to healthcare facilities.
- Healthcare providers can analyze access points and improve service delivery.
- Commuters can plan their journeys to include stops at necessary healthcare facilities.

## Feedback and Contributions
We welcome contributions to enhance this project. Please open an issue or pull request on the GitHub repository if you have suggestions or improvements.