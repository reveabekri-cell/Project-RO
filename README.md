# Projet de Recherche Opérationnelle

Modélisation et résolution de trois problèmes 
d'optimisation implémentés en Python avec 
Pyomo, OR-Tools et LibreOffice Calc.

## Contributeurs
- Emmekelthoume Sidaty — Matricule: C27092
- Revea Bakry — Matricule: C22688

## Sujets traités
1. Dimensionnement de Stock (EOQ) — LibreOffice Calc
2. Problème d'affectation — OR-Tools CP-SAT
3. Routage des camions d'eau — Pyomo + GLPK

## Outils utilisés
- Python 3.13
- Pyomo & GLPK
- OR-Tools
- LibreOffice Calc Solver
- Overleaf (LaTeX)

## Fichiers du projet
- `EOQ.xlsx` — Modèle EOQ sur tableur
- `Probleme_d_affectation.py` — Code Python
- `Routage_camions_d_eau.py` — Code Python
- `Projet_RO.pdf` — Rapport final (LaTeX)

## Résultats clés
- **EOQ** : Q* = 244.95 unités | Coût = 489.90 MRU
- **Affectation** : W1→T2, W2→T1, W3→T3, W4→T4 | Coût = 13 MRU
- **Routage** : 0→1→2→3→4→6→5→0 | Distance = 101.00 km
