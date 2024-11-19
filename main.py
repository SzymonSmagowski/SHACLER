import argparse
from pathlib import Path
from shacl_doc_generator.parser import ShaclParser
from shacl_doc_generator.generator import MarkdownGenerator
from shacl_doc_generator.config import Settings

def main():
    parser = argparse.ArgumentParser(description='Generate documentation from SHACL files')
    parser.add_argument('filename', help='Name of the SHACL file to process')
    args = parser.parse_args()

    settings = Settings()
    shacl_parser = ShaclParser()
    shapes = shacl_parser.parse_file(settings.shacl_dir / args.filename)

    output_filename = Path(args.filename).stem + ".md"
    generator = MarkdownGenerator(settings.docs_dir)
    generator.generate_docs(shapes, output_filename)

if __name__ == "__main__":
    main()