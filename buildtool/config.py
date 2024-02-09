class Configuration:
    RELEASE = "__release"

    IGUNORE_DIRECTORYS =  [
        ".git",
        ".venv",
        "__pycache__",
        RELEASE,
    ]
  
    IGUNORE_FILENAMES = [
        "__buildtool__.py",
    ]