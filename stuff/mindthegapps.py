import os
import shutil
from stuff.general import General
from tools.helper import get_download_dir, host, print_color, run, bcolors


class MindTheGapps(General):
    dl_links = {
        "15.0.0": {
            "x86_64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20250330/MindTheGapps-15.0.0-x86_64-20250330.zip",
                "e54694828bd74e9066b2534a9675c31e",
            ],
            "arm64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20250330/MindTheGapps-15.0.0-arm64-20250330.zip",
                "79acb62f0f7c66b0f0bcadae5624f3d1",
            ],
            "arm": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20250330/MindTheGapps-15.0.0-arm-20250330.zip",
                "4ced6a404a714e61831e16068c3642b3",
            ],
        },
        "14.0.0": {
            "x86_64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-14.0.0-x86_64-20240619.zip",
                "9fd3e7fe2370183a9cdcff8f26837516",
            ],
            "x86": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-14.0.0-x86-220240619.zip",
                "eeeaec8e7225a7f7c8cfc31538e9f804",
            ],
            "arm64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-14.0.0-arm64-20240619.zip",
                "be537e97339ae822b791c8e8a1173f7e",
            ],
            "arm": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-14.0.0-arm-20240619.zip",
                "5309a641271151fc1dea878f61bd16bd",
            ],
        },
        "13.0.0": {
            "x86_64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-13.0.0-x86_64-20240619.zip",
                "25927de9f175e1db6647ccb62c5503ce",
            ],
            "x86": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-13.0.0-x86-20240619.zip",
                "821ae859631f3d22190831e28ffcc71d",
            ],
            "arm64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-13.0.0-arm64-20240619.zip",
                "4205fb7a6313ddc595cb41ad7d850474",
            ],
            "arm": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-13.0.0-arm-20240619.zip",
                "ec7aa5efc9e449b101bc2ee7448a49bf",
            ],
        },
        "12.0.0": {
            "x86_64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-12.1.0-x86_64-20240619.zip",
                "05d6e99b6e6567e66d43774559b15fbd"
            ],
            "x86": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-12.1.0-x86-20240619.zip",
                "ff2421a75afbdda8a003e4fd25e95050"
            ],
            "arm64": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-12.1.0-arm64-20240619.zip",
                "94dd174ff16c2f0006b66b25025efd04",
            ],
            "arm": [
                "https://github.com/s1204IT/MindTheGappsBuilder/releases/download/20240619/MindTheGapps-12.1.0-arm-20240619.zip",
                "5af756b3b5776c2f6ee024a9f7f42a2f",
            ],
        },
    }

    arch = host()
    download_loc = get_download_dir()
    dl_file_name = os.path.join(download_loc, "mindthegapps.zip")
    dl_link = ...
    act_md5 = ...
    copy_dir = "./mindthegapps"
    extract_to = "/tmp/mindthegapps/extract"

    def __init__(self, version):
        self.version = version
        self.dl_link = self.dl_links[self.version][self.arch[0]][0]
        self.act_md5 = self.dl_links[self.version][self.arch[0]][1]

    def download(self):
        print_color("Downloading MindTheGapps now .....", bcolors.GREEN)
        super().download()

    def copy(self):
        if os.path.exists(self.copy_dir):
            shutil.rmtree(self.copy_dir)
        if not os.path.exists(self.extract_to):
            os.makedirs(self.extract_to)

        shutil.copytree(
            os.path.join(self.extract_to, "system", ),
            os.path.join(self.copy_dir, "system"), dirs_exist_ok=True, )
