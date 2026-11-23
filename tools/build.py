#!/usr/bin/env python3
"""Costruisce i dati pubblici del sito a partire dall'Excel degli annunci.

Legge:
  - foglio "Annunci" : una riga per oggetto (testi, prezzo, stato, link)
  - foglio "Foto"    : una riga per foto (file, ordine, rotazione, ritaglio, sfocature)

Scrive:
  - site/data/annunci.json  (solo campi pubblici: mai prezzo minimo, note interne, "da verificare")
  - site/foto/<ID>/<n>.jpg  (foto ricentrate, ridimensionate, senza EXIF)

Uso (da Windows, dalla cartella del repository):
  python tools/build.py --excel "C:\\...\\Soffitta\\Annunci_soffitta.xlsx" --foto-dir "C:\\...\\Soffitta"

Dipendenze: pip install -r tools/requirements.txt
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

from openpyxl import load_workbook
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageStat

LARGHEZZA, ALTEZZA = 1100, 825          # tutte le foto finali sono 4:3
MARGINE_RITAGLIO = 0.05                  # margine attorno all'oggetto
RIEMPIMENTO = 0.94                       # quanto del riquadro occupa l'oggetto
STATI_OGGETTO = {"ottimo": "Ottimo", "buono": "Buono", "discreto": "Discreto", "accettabile": "Accettabile"}
PIATTAFORME = ["eBay", "Vinted", "Subito", "Wallapop", "Facebook Marketplace"]


def testo(v):
    return "" if v is None else str(v).strip()


def numero(v):
    if v is None or str(v).strip() == "":
        return None
    try:
        n = float(str(v).replace(",", ".").replace("€", "").strip())
    except ValueError:
        return None
    return int(n) if n == int(n) else n


def leggi_foglio(wb, nome, obbligatorio=True):
    if nome not in wb.sheetnames:
        if obbligatorio:
            sys.exit(f"Manca il foglio '{nome}' nell'Excel.")
        return []
    righe = list(wb[nome].iter_rows(values_only=True))
    if not righe:
        return []
    intest = [testo(c) for c in righe[0]]
    out = []
    for r in righe[1:]:
        if all(c is None or testo(c) == "" for c in r):
            continue
        out.append({intest[i]: r[i] for i in range(len(intest)) if intest[i]})
    return out


def specifiche(valore):
    """'Etichetta: valore' una per riga (o separate da ';')."""
    out = []
    for riga in re.split(r"[\n;]+", testo(valore)):
        riga = riga.strip()
        if not riga:
            continue
        if ":" in riga:
            a, b = riga.split(":", 1)
            out.append([a.strip(), b.strip()])
        else:
            out.append(["", riga])
    return out


def regioni(valore):
    """Regioni da sfocare: 'LxA+X+Y' separate da ';' (coordinate sull'immagine già ruotata)."""
    out = []
    for r in re.split(r"[;\n]+", testo(valore)):
        m = re.fullmatch(r"\s*(\d+)x(\d+)\+(\d+)\+(\d+)\s*", r)
        if m:
            w, h, x, y = map(int, m.groups())
            out.append((x, y, x + w, y + h))
    return out


def ritaglio(valore, dim):
    m = re.fullmatch(r"\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*", testo(valore))
    if not m:
        return None
    x0, y0, x1, y1 = map(int, m.groups())
    w, h = dim
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(w, x1), min(h, y1)
    return (x0, y0, x1, y1) if x1 > x0 and y1 > y0 else None


def elabora_foto(sorgente, destinazione, rotazione=0, box=None, sfoca=()):
    img = ImageOps.exif_transpose(Image.open(sorgente)).convert("RGB")
    if rotazione:
        # gli angoli lasciati vuoti dalla rotazione si riempiono con il colore tipico della foto (non nero)
        riempi = tuple(int(v) for v in ImageStat.Stat(img.resize((64, 64))).median)
        img = img.rotate(-rotazione, expand=True, fillcolor=riempi)   # gradi in senso orario
    for (x0, y0, x1, y1) in sfoca:
        zona = img.crop((x0, y0, x1, y1)).filter(ImageFilter.GaussianBlur(30))
        img.paste(zona, (x0, y0))
    w, h = img.size
    if box is None:
        box = (0, 0, w, h)
    x0, y0, x1, y1 = box
    mx, my = int((x1 - x0) * MARGINE_RITAGLIO), int((y1 - y0) * MARGINE_RITAGLIO)
    x0, y0, x1, y1 = max(0, x0 - mx), max(0, y0 - my), min(w, x1 + mx), min(h, y1 + my)
    primo = img.crop((x0, y0, x1, y1))
    primo = ImageOps.contain(primo, (int(LARGHEZZA * RIEMPIMENTO), int(ALTEZZA * RIEMPIMENTO)), Image.LANCZOS)
    sfondo = ImageOps.fit(img, (LARGHEZZA, ALTEZZA), Image.LANCZOS).filter(ImageFilter.GaussianBlur(22))
    sfondo = ImageEnhance.Brightness(sfondo).enhance(0.88)
    sfondo.paste(primo, ((LARGHEZZA - primo.width) // 2, (ALTEZZA - primo.height) // 2))
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    sfondo.save(destinazione, "JPEG", quality=80, optimize=True)      # senza EXIF


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--excel", required=True, help="percorso di Annunci_soffitta.xlsx")
    ap.add_argument("--foto-dir", required=True, help="cartella che contiene le foto originali")
    ap.add_argument("--site", default=str(Path(__file__).resolve().parent.parent / "site"), help="cartella del sito")
    ap.add_argument("--non-pulire", action="store_true", help="non cancellare le foto di oggetti non più pubblicati")
    a = ap.parse_args()

    site, foto_dir = Path(a.site), Path(a.foto_dir)
    wb = load_workbook(a.excel, data_only=True)
    annunci = leggi_foglio(wb, "Annunci")
    foto = leggi_foglio(wb, "Foto", obbligatorio=False)

    foto_per_id = {}
    for f in foto:
        foto_per_id.setdefault(testo(f.get("ID")), []).append(f)

    avvisi, pubblicati, ids = [], [], set()
    for r in annunci:
        oid = testo(r.get("ID"))
        titolo = testo(r.get("Titolo"))
        if not oid or not titolo:
            continue
        if oid in ids:
            avvisi.append(f"{oid}: ID duplicato, riga ignorata")
            continue
        ids.add(oid)
        stato_vendita = testo(r.get("Stato vendita")).lower()
        if stato_vendita != "in vendita":
            continue                                   # bozze e venduti non vanno sul sito
        prezzo = numero(r.get("Prezzo"))
        if prezzo is None:
            avvisi.append(f"{oid} {titolo}: manca il prezzo, non pubblicato")
            continue
        if testo(r.get("Da verificare")):
            avvisi.append(f"{oid} {titolo}: ha dati 'Da verificare' ({testo(r.get('Da verificare'))[:60]})")

        # foto pubbliche, in ordine
        righe_foto = [f for f in foto_per_id.get(oid, []) if testo(f.get("Pubblica", "Sì")).lower() not in ("no", "n", "false", "0")]
        righe_foto.sort(key=lambda f: (numero(f.get("Ordine")) is None, numero(f.get("Ordine")) or 0))
        foto_out = []
        for n, f in enumerate(righe_foto, 1):
            sorgente = foto_dir / testo(f.get("File"))
            if not sorgente.is_file():
                avvisi.append(f"{oid}: foto non trovata: {sorgente}")
                continue
            dest = site / "foto" / oid / f"{n}.jpg"
            try:
                tmp = Image.open(sorgente)
                dim = ImageOps.exif_transpose(tmp).size
                rot = int(numero(f.get("Rotazione")) or 0) % 360
                if rot in (90, 270):
                    dim = (dim[1], dim[0])
                elabora_foto(sorgente, dest, rot, ritaglio(f.get("Ritaglio"), dim), regioni(f.get("Sfoca")))
            except Exception as e:                      # file corrotto o formato non leggibile
                avvisi.append(f"{oid}: errore sulla foto {sorgente.name}: {e}")
                continue
            foto_out.append(f"foto/{oid}/{n}.jpg")
        if not foto_out:
            avvisi.append(f"{oid} {titolo}: nessuna foto pubblica, non pubblicato")
            continue

        stato = STATI_OGGETTO.get(testo(r.get("Stato")).lower(), "Ottimo")
        lotto = numero(r.get("Quantità lotto"))
        piattaforme = [{"name": p, "url": testo(r.get(p))} for p in PIATTAFORME if testo(r.get(p)).startswith("http")]
        pubblicati.append({
            "id": oid,
            "title": titolo,
            "subtitle": testo(r.get("Sottotitolo")),
            "description": testo(r.get("Descrizione")),
            "category": testo(r.get("Categoria")),
            "subcategory": testo(r.get("Sottocategoria")),
            "specs": specifiche(r.get("Specifiche")),
            "price": prezzo,
            "condition": stato,
            "lot": int(lotto) if lotto and lotto > 1 else None,
            "photos": foto_out,
            "platforms": piattaforme,
        })

    for oid in foto_per_id:
        if oid not in ids:
            avvisi.append(f"foglio Foto: l'ID '{oid}' non esiste nel foglio Annunci, righe ignorate")

    (site / "data").mkdir(parents=True, exist_ok=True)
    with open(site / "data" / "annunci.json", "w", encoding="utf-8") as fh:
        json.dump({"generated": datetime.date.today().isoformat(), "items": pubblicati}, fh, ensure_ascii=False, indent=1)

    if not a.non_pulire:
        attivi = {p["id"] for p in pubblicati}
        base = site / "foto"
        if base.is_dir():
            for d in base.iterdir():
                if d.is_dir() and d.name not in attivi:
                    shutil.rmtree(d)

    print(f"Annunci pubblicati: {len(pubblicati)}")
    for av in avvisi:
        print("ATTENZIONE:", av)


if __name__ == "__main__":
    main()
