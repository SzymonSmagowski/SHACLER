import argparse
from pathlib import Path
from shacl_doc_generator.parser import ShaclParser
from shacl_doc_generator.generator import MarkdownGenerator

def main():
    parser = argparse.ArgumentParser(description="SHACLER - SHACL Documentation Generator")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to SHACL file OR directory containing one or more *.ttl SHACL files."
    )
    parser.add_argument(
        "--output",
        required=False,
        default="./docs",
        help="Path to output directory for the generated .md files."
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    md_generator = MarkdownGenerator()

    if input_path.is_dir():
        ttl_files = list(input_path.glob("*.ttl"))
        if not ttl_files:
            print(f"No .ttl files found in {input_path}")
            return

        for ttl_file in ttl_files:
            print(f"Processing file: {ttl_file}")

            shacl_parser = ShaclParser()  # create a fresh parser
            shapes_for_this_file = shacl_parser.parse_file(ttl_file)

            output_file = output_dir / f"{ttl_file.stem}.md"
            md_generator.generate_docs(shapes_for_this_file, output_filename=str(output_file))

            with open(ttl_file, 'r', encoding='utf-8') as fp:
                turtle_content = fp.read()

            with open(output_file, 'a', encoding='utf-8') as out:
                out.write("\n## Original SHACL File\n\n")
                out.write("```turtle\n")
                out.write(turtle_content)
                out.write("\n```\n")

    else:
        if not input_path.is_file():
            print(f"Error: {input_path} is not a file.")
            return

        print(f"Processing single file: {input_path}")

        shacl_parser = ShaclParser()
        shapes_for_this_file = shacl_parser.parse_file(input_path)

        output_file = output_dir / f"{input_path.stem}.md"
        md_generator.generate_docs(shapes_for_this_file, output_filename=str(output_file))

        with open(input_path, 'r', encoding='utf-8') as fp:
            turtle_content = fp.read()
        with open(output_file, 'a', encoding='utf-8') as out:
            out.write("\n## Original SHACL File\n\n")
            out.write("```turtle\n")
            out.write(turtle_content)
            out.write("\n```\n")


if __name__ == "__main__":
    main()

