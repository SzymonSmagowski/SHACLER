from pathlib import Path
from typing import Dict, Any

class MarkdownGenerator:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        
    def format_property_value(self, value: Any) -> str:
        """Format property values for markdown."""
        if isinstance(value, list):
            return "\n".join(f"- {v}" for v in value)
        return str(value)
        
    def write_properties(self, f, properties: Dict[str, Any], indent: str = ""):
        """Write properties recursively with proper formatting."""
        if not properties:
            return
            
        f.write(f"\n{indent}**Properties:**\n\n")
        
        for prop_name, value in properties.items():
            if prop_name == 'property_shapes':
                f.write(f"\n{indent}**Nested Property Shapes:**\n\n")
                for shape in value:
                    f.write(f"{indent}- Path: {shape['path']}\n")
                    self.write_properties(f, shape['properties'], indent + "  ")
                continue
                
            formatted_value = self.format_property_value(value)
            f.write(f"{indent}- **{prop_name}:** {formatted_value}\n")

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
                
                self.write_properties(f, info.get('properties', {}))
                    
                f.write("---\n\n")