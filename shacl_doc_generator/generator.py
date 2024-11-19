from pathlib import Path
from typing import Dict

class MarkdownGenerator:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        
    def generate_docs(self, shapes: Dict[str, Dict], output_filename: str = "shapes.md"):
        """Generate Markdown documentation from shapes dictionary."""
        output_path = self.output_dir / output_filename
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# SHACL Shapes Documentation\n\n")
            
            for shape_id, info in shapes.items():
                f.write(f"## Shape: {shape_id}\n\n")
                
                if info['label']:
                    f.write(f"**Label:** {info['label']}\n\n")
                    
                if info['type']:
                    f.write(f"**Type:** {info['type']}\n\n")
                    
                if info['comment']:
                    f.write(f"**Description:** {info['comment']}\n\n")
                    
                if info['target_class']:
                    f.write(f"**Target Class:** {info['target_class']}\n\n")
                    
                f.write("---\n\n")