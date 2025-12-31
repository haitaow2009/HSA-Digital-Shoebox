import logging
import re
import csv
from pypdf import PdfReader  # or your preferred library like pdfplumber
from pathlib import Path


logger = logging.getLogger(__name__)

class PDFExtractor:
    def __init__(self, upload_dir="data/raw"):
        self.upload_dir = Path(upload_dir)
        self.pdf = ""
        self.text = ""
        self.details = {}


    def extract_text_from_file(self, filename) -> None:
        logger.info(f"Extracting text from {filename}")
        """Extracts text from a PDF file located in the data/raw folder."""
        self.pdf = filename
        file_path = self.upload_dir / filename
        reader = PdfReader(file_path)

        for page in reader.pages:
            self.text += page.extract_text()
            
    
    def parse_hsa_details(self) -> None:
        """
        Reuse your original logic here to find dates, amounts, 
        and providers within the extracted text string.
        """
        logger.info("Parsing HSA details from extracted text")
        # Example: regex or string parsing logic you already built
        details = {
            "source": "PDF",
            "date": None,
            "provider": "Unknown",
            "amount": "0.00"
        }
        
        # Search for Date
        self.details["date"] = self.extract_date()

        # Search for Provider
        self.details["provider"] = self.extract_provider()

        # Search for Amount
        self.details["amount"] = self.extract_amount()
        
        #update the details dictionary to csv file
        self.auto_log_eob
        
    
    def extract_date(self) -> str:
        """Extracts date from the given text using regex."""
        date_pattern = r'(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2})'
        match = re.search(date_pattern, self.text)
        if match:
            return match.group(1)
        return None


    def extract_provider(self) -> str:
        # Look for "ROSS D NOCHIMSON MD." specifically 
        # This pattern looks for names followed by medical titles like MD or DO
        provider_pattern = r'([A-Z\s]+(?:MD|DO|M\.D\.))'
        match = re.search(provider_pattern, self.text)
        if match:
            return match.group(1).strip()
        return "Unknown"


    def extract_amount(self) -> str:
        # This pattern looks for "What I owe" followed by a currency amount
        # it handles optional colons, spaces, and the dollar sign
        owe_pattern = r'What\s+I\s+owe[:\s]*\$?\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2}))'
        
        # Search for the specific "What I owe" section
        match = re.search(owe_pattern, self.text, re.IGNORECASE)
        if match:
            return match.group(1)
        return "0.00"
    

    def auto_log_eob(self):
        # Extract all details from the PDF
        service_date = self.details["date"] or "Manual Entry Needed"
        provider = self.details["provider"] if self.details["provider"] != "Unknown" else input(f"Provider not found. Enter for {self.pdf}: ")
        amount = self.details["amount"] if self.details["amount"] != "0.00" else input(f"Amount not found. Enter for {self.pdf}: ")         

        # Save to your CSV database
        with open(self.upload_dir / 'hsa_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([service_date, provider, amount, "Unreimbursed", self.pdf])
        
        print(f"Successfully logged! Date Found: {service_date}")