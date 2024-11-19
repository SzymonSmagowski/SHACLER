from pathlib import Path

class Settings:
    def __init__(self):
        self.docs_output_dir = Path('./docs')
        self.shacl_files_dir = Path('./shacl_files')
        
        # Create output directory if it doesn't exist
        self.docs_output_dir.mkdir(parents=True, exist_ok=True)
        
    @property
    def docs_dir(self) -> Path:
        return self.docs_output_dir
        
    @property
    def shacl_dir(self) -> Path:
        return self.shacl_files_dir