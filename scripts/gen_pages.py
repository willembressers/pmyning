"""Generate the code reference pages."""

from pathlib import Path

import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
root = Path(__file__).parent.parent
src = root / "pmyning"

for path in sorted(src.rglob("*.py")):
    # skip init files
    if path.stem in ["__init__", "__main__"]:
        continue

    module_path = path.relative_to(root).with_suffix("")
    doc_path = path.relative_to(root).with_suffix(".md")
    parts = tuple(module_path.parts)
    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(doc_path, "w") as fd:
        identifier = ".".join(parts)
        fd.write(f"::: {identifier}")
