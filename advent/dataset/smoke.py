import numpy as np

from advent.dataset.base_dataset import BaseDataset


class SmokeDataSet(BaseDataset):
    def __init__(self, root, list_path, set='all',
                 max_iters=None, crop_size=(321, 321), mean=(128, 128, 128)):
        super().__init__(root, list_path, set, max_iters, crop_size, None, mean)
        self.class_names = np.array(['background', 'smoke'], dtype=np.str)
      

    def get_metadata(self, name):
        img_file = self.root / 'images' / name
        label_file = self.root / 'masks' / name
        return img_file, label_file

    def __getitem__(self, index):
        img_file, label_file, name = self.files[index]
        image = self.get_image(img_file)
        label = self.get_labels(label_file)
    
#         label_copy = np.ones(label.shape, dtype=np.float32)
#         label_copy[label != 0] = 0
        label_copy = label.copy()
        label_copy[label == 255] = 1
        image = self.preprocess(image)
        return image.copy(), label_copy.copy(), np.array(image.shape), name
