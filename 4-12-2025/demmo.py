import requests
import json
from typing import Any, Dict, List
from pydantic import BaseModel, ValidationError, validator

# --- Pydantic models for basic structure validation ---
class DailyModel(BaseModel):
    # We don't enumerate every daily field; just ensure 'time' exists and is a non-empty list
    time: List[Any]

    @validator("time")
    def time_non_empty(cls, v):
        if not isinstance(v, list) or len(v) == 0:
            raise ValueError("daily.time must be a non-empty list")
        return v

class HourlyModel(BaseModel):
    time: List[Any]

    @validator("time")
    def time_non_empty(cls, v):
        if not isinstance(v, list) or len(v) == 0:
            raise ValueError("hourly.time must be a non-empty list")
        return v

class ForecastModel(BaseModel):
    latitude: float
    longitude: float
    # keep daily/hourly optional but validate shape if present
    daily: Dict[str, Any] = None
    hourly: Dict[str, Any] = None

    @validator("daily", pre=True, always=False)
    def validate_daily(cls, v):
        if v is None:
            return v
        # use DailyModel to validate relevant substructure
        DailyModel(**v)
        return v

    @validator("hourly", pre=True, always=False)
    def validate_hourly(cls, v):
        if v is None:
            return v
        HourlyModel(**v)
        return v

# --- helper validation function ---
def validate_response_json(resp_json: Dict[str, Any]) -> None:
    """
    Raises ValidationError or ValueError if invalid.
    """
    # Basic presence/shape validation using Pydantic
    ForecastModel(**resp_json)

# --- Main flow ---
url1 = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=13.1377&longitude=78.13"
    "&daily=weather_code,sunrise,daylight_duration,sunshine_duration,"
    "rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,"
    "precipitation_probability_max"
    "&hourly=temperature_2m,weather_code"
    "&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"
)

url2 = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=15.4608&longitude=76.2883"
    "&daily=weather_code,sunrise,daylight_duration,sunshine_duration,"
    "rain_sum,showers_sum,snowfall_sum,precipitation_sum,precipitation_hours,"
    "precipitation_probability_max"
    "&hourly=temperature_2m"
    "&current=temperature_2m,rain,weather_code,cloud_cover,showers,is_day"
)

paths_out = r"C:\Users\ADMIN\OneDrive\Desktop\telcom\4-12-2025\location_combined.json"

def fetch_and_validate(url: str) -> Dict:
    try:
        resp = requests.get(url, timeout=15)
    except requests.RequestException as e:
        raise RuntimeError(f"Request failed for {url!r}: {e}")

    if resp.status_code != 200:
        raise RuntimeError(f"Non-200 status code {resp.status_code} from {url!r}")

    try:
        data = resp.json()
    except ValueError as e:
        raise RuntimeError(f"Response from {url!r} is not valid JSON: {e}")

    try:
        validate_response_json(data)
    except ValidationError as ve:
        # re-raise with clearer message
        raise RuntimeError(f"Schema validation failed for {url!r}: {ve}")

    return data

def main():
    errors = []
    combined: List[Dict] = []

    for i, url in enumerate((url1, url2), start=1):
        try:
            data = fetch_and_validate(url)
            print(f"[OK] URL {i} validated (latitude={data.get('latitude')}, longitude={data.get('longitude')})")
            combined.append(data)
        except Exception as e:
            msg = f"[ERROR] URL {i} validation failed: {e}"
            print(msg)
            errors.append(msg)

    if errors:
        print("One or more fetches failed validation — not writing combined file.")
        for e in errors:
            print(e)
        return

    # All good -> write file
    try:
        with open(paths_out, "w", encoding="utf-8") as f:
            json.dump(combined, f, indent=4)
        print(f"Wrote combined validated data to: {paths_out}")
    except Exception as e:
        print(f"Failed to write combined file: {e}")

    # Re-open and print a short summary
    try:
        with open(paths_out, "r", encoding="utf-8") as file:
            data_loaded = json.load(file)
        print("Loaded combined file, entries:", len(data_loaded))
    except Exception as e:
        print(f"Failed to read back combined file: {e}")

if __name__ == "__main__":
    main()
