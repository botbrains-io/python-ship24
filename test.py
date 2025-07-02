import ship_24
from ship_24 import models
import os

# --- 1. Initialization ---
# The SDK likely needs an API key. While not shown in the constructor,
# Speakeasy-generated SDKs often use other mechanisms. You would typically
# configure this when initializing the client or through environment variables.
# For this example, we'll assume authentication is configured correctly.
# Please refer to the Ship24 API documentation for authentication details.

# A simple instantiation of the SDK
s = ship_24.Ship24()

# The tracking number you want to track
tracking_number_to_track = "YOUR_TRACKING_NUMBER_HERE"

# --- 2. Prepare the Request ---
# The only required field is the tracking_number.
# The SDK automatically detects the courier.
try:
    request = models.TrackerCreateRequest(
        tracking_number=tracking_number_to_track,
    )

    # --- 3. Call the API ---
    print(f"Creating tracker and fetching results for {tracking_number_to_track}...")
    response = s.trackers.create_tracker_and_get_tracking_results(request=request)

    # --- 4. Process the Response ---
    if response and response.data and response.data.trackings:
        print("Successfully retrieved tracking information.")
        # The response is a list, as a tracking number could potentially
        # be associated with multiple shipments.
        for tracking_info in response.data.trackings:
            if tracking_info.shipment:
                print("\n--- Shipment Details ---")
                print(f"  Shipment ID: {tracking_info.shipment.shipment_id}")
                print(f"  Status: {tracking_info.shipment.status_milestone}")

            if tracking_info.events:
                print("\n--- Tracking Events ---")
                for event in tracking_info.events:
                    print(
                        f"  - {event.occurrence_datetime}: {event.status} at {event.location}"
                    )
    else:
        print("No tracking data returned in the response.")

except ship_24.errors.APIError as e:
    print(f"\nAn API error occurred:")
    print(f"  Status Code: {e.status_code}")
    print(f"  Body: {e.body}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
