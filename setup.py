from collections.abc import Iterator
from setuptools import setup, find_namespace_packages  # type: ignore


# TODO: should probably migrate to src/promnesia_pura to fix this issue?
def subpackages() -> Iterator[str]:
    for p in find_namespace_packages("."):
        if p.startswith("promnesia_pura"):
            yield p


def main() -> None:
    pkg = "promnesia_pura"
    pkgs = list(subpackages())
    setup(
        name=pkg,
        zip_safe=False,
        packages=pkgs,
        package_data={pkg: ["py.typed"]},
        url="https://github.com/purarue/promnesia",
        author="purarue",
    )


if __name__ == "__main__":
    main()
