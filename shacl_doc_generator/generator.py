from typing import Dict
from shacl_doc_generator.models import NodeShapeInfo, PropertyShapeInfo, Constraint, Path, PathEnum

class MarkdownGenerator:
    def generate_docs(self, shapes: Dict[str, NodeShapeInfo], output_filename: str = "shapes.md"):
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("# SHACL Shapes Documentation\n\n")
            for shape_id, shape_info in shapes.items():
                f.write(f"## Shape: {shape_id}\n\n")

                if shape_info.constraints:
                    f.write("### NodeShape Constraints\n\n")
                    for c in shape_info.constraints:
                        f.write(f"- **{c.name}:** {c.value}\n")
                    f.write("\n")

                if shape_info.properties:
                    f.write("### Properties\n\n")
                    for pshape in shape_info.properties:
                        f.write(f"#### Property: {pshape.id}\n\n")
                        f.write("**Path:**\n\n")
                        tree_lines = self._render_path_tree(pshape.path)
                        for line in tree_lines:
                            f.write(line + "\n")

                        f.write("\n")

                        encoded_path = self._format_path(pshape.path)
                        f.write(f"{encoded_path}\n\n")

                        if pshape.constraints:
                            f.write("**Constraints:**\n")
                            for c in pshape.constraints:
                                f.write(f"- **{c.name}:** {c.value}\n")
                            f.write("\n")

                f.write("---\n\n")

    def _render_path_tree(self, path: Path, indent: int = 0) -> list[str]:
        """
        Recursively render a SHACL Path as a bullet point tree.
        Each Path can be a sequence, alternative, inverse, etc.
        """
        lines = []

        # Make a user-friendly label for the path type
        label = self._path_type_label(path.type)

        prefix = "  " * indent  # 2 spaces per level
        lines.append(f"{prefix}- {label}")

        for item in path.items:
            if isinstance(item, str):
                lines.append(f"{'  ' * (indent+1)}- {item}")
            elif isinstance(item, Path):
                nested_lines = self._render_path_tree(item, indent + 1)
                lines.extend(nested_lines)
            else:
                lines.append(f"{'  ' * (indent+1)}- ???")
        return lines

    def _path_type_label(self, path_type: PathEnum) -> str:
        """
        Convert a PathEnum to a more human-readable label for the bullet point tree.
        """
        if path_type == PathEnum.sequence:
            return "Sequence of:"
        elif path_type == PathEnum.alternative:
            return "Alternative of:"
        elif path_type == PathEnum.inverse:
            return "Inverse of:"
        elif path_type == PathEnum.zero_or_more:
            return "Zero-or-more of:"
        elif path_type == PathEnum.one_or_more:
            return "One-or-more of:"
        elif path_type == PathEnum.zero_or_one:
            return "Zero-or-one of:"
        elif path_type == PathEnum.predicate:
            return "Predicate path:"
        else:
            return str(path_type)  # fallback

    def _format_path(self, path: Path) -> str:
        """Convert a Path object into a human-readable string representation."""
        # Different formatting depending on path type
        if path.type == PathEnum.predicate:
            # items should contain a single string (the URI)
            return path.items[0] if path.items else "???"

        elif path.type == PathEnum.inverse:
            # inverse has one inner path
            inner = self._format_path(path.items[0]) if path.items else "???"
            return f"^{inner}"

        elif path.type == PathEnum.sequence:
            # sequence has multiple items, each item could be a string or another Path
            parts = [self._format_path_item(it) for it in path.items]
            return "/".join(parts)

        elif path.type == PathEnum.alternative:
            # alternative paths separated by '|'
            parts = [self._format_path_item(it) for it in path.items]
            return "|".join(parts)

        elif path.type == PathEnum.zero_or_more:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}*"

        elif path.type == PathEnum.one_or_more:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}+"

        elif path.type == PathEnum.zero_or_one:
            inner = self._format_path_item(path.items[0]) if path.items else "???"
            return f"{inner}?"

        else:
            # Unknown path type
            return "???"

    def _format_path_item(self, item):
        """
        Format a single path item which can be either a string (prefixed IRI) 
        or a Path. If it's a string, wrap it in backticks for Markdown.
        """
        if isinstance(item, str):
            # Now item should already be "prefix:suffix".
            return f"`{item}`"  # <--- wrap in backticks
        elif isinstance(item, Path):
            return f"({self._format_path(item)})"
        else:
            return "???"
