import subprocess

def main():
    command = "poetry run python python/1_clean_geojson.py && poetry run python python/2_clean_death_rate.py"
    res = subprocess.call(command, shell=True)

if __name__ == "__main__":
    main()
