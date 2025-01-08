# config.py

RAW_DATA_DIR = "data/raw/US_Counties_Health_Stats.csv"
CLEANED_DATA_DIR = "data/cleaned/US_Counties_Health_Stats_Cleaned.csv"
STATE_DATA_DIR = "data/cleaned/US_States_Health_Stats.csv"
GEOJSON_FILE = "counties.geojson"
STATES_GEOJSON = "states.geojson"
OUTPUT_MAP_FILE = "US_Counties_Health_Study.html"

OPTIONS=[
    {'label': 'Obesity', 'value': 'Obesity Prevalence (%)'},
    {'label': 'Cancer', 'value': 'Cancer Prevalence (%)'},
    {'label': 'Stroke', 'value': 'Stroke Prevalence (%)'},
    {'label': 'Arthritis', 'value': 'Arthritis Prevalence (%)'},
    {'label': 'Depression', 'value': 'Depression Prevalence (%)'},
    {'label': 'Diabetes', 'value': 'Diabetes Prevalence (%)'},
    {'label': 'High cholesterol', 'value': 'High Cholesterol Prevalence (%)'},
    {'label': 'Teeth lost', 'value': 'Teeth Lost Prevalence (%)'}
]

# Plot and visualization settings
CHOROPLETH_COLOR_SCALE = "Viridis"  #  or 'Plasma', etc.
HISTOGRAM_BINS = 20  # Number of bins for histogram

pages = {
    '/' : 'home',
    '/choropleth' : 'Choropleth maps',
    '/histograms' : 'Histograms'
}

# Logging settings
LOG_FILE = "project.log"
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Miscellaneous settings
DEFAULT_COUNTY = "Los Angeles"  # Example default value for filtering
DEFAULT_DISEASE1 = "Obesity Prevalence (%)"
DEFAULT_DISEASE2 = "Diabetes Prevalence (%)"
CACHE_DIR = "cache"  # Directory for caching intermediate data (if applicable)

API_URL = "https://data.cdc.gov/resource/i46a-9kgh.json"
FIELDS = ["StateDesc", "CountyName", "CountyFIPS", "TotalPopulation",
          'TotalPop18plus', 'OBESITY_CrudePrev', 'CANCER_CrudePrev',
          'STROKE_CrudePrev', 'ARTHRITIS_CrudePrev', 'DEPRESSION_CrudePrev',
          'DIABETES_CrudePrev', 'HIGHCHOL_CrudePrev','TEETHLOST_CrudePrev']

# Debugging mode
DEBUG = True
