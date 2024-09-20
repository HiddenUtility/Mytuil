from enum import Enum, auto


class ProjectTagElemetName(Enum):
    """Projectエレメントのタグ"""
    PackageName = auto()
    RequiredDirecotryPaths = auto()
    RequiredFilePaths = auto()
    IgnoreDirectoryName = auto()
    IgnoreFileName = auto()