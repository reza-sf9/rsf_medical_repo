# MyPackage 🌆

🚀 A Python package containing **various utility modules**, including:
- **FastFolderFinder**: Quickly search for a folder in your system.
- **PIIDDatasetLoader**: Load and preprocess datasets.
- **GPUInfo**: Get detailed GPU information.
- **APILoginManager**: Manage API authentication for Hugging Face & OpenAI.

## **💌 Installation**
### **1️⃣ Install from Source (Recommended)**
If you cloned the repository, install it locally using:
```bash
pip install -e .
```
(The `-e` flag allows you to modify the package without reinstalling.)

---

## **💌 Usage**
### **💡 Importing Modules**
Once installed, you can import modules easily:
```python
from pkg_rsf_medical_proj import FastFolderFinder, PIIDDatasetLoader, GPUInfo, APILoginManager
```

---

### **💡 1️⃣ FastFolderFinder (Search for a Folder)**
Finds a folder starting from the current directory and moving **forward/backward** within a limit.

```python
from pkg_rsf_medical_proj import FastFolderFinder

finder = FastFolderFinder(folder_name="target_folder", forward_limit=10, backward_limit=5, start_offset=2)
result = finder.find_folder()
print(result)  # Returns path if found, else error message
```

#### **✅ Features:**
✔ **BFS Search** for fast folder lookup  
✔ **Limits depth** to prevent unnecessary traversal  
✔ **Custom start position** to optimize search  

---

### **💡 2️⃣ PIIDDatasetLoader (Load Image Dataset)**
Handles structured datasets with **training & validation sets**.

```python
from pkg_rsf_medical_proj import PIIDDatasetLoader

data_dir = "/path/to/dataset"
loader = PIIDDatasetLoader(data_dir)
train_data, val_data = loader.get_datasets()

# Access first sample
sample_0 = train_data[0]
print(sample_0["id"], sample_0["image"], sample_0["label"])
```

#### **✅ Features:**
✔ Loads **images** & **labels** from structured folders  
✔ Displays **progress bar** using `tqdm`  
✔ Returns dataset in **dictionary format**  

---

### **💡 3️⃣ GPUInfo (Check GPU Details)**
Displays information about your **GPU, CUDA version, and memory usage**.

```python
from pkg_rsf_medical_proj import GPUInfo

gpu_info = GPUInfo()
gpu_info.is_gpu_available()  # ✅ Checks if GPU is available
gpu_info.get_gpu_name()  # 🔹 Displays GPU Name
gpu_info.get_cuda_version()  # 🔹 Shows CUDA version
gpu_info.get_gpu_memory()  # 🔹 Shows memory usage
```

#### **✅ Features:**
✔ Detects **CUDA-enabled GPUs**  
✔ Retrieves **total/free/used memory**  
✔ Prints **GPU device name**  

---

### **💡 4️⃣ APILoginManager (Log in to APIs)**
Handles **Hugging Face & OpenAI API authentication**.

```python
from pkg_rsf_medical_proj import APILoginManager

api_manager = APILoginManager(hf_api_key="your_hf_key", openai_api_key="your_openai_key")
api_manager.login_huggingface()  # ✅ Logs into Hugging Face
api_manager.login_openai()  # ✅ Logs into OpenAI
```

#### **✅ Features:**
✔ **Login** to APIs with a single function  
✔ **Automatically sets environment variables**  
✔ **Supports multiple APIs**  

---

## **💌 Dependencies**
This package requires:
- `Pillow` (Image processing)
- `tqdm` (Progress bar)
- `torch` (GPU info)
- `huggingface_hub` (API login)
- `openai` (OpenAI API)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **💌 Contributing**
Feel free to contribute! 🚀  
1. Fork the repo  
2. Create a new branch (`git checkout -b feature-xyz`)  
3. Commit changes (`git commit -m "Added new feature"`)  
4. Push (`git push origin feature-xyz`)  
5. Open a Pull Request  
```


