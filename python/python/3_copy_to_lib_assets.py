from pathlib import Path
import shutil

print("start: 3_copy_to_lib_assets")

data_path = Path("../data")
assets_path = Path("../src/lib/assets")

shutil.copy(data_path / "reputation.json", assets_path / "reputation.json")
shutil.copy(data_path / "countries.geo.json", assets_path / "countries.geo.json")

print("done")
