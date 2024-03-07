# Release Notes

Below are some examples (of the mkdocs package) of how we can keep track of changes.

---

## Version 1.5.3 (2023-09-18)

*   Fix `mkdocs serve` sometimes locking up all browser tabs when navigating quickly (#3390)
*   Add many new supported languages for "search" plugin - update lunr-languages to 1.12.0 (#3334)
*   Bugfix (regression in 1.5.0): In "readthedocs" theme the styling of "breadcrumb navigation" was broken for nested pages (#3383)
*   Built-in themes now also support Chinese (Traditional, Taiwan) language (#3154)
*   Plugins can now set `File.page` to their own subclass of `Page`. There is also now a warning if `File.page` is set to anything other than a strict subclass of `Page`. (#3367, #3381)
    Note that just instantiating a `Page` [sets the file automatically](https://github.com/mkdocs/mkdocs/blob/f94ab3f62d0416d484d81a0c695c8ca86ab3b975/mkdocs/structure/pages.py#L34), so care needs to be taken not to create an unneeded `Page`.

Other small improvements; see [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.2...1.5.3).

## Version 1.5.2 (2023-08-02)

*   Bugfix (regression in 1.5.0): Restore functionality of `--no-livereload`. (#3320)
*   Bugfix (regression in 1.5.0): The new page title detection would sometimes be unable to drop anchorlinks - fix that. (#3325)
*   Partly bring back pre-1.5 API: `extra_javascript` items will once again be mostly strings, and only sometimes `ExtraScriptValue` (when the extra `script` functionality is used).
    Plugins should be free to append strings to `config.extra_javascript`, but when reading the values, they must still make sure to read it as `str(value)` in case it is an `ExtraScriptValue` item. For querying the attributes such as `.type` you need to check `isinstance` first. Static type checking will guide you in that. (#3324)

See [commit log](https://github.com/mkdocs/mkdocs/compare/1.5.1...1.5.2).

## Version 0.10.0 (2014-10-29)

* Added support for Python 3.3 and 3.4. (#103)
* Configurable Python-Markdown extensions with the config setting `markdown_extensions`. (#74)
* Added `mkdocs json` command to output your rendered documentation as json files. (#128)
* Added `--clean` switch to `build`, `json` and `gh-deploy` commands to remove stale files from the output directory. (#157)
* Support multiple theme directories to allow replacement of individual templates rather than copying the full theme. (#129)
* Bugfix: Fix `<ul>` rendering in readthedocs theme. (#171)
* Bugfix: Improve the readthedocs theme on smaller displays. (#168)
* Bugfix: Relaxed required python package versions to avoid clashes. (#104)
* Bugfix: Fix issue rendering the table of contents with some configs. (#146)
* Bugfix: Fix path for embedded images in sub pages. (#138)
* Bugfix: Fix `use_directory_urls` config behavior. (#63)
* Bugfix: Support `extra_javascript` and `extra_css` in all themes. (#90)
* Bugfix: Fix path-handling under Windows. (#121)
* Bugfix: Fix the menu generation in the readthedocs theme. (#110)
* Bugfix: Fix the mkdocs command creation under Windows. (#122)
* Bugfix: Correctly handle external `extra_javascript` and `extra_css`. (#92)
* Bugfix: Fixed favicon support. (#87)
