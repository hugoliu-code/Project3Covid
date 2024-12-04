import pandas
import os

def get_data() -> list[tuple]:
    current_folder = os.path.dirname(os.path.abspath(__file__))
    df = pandas.read_csv(current_folder + "/Data.csv")

    df.columns
    """Columns are: county, county_fips, state, county_population, health_service_area_number, heath_service_area, 
    health_service_area_population, covid_inpatient_bed_utilization, covid_hospital_admissions_per_100k, 
    covid_cases_per_100k, covid-19_community_level, data_updated"""

    # Protocol: Use county and state to use as identification, then use covid_cases_per_100k to use for sorting

    df = df.drop(df.columns.difference(["county","state","covid_cases_per_100k"]), axis=1)

    return [tuple(row) for row in df.itertuples(index=False)]
