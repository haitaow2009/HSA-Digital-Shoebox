# initial version of cigna_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Loads Client ID/Secret from your .env file

class CignaClient:
    def __init__(self):
        # Use Sandbox URLs for testing; update to Production later
        self.base_url = "https://fhir.cigna.com/PatientAccess/v1-devportal"
        self.token_url = "https://r-hi2.cigna.com/mga/sps/oauth/oauth20/token"
        self.client_id = os.getenv("CIGNA_CLIENT_ID")
        self.client_secret = os.getenv("CIGNA_CLIENT_SECRET")
        self.access_token = None

    def refresh_access_token(self, auth_code, redirect_uri):
        """Exchanges an authorization code for a JWT access token."""
        payload = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.token_url, data=payload)
        response.raise_for_status()
        
        data = response.json()
        self.access_token = data.get("access_token")
        return self.access_token

    def get_user_info(self):
        """Fetches the unique patient ID for the authenticated user."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        # The $userinfo endpoint is used to discover your patient ID
        response = requests.get(f"{self.base_url}/$userinfo", headers=headers)
        response.raise_for_status()
        return response.json()

    def get_explanation_of_benefits(self, patient_id):
        """Retrieves EOB (claims) records for the specified patient ID."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        # Endpoint for Explanation of Benefit resources
        params = {"patient": patient_id}
        response = requests.get(f"{self.base_url}/ExplanationOfBenefit", 
                                headers=headers, params=params)
        response.raise_for_status()
        return response.json()