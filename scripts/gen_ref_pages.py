"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
root = Path(__file__).parent.parent
src = root / "pmyning"
docs = root / "docs" / "reference"

for path in sorted(src.rglob("*.py")):
    # skip init files
    if path.stem in ["__init__", "__main__"]:
        continue

    module_path = path.relative_to(root).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = docs / doc_path

    parts = tuple(module_path.parts)

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print("::: " + identifier, file=fd)

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open(docs / "SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
