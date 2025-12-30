# Entry point (orchestrator) for HSA Shoebox application

import os
import sys
import logging
from pathlib import Path
# from hsa_shoebox.cigna_api import CignaClient
# from hsa_shoebox.processor import DataProcessor
from hsa_shoebox import PDFExtractor

# Configure logging at the top level
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("hsa_shoebox")

def main():

    
    try:
        # Initialize modules
        # client = CignaClient()
        # processor = DataProcessor()
        pdf_tool = PDFExtractor()
        
        # --- PROCESS SOURCE 1: Local PDFs ---
        # Process any PDFs manually dropped into data/raw/
        for pdf_file in Path("data/sample").glob("*.pdf"):
            logger.info(f"Processing manual upload: {pdf_file.name}")
            raw_text = pdf_tool.extract_text_from_file(pdf_file.name)
            pdf_data = pdf_tool.parse_hsa_details(raw_text)
            # You can now pass pdf_data to your processor or database
            pdf_tool.auto_log_eob()
    
        """ 
            --- PROCESS SOURCE 2: Cigna API ---
            # Step 1: Authentication and ID Discovery
            # (Assuming you have logic to handle the auth_code and redirect_uri)
            # client.refresh_access_token(auth_code, redirect_uri)
            user_info = client.get_user_info()
            patient_id = user_info['parameter'][0]['valueString'] # Based on Cigna response
            
            # Step 2: Fetch EOBs
            raw_bundle = client.get_explanation_of_benefits(patient_id)
            
            # Step 3: Process and Save
            processor.save_raw_data(f"eob_{patient_id}.json", raw_bundle)
            eob_list = processor.parse_fhir_bundle(raw_bundle)
            
            for eob in eob_list:
                summary = processor.extract_summary(eob)
                logger.info(f"Processed: {summary['date']} - Owed: ${summary['member_owed']}")
        """

        return 0

    except Exception as e:
        logger.error(f"Application failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
