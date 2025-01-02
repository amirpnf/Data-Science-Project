# config.py

RAW_DATA_DIR = "data/raw/US_Counties_Health_Stats.csv"
CLEANED_DATA_DIR = "data/cleaned/US_Counties_Health_Stats_Cleaned.csv"
GEOJSON_FILE = "counties.geojson"
OUTPUT_MAP_FILE = "US_Counties_Health_Study.html"

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
DEFAULT_DISEASE = "OBESITY_CrudePrev"
CACHE_DIR = "cache"  # Directory for caching intermediate data (if applicable)

# Debugging mode
DEBUG = True
