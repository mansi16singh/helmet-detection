import os
import shutil
import random


def create_folders(base_path):
    os.makedirs(os.path.join(base_path, 'train/images'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'train/labels'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'val/images'), exist_ok=True)
    os.makedirs(os.path.join(base_path, 'val/labels'), exist_ok=True)


def split_dataset(image_dir, label_dir, output_dir, split_ratio=0.8):
    images = os.listdir(image_dir)
    random.shuffle(images)

    split_idx = int(len(images) * split_ratio)
    train_imgs = images[:split_idx]
    val_imgs = images[split_idx:]

    for img_set, split in [(train_imgs, 'train'), (val_imgs, 'val')]:
        for img in img_set:
            shutil.copy(
                os.path.join(image_dir, img),
                os.path.join(output_dir, f'{split}/images/{img}')
            )

            label_file = os.path.splitext(img)[0] + '.txt'
            shutil.copy(
                os.path.join(label_dir, label_file),
                os.path.join(output_dir, f'{split}/labels/{label_file}')
            )
