#!/usr/bin/env python

import sys
import sh
import pathlib
from rich import print

script_path = pathlib.Path(__file__).parent

cfg_dir = script_path.parent / "config" / "timing_systems"

commands = [
    f"daqconf_multiru_gen -n --detector-readout-map-file {cfg_dir}/timing_system_cern_DetReadoutMap.json -c {cfg_dir}/timing_system_cern_daq.json test",
    f"daqconf_multiru_gen -n --detector-readout-map-file {cfg_dir}/timing_system_cern_DetReadoutMap.json -c {cfg_dir}/timing_system_cern_timing.json test",
    f"daqconf_multiru_gen -n --detector-readout-map-file {cfg_dir}/timing_system_iceberg_DetReadoutMap.json -c {cfg_dir}/timing_system_iceberg_daq.json test",
    f"daqconf_multiru_gen -n --detector-readout-map-file {cfg_dir}/timing_system_iceberg_DetReadoutMap.json -c {cfg_dir}/timing_system_iceberg_timing.json test",
]

failed = []
success = []
for cmd in commands:
    print(f"Executing '{cmd}'")
    cmd_tokens = cmd.split()
    exe = getattr(sh, cmd_tokens[0])
    try:
        exe(*cmd_tokens[1:], _out=sys.stdout, _err=sys.stderr)
    except sh.ErrorReturnCode:
        failed.append(cmd)
        continue

    success.append(cmd)


print(f"Successful {success}")
print(f"Failed {failed}")