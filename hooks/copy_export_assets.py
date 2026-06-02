"""MkDocs build hook: publish build artifacts from the repo-root ``export/``
directory into the documentation site.

The draw.io export workflow (``.github/workflows/drawio-export.yml``) renders
each ``*.drawio`` file to ``export/*.png``. Those PNGs live outside ``docs/``,
so MkDocs does not serve them by default. This hook copies selected export
artifacts into the site at build time — for ``mkdocs serve``, ``mkdocs build``,
and any deployment that runs a build — so the diagrams stay current with the
source automatically and no generated copies are committed under ``docs/``.

To publish another export artifact, add an entry to ``ASSETS``:

    "export/<source-file>": "<path under docs_dir>"

``dest`` is the path the file lives at inside the site relative to ``docs_dir``,
so pages reference it with the normal central-image convention, e.g.
``![alt](../../images/lj-tub-map-power-distribution.png)``.
"""

import os

from mkdocs.plugins import get_plugin_logger
from mkdocs.structure.files import File

log = get_plugin_logger(__name__)

# export artifact (repo-root relative)  ->  site path (docs_dir relative)
ASSETS = {
    "export/Jeep LJ Tub Map-Power-Distribution.png":
        "jeep_lj/images/lj-tub-map-power-distribution.png",
    "export/Jeep LJ Tub Map-Lighting---SwitchPros.png":
        "jeep_lj/images/lj-tub-map-lighting-switchpros.png",
    "export/Jeep LJ Tub Map-Controls--Recovery---Drivetrain.png":
        "jeep_lj/images/lj-tub-map-controls-recovery-drivetrain.png",
}


def on_files(files, config):
    repo_root = os.path.dirname(config["config_file_path"])
    for src, dest in ASSETS.items():
        abs_src = os.path.join(repo_root, src)
        if not os.path.isfile(abs_src):
            log.warning("export asset not found, skipping: %s", src)
            continue
        published = File(
            dest,
            config["docs_dir"],
            config["site_dir"],
            config["use_directory_urls"],
        )
        # Source the file from export/ rather than from docs_dir.
        published.abs_src_path = abs_src
        # Replace any file already registered at this destination.
        existing = files.get_file_from_path(dest)
        if existing is not None:
            files.remove(existing)
        files.append(published)
        log.info("published export asset: %s -> %s", src, dest)
    return files
