from pathlib import Path
from buildtool.build_tool import BuildTool


if __name__ == "__main__":
    
    dst = Path(r"C:\hrks")
    builder = BuildTool(
        Path().cwd(),
        dst,
        build_name = "buildtool1000",
        ignore_files = [".gitignore"],
        ignore_direcotry = ["log","settings"], #//
        initialize_dirnames = ["log","settings"],
        ).run()
    
    
