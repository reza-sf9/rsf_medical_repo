import os
from collections import deque

class FastFolderFinder:
    def __init__(self, folder_name: str, forward_limit: int = 10, backward_limit: int = 10, backward_start_offset: int = 0):
        """
        Initializes the FastFolderFinder class.
        
        Args:
            folder_name (str): The folder name to search for.
            forward_limit (int): Maximum depth to search forward.
            backward_limit (int): Maximum number of parent directories to move back.
            backward_start_offset (int): Number of levels to move up before starting the search (default: 0).
        """
        self.folder_name = folder_name
        self.forward_limit = forward_limit
        self.backward_limit = backward_limit
        self.backward_start_offset = backward_start_offset  # Steps to move up before starting search

    def _bfs_search(self, start_dir: str) -> str:
        """
        Performs a Breadth-First Search (BFS) to find the target folder.

        Args:
            start_dir (str): The directory from where the search starts.

        Returns:
            str: Path to the found folder or None if not found.
        """
        queue = deque([(start_dir, 0)])  # (current_dir, depth)

        while queue:
            current_dir, depth = queue.popleft()
            if depth > self.forward_limit:
                continue  # Skip if beyond forward limit

            try:
                for item in os.listdir(current_dir):
                    item_path = os.path.join(current_dir, item)

                    if os.path.isdir(item_path) and item == self.folder_name:
                        return item_path  # Folder found!

                    # Add subdirectories to the search queue
                    if os.path.isdir(item_path):
                        queue.append((item_path, depth + 1))
            except PermissionError:
                pass  # Skip directories without permission

        return None  # Not found within forward limit

    def find_folder(self) -> str:
        """
        Searches for the folder using BFS in forward branches and backtracking.

        Returns:
            str: Path to the found folder or a message if not found.
        """
        current_dir = os.getcwd()  # Start from the current directory

        # Move `backward_start_offset` steps up before beginning the search
        for step in range(self.backward_start_offset):
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:  # Reached the root
                break
            current_dir = parent_dir

        print(f"Starting search from: {current_dir}")

        # Try moving forward first
        found_path = self._bfs_search(current_dir)
        if found_path:
            return found_path

        # Move backward and repeat BFS
        for step in range(1, self.backward_limit + 1):
            parent_dir = os.path.dirname(current_dir)
            if parent_dir == current_dir:  # Reached the root
                break

            current_dir = parent_dir  # Move up
            print(f"Moving back to: {current_dir} (Step {step})")
            found_path = self._bfs_search(current_dir)
            if found_path:
                return found_path

        return f"Folder '{self.folder_name}' not found within the given search limits."

# Example Usage
if __name__ == "__main__":
    finder = FastFolderFinder(folder_name="target_folder", forward_limit=10, backward_limit=5, backward_start_offset=2)
    result = finder.find_folder()
    print(result)
