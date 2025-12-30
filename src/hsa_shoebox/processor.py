import json
from pathlib import Path
from fhir.resources.explanationofbenefit import ExplanationOfBenefit
from fhir.resources.bundle import Bundle

class DataProcessor:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
        
        # Ensure directories exist locally (ignored by git)
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def parse_fhir_bundle(self, bundle_json):
        """Parses a FHIR Bundle containing multiple EOB resources."""
        bundle = Bundle.parse_obj(bundle_json)
        eobs = []
        
        if bundle.entry:
            for entry in bundle.entry:
                if entry.resource.resourceType == "ExplanationOfBenefit":
                    eobs.append(entry.resource)
        
        return eobs

    def extract_summary(self, eob: ExplanationOfBenefit):
        """Extracts key HSA-relevant data from a single EOB resource."""
        # Cigna EOBs include adjudication details and cost breakdowns
        summary = {
            "id": eob.id,
            "date": str(eob.created),
            "provider": eob.provider.display if eob.provider else "Unknown",
            "total_billed": 0.0,
            "plan_paid": 0.0,
            "member_owed": 0.0
        }

        # FHIR 'total' field usually contains the cost breakdown
        if eob.total:
            for item in eob.total:
                category_code = item.category.coding[0].code
                amount = float(item.amount.value)
                
                if category_code == "submitted":
                    summary["total_billed"] = amount
                elif category_code == "benefit":
                    summary["plan_paid"] = amount
                elif category_code == "member_liability":
                    summary["member_owed"] = amount

        return summary

    def save_raw_data(self, filename, data):
        """Saves raw JSON response to the local data/raw directory."""
        file_path = self.raw_dir / filename
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return file_path