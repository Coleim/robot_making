# 09 — Personnalisation (avec votre fille) 🎨

C'est le moment le plus amusant ! Une fois le robot fonctionnel, place à la
déco pour qu'il devienne vraiment **son** robot.

## Idées de personnalisation

- **Peindre le corps** à la peinture acrylique ou aux feutres posca
  (le PLA accroche bien la peinture acrylique, poncez légèrement avant si besoin).
- **Choisir un nom** pour le robot ensemble, et pourquoi pas l'ajouter en
  code (voir plus bas) pour qu'il se présente au démarrage.
- **Oreilles interchangeables** : imprimez plusieurs paires d'oreilles de
  formes différentes (rondes, pointues, tombantes) pour changer l'allure
  du robot selon l'humeur du jour.
- **Décorations amovibles** : autocollants, petits accessoires en PLA
  (noeud, chapeau...) à coller avec de la pâte adhésive réutilisable.
- **Nouvelles émotions** sur l'écran (voir `07-code-yeux.md`), imaginées
  et dessinées avec votre fille.

## Faire parler le robot de son nom (mini-extension de code)

Une petite étape de code simple à faire ensemble, sans attendre les
évolutions plus avancées (son/voix) :

```python
# Dans config.py
ROBOT_NAME = "Layla"  # à remplacer par le nom choisi !
```

```python
# Dans main.py, au tout début de main()
print(f"Je m'appelle {config.ROBOT_NAME} et je suis prêt à jouer !")
```

## Activité : "carnet du robot"

Avec votre fille, tenez un petit carnet (papier ou fichier) où elle note :
- Les pannes rencontrées et comment vous les avez résolues
- Les nouvelles émotions inventées
- Les idées d'évolutions pour la suite (voir `10-evolutions.md`)

C'est une chouette façon de la faire participer à la conception, pas
seulement au montage.
