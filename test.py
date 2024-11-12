from pathlib import Path

if __name__ == "__main__":
    path_dir = Path("./training-data/legible")

    for i in range(10):
        path_file = path_dir / f"file_{i+1}.txt"
        path_file.touch()
