import argparse
from pathlib import Path

from shacl_doc_generator.generator import MarkdownGenerator
from shacl_doc_generator.parser import ShaclParser


def main():
    supported_file_extensions = [".ttl"]
    argparser = argparse.ArgumentParser(
        description="SHACLER - SHACL Documentation Generator"
    )
    argparser.add_argument(
        "--input",
        required=True,
        help=f"Path to SHACL file OR directory containing one or more SHACL files. Supported extensions: {supported_file_extensions}",
    )
    argparser.add_argument(
        "--output",
        required=False,
        default="./docs",
        help="Path to output directory for the generated .md files.",
    )
    args = argparser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    shacl_parser = ShaclParser()
    md_generator = MarkdownGenerator()

    if input_path.is_file():
        if input_path.suffix not in supported_file_extensions:
            print(
                f"File extension {input_path.suffix} not supported. Supported file extensions: {supported_file_extensions}"
            )
            exit(1)
        shacl_files = [input_path]

    elif input_path.is_dir():
        shacl_files = []
        for file_path in input_path.iterdir():
            if file_path.suffix in supported_file_extensions:
                shacl_files.append(file_path)
        if not shacl_files:
            print(
                f"SHACL files not found. Supported file extensions {supported_file_extensions}"
            )
            exit(1)

    for shacl_file in shacl_files:
        print(f"Parsing file {shacl_file}")

        try:
            shapes_for_this_file = shacl_parser.parse_file(shacl_file)
        except Exception as e:
            print(f"Failed to parse file {shacl_file}: {e}")
            continue

        output_file = output_dir / f"{shacl_file.stem}.md"

        print(f"Writing to {output_file}")
        try:
            md_generator.generate_docs(
                shapes_for_this_file, output_filename=str(output_file)
            )

            with open(shacl_file, "r", encoding="utf-8") as fp:
                turtle_content = fp.read()

            with open(output_file, "a", encoding="utf-8") as out:
                out.write("\n## Original SHACL File\n\n")
                out.write("```turtle\n")
                out.write(turtle_content)
                out.write("\n```\n")
        except Exception as e:
            print(f"Error occured when generating docs {output_file}: {e}")
            continue


if __name__ == "__main__":
    main()
