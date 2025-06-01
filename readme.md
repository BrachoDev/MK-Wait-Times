# Disney Magic Kingdom Wait Times Data Project

This project provides a Python script that automatically downloads live wait times for all Magic Kingdom attractions from the [themeparks.wiki](https://themeparks.wiki) API. The script processes the data and generates a CSV file containing the current status and wait times for each attraction.

## Features

- Fetches live attraction data from the Magic Kingdom park using the official API.
- Extracts attraction names, operational status, and wait times.
- Outputs the data to a CSV file (`Attractions_waitTimes.csv`) for further analysis or visualization (In this case Tableau).

## Files

- [`script.py`](script.py): Python script to fetch and process the data.
- [`Attractions_waitTimes.csv`](Attractions_waitTimes.csv): Generated CSV file with the latest wait times.
- [`Tableau_project.twb`](Tableau_project.twb): Tableau workbook for visualizing the data.
- `.gitignore`: Excludes sensitive or generated files from version control.

## Usage

1. **Install dependencies**  
   Make sure you have Python 3 and the required packages:
   ```sh
   pip install requests pandas