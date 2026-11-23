# La soffitta del Cherioni

Vetrina online degli oggetti usati di casa: foto, descrizione, specifiche, prezzo e link agli annunci sulle piattaforme di vendita.

- **Sito**: cartella `site/` (HTML statico, pubblicato su Netlify).
- **Come si aggiorna**: si modifica l'Excel degli annunci e si lancia "aggiorna il sito" da Claude Code (`.claude/skills/aggiorna-sito`), oppure a mano con `python tools/build.py --excel ... --foto-dir ...`.
- **Disegno e regole**: `docs/PIANO.md` e `CLAUDE.md`.
- **Dati ancora da controllare**: `docs/DA_VERIFICARE.md`.

L'Excel degli annunci, le foto originali e il prezzo minimo non stanno in questo repository (che è pubblico): restano su OneDrive.
