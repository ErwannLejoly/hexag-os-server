# Hexag OS — Noyau Hybride Quantique-Classique

**Hexag OS** est un projet innovant visant à créer un noyau hybride combinant des fonctionnalités classiques basées sur des CPU avec des capacités quantiques utilisant des qubits. Ce noyau est conçu pour s'intégrer facilement avec des systèmes Linux existants, tout en permettant de soumettre des tâches quantiques à des simulateurs ou à du matériel quantique réel.

## Fonctionnalités principales

- **Hybridation Quantique-Classique** : Combinaison des capacités de calcul classiques (processeurs) et quantiques (qubits) au sein d'un même noyau.
- **Compatibilité Linux** : Conçu pour fonctionner avec des systèmes Linux déjà en place.
- **Accès au Matériel Quantique** : Support pour soumettre des tâches à des simulateurs ou à des processeurs quantiques réels.

## Objectifs du Projet

- Offrir un cadre flexible pour l'exécution de tâches combinant des algorithmes classiques et quantiques.
- Permettre aux développeurs et chercheurs de tester et déployer des algorithmes quantiques dans un environnement familier et accessible.
- Faciliter l'adoption des technologies quantiques grâce à une intégration fluide avec les outils de développement existants.


## Étape 1 : Création de la structure du projet
### Structure du projet

```bash
HexagOS/
│
├── src/
│   ├── core/
│   │   ├── hybrid_scheduler.py       # Planificateur de tâches
│   │   ├── quantum_driver.py         # Gestionnaire des tâches quantiques
│   │   ├── classic_driver.py         # Gestionnaire des tâches classiques
│   │   ├── memory_manager.py         # Gestion de la mémoire des qubits
│   │   └── security.py               # Sécurisation des tâches
│   ├── api/
│   │   └── hybrid_api.py             # Interface API pour interagir avec le noyau
│   ├── cli/
│   │   └── hexag_cli.py              # Interface utilisateur en ligne de commande
│   ├── tests/                        # Dossier des tests unitaires
│   └── utils.py                      # Fonctions utilitaires (logs, etc.)
├── docs/                             # Documentation du projet
├── requirements.txt                  # Fichier des dépendances
└── README.md                         # Explication du projet
```

## Étape 2 : Planificateur des tâches hybrides

Le planificateur est au cœur du système **Hexag OS**. Il gère la répartition des tâches entre les processeurs classiques et quantiques. Cette étape est cruciale pour assurer une gestion optimale des ressources et permettre une exécution efficace des algorithmes hybrides, combinant les puissances de calcul classiques et quantiques.

### Fonctionnalités principales du planificateur

- **Répartition des tâches** : Assigne dynamiquement les tâches aux processeurs classiques ou quantiques en fonction de la nature des calculs à effectuer.
- **Optimisation des ressources** : Utilise des algorithmes d'optimisation pour minimiser le temps de traitement global.
- **Suivi des tâches** : Gère l'état d'exécution des tâches, surveille leur progression et récupère les résultats.
