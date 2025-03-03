import os
from PIL import Image
from tqdm import tqdm  # Import tqdm for the progress bar

class PIIDDatasetLoader:
    def __init__(self, data_dir: str):
        """
        Initializes the dataset loader.
        
        Args:
            data_dir (str): Path to the root directory of the dataset.
        """
        self.data_dir = data_dir
        self.train_dir = os.path.join(data_dir, "tr")
        self.val_dir = os.path.join(data_dir, "te")
        
        # Check if directories exist
        if not os.path.exists(self.train_dir) or not os.path.exists(self.val_dir):
            raise ValueError("Invalid dataset directory structure. 'tr' or 'te' folder not found.")

        # Define image transformations (only resizing, no ToTensor)
        self.transform = lambda img: img.resize((224, 224))  # Keep images as PIL

    def _load_dataset_dict(self, dataset_path: str) -> list:
        """
        Loads dataset from the given directory with a progress bar.
        
        Args:
            dataset_path (str): Path to the dataset folder (train or validation).
        
        Returns:
            list: A list of dictionaries where each dictionary has 'id', 'image', 'label', and 'path'.
        """
        dataset = []  # Store as a list of dictionaries

        # Get all subfolders (class directories)
        class_folders = sorted([f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f))])

        # Count total images for progress tracking
        total_images = sum(len(os.listdir(os.path.join(dataset_path, class_folder))) for class_folder in class_folders)

        with tqdm(total=total_images, desc=f"Loading {os.path.basename(dataset_path)}", unit="img") as pbar:
            for class_folder in class_folders:
                class_path = os.path.join(dataset_path, class_folder)
                class_label = int(class_folder)  # Folder name represents class label
                
                for img_filename in os.listdir(class_path):
                    img_path = os.path.join(class_path, img_filename)
                    
                    try:
                        image = Image.open(img_path).convert("RGB")  # Load image as PIL
                        
                        # Resize the image (keep as PIL, no conversion to tensor)
                        image = self.transform(image)

                        # Append as a dictionary with 'path' included
                        dataset.append({
                            "id": img_filename,
                            "image": image,
                            "label": class_label,
                            "path": img_path  # Store the local image path
                        })

                        pbar.update(1)  # Update progress bar

                    except Exception as e:
                        print(f"Error loading {img_filename}: {e}")
        
        return dataset

    def get_datasets(self) -> tuple:
        """
        Loads both training and validation datasets with progress bars.
        
        Returns:
            tuple: (train_dataset, validation_dataset) where both are lists of dictionaries.
        """
        dataset_tr = self._load_dataset_dict(self.train_dir)
        dataset_val = self._load_dataset_dict(self.val_dir)
        return dataset_tr, dataset_val

