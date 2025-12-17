import os
import re
import shutil
from stuff.general import General
from tools.helper import bcolors, get_download_dir, print_color, run


class Houdini_Hack(General):
    download_loc = get_download_dir()
    copy_dir = "./houdini"
    dl_file_name = os.path.join(download_loc, "libhoudini_hack.zip")
    extract_to = "/tmp/houdinihackunpack"

    def __init__(self, version):
        self.version = version
        self.dl_link = "https://github.com/rote66/redroid_libhoudini_hack/archive/6b436ad1f49dca5cf74f6ae237504911bfd93687.zip"
        self.act_md5 = "0db90e44c6dd855513d65bcfb73395e3"

    def download(self):
        print_color("Downloading libhoudini_hack now .....", bcolors.GREEN)
        super().download()

    def copy(self):
        run(["chmod", "+x", self.extract_to, "-R"])

        print_color("Copying libhoudini hack files ...", bcolors.GREEN)
        name = re.findall("([a-zA-Z0-9]+)\.zip", self.dl_link)[0]
        shutil.copytree(os.path.join(self.extract_to, "redroid_libhoudini_hack-" + name,
                        self.version), os.path.join(self.copy_dir, "system"), dirs_exist_ok=True)

        if not self.version == "9.0.0":
            init_path = os.path.join(self.copy_dir, "system", "etc", "init", "hw", "init.rc")
            os.chmod(init_path, 0o644)
