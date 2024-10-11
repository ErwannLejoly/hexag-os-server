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

## Sécurisation de l'ordonnancement des tâches

### Utilisation de mécanismes de verrouillage

Pour éviter les conflits lors de l'accès simultané aux files d'attente des tâches, il est essentiel d'utiliser des mécanismes de verrouillage. La gestion des tâches dans un environnement multi-threadé ou multi-utilisateur peut introduire des conditions de course, où plusieurs processus ou utilisateurs tentent d'accéder aux ressources en même temps. Ce verrouillage garantit que chaque tâche est correctement ajoutée ou planifiée sans risque de conflit.

### Objectifs de la sécurisation

- **Prévention des conditions de course** : Assurer que deux tâches ne modifient pas simultanément une même file d'attente ou une même ressource partagée.
- **Gestion des accès concurrentiels** : Implémenter des mécanismes pour éviter les accès concurrentiels non sécurisés aux files d'attente des tâches.
- **Assurance de l'intégrité des tâches** : Garantir que les tâches sont ajoutées, exécutées et récupérées dans l'ordre prévu sans interférence.

## Étape 3 : Gestionnaire des tâches classiques et quantiques

### Pourquoi cette étape ?

Il est nécessaire de créer des composants distincts pour gérer l'exécution des tâches classiques et quantiques, chacun ayant des contraintes et des méthodes d'exécution différentes. Les tâches classiques sont exécutées directement sur le CPU, tandis que les tâches quantiques doivent être compilées et envoyées à un simulateur ou à un matériel quantique réel.

### Fonctionnalités principales

- **Gestion des tâches classiques** : Exécution directe des calculs sur les processeurs classiques en utilisant des algorithmes traditionnels.
- **Gestion des tâches quantiques** : Compilation des algorithmes quantiques et envoi vers des simulateurs ou des processeurs quantiques réels.
- **Séparation des responsabilités** : Création de modules spécifiques pour chaque type de tâche, garantissant une meilleure organisation et une gestion optimisée des ressources.

