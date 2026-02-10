import os
import subprocess
import sys
from pathlib import Path

# ==========================================
# 1. KONFIGURACJA ZASOBÓW STATYCZNYCH (NOWOŚĆ)
# Tutaj wpisz foldery z animacjami/obrazkami, które mają być dostępne
# pod konkretnymi ścieżkami w docs/.
# ==========================================
STATIC_ASSETS = [
    # Rozwiązanie Twojego błędu 404:
    # Źródło: Lecture_Notes/Physics/html_anim
    # Cel:    docs/Physics/Modern_Physics/html_anim (bo tam szuka przeglądarka z poziomu Cosmology.html)
    {
        "src": "Lecture_Notes/Physics/html_anim",
        "dest": "docs/Physics/Modern_Physics/html_anim"
    },
    # Jeśli animacje są też potrzebne w Mechanice (np. dla fal):
    {
        "src": "Lecture_Notes/Physics/html_anim",
        "dest": "docs/Physics/Mechanics/html_anim"
    },
     # Jeśli animacje są też potrzebne w Elektromagnetyzmie:
    {
        "src": "Lecture_Notes/Physics/html_anim",
        "dest": "docs/Physics/Electromagnetism/html_anim"
    },
]

# ==========================================
# 2. MANIFEST PLIKÓW QUARTO
# Źródło (.qmd) -> Cel (katalog w docs/)
# ==========================================
MANIFEST = [
    # --- PHYSICS: Mechanics ---
    {"src": "Lecture_Notes/Physics/Language_of_physics.qmd", "dest_dir": "docs/Physics/Mechanics"},
    {"src": "Lecture_Notes/Physics/Mechanics.qmd",           "dest_dir": "docs/Physics/Mechanics"},
    {"src": "Lecture_Notes/Physics/Waves.qmd",               "dest_dir": "docs/Physics/Mechanics"},
    
    # --- PHYSICS: Electromagnetism ---
    {"src": "Lecture_Notes/Physics/Electromagnetism.qmd",    "dest_dir": "docs/Physics/Electromagnetism"},
    {"src": "Lecture_Notes/Physics/Circuits.qmd",            "dest_dir": "docs/Physics/Electromagnetism"},
    
    # --- PHYSICS: Experiments ---
    {"src": "Lecture_Notes/Physics/Measurement.qmd",         "dest_dir": "docs/Physics/Experiments_Statistics"},
    {"src": "Lecture_Notes/Physics/Statistics.qmd",          "dest_dir": "docs/Physics/Experiments_Statistics"},

    # --- PHYSICS: Modern Physics ---
    {"src": "Lecture_Notes/Physics/Quantum_mechanics.qmd",   "dest_dir": "docs/Physics/Modern_Physics"},
    {"src": "Lecture_Notes/Physics/Cosmology.qmd",           "dest_dir": "docs/Physics/Modern_Physics"},
    {"src": "Lecture_Notes/Physics/Relativity.qmd",          "dest_dir": "docs/Physics/Modern_Physics"},

    # --- MATHEMATICS ---
    {"src": "Lecture_Notes/Mathematics/Linear_Algebra.qmd",    "dest_dir": "docs/Mathematics"},
    {"src": "Lecture_Notes/Mathematics/Analytic_Geometry.qmd", "dest_dir": "docs/Mathematics"},
    {"src": "Lecture_Notes/Mathematics/Calculus.qmd",          "dest_dir": "docs/Mathematics"},

    # --- DISCRETE MATHEMATICS ---
    {"src": "Lecture_Notes/Discrete_Mathematics/Discrete_Mathematics.qmd", "dest_dir": "docs/Discrete_Mathematics"},

    # --- PROBABILISTIC METHODS ---
    {"src": "Lecture_Notes/Probabilistic_methods/introduction.qmd", "dest_dir": "docs/Probabilistic_methods"},
]

# ==========================================
# NARZĘDZIA I KOLORY
# ==========================================
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    GREY = '\033[90m' # Dla info o pominięciu
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
# INTELIGENTNE LINKOWANIE
# ==========================================
def ensure_smart_symlink(src_path, link_path):
    """
    Tworzy symlink TYLKO jeśli nie istnieje lub jest błędny.
    Nie dotyka pliku, jeśli link jest poprawny.
    """
    # Upewnij się, że katalog nadrzędny linku istnieje
    link_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Oblicz relatywną ścieżkę (target), na którą link ma wskazywać
    # Np. ../../../Lecture_Notes/Physics/html_anim
    try:
        target_relative = os.path.relpath(src_path, link_path.parent)
    except ValueError:
        # Na Windows czasem problem przy różnych dyskach, fallback do absolutnej
        target_relative = str(src_path)

    # 1. Sprawdź czy cokolwiek istnieje pod ścieżką linku
    if link_path.is_symlink():
        # Pobierz, gdzie ten link aktualnie wskazuje
        current_target = os.readlink(link_path)
        
        # Jeśli wskazuje tam gdzie chcemy -> NIC NIE RÓB
        if current_target == str(target_relative):
            log_skip(f"Link poprawny: {link_path.name}")
            return True
        else:
            log_warn(f"Naprawa linku (zły cel): {link_path.name}")
            link_path.unlink() # Usuwamy błędny link
            
    elif link_path.exists():
        log_warn(f"Pod ścieżką '{link_path.name}' istnieje zwykły plik/katalog! Pomijam.")
        return False

    # 2. Tworzenie linku (tylko jeśli go nie ma lub został usunięty)
    try:
        link_path.symlink_to(target_relative)
        log_success(f"Utworzono link: {link_path.name} -> {target_relative}")
        return True
    except OSError as e:
        log_error(f"Błąd tworzenia linku {link_path.name}: {e}")
        return False

# ==========================================
# FUNKCJE GŁÓWNE
# ==========================================
def validate_mkdocs_entry(html_filename, dest_dir):
    mkdocs_file = PROJECT_ROOT / "mkdocs.yml"
    if not mkdocs_file.exists(): return False
    try:
        rel_path = Path(dest_dir).relative_to("docs") / html_filename
        search_pattern = str(rel_path).replace("\\", "/")
    except ValueError:
        search_pattern = html_filename
    
    with open(mkdocs_file, 'r', encoding='utf-8') as f:
        return search_pattern in f.read()

def process_static_assets():
    """Obsługa folderów z animacjami itp."""
    log_section("ZASOBY STATYCZNE (HTML_ANIM)")
    for item in STATIC_ASSETS:
        src = PROJECT_ROOT / item['src']
        dest = PROJECT_ROOT / item['dest']
        
        if not src.exists():
            log_error(f"Katalog źródłowy nie istnieje: {item['src']}")
            continue
            
        ensure_smart_symlink(src, dest)

def process_quarto_item(item):
    """Kompilacja i linkowanie plików .qmd"""
    src_path = PROJECT_ROOT / item['src']
    dest_dir_path = PROJECT_ROOT / item['dest_dir']
    
    qmd_name = src_path.name
    html_name = src_path.with_suffix('.html').name
    
    if not src_path.exists():
        log_error(f"Brak pliku: {src_path}")
        return False

    # Walidacja mkdocs.yml (tylko Warning)
    if not validate_mkdocs_entry(html_name, item['dest_dir']):
        log_warn(f"Brak wpisu w mkdocs.yml dla: {html_name}")

    # Kompilacja Quarto (zawsze, bo user pracuje nad treścią)
    print(f"   -> Renderowanie: {qmd_name}...")
    try:
        subprocess.run(
            ["quarto", "render", qmd_name],
            cwd=src_path.parent,
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        log_error(f"Błąd Quarto: {e.stderr}")
        return False

    # Linkowanie wynikowego HTML (Smart Link)
    source_html = src_path.with_suffix('.html')
    target_link = dest_dir_path / html_name
    
    return ensure_smart_symlink(source_html, target_link)

def run_deploy():
    log_section("PUBLIKACJA (DEPLOY)")
    try:
        subprocess.run(["mkdocs", "gh-deploy"], check=True)
        log_success("Opublikowano!")
    except subprocess.CalledProcessError:
        log_error("Błąd mkdocs gh-deploy.")

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    
    # --- KONFIGURACJA STEROWANIA ---
    FILTER_NAME = "Cosmo"   # Np. "Cosmology" lub puste "" dla wszystkich
    DO_DEPLOY = False       # True = publikuj na GitHub
    # -------------------------------
    
    log_section(f"START (Filtr: '{FILTER_NAME}')")
    
    # 1. Najpierw ogarniamy zasoby statyczne (żeby foldery istniały)
    process_static_assets()
    
    # 2. Potem pliki Quarto
    log_section("PLIKI QUARTO")
    processed, errors = 0, 0
    
    for entry in MANIFEST:
        if FILTER_NAME and FILTER_NAME.lower() not in entry['src'].lower():
            continue
            
        if not process_quarto_item(entry):
            errors += 1
        processed += 1

    # Podsumowanie
    print("-" * 40)
    if errors == 0:
        log_success(f"Przetworzono: {processed}. Brak błędów.")
        if DO_DEPLOY: run_deploy()
    else:
        log_error(f"Błędy: {errors}. Deploy wstrzymany.")