from redditscraper import aggregation
from redditscraper import config

import datetime
import io
import pathlib
import shutil
import tarfile


archive_path_dir = pathlib.Path(config['Data']['archive-data-dir'])
process_path_dir = pathlib.Path(config['Data']['process-data-dir'])
raw_path_dir = pathlib.Path(config['Data']['raw-data-dir'])

# Move all raw files to process directory
for f in raw_path_dir.iterdir():
    shutil.move(str(f.resolve()), str(process_path_dir.resolve()))

# Process files
aggregation.process_files()

# Archive processed files and delete
tarfile_name = str(archive_path_dir.resolve()) + '/archive-'+datetime.datetime.now().isoformat()+'-.tar.gz'
with tarfile.open(tarfile_name, "w:gz") as tar:
    for f in process_path_dir.iterdir():
        info = tarfile.TarInfo(str(f.stem)+str(f.suffix))
        fb = f.open("rb+")

        # Do this sillyness because files in archive 
        # appear empty if the TarInfo doesn't get a 
        # size
        fb.seek(0, io.SEEK_END)
        info.size = fb.tell()
        fb.seek(0, io.SEEK_SET)

        tar.addfile(info, fb)
        f.unlink()
