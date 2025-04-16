import os
import re

def extract_and_save_url():
    possible_paths = [
        os.path.expandvars(r"%userprofile%\AppData\LocalLow\miHoYo\Genshin Impact\output_log.txt"),
        os.path.expandvars(r"%userprofile%\AppData\LocalLow\miHoYo\Genshin Impact\output_log.txt.last"),
    ]

    wishlink_file = ".wishlink"
    wish_url = None
    pattern = re.compile(r"https://webstatic.*?getGachaLog.*?authkey=[^\"&]+")

    for path in possible_paths:
        if os.path.exists(path):
            with open(path, encoding="utf-8", errors="ignore") as file:
                log = file.read()
                match = pattern.search(log)
                if match:
                    wish_url = match.group(0)
                    break

    if wish_url:
        with open(wishlink_file, "w") as f:
            f.write(wish_url)
        print("Wish link extraído e salvo com sucesso!")
    else:
        print("Não foi possível encontrar o link nos logs.")

def get_wish_url():
    if os.path.exists(".wishlink"):
        with open(".wishlink") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
    else:
        extract_and_save_url()
        if os.path.exists(".wishlink"):
            return get_wish_url()
    return None

# Teste
if __name__ == "__main__":
    url = get_wish_url()
    if url:
        print(f"Link encontrado: {url}")
    else:
        print("Nenhum link foi encontrado.")
