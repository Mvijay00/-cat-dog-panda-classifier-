from pathlib import Path
import random
import shutil

SOURCE = Path(r"C:\Users\admin\Downloads\catdog\animals\animals")
DEST = Path("dataset")

CLASSES = {
    "cats": "cats",
    "dogs": "dogs",
    "panda": "pandas",
}

TRAIN_RATIO = 0.70
VAL_RATIO = 0.15

random.seed(42)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

for source_folder, class_name in CLASSES.items():

    source_path = SOURCE / source_folder

    if not source_path.exists():
        print(f"ERROR: Folder not found: {source_path}")
        continue

    images = [
        file
        for file in source_path.iterdir()
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    random.shuffle(images)

    total = len(images)

    train_end = int(total * TRAIN_RATIO)
    val_end = train_end + int(total * VAL_RATIO)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    print(f"\nClass: {class_name}")
    print(f"Total: {total}")
    print(f"Train: {len(train_images)}")
    print(f"Validation: {len(val_images)}")
    print(f"Test: {len(test_images)}")

    splits = {
        "train": train_images,
        "val": val_images,
        "test": test_images,
    }

    for split_name, split_images in splits.items():

        destination_folder = DEST / split_name / class_name
        destination_folder.mkdir(parents=True, exist_ok=True)

        for image_file in split_images:
            shutil.copy2(
                image_file,
                destination_folder / image_file.name
            )

print("\nDataset preparation completed successfully!")
