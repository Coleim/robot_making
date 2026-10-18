# 02 — Impression 3D

Suivez d'abord `cad/README.md` pour exporter vos fichiers STL.

## Ordre d'impression conseillé

1. **`support_batterie.stl`** — rapide, permet de vérifier que votre pack de
   piles rentre bien (ajustez `params.scad` sinon et réimprimez).
2. **`base.stl`** — la pièce la plus importante, vérifiez que vos moteurs et
   la roulette folle s'emboîtent correctement.
3. **`oreilles.stl`** — rapide et amusant, à faire avec votre fille si elle
   veut choisir les couleurs.
4. **`tete.stl`** — la plus longue et la plus technique (nécessite des
   supports), à lancer en dernier une fois les autres dimensions validées.

## Réglages du slicer

| Réglage | Valeur conseillée |
|---|---|
| Matière | PLA |
| Hauteur de couche | 0.2mm |
| Remplissage (infill) | 15-20% |
| Supports | Désactivés, sauf pour la tête (voir ci-dessous) |
| Adhérence plateau (brim) | Activé si votre imprimante a tendance au décollement |

### Spécifique à la tête (`tete.scad`)

- Orientez la pièce **ouverture vers le bas** sur le plateau.
- Activez les supports uniquement **"touching buildplate only"** (pas de
  support partout, ça gâche du filament et complique le post-traitement).
- Retirez les supports délicatement avec une pince fine après impression.

## Astuce "test rapide"

Avant de lancer une impression longue, imprimez juste un coin de la pièce
(fonction "modifier mesh" ou en coupant le STL avec un outil comme
[Meshmixer](https://www.meshmixer.com) ou directement dans le slicer avec
l'option de découpe) pour vérifier les tolérances de vos moteurs/écran
avant d'engager plusieurs heures d'impression.

## Temps d'impression estimé (à 0.2mm, 20% infill)

| Pièce | Temps approximatif |
|---|---|
| Support batterie | ~45 min |
| Base | ~3h |
| Oreilles (x2) | ~1h |
| Tête | ~4-5h (avec supports) |

👉 Pas besoin de tout imprimer d'un coup ! C'est l'occasion de faire des
sessions courtes avec votre fille : lancer l'impression ensemble, puis
revenir la voir progresser de temps en temps.
