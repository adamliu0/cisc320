from zipfile import Path
import password_hash

#worked with Rohan Yarlagadda (rohany@udel.edu)
#CRACKED PASSWORD: AdaIsGoodDog

def search_zip(folder: Path, file_type: str) -> list[Path]:
    result = []
    for folder_item in folder.iterdir():
        if folder_item.is_dir():
            result.extend(search_zip(folder_item, file_type))
        if folder_item.is_file():
            if folder_item.name.endswith(file_type):
                result.append(folder_item)
    return result

def find_password(dictionary: list[str], password: list[str], target_value = 81445731, depth = 0) -> str:
    if password_hash.simple_hash("".join(password), 10**9) == 81445731:
        return "".join(password)
    else:
        if depth < 4:
            for word in dictionary:
                password.append(word)
                x = find_password(dictionary, password, target_value, depth + 1)
                password.pop()
                if x is not None:
                    return x

def main():
    #this is how we find where password_hash.py and dictionary.txt are located
    #ZIP_FILE_NAME = 'mysterious_drive.zip'
    #root = Path(ZIP_FILE_NAME)
    #password_hash_path = search_zip(root, ".py")[0]
    #print(password_hash_path)

    with open("dictionary.txt", "r") as file:
        words = file.read().splitlines()
    print(find_password(words, [], 81445731))
    
    

if __name__ == '__main__':
    main()