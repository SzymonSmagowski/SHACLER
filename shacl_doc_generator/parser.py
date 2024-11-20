from pathlib import Path
from typing import Dict, List
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, SH

class ShaclParser:
    def __init__(self):
        self.shapes: Dict[str, Dict] = {}
        
    def get_properties(self, g: Graph, node: URIRef) -> Dict:
        """Extract all SHACL properties for a node."""
        properties = {}
        
        # Common SHACL properties to check
        sh_properties = [
            SH.path, SH.datatype, SH.minCount, SH.maxCount, 
            SH.pattern, SH.flags, SH.minLength, SH.maxLength,
            SH.minExclusive, SH.maxExclusive, SH.minInclusive, 
            SH.maxInclusive, SH['class'], SH.nodeKind,
            SH.hasValue, SH.property, SH['in']
        ]
        
        for prop in sh_properties:
            values = list(g.objects(node, prop))
            if values:
                prop_name = str(prop).replace(str(SH), 'sh:')
                if len(values) == 1:
                    properties[prop_name] = str(values[0])
                else:
                    properties[prop_name] = [str(v) for v in values]
                    
        # Get nested property shapes
        if (node, RDF.type, SH.NodeShape) in g:
            nested_properties = []
            for prop_shape in g.objects(node, SH.property):
                nested_info = {
                    'type': 'PropertyShape',
                    'path': str(g.value(prop_shape, SH.path) or ''),
                    'properties': self.get_properties(g, prop_shape)
                }
                nested_properties.append(nested_info)
            if nested_properties:
                properties['property_shapes'] = nested_properties
                
        return properties

    def parse_file(self, file_path: Path) -> Dict[str, Dict]:
        """Parse a SHACL file and extract shapes with all properties."""
        g = Graph()
        print(f"Parsing file: {file_path}")
        g.parse(file_path, format="turtle")
        
        # Find all NodeShape and PropertyShape declarations
        shape_nodes = []
        for s in g.subjects(RDF.type, SH.NodeShape):
            shape_nodes.append(s)
            print(f"Found NodeShape: {s}")
        for s in g.subjects(RDF.type, SH.PropertyShape):
            shape_nodes.append(s)
            print(f"Found PropertyShape: {s}")
            
        # Extract information for each shape
        for node in shape_nodes:
            shape_info = {
                'type': 'NodeShape' if (node, RDF.type, SH.NodeShape) in g else 'PropertyShape',
                'label': str(g.value(node, RDFS.label) or ''),
                'comment': str(g.value(node, RDFS.comment) or ''),
                'target_class': str(g.value(node, SH.targetClass) or ''),
                'properties': self.get_properties(g, node)
            }
            
            self.shapes[str(node)] = shape_info
            
        return self.shapes