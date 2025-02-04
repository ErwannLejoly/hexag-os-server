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

Installation de Qiskit

Prérequis

Avant de commencer, assurez-vous d'utiliser Debian 12 et d'avoir un accès à un terminal avec les droits administrateur.

1. Mise à jour du système

Avant d'installer Qiskit, mettez votre système à jour pour vous assurer que vous disposez des dernières versions des paquets :

sudo apt update && sudo apt upgrade -y

2. Installation de Python et pip

Qiskit nécessite Python 3.8 ou une version ultérieure. Debian 12 inclut déjà Python 3.11, donc nous avons seulement besoin d'installer pip :

sudo apt install python3-pip -y

3. Installation de Qiskit

Installez Qiskit avec la commande suivante :

pip install qiskit

Si vous souhaitez exécuter des circuits quantiques sur un ordinateur quantique réel via IBM Quantum, installez les outils supplémentaires :

pip install qiskit[visualization] qiskit-ibm-provider

4. Vérification de l'installation

Vérifiez que Qiskit est bien installé en exécutant la commande suivante :

python3 -c "import qiskit; print(qiskit.__version__)"

Si Qiskit est correctement installé, vous verrez s'afficher sa version.

Configuration de l'accès aux processeurs quantiques IBM

Qiskit permet d'exécuter des simulations en local, mais aussi d'envoyer des calculs à des processeurs quantiques réels via IBM Quantum.

1. Créer un compte IBM Quantum

Si ce n'est pas encore fait, inscrivez-vous gratuitement sur IBM Quantum.

2. Obtenir une clé API

Une fois connecté à IBM Quantum :

Accédez à "Mon Compte" > "API Keys"

Cliquez sur "Générer une nouvelle clé API"

Copiez la clé API qui vous est fournie

3. Configurer la connexion à IBM Quantum

Dans un terminal Python, exécutez la commande suivante en remplaçant VOTRE_CLE_API par la clé obtenue :

from qiskit_ibm_provider import IBMProvider

IBMProvider.save_account('VOTRE_CLE_API', overwrite=True)

Cette configuration permettra à votre OS d'exécuter des tâches sur un processeur quantique IBM.

✅ Félicitations ! Votre système est maintenant prêt à exploiter la puissance du calcul quantique. 🎉

HexagOS/
│
├── src/
│   ├── core/
│   │   ├── hybrid_scheduler.py       # Planificateur de tâches
│   │   ├── quantum_driver.py         # Gestionnaire des tâches quantiques
│   │   ├── classic_driver.py         # Gestionnaire des tâches classiques
│   │   ├── memory_manager.py         # Gestion de la mémoire des qubits
│   │   └── security.py               # Sécurisation des tâches
│   |
|   ├── api/
│   │   └── hybrid_api.py             # Interface API pour interagir avec le noyau
│   |
|   ├── cli/
│   │   └── hexag_cli.py              # Interface utilisateur en ligne de commande
│   |
|   ├── tests/                        # Dossier des tests unitaires
│   └── utils.py                      # Fonctions utilitaires (logs, etc.)
|

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

## Étape 4 : Gestion de la mémoire quantique

La gestion de la mémoire quantique, en particulier l'allocation et la libération des qubits, est cruciale pour éviter les conflits de ressources. Une gestion efficace permet d'assurer que les tâches quantiques sont exécutées correctement sans rencontrer de limitations liées à la disponibilité des qubits.
Une gestion optimale des qubits permet d'éviter des blocages ou des erreurs de ressources insuffisantes lorsque plusieurs tâches quantiques sont soumises. Cela garantit que chaque tâche dispose des qubits nécessaires à son exécution, tout en assurant une allocation efficace et une libération rapide des qubits une fois leur utilisation terminée.

## Étape 5 : API pour Hexag OS

Une API permet aux utilisateurs ou aux développeurs d'interagir avec **Hexag OS** de manière simple et structurée. Elle offre des moyens d'envoyer des tâches au système, de récupérer les résultats, et de surveiller l'état des ressources. Une API bien conçue améliore l'accessibilité du système et facilite son intégration dans des applications et des workflows externes.

### Fonctionnalités principales de l'API

- **Soumission de tâches** : Permet aux utilisateurs de soumettre des tâches classiques ou quantiques au planificateur.
- **Récupération des résultats** : Permet d'obtenir les résultats des tâches exécutées sur les processeurs classiques ou quantiques.
- **Surveillance des ressources** : Permet de vérifier l'état actuel des ressources, telles que la mémoire des qubits et la charge des processeurs.

## Étape 6 : Interface utilisateur en ligne de commande (CLI)

### Pourquoi cette étape ?

Une interface CLI permet aux utilisateurs d'interagir facilement avec **Hexag OS** sans avoir à utiliser des scripts ou à entrer dans le code source. Elle simplifie l'utilisation du système en offrant des commandes intuitives pour soumettre des tâches, surveiller l'état du système, et récupérer les résultats sans avoir besoin d'une interface graphique complexe.

### Fonctionnalités principales de la CLI

- **Soumission de tâches** : Soumettre des tâches classiques et quantiques via des commandes simples.
- **Surveillance du système** : Vérifier l'utilisation des ressources et l'état des qubits.
- **Récupération des résultats** : Obtenir les résultats des tâches exécutées directement dans le terminal.

---

## Étape 7 : Sécurisation supplémentaire



La sécurité des tâches et des communications est primordiale, en particulier dans un environnement hybride classique-quantique où des données sensibles peuvent être traitées. Renforcer la sécurité permet de garantir la confidentialité et l'intégrité des données tout au long de leur traitement et de leur transmission entre les composants du système.

### Mesures de sécurité supplémentaires

- **Chiffrement des communications entre les composants** : Utilisation de la bibliothèque `pycryptodome` pour chiffrer les données transmises entre les différents composants du système, garantissant ainsi leur confidentialité.
- **Vérification des entrées utilisateur** : Mise en place de filtres pour éviter l'exécution de commandes dangereuses ou non sécurisées à travers les entrées utilisateur, réduisant ainsi les risques d'injections ou d'autres vulnérabilités.

---

## Étape 8 : Tests unitaires



Les tests unitaires garantissent que chaque composant du système fonctionne correctement de manière isolée. Ils permettent de vérifier que les différentes parties d'**Hexag OS** (planificateur, gestionnaire de mémoire, API, etc.) respectent leurs spécifications et que les modifications du code n'introduisent pas de nouvelles erreurs.

### Fonctionnalités principales des tests

- **Isolation des composants** : Chaque composant est testé de manière indépendante pour s'assurer qu'il fonctionne sans dépendre des autres.
- **Détection des erreurs** : Les tests permettent de détecter les erreurs potentielles dans le code avant de les déployer en production.
- **Maintenance continue** : Facilite la maintenance à long terme du projet en validant que les mises à jour ne cassent pas les fonctionnalités existantes.
