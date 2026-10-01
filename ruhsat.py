#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmus Sarki Ruhsat Dairesi.

Gercekten calisir. Bilimsel oldugu iddia edilmez.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import date

DAMGA = "MUHUR-2026-10-01-TENTIVORY-DOLMUS"
IMZA = "Kayyum Grok"
ISIM = "Tentivory"
TARIH = "2026-10-01"


def desibel(sanatci: str, sarki: str) -> int:
    ham = hashlib.sha256(f"{sanatci}|{sarki}".encode("utf-8")).hexdigest()
    return 62 + (int(ham[:2], 16) % 29)


def ruhsat_no(sanatci: str, sarki: str) -> str:
    kisalt = hashlib.md5(f"{sanatci}-{sarki}".encode("utf-8")).hexdigest()[:6].upper()
    return f"DSR-{date.today().strftime('%Y%m%d')}-{kisalt}"


def ceza(db: int) -> str:
    if db < 70:
        return "ceza yok, yolcu uyuyabilir"
    if db < 80:
        return "bir durak erken inme veya cay ismarlama"
    if db < 88:
        return "sofor kaş kaldirma hakkini kullanir, sarki bir kez kisilir"
    return "bluetooth baglantisi mahkeme kararina kadar askida (mahkeme = on koltuk)"


def tutanak(sanatci: str, sarki: str) -> str:
    db = desibel(sanatci, sarki)
    no = ruhsat_no(sanatci, sarki)
    itiraz = "kabul" if db % 2 == 0 else "red (dolmus kalkti)"
    cizgi = "=" * 46
    return "\n".join(
        [
            cizgi,
            "DOLMUS SARKI RUHSAT TUTANAGI",
            cizgi,
            f"Ruhsat no : {no}",
            f"Sanatci   : {sanatci}",
            f"Sarki     : {sarki}",
            f"Desibel   : {db} dB (tahmini, kulak ile olculdu)",
            f"Itiraz    : {itiraz}",
            f"Yaptirim  : {ceza(db)}",
            "Yolcu imza: ________________  (bos kalmasin diye cizildi)",
            "Sofor not : birazdan kalkiyoruz abi",
            cizgi,
            f"DAMGA: {DAMGA}",
            f"Imza (ciddi): {IMZA}, daire muduru vekili",
            f"Imza (ciddi degil): {IMZA}, cay devirmis halde",
            f"Tarih: {TARIH}",
            f"Isim: {ISIM}",
            cizgi,
        ]
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Dolmus sarki ruhsat dairesi")
    p.add_argument("sanatci", nargs="?", help="soyleyen kisi veya grup")
    p.add_argument("sarki", nargs="?", help="calan parca")
    p.add_argument("--demo", action="store_true", help="ornek tutanak bas")
    args = p.parse_args(argv)

    if args.demo or not (args.sanatci and args.sarki):
        print(tutanak("Baris Manco", "Domates Biber Patlican"))
        print()
        print("(demo parcasi sebze sayar, daire patates islemez, karistirmayin)")
        if not args.demo and not (args.sanatci and args.sarki):
            print("Kullanim: python3 ruhsat.py \"Sanatci\" \"Sarki\"")
        return 0

    print(tutanak(args.sanatci.strip(), args.sarki.strip()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
