"""Tester at LaTeX-hovedmanuset kan kompileres til PDF uten feil."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

MANUS_ROOT = Path(__file__).resolve().parents[1]
MAIN_TEX = MANUS_ROOT / "main.tex"


def _finn_kompilator() -> str | None:
    """Returnerer navnet på den første tilgjengelige LaTeX-kompilatoren."""
    for kandidat in ("latexmk", "pdflatex"):
        if shutil.which(kandidat):
            return kandidat
    return None


def _kjor_kommando(kommando: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Kjører kommando og returnerer resultatet med samlet tekststrøm."""
    return subprocess.run(
        kommando,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )


def _feilmedling(resultat: subprocess.CompletedProcess[str], steg: str) -> str:
    """Formaterer en kort logg ved feil."""
    logg = (resultat.stdout or "") + (resultat.stderr or "")
    linjer = [linje.rstrip() for linje in logg.splitlines() if linje.strip()]
    maks = 80
    if len(linjer) > maks:
        linjer = linjer[:maks] + ["… (resten av loggen er avkortet)"]
    innhold = "\n".join(linjer) or "(ingen loggmeldinger)"
    return f"LaTeX-kompilering feilet under {steg} med kode {resultat.returncode}:\n{innhold}"


@pytest.mark.skipif(not MAIN_TEX.exists(), reason="Fant ikke main.tex for manus")
def test_main_tex_kompilerer(tmp_path: Path) -> None:
    """Sikrer at prosjektets hovedfil kan kompileres ferdig."""
    kompilator = _finn_kompilator()
    if kompilator is None:
        pytest.skip("Ingen støttet LaTeX-kompilator (latexmk eller pdflatex) er installert")

    build_dir = tmp_path / "latex-build"
    build_dir.mkdir()

    if kompilator == "latexmk":
        resultat = _kjor_kommando(
            [
                "latexmk",
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-outdir={build_dir}",
                "main.tex",
            ],
            cwd=MANUS_ROOT,
        )
        if resultat.returncode != 0:
            pytest.fail(_feilmedling(resultat, "latexmk"))
    else:
        pdflatex_cmd = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={build_dir}",
            "main.tex",
        ]

        første = _kjor_kommando(pdflatex_cmd, cwd=MANUS_ROOT)
        if første.returncode != 0:
            pytest.fail(_feilmedling(første, "første pdflatex-kjøring"))

        bibtex = shutil.which("bibtex")
        aux_fil = build_dir / "main.aux"
        if bibtex and aux_fil.exists():
            bib_resultat = _kjor_kommando(["bibtex", "main"], cwd=build_dir)
            if bib_resultat.returncode != 0:
                pytest.fail(_feilmedling(bib_resultat, "bibtex"))

        andre = _kjor_kommando(pdflatex_cmd, cwd=MANUS_ROOT)
        if andre.returncode != 0:
            pytest.fail(_feilmedling(andre, "andre pdflatex-kjøring"))

        tredje = _kjor_kommando(pdflatex_cmd, cwd=MANUS_ROOT)
        if tredje.returncode != 0:
            pytest.fail(_feilmedling(tredje, "tredje pdflatex-kjøring"))

    pdf = build_dir / "main.pdf"
    assert pdf.exists(), "Kompileringen produserte ikke en PDF-fil i byggekatalogen"
