# PJA_ASI_12c_GR3 - Instrukcja Instalacji Środowiska

Projekt wykorzystuje Pythona w wersji 3.9.6

## Instalacja Minicondy

### Windows:

1. Odwiedź stronę [Minicondy](https://docs.anaconda.com/free/miniconda/index.html) i pobierz instalator dla Windows.
2. Wybierz odpowiedni instalator dla swojej wersji systemu (32-bit lub 64-bit) oraz pożądanej wersji Pythona (3.9.6).
3. Uruchom pobrany plik `.exe` i postępuj zgodnie z instrukcjami na ekranie, aby zakończyć instalację. Podczas instalacji zwróć uwagę na opcję dodania Minicondy do zmiennej środowiskowej `PATH` (opcjonalne).

### Linux:

Wykonaj w terminalu:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# lub, jeśli nie masz wget:
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

### macOS:

W terminalu wykonaj:

```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
chmod +x Miniconda3-latest-MacOSX-x86_64.sh
./Miniconda3-latest-MacOSX-x86_64.sh
```

## Sprawdzenie Wersji Condy

Po instalacji sprawdź wersję Condy:

conda --version

## Przygotowanie Środowiska

### Przygotowanie Środowiska Conda

W terminalu przejdź do katalogu projektu:

cd nazwa-repozytorium

Aktywuj utworzone środowisko:

conda env create -f environment.yml

conda activate nazwasrodowiska

conda list

### Sprawdź zainstalowane pakiety:

conda list

## Aktualizacja Condy

conda update conda
