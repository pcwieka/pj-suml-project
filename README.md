# PJA_ASI_12c_GR3

## Aplikacja

### Uruchomienie

`python main.py --filename=ObesityDataSet.csv --train_ratio=0.60 --test_ratio=0.35 --validation_ratio=0.05 --seed=50`

Z domyślnymi argumentami:

`python main.py`

## Instrukcja Instalacji Środowiska

## Instalacja Conda na Windows, Linux, i MacOS

Conda to zarządca pakietów i środowisk, który ułatwia instalację, uruchamianie i aktualizację pakietów oraz ich zależności. Jest on szczególnie przydatny w społecznościach Data Science i Machine Learning.

### Instalacja na Windows

1. Pobierz instalator Anaconda dla Windows z [oficjalnej strony](https://www.anaconda.com/products/individual).
2. Uruchom pobrany plik `.exe` i postępuj zgodnie z instrukcjami instalatora.
3. Zaleca się pozostawienie opcji dodania Anacony do zmiennej środowiskowej PATH odznaczonej, ale upewnij się, że zaznaczyłeś opcję zarejestrowania Anacondy jako domyślnej wersji Pythona.

### Instalacja na Linux

1. Pobierz odpowiedni instalator skryptowy Anaconda dla Linuxa z [oficjalnej strony](https://www.anaconda.com/products/individual).
2. Otwórz terminal i przejdź do katalogu, w którym został pobrany instalator.
3. Uruchom skrypt instalacyjny przy użyciu polecenia `bash Anaconda3-2020.02-Linux-x86_64.sh`, zastępując nazwę pliku aktualną wersją pobranego instalatora.
4. Postępuj zgodnie z instrukcjami wyświetlanymi w terminalu.

### Instalacja na MacOS

1. Pobierz instalator Anaconda dla MacOS z [oficjalnej strony](https://www.anaconda.com/products/individual).
2. Możesz wybrać wersję graficzną instalatora lub instalator lini poleceń. Dla instalatora lini poleceń, otwórz terminal, przejdź do folderu z pobranym instalatorem i uruchom go za pomocą `bash Anaconda3-2020.02-MacOSX-x86_64.sh`, dostosowując nazwę do wersji instalatora.
3. Postępuj zgodnie z instrukcjami instalatora.

### Podstawowe polecenia Conda

Po zainstalowaniu Conda, możesz użyć poniższych poleceń do zarządzania środowiskami i pakietami:

- Sprawdź wersję Conda:
  `conda --version`

- Przejdź do katalogu Twojego projektu:
  `cd ścieżka/do/twojego/projektu`

- Utwórz środowisko z pliku `conda.yml`:
  `conda env create -f conda.yml`

- Zaktualizuj środowisko
 `conda env update -f conda.yml`

- Aktywuj środowisko:
  `conda activate nazwa_środowiska`

- Wyświetl listę zainstalowanych pakietów w aktywnym środowisku:
`conda list`

- Zaktualizuj Conda do najnowszej wersji:
`conda update conda`

### Korzystanie z Conda Forge

Conda Forge to społecznościowe repozytorium pakietów dla Conda. Aby zainstalować pakiet z Conda Forge, użyj:

`conda install -c conda-forge nazwa_pakietu`

### Instalacja nowych bibliotek

Conda instalacja biblioteki:

`conda install nazwa_biblioteki`