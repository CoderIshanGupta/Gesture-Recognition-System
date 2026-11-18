import os
import random
import shutil

def split_dataset(source_dir, output_dir, split_ratio=0.8):
    os.makedirs(output_dir, exist_ok=True)
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    classes = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    print(f"Found classes: {classes}")

    for cls in classes:
        cls_path = os.path.join(source_dir, cls)
        images = [f for f in os.listdir(cls_path) if os.path.isfile(os.path.join(cls_path, f))]
        random.shuffle(images)
        split_point = int(len(images) * split_ratio)

        train_images = images[:split_point]
        val_images = images[split_point:]

        for img in train_images:
            dest_dir = os.path.join(train_dir, cls)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy(os.path.join(cls_path, img), dest_dir)

        for img in val_images:
            dest_dir = os.path.join(val_dir, cls)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy(os.path.join(cls_path, img), dest_dir)

        print(f"Class '{cls}': {len(train_images)} train, {len(val_images)} val images")

    print(f"Dataset successfully split into:\n- {train_dir}\n- {val_dir}")

if __name__ == "__main__":
    # Change these paths accordingly
    source_dataset_path = "asl_alphabet"        # Your original dataset folder path
    output_dataset_path = "asl_alphabet_train"  # Output folder for train/val split

    split_dataset(source_dataset_path, output_dataset_path, split_ratio=0.8)
