import subprocess


def main():
    command = (
        "poetry run python python/1_clean_geojson.py"
        + "&& poetry run python python/2_clean_death_rate.py"
        + "&& poetry run python python/3_copy_to_lib_assets.py"
    )
    res = subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()
