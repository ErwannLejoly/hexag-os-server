
**Hexag-OS_server** est un système d'exploitation serveur personnalisé développé pour offrir une solution robuste de gestion de serveurs avec des fonctionnalités avancées de virtualisation. Ce projet inclut un noyau personnalisé, un gestionnaire de paquets, et des outils de configuration pour une administration efficace et sécurisée.

## Table des Matières

- [Présentation](#présentation)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Sécurité](#sécurité)
- [Maintenance](#maintenance)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Présentation

Hexag-OS_server vise à fournir une plateforme serveur flexible et sécurisée avec les caractéristiques suivantes :

- **Noyau Personnalisé** : Optimisé pour la gestion multi-cœurs et la virtualisation.
- **Gestion des Paquets** : Un gestionnaire de paquets personnalisé, `hexag-apt`, pour gérer l'installation et les mises à jour des logiciels.
- **Virtualisation KVM** : Support complet pour la création et la gestion de machines virtuelles avec une option de configuration DRBD.
- **Gestion des Utilisateurs** : Utilisation de sudo pour une gestion des permissions sécurisée, avec désactivation du compte root par défaut.

## Prérequis

Avant de commencer, assurez-vous de disposer des éléments suivants :

- Un système Ubuntu ou Debian à jour.
- Privilèges root ou sudo pour l'installation et la configuration.
- `git` pour cloner le dépôt.

## Installation

1. **Clonez le dépôt Git** :

   ```sh
   git clone https://github.com/ErwannLejoly/hexag-os-server.git
   cd hexag-os-server

   cd hexag-os_server
