from setuptools import setup, find_packages

setup(
    name="rsf_medical_repo",
    version="1.0.1", # Version number (Major.Minor.Patch)
    packages=find_packages(),  # Automatically finds all subpackages
    description="A Python package containing utilities for folder searching, dataset loading, GPU info, and API authentication.",
    author="Reza Saadati Fard",
    author_email="saadatifard.reza@gmail.com",  # Optional
    url="https://github.com/yourusername/mypackage",  # Optional: Add your GitHub link
    install_requires=[
        "Pillow",  # Required for image processing
        "tqdm",  # Required for progress bars
        "torch",  # Required for GPUInfo (PyTorch)
        "huggingface_hub",  # Required for API authentication
        "openai",  # Required for OpenAI API
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust license if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Specify minimum Python version
)

