import sys
import json
import importlib
import multiprocessing as mp

import make_case_folder_structure

SOURCES = "./sources.json"

def run_src(src):
    print(f"Running {src}", file=sys.stderr)
    country = importlib.import_module(f"parsers.{src}")
    country.parse()


if __name__ == "__main__":
    make_case_folder_structure.main()

    srcs = list(json.load(open(SOURCES)).keys())
    pool = mp.Pool(mp.cpu_count())
    pool.map(run_src, srcs)
    pool.close()
    pool.join()
