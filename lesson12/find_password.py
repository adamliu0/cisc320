"""
Dr. Bart's script to try and figure out the passwords stored in the "mysterious_drive.zip" file.

Some parts are incomplete! Please help me by filling in the blanks.
"""

from zipfile import Path
import json


def search_zip(folder: Path, file_type: str) -> list[Path]:
    """
    Recursively search a zip file by iterating through its files and subfolders.
    Paths are basically just fancy strings with some extra features, like checking
    if they are directories or files.

    Args:
        folder (Path): A ZipFile Path that represents a folder.
        file_type (str): The extension to check against the individual files
    Returns:
        list[Path]: All the matched Paths
    """
    result = []
    for folder_item in folder.iterdir():
        # Is it a directory?
        if folder_item.is_dir():
            result.extend(search_zip(folder_item, file_type))
        # Is it a file?
        if folder_item.is_file():
            if folder_item.name.endswith(file_type):
                result.append(folder_item)
    return result


def access_path(data: dict or any, path: list[str]) -> any:
    """
    Recursively access each key from `path` that is stored in `data`.

    Args:
        data (dict or any): The dictionary to crack open and access, or the final data to return.
        path (list[str]): A sequence of keys available at each nested level of the `data` dictionary.
    Returns:
        any: The data stored in the last nested level of the `data` dictionary.
    """
    if path:
        key = path[0]
        remaining_path = path[1:]
        return access_path(data[key], remaining_path)
    return data


def binary_search_time(values: list[any], low: int, high: int, target: int) -> any:
    """
    Recursively search in a list of values, repeatedly dividing the search space in half.
    Ultimately returns the element of the list that has a `time` field closest to the
    given `target`.

    Args:
         values (list[any]): A list of any type of values, to be searched.
         low (int): The lowest possible index to consider from the list
         high (int): The highest possible index to consider from the list
         target (int): The target index
     Returns:
         any: The data stored in the target element.
    """
    if low <= high:
        middle_index = (low+high) // 2
        middle_value = values[middle_index]['time']
        if middle_value < target:
            return binary_search_time(values, middle_index+1, high, target)
        elif middle_value > target:
            return binary_search_time(values, low, middle_index-1, target)
        else:
            return values[middle_index]
    return values[high]


def solve(maze: str, at: int, visited: set[int]) -> str:
    """
    Recursively explores the maze, following the arrows until the final emoji is reached.
    
    The directional emoji are:
     → right
     ↕ left AND right
     ← left
     ↖ left twice
     ↗ right twice

    Args:
        maze (str): The one-dimensional string maze.
        at (int): The current location in the maze. Should default to 0.
        visited (set[int]): A set of previously visited nodes.
    Returns:
        str: The final emoji at the end of the maze.
    """

    if len(visited) == 0:
        visited = set()
    visited.add(at)

    if maze[at] == '→':
        at = at + int(maze[at+1])
        #return solve(maze, at, visited)
    
    elif maze[at] == '↕':
        if at+1 not in visited:
            moveval = maze[at+1]
            visited.add(at+1)
            at = at - int(moveval)
        else:
            moveval = maze[at+2]
            visited.add(at+2)
            at = at + int(moveval)
    
    # Recursively follow the maze
        if at not in visited:
            return solve(maze, at=at, visited=visited)
        else:
            return solve(maze, at=visited.pop(), visited=visited)
    
    if maze[at] == '←':
        at = at - int(maze[at+1])
        #return solve(maze, at, visited)
    
    if maze[at] == '↖':
        return solve(maze, at = at - int(maze[at+1]), visited = visited) or solve(maze, at = at - int(maze[at+2]), visited = visited)
    
    if maze[at] == '↗':
        return solve(maze, at = at + int(maze[at+1]), visited = visited) or solve(maze, at = at + int(maze[at+2]), visited = visited)
    
    if maze[at] == 'X':
        return solve(maze, at=visited.pop(), visited = visited)

    return visited[-1]


def main(location: list[str], target_time: int):
    """
    The main function that runs all the other parts of the program, in the proper sequence.
    This part of the program is fine - no fixes needed!

    Args:
        location (list[str]): A sequence of locations and sublocations that will navigate
            us through the Security JSON file.
        target_time (int): The current time we are expecting to arrive at the location.
    Prints:
        The final, single emoji password
    """
    # Load the Zip File
    ZIP_FILE_NAME = 'mysterious_drive.zip'
    root = Path(ZIP_FILE_NAME)
    # Search the Zip File
    #security_file = search_zip(root, ".json")[0]
    security_file = search_zip(root, ".py")[0]
    # Read the JSON file
    #security = json.loads(security_file.read_bytes())
    # Access the JSON path
    #passwords = access_path(security, location)
    # Binary Search the Times
    #time_data = binary_search_time(passwords, 0, len(passwords)-1, target_time)
    #maze = time_data['password']
    # Solve the 1d Maze
    #answer = solve(maze, 0, set())
    # Print the Answer
    #print(answer)
    print(security_file)


if __name__ == '__main__':
    main(["Basement 2", "Quadrant A", "Region 1", "North"], 6)