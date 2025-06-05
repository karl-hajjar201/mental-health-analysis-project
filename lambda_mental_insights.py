import json

INSIGHTS = {
    "top_stress_features": ["mental_health_status", "air_quality_index", "sleep_hours"],
    "correlations": {
        "mental_health_status": 0.83,
        "air_quality_index": 0.56,
        "sleep_hours": -0.44
    }
}

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(INSIGHTS)
    }
