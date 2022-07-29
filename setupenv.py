from genericpath import isdir
import os

tool_dir = "./tool"

arm_none_eabi_url = "https://developer.arm.com/-/media/Files/downloads/gnu/11.2-2022.02/binrel/gcc-arm-11.2-2022.02-darwin-x86_64-arm-none-eabi.tar.xz"
arm_none_eabi_tar = "gcc-arm-11.2-2022.02-darwin-x86_64-arm-none-eabi.tar.xz"
arm_none_eabi_dir = "gcc-arm-11.2-2022.02-darwin-x86_64-arm-none-eabi"

qemu_url          = "https://github.com/xpack-dev-tools/qemu-arm-xpack/releases/download/v7.0.0-1/xpack-qemu-arm-7.0.0-1-darwin-x64.tar.gz"
qemu_tar          = "xpack-qemu-arm-7.0.0-1-darwin-x64.tar.gz"
qemu_dir          = "xpack-qemu-arm-7.0.0-1"

openocd_url       = "https://github.com/xpack-dev-tools/openocd-xpack/releases/download/v0.10.0-15/xpack-openocd-0.10.0-15-darwin-x64.tar.gz"
openocd_tar       = "xpack-openocd-0.10.0-15-darwin-x64.tar.gz"
openocd_dir       = "xpack-openocd-0.10.0-15"

if os.path.isdir(tool_dir) == False:
    os.mkdir(tool_dir)

os.chdir(tool_dir)

if os.path.isdir(arm_none_eabi_dir) == False:
    os.mkdir(arm_none_eabi_dir)
    print("Download GNU C/C++ ARM Toolchain:")
    os.system(f"wget {arm_none_eabi_url} -q --show-progress")
    print("Extracting compiler ")
    os.system(f"tar -xf {arm_none_eabi_tar}")
    os.remove(f"./{arm_none_eabi_tar}")
    print("")

if os.path.isdir(qemu_dir) == False:
    os.mkdir(qemu_dir)
    print("Download QEMU for ARM Cortex-M:")
    os.system(f"wget {qemu_url} -q --show-progress")
    print("Extracting xpack-qemu-arm ")
    os.system(f"tar -xf {qemu_tar}")
    os.remove(f"./{qemu_tar}")

if os.path.isdir(openocd_dir) == False:
    os.mkdir(openocd_dir)
    print("Download open On-Chip Debugger:")
    os.system(f"wget {openocd_url} -q --show-progress")
    print("Extracting xpack-openocd")
    os.system(f"tar -xf {openocd_tar}")
    os.remove(f"./{openocd_tar}")
