import torch

class GPUInfo:
    def __init__(self):
        """Initialize the class and check if GPU is available."""
        self.gpu_available = torch.cuda.is_available()

    def is_gpu_available(self):
        """Check if GPU is available and print the result."""
        if self.gpu_available:
            print("✅ GPU is available!")
        else:
            print("❌ No GPU detected.")

    def get_gpu_name(self):
        """Get the name of the GPU hardware if available."""
        if self.gpu_available:
            gpu_name = torch.cuda.get_device_name(0)
            print(f"🔹 GPU Name: {gpu_name}")
            return gpu_name
        else:
            print("❌ No GPU detected.")
            return None

    def get_cuda_version(self):
        """Get the CUDA version installed if GPU is available."""
        if self.gpu_available:
            cuda_version = torch.version.cuda
            print(f"🔹 CUDA Version: {cuda_version}")
            return cuda_version
        else:
            print("❌ No GPU detected.")
            return None

    def get_gpu_memory(self):
        """Get GPU memory details: total, used, and free memory in GB."""
        if self.gpu_available:
            total_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)  # Convert bytes to GB
            used_mem = torch.cuda.memory_allocated(0) / (1024**3)
            free_mem = total_mem - used_mem
            print(f"🔹 GPU Memory (Total): {total_mem:.2f} GB")
            print(f"🔹 GPU Memory (Used): {used_mem:.2f} GB")
            print(f"🔹 GPU Memory (Free): {free_mem:.2f} GB")
            return {"total": total_mem, "used": used_mem, "free": free_mem}
        else:
            print("❌ No GPU detected.")
            return None

