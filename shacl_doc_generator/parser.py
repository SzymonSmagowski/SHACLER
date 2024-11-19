from pathlib import Path
from typing import Dict, List
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, SH

class ShaclParser:
    def __init__(self):
        self.shapes: Dict[str, Dict] = {}
        
    def parse_file(self, file_path: Path) -> Dict[str, Dict]:
        """Parse a SHACL file and extract shapes."""
        g = Graph()
        g.parse(file_path, format="turtle")
        
        # Find all NodeShape and PropertyShape declarations
        shape_nodes = []
        for s in g.subjects(RDF.type, SH.NodeShape):
            shape_nodes.append(s)
        for s in g.subjects(RDF.type, SH.PropertyShape):
            shape_nodes.append(s)
            
        # Extract information for each shape
        for node in shape_nodes:
            shape_info = {
                'type': 'NodeShape' if (node, RDF.type, SH.NodeShape) in g else 'PropertyShape',
                'label': str(g.value(node, RDFS.label) or ''),
                'comment': str(g.value(node, RDFS.comment) or ''),
                'target_class': str(g.value(node, SH.targetClass) or '')
            }
            
            self.shapes[str(node)] = shape_info
            
        return self.shapes