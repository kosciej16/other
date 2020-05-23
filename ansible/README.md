Zadanie:

Krok 'Make sure python3-venv is installed' i następne muszą być wykonywane dopiero po odpaleniu zadań robiących odpowiedni setup.

Prawdopodobnie będzie to rola, której będzie obsługiwała dwie rzeczy (użytkownik wybiera jedną albo drugą):
1) Skopiowanie plików z danego katalogu do 'siebie' (czy do miejsca w repozytorium).
2) Instalację odpowiednich paczek i skopiowanie plików z repozytorium w odpowiednie miejsce na dysku.

W katalogu 'pliki' znajdują się przykładowe pliki, które należy skopiować.

Wyżej wspomniany setup to krok 2, krok pierwszy jest robiony tylko, gdy robione są zmiany w plikach na dysku i uzytkownik chce je wypchnąć.

Trudności:
Rola ta ma się odpalać tylko, gdy użytkownik jawnie ją wywoła (tj. jeśli ktoś chce mieć support pythona w neovimie, to odpala playbook
z opdowiednim parametrem). Prawdopodobnie trzeba użyć tagu never, ale nie mam pewności.

Niektóre pliki podczas kopiowania muszę zostać zmienione - jak w przypadku pliku test.json. Przy kopiowaniu z repo na dysk należy zamienić
ścieżki znajdujące się tam na prawdziwe ścieżki zainstalowanych aplikacji (można je zdobyć robiąc np. which <nazwa aplikacji>).
Przy kopiowaniu z dysku na repo pomocne może być podmienienie wartości tych ścieżek na jakieś zmienne. Może ansible template pomoże.
Plik add.yml zawiera przykład tego, jak można dodać coś do jsona w ansible. Być może da się to zrobić lepiej.

Krok 1 będzie stosowany niemalże w każdej roli/playbooku. Jeśli się da, uniknąć duplikacji kodu (idealnie - tylko jedna lista par na każdy krok 1)

