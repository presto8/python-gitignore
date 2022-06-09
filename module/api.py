class GitignoreException(Exception):
    pass


class Gitignore:
    "Abstract class"

    def __init__(self, basedir, debug=False):
        raise

    def scan(self) -> None | GitignoreException:
        raise

    def import_gitignore(self, path, basedir) -> None | GitignoreException:
        raise

    def match(self, path) -> bool:
        raise
