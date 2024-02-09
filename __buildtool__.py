from pathlib import Path
from buildtool.build_tool import BuildTool


if __name__ == "__main__":
    
    dst = Path(r"C:\hrks")
    builder = BuildTool(
        src = Path().cwd(),
        build_name = "buildtool1000",
        ignore_files = [],
        ignore_direcotry = [], #//
        initialize_dirnames = ["log"],
        ).run()
    
    
