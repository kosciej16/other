from glob import glob
from pathlib import Path

for f in glob("import/*"):
    print(Path(f).stem)
