import os
import subprocess
import sys
import re
from pathlib import Path

# ==========================================
# 1. KONFIGURACJA ZASOBÓW STATYCZNYCH
# ==========================================
STATIC_ASSETS = [
    {
        "src": "Lecture_Notes/Physics/html_anim",
        "dest": "docs/Physics/Modern_Physics/html_anim"
    },
]

# ==========================================
# 2. MANIFEST - TYLKO PLIKI DO PRZETWORZENIA!
# Wpisuj tu tylko to, co leży w 'Lecture_Notes' i musi trafić do 'docs'.
# Pliki, które już są w 'docs' (jak Twoje .md), NIE MUSZĄ tu być.
# ==========================================
MANIFEST = [
    # --- PHYSICS (Quarto .qmd) ---
    {"src": "Lecture_Notes/Physics/Language_of_physics.qmd", "dest_dir": "docs/Physics/Mechanics"},
    {"src": "Lecture_Notes/Physics/Mechanics.qmd",           "dest_dir": "docs/Physics/Mechanics"},
    {"src": "Lecture_Notes/Physics/Waves.qmd",               "dest_dir": "docs/Physics/Mechanics"},
    {"src": "Lecture_Notes/Physics/Electromagnetism.qmd",    "dest_dir": "docs/Physics/Electromagnetism"},
    {"src": "Lecture_Notes/Physics/Circuits.qmd",            "dest_dir": "docs/Physics/Electromagnetism"},
    {"src": "Lecture_Notes/Physics/Measurement.qmd",         "dest_dir": "docs/Physics/Experiments_Statistics"},
    {"src": "Lecture_Notes/Physics/Statistics.qmd",          "dest_dir": "docs/Physics/Experiments_Statistics"},
    {"src": "Lecture_Notes/Physics/Quantum_mechanics.qmd",   "dest_dir": "docs/Physics/Modern_Physics"},
    {"src": "Lecture_Notes/Physics/Cosmology.qmd",           "dest_dir": "docs/Physics/Modern_Physics"},
    {"src": "Lecture_Notes/Physics/Relativity.qmd",          "dest_dir": "docs/Physics/Modern_Physics"},
    
    # --- MATHEMATICS ---
    {"src": "Lecture_Notes/Mathematics/Linear_Algebra.qmd",    "dest_dir": "docs/Mathematics"},
    {"src": "Lecture_Notes/Mathematics/Analytic_Geometry.qmd", "dest_dir": "docs/Mathematics"},
    {"src": "Lecture_Notes/Mathematics/Calculus.qmd",          "dest_dir": "docs/Mathematics"},

    # --- DISCRETE MATHEMATICS ---
    {"src": "Lecture_Notes/Discrete_Mathematics/Discrete_Mathematics.qmd", "dest_dir": "docs/Discrete_Mathematics"},

    # UWAGA: Usunąłem stąd pliki .md (np. logistic_equation), które są już w docs.
    # Skoro są w docs, skrypt nie musi ich kopiować/linkować.
    # Walidator poniżej sam je znajdzie w folderze docs.
]

# ==========================================
# NARZĘDZIA
# ==========================================
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    GREY = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_info(msg): print(f"{Colors.OKBLUE}[INFO]{Colors.ENDC} {msg}")
def log_success(msg): print(f"{Colors.OKGREEN}[OK]{Colors.ENDC} {msg}")
def log_skip(msg): print(f"{Colors.GREY}[SKIP]{Colors.ENDC} {msg}")
def log_warn(msg): print(f"{Colors.WARNING}[WARN]{Colors.ENDC} {msg}")
def log_error(msg): print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} {msg}")
def log_section(msg): print(f"\n{Colors.HEADER}{Colors.BOLD}=== {msg} ==={Colors.ENDC}")

PROJECT_ROOT = Path(__file__).parent.resolve()
os.chdir(PROJECT_ROOT)

# ==========================================
# 0. WALIDACJA HYBRYDOWA (Manifest OR Docs)
# ==========================================
def validate_project_structure():
    log_section("WALIDACJA STRUKTURY PROJEKTU")
    mkdocs_path = PROJECT_ROOT / "mkdocs.yml"
    
    if not mkdocs_path.exists():
        log_error("CRITICAL: Brak pliku mkdocs.yml!")
        sys.exit(1)

    # 1. Mapa Manifestu (Co my generujemy/linkujemy?)
    manifest_map = {}
    for entry in MANIFEST:
        src_p = Path(entry['src'])
        dest_d = Path(entry['dest_dir'])
        target_name = src_p.with_suffix('.html').name if src_p.suffix == '.qmd' else src_p.name
        
        # Klucz = relatywna ścieżka w docs
        try:
            rel_dest = (dest_d.relative_to("docs") / target_name).as_posix()
        except ValueError:
            rel_dest = (dest_d / target_name).as_posix() # Fallback
            
        manifest_map[rel_dest] = entry['src']

    # 2. Parsowanie mkdocs.yml i sprawdzanie
    errors_found = []
    pattern = re.compile(r':\s*([^\s#]+\.(?:md|html))')
    
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        match = pattern.search(line)
        if match:
            mkdocs_file_ref = match.group(1).strip() # np. Physics/Mechanics/sp/logistic.md
            
            # --- SCENARIUSZ A: Plik jest w MANIFEŚCIE (generowany/linkowany) ---
            if mkdocs_file_ref in manifest_map:
                source_file = manifest_map[mkdocs_file_ref]
                full_src_path = PROJECT_ROOT / source_file
                if not full_src_path.exists():
                    errors_found.append(f"Linia {i+1}: '{mkdocs_file_ref}'\n      -> Zdefiniowany w Manifest, ale brak pliku źródłowego: '{source_file}'")
                continue # Jest w Manifeście i istnieje -> OK

            # --- SCENARIUSZ B: Plik jest "Natywny" (leży bezpośrednio w docs/) ---
            # Sprawdzamy czy plik fizycznie istnieje w docs/
            direct_path_in_docs = PROJECT_ROOT / "docs" / mkdocs_file_ref
            
            if direct_path_in_docs.exists():
                # To jest OK - plik istnieje statycznie w docs.
                # Nie robimy nic, skrypt go po prostu zaakceptuje.
                pass 
            else:
                # --- BŁĄD: Ani w Manifeście, ani w Docs ---
                errors_found.append(f"Linia {i+1}: '{mkdocs_file_ref}'\n      -> Nie znaleziono ani w MANIFEŚCIE (Lecture_Notes), ani bezpośrednio w folderze 'docs/'!")

    if errors_found:
        log_error(f"Znaleziono {len(errors_found)} błędów spójności!")
        for e in errors_found:
            print(f"{Colors.FAIL} [x] {e}{Colors.ENDC}")
        print(f"\n{Colors.WARNING}Skrypt zatrzymany. Upewnij się, że pliki istnieją w 'docs/' lub są w Manifeście.{Colors.ENDC}")
        sys.exit(1)
    else:
        log_success("Struktura OK: Wszystkie pliki z mkdocs.yml istnieją (w Manifest lub lokalnie w docs).")

# ==========================================
# 3. SMART SYMLINK
# ==========================================
def ensure_smart_symlink(src_abs, dest_link_abs):
    dest_link_abs.parent.mkdir(parents=True, exist_ok=True)
    try:
        target_relative = os.path.relpath(src_abs, dest_link_abs.parent)
    except ValueError:
        target_relative = str(src_abs)

    if dest_link_abs.is_symlink():
        if os.readlink(dest_link_abs) == str(target_relative):
            log_skip(f"Link OK: {dest_link_abs.name}")
            return True
        dest_link_abs.unlink()
    elif dest_link_abs.exists():
        log_warn(f"Plik istnieje (nie link), pomijam: {dest_link_abs.name}")
        return False

    try:
        dest_link_abs.symlink_to(target_relative)
        log_success(f"Link utworzony: {dest_link_abs.name}")
        return True
    except OSError as e:
        log_error(f"Błąd linkowania {dest_link_abs.name}: {e}")
        return False

# ==========================================
# 4. PRZETWARZANIE
# ==========================================
def process_item(item):
    src_path = PROJECT_ROOT / item['src']
    dest_dir_path = PROJECT_ROOT / item['dest_dir']
    
    is_quarto = src_path.suffix == '.qmd'
    target_filename = src_path.with_suffix('.html').name if is_quarto else src_path.name
    target_link_path = dest_dir_path / target_filename
    source_to_link = src_path.with_suffix('.html') if is_quarto else src_path

    if is_quarto:
        print(f"   -> Renderowanie Quarto: {src_path.name}...")
        try:
            subprocess.run(["quarto", "render", src_path.name], cwd=src_path.parent, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            log_error(f"Błąd kompilacji Quarto: {e.stderr}")
            return False
    
    return ensure_smart_symlink(source_to_link, target_link_path)

def process_static_assets():
    log_section("ZASOBY STATYCZNE")
    for item in STATIC_ASSETS:
        src = PROJECT_ROOT / item['src']
        dest = PROJECT_ROOT / item['dest']
        if not src.exists():
            log_error(f"Brak folderu źródłowego: {item['src']}")
            continue
        ensure_smart_symlink(src, dest)

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    
    # --- KONFIGURACJA UŻYTKOWNIKA ---
    FILTER_NAME = "Cosmo"      
    DO_DEPLOY = False     
    # --------------------------------
    
    # 1. Walidacja Hybrydowa
    validate_project_structure()
    
    log_section(f"START (Filtr: '{FILTER_NAME}')")
    
    process_static_assets()
    
    errors = 0
    # Przetwarzamy tylko to, co jest w MANIFEŚCIE (czyli wymaga pracy)
    # Pliki statyczne z 'docs' są ignorowane w tej pętli, bo są już na miejscu.
    for entry in MANIFEST:
        if FILTER_NAME and FILTER_NAME.lower() not in entry['src'].lower():
            continue
        if not process_item(entry):
            errors += 1
            
    log_section("FINAŁ")
    if errors == 0:
        if DO_DEPLOY:
            log_info("Deploy...")
            subprocess.run(["mkdocs", "gh-deploy"], check=True)
        else:
            log_info("Gotowe (Lokalnie).")
    else:
        log_error("Napraw błędy kompilacji.")