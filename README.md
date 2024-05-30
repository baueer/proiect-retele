
10.  Rutarea mesajelor:
-   Server-ul gestioneaza o lista de destinatari, fiecare destinatar fiind identificat printr-un nume unic;
-   Clientul se conecteaza la server si trimite un mesaj, in care precizeaza destinatarul, emitentul, subiectul si textul mesajului;
-   In cazul in care destinatarul apare in lista gestionata de server, acesta va salva mesajul intr-un director local cu numele destinatarului, generand un nume de fisier bazat pe momentul salvarii mesajului;
-   In cazul in care destinatarul nu apare in lista, server-ul are o lista de alte server-e pe care le interogheaza in momentul primirii unui mesaj, pentru a stabili catre ce alt server trebuie sa ruteze meajul;
-   Server-ul confirma clientului acceptarea mesajului;
-   Server-ul poate primi pe aceeasi conexiune mesaje de la alte server-e pentru a verifica daca un anumit destinatar se gaseste in lista sa;
-   In cazul in care destinatarul cautat nu se gaseste in lista sa, server-ul procedeaza similar livrarii unui mesaj interogand lista de server-e la care se poate conecta direct.
