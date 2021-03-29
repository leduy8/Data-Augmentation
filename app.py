from image_utils import plot_images, gen_images
from file_utils import read_files_from_dir


# * Get all available paths
train_healthy_image_path = 'data/train/healthy/'
train_rust_image_path = 'data/train/rust/'
train_scab_image_path = 'data/train/scab/'
valid_healthy_image_path = 'data/valid/healthy/'
valid_rust_image_path = 'data/valid/rust/'
valid_scab_image_path = 'data/valid/scab/'
test_healthy_image_path = 'data/test/healthy/'
test_rust_image_path = 'data/test/rust/'
test_scab_image_path = 'data/test/scab/'

# * Read all image filenames
train_healthy_image_filenames = read_files_from_dir(train_healthy_image_path)
train_rust_image_filenames = read_files_from_dir(train_rust_image_path)
train_scab_image_filenames = read_files_from_dir(train_scab_image_path)
valid_healthy_image_filenames = read_files_from_dir(valid_healthy_image_path)
valid_rust_image_filenames = read_files_from_dir(valid_rust_image_path)
valid_scab_image_filenames = read_files_from_dir(valid_scab_image_path)
test_healthy_image_filenames = read_files_from_dir(test_healthy_image_path)
test_rust_image_filenames = read_files_from_dir(test_rust_image_path)
test_scab_image_filenames = read_files_from_dir(test_scab_image_path)

for chosen_image in train_healthy_image_filenames:
    gen_images(chosen_image=chosen_image, path=train_healthy_image_path)

for chosen_image in train_rust_image_filenames:
    gen_images(chosen_image=chosen_image, path=train_rust_image_path)

for chosen_image in train_scab_image_filenames:
    gen_images(chosen_image=chosen_image, path=train_scab_image_path)

for chosen_image in valid_healthy_image_filenames:
    gen_images(chosen_image=chosen_image, path=valid_healthy_image_path)

for chosen_image in valid_rust_image_filenames:
    gen_images(chosen_image=chosen_image, path=valid_rust_image_path)

for chosen_image in valid_scab_image_filenames:
    gen_images(chosen_image=chosen_image, path=valid_scab_image_path)

for chosen_image in test_healthy_image_filenames:
    gen_images(chosen_image=chosen_image, path=test_healthy_image_path)

for chosen_image in test_rust_image_filenames:
    gen_images(chosen_image=chosen_image, path=test_rust_image_path)

for chosen_image in test_scab_image_filenames:
    gen_images(chosen_image=chosen_image, path=test_scab_image_path)
