#!/usr/bin/env python3

import argparse
from stuff.gapps import Gapps
from stuff.litegapps import LiteGapps
from stuff.magisk import Magisk
from stuff.mindthegapps import MindTheGapps
from stuff.ndk import Ndk
from stuff.houdini import Houdini
from stuff.houdini_hack import Houdini_Hack
from stuff.widevine import Widevine
import tools.helper as helper
import subprocess
import os


def main():
    dockerfile = ""
    tags = []
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a', '--android-version',
                        dest='android',
                        help='Specify the Android version to build',
                        default='11.0.0',
                        choices=['16.0.0', '15.0.0', '14.0.0', '13.0.0', '12.0.0', '11.0.0', '10.0.0', '9.0.0', '8.1.0'])
    parser.add_argument('-g', '--install-gapps',
                        dest='gapps',
                        help='Install OpenGapps to ReDroid',
                        action='store_true')
    parser.add_argument('-l', '--install-litegapps',
                        dest='litegapps',
                        help='Install LiteGapps to ReDroid',
                        action='store_true')
    parser.add_argument('-n', '--install-ndk-translation',
                        dest='ndk',
                        help='Install libndk translation files',
                        action='store_true')
    parser.add_argument('-i', '--install-houdini',
                        dest='houdini',
                        help='Install houdini files',
                        action='store_true')
    parser.add_argument('-d', '--install-mindthegapps',
                        dest='mindthegapps',
                        help='Install MindTheGapps to ReDroid',
                        action='store_true')
    parser.add_argument('-m', '--install-magisk', dest='magisk',
                        help='Install Magisk ( Bootless )',
                        action='store_true')
    parser.add_argument('-w', '--install-widevine', dest='widevine',
                        help='Integrate Widevine DRM (L3)',
                        action='store_true')
    parser.add_argument('-u', '--fix-systemui', dest='systemui',
                        help='remove ui odex to fix crash (android12)',
                        action='store_true')
    parser.add_argument('-p', '--nodata-perm', dest='nodataperm',
                        help='granting full permission for apps data (above android11)',
                        action='store_true')
    parser.add_argument('-c', '--container', 
                        dest='container',
                        default='docker',
                        help='Specify container type', 
                        choices=['docker', 'podman'])

    args = parser.parse_args()
    dockerfile = dockerfile + \
        "FROM redroid/redroid:{}-latest\n".format(
            args.android)
    tags.append(args.android)
    if args.gapps:
        if args.android in ["11.0.0", "10.0.0", "9.0.0", "8.1.0"]:
            Gapps(args.android).install()
            dockerfile = dockerfile + "COPY gapps /\n"
            tags.append("gapps")
        else:
            helper.print_color( "WARNING: OpenGapps only supports 11.0.0", helper.bcolors.YELLOW)
    if args.litegapps:
        LiteGapps(args.android).install()
        dockerfile = dockerfile + "COPY litegapps /\n"
        tags.append("litegapps")
    if args.mindthegapps:
        if args.android in ["12.0.0", "13.0.0", "14.0.0"]:
            MindTheGapps(args.android).install()
            dockerfile = dockerfile + "COPY mindthegapps /\n"
            tags.append("mindthegapps")
        else:
            helper.print_color(
                "WARNING: MindTheGapps seems to work only 12 - 15", helper.bcolors.YELLOW)
    if args.ndk:
        if args.android in ["11.0.0", "12.0.0", "13.0.0", "14.0.0"]:
            arch = helper.host()[0]
            if arch == "x86" or arch == "x86_64":
                Ndk(args.android).install()
                dockerfile = dockerfile+"COPY ndk /\n"
                tags.append("ndk")
        else:
            helper.print_color(
                "WARNING: Libndk seems to work only 11 - 15", helper.bcolors.YELLOW)
    if args.houdini:
        if args.android in ["8.1.0", "9.0.0", "11.0.0", "12.0.0", "13.0.0", "14.0.0"]:
            arch = helper.host()[0]
            if arch == "x86" or arch == "x86_64":
                Houdini(args.android).install()
                if not args.android == "8.1.0":
                    Houdini_Hack(args.android).install()
                dockerfile = dockerfile+"COPY houdini /\n"
                tags.append("houdini") 
        else:
            helper.print_color(
                "WARNING: Houdini seems to work only above redroid:11.0.0", helper.bcolors.YELLOW)
    if args.magisk:
        Magisk().install()
        dockerfile = dockerfile+"COPY magisk /\n"
        tags.append("magisk")
    if args.widevine:
        if args.android in ["11.0.0", "12.0.0", "13.0.0"]:
            Widevine(args.android).install()
            dockerfile = dockerfile+"COPY widevine /\n"
            tags.append("widevine")
        else:
            helper.print_color(
                "WARNING: widevine seems to work only 11 - 13", helper.bcolors.YELLOW)
    if args.systemui:
        dockerfile = dockerfile+"COPY dirty_fix/ui /\n"
        tags.append("systemui")
    if args.nodataperm:
        os.chmod(os.path.join(os.getcwd(), "dirty_fix", "nodataperm", "system", "etc", "no_data_perm.sh"), 0o755)
        dockerfile = dockerfile+"COPY dirty_fix/nodataperm /\n"
        tags.append("nodataperm")
    print("\nDockerfile\n"+dockerfile)
    with open("./Dockerfile", "w") as f:
        f.write(dockerfile)
    new_image_name = "redroid/redroid:"+"_".join(tags)
    subprocess.run([args.container, "build", "-t", new_image_name, "."])
    helper.print_color("Successfully built {}".format(
        new_image_name), helper.bcolors.GREEN)


if __name__ == "__main__":
    main()
