import logging
from pypdf import PdfReader  # or your preferred library like pdfplumber
from pathlib import Path
import re

class PDFExtractor:
    def __init__(self, upload_dir="data/raw"):
        self.upload_dir = Path(upload_dir)
        self.logger = logging.getLogger("hsa_shoebox.extractor")

    def extract_text_from_file(self, filename):
        self.logger.info(f"Extracting text from {filename}")
        """Extracts text from a PDF file located in the data/raw folder."""
        file_path = self.upload_dir / filename
        reader = PdfReader(file_path)
        
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
            
        return full_text

    def parse_hsa_details(self, text):
        """
        Reuse your original logic here to find dates, amounts, 
        and providers within the extracted text string.
        """
        self.logger.info("Parsing HSA details from extracted text")
        # Example: regex or string parsing logic you already built
        details = {
            "source": "PDF",
            "date": None,
            "provider": "Unknown",
            "amount": "0.00"
        }
        
        # Search for Date
        details["date"] = extract_date_from_pdf_page(text)

        # Search for Provider
        details["provider"] = extract_provider_from_pdf_page(text)

        # Search for Amount
        details["amount"] = extract_amount_from_pdf_page(text)
        
        return details
    
    def extract_date_from_pdf_page(self, text: str):
        """Extracts date from the given text using regex."""
        date_pattern = r'(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2})'
        match = re.search(date_pattern, text)
        if match:
            return match.group(1)
        return None

    def extract_provider_from_pdf_page(self, text: str):
        # Look for "ROSS D NOCHIMSON MD." specifically 
        # This pattern looks for names followed by medical titles like MD or DO
        provider_pattern = r'([A-Z\s]+(?:MD|DO|M\.D\.))'
        match = re.search(provider_pattern, text)
        if match:
            return match.group(1).strip()
        return "Unknown"

    def extract_amount_from_pdf_page(self, text: str):
        # This pattern looks for "What I owe" followed by a currency amount
        # it handles optional colons, spaces, and the dollar sign
        owe_pattern = r'What\s+I\s+owe[:\s]*\$?\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2}))'
        
        # Search for the specific "What I owe" section
        match = re.search(owe_pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
        return "0.00"
    

    def auto_log_eob(self):
        temp_folder = "data/temp_eob"
        # Check for the first PDF in the temp folder
        files = [f for f in os.listdir(temp_folder) if f.endswith('.pdf')]
        
        if not files:
            print("No EOB PDFs found in data/temp_eob.")
            return

        pdf_path = os.path.join(temp_folder, files[0])
        print(f"Processing: {files[0]}...")
        
        # Use the updated extraction function
        extracted_data = extract_details_from_pdf(pdf_path)
        
        # Extract all details from the PDF
        service_date = extracted_data["date"] or "Manual Entry Needed"
        provider = extracted_data["provider"] if extracted_data["provider"] != "Unknown" else input(f"Provider not found. Enter for {files[0]}: ")
        amount = extracted_data["amount"] if extracted_data["amount"] != "0.00" else input(f"Amount not found. Enter for {files[0]}: ")         

        # Save to your CSV database
        with open('hsa_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([service_date, provider, amount, "Unreimbursed", pdf_path])
        
        print(f"Successfully logged! Date Found: {service_date}")