# Fichiers 3D — Robot Layla

Ces fichiers sont en **OpenSCAD** (`.scad`), pas directement en `.stl`.
C'est volontaire : OpenSCAD permet de **paramétrer** le modèle (tailles de
moteurs, d'écran, etc.) facilement sans refaire tout le design dans un
logiciel de modélisation classique.

## Installer OpenSCAD

Gratuit, toutes plateformes : https://openscad.org/downloads.html

## Fichiers

| Fichier | Description |
|---|---|
| `params.scad` | Tous les paramètres/dimensions (à ajuster en premier !) |
| `base.scad` | Châssis principal (supports moteurs + roulette folle + fixation Pi) |
| `tete.scad` | Tête avec fenêtre écran OLED + logement capteur ultrason |
| `oreilles.scad` | 2 oreilles amovibles (impression en couleur séparée possible) |
| `support_batterie.scad` | Tiroir à piles amovible |

## Étapes pour exporter les STL

1. **Mesurez vos composants réels** (moteurs, écran OLED, capteur
   ultrason) et ajustez les valeurs dans `params.scad`. Les valeurs par
   défaut correspondent aux dimensions standards des kits les plus courants
   trouvés dans le commerce, mais il peut y avoir de petites variations.
2. Ouvrez un fichier (ex: `base.scad`) dans OpenSCAD.
3. Appuyez sur F6 (rendu complet), puis `File > Export > Export as STL`.
4. Répétez pour `tete.scad`, `oreilles.scad`, `support_batterie.scad`.
5. Importez les `.stl` dans votre slicer habituel (Cura, PrusaSlicer...).

## Conseils d'impression

- **Matière** : PLA, le plus simple et le moins cher.
- **Remplissage (infill)** : 15-20% suffit pour toutes les pièces.
- **Supports** : uniquement nécessaires pour `tete.scad` (sous les
  fenêtres), à activer en mode "touching buildplate only".
- **Hauteur de couche** : 0.2mm, suffisant pour ce robot (pas besoin de
  précision extrême).
- Imprimez d'abord la **base** en rapide/brouillon pour vérifier que vos
  moteurs et la roulette folle rentrent bien, avant de lancer les pièces
  plus longues (tête).

## Idée d'activité avec votre fille 🎨

Imprimez les oreilles (`oreilles.scad`) dans 2 couleurs différentes au choix,
et laissez-la peindre/décorer la tête et le corps une fois assemblés
(voir `docs/09-personnalisation.md`).
