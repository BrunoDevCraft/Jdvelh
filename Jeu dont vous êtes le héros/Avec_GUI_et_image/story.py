# story.py

import os

# Déterminer le chemin du dossier actuel
current_dir = os.path.dirname(__file__)

# Les scènes de l'histoire
story = {
    1: {
        "text": "Luna se trouve dans une vallée brumeuse où les arbres semblent murmurer des secrets anciens. Une petite maison en pierre est visible à distance.",
        "image": os.path.join(current_dir, "images", "image1.png"),
        "choices": {
            "1": {"text": "Explorer la maison en pierre", "next_part": 201},
            "2": {"text": "Suivre un chemin sinueux dans la forêt", "next_part": 202},
            "3": {"text": "Chercher un passage secret sous les arbres", "next_part": 203}
        }
    },
    
    201: {
        "text": "Luna entre dans la maison en pierre et découvre un vieux grimoire sur une table poussiéreuse.",
        "image": os.path.join(current_dir, "images", "image2.png"),
        "choices": {
            "1": {"text": "Lire le grimoire pour en savoir plus sur la magie ancienne", "next_part": 204},
            "2": {"text": "Explorer les autres pièces de la maison", "next_part": 205},
            "3": {"text": "Quitter la maison et retourner dans la vallée", "next_part": 206}
        }
    },
    
    202: {
        "text": "Luna suit le chemin sinueux et se retrouve devant une cascade cachée avec une grotte derrière.",
        "image": os.path.join(current_dir, "images", "image3.png"),
        "choices": {
            "1": {"text": "Entrer dans la grotte pour explorer", "next_part": 207},
            "2": {"text": "Observer la cascade depuis l'extérieur", "next_part": 208},
            "3": {"text": "Chercher un autre chemin à travers la forêt", "next_part": 209}
        }
    },
    
    203: {
        "text": "Luna trouve un passage secret sous les arbres qui mène à une ancienne ruine couverte de vignes.",
        "image": os.path.join(current_dir, "images", "image4.png"),
        "choices": {
            "1": {"text": "Explorer les ruines à la recherche d'artefacts", "next_part": 210},
            "2": {"text": "Se reposer dans les ruines pour se revitaliser", "next_part": 211},
            "3": {"text": "Continuer à chercher d'autres passages dans la forêt", "next_part": 212}
        }
    },
    
    204: {
        "text": "En lisant le grimoire, Luna découvre une incantation pour invoquer des esprits anciens.",
        "image": os.path.join(current_dir, "images", "image5.png"),
        "choices": {
            "1": {"text": "Invoquer un esprit pour obtenir des conseils", "next_part": 213},
            "2": {"text": "Conserver le grimoire et chercher un autre lieu", "next_part": 214},
            "3": {"text": "Brûler le grimoire\n" "pour éviter qu'il ne tombe entre de mauvaises mains", "next_part": 215}
        }
    },
    
    205: {
        "text": "Luna explore les autres pièces et trouve une carte ancienne menant à un temple oublié.",
        "image": os.path.join(current_dir, "images", "image6.png"),
        "choices": {
            "1": {"text": "Suivre la carte vers le temple", "next_part": 216},
            "2": {"text": "Chercher des indices dans la maison", "next_part": 217},
            "3": {"text": "Revenir à la vallée pour explorer d'autres lieux", "next_part": 218}
        }
    },
    
    206: {
        "text": "Luna quitte la maison et retourne dans la vallée, découvrant un village caché en ruines.",
        "image": os.path.join(current_dir, "images", "image7.png"),
        "choices": {
            "1": {"text": "Explorer les ruines du village", "next_part": 219},
            "2": {"text": "Chercher des survivants ou des indices", "next_part": 220},
            "3": {"text": "Suivre un sentier menant à une montagne lointaine", "next_part": 221}
        }
    },
    
    207: {
        "text": "Luna entre dans la grotte derrière la cascade et découvre un ancien temple avec des fresques mystérieuses.",
        "image": os.path.join(current_dir, "images", "image8.png"),
        "choices": {
            "1": {"text": "Étudier les fresques pour comprendre leur signification", "next_part": 222},
            "2": {"text": "Chercher un trésor caché dans le temple", "next_part": 223},
            "3": {"text": "Sortir de la grotte et continuer l'exploration", "next_part": 224}
        }
    },
    
    208: {
        "text": "Luna observe la cascade et remarque une porte secrète derrière le rideau d'eau.",
        "image": os.path.join(current_dir, "images", "image9.png"),
        "choices": {
            "1": {"text": "Entrer par la porte secrète", "next_part": 225},
            "2": {"text": "Prendre des échantillons de l'eau pour analyse", "next_part": 226},
            "3": {"text": "Retourner à la vallée", "next_part": 227}
        }
    },
    
    209: {
        "text": "Luna cherche un autre chemin dans la forêt et tombe sur une chute de pierre entourée de mystères.",
        "image": os.path.join(current_dir, "images", "image10.png"),
        "choices": {
            "1": {"text": "Explorer les alentours de la chute de pierre", "next_part": 228},
            "2": {"text": "Chercher des indices dans les environs", "next_part": 229},
            "3": {"text": "Suivre le chemin vers une montagne lointaine", "next_part": 230}
        }
    },
    
    210: {
        "text": "Dans les ruines, Luna trouve un puits ancien avec des inscriptions mystérieuses.",
        "image": os.path.join(current_dir, "images", "image11.png"),
        "choices": {
            "1": {"text": "Descendre dans le puits pour explorer", "next_part": 231},
            "2": {"text": "Examiner les inscriptions sur le mur", "next_part": 232},
            "3": {"text": "Retourner vers la vallée", "next_part": 233}
        }
    },
    
    211: {
        "text": "Luna se repose dans les ruines et trouve un objet magique caché dans un coin sombre.",
        "image": os.path.join(current_dir, "images", "image12.png"),
        "choices": {
            "1": {"text": "Utiliser l'objet magique", "next_part": 234},
            "2": {"text": "Conserver l'objet pour plus tard", "next_part": 235},
            "3": {"text": "Continuer l'exploration dans la forêt", "next_part": 236}
        }
    },
    
    212: {
        "text": "Luna cherche d'autres passages dans la forêt et découvre une caverne mystérieuse avec des symboles anciens.",
        "image": os.path.join(current_dir, "images", "image13.png"),
        "choices": {
            "1": {"text": "Entrer dans la caverne", "next_part": 237},
            "2": {"text": "Étudier les symboles à l'entrée", "next_part": 238},
            "3": {"text": "Chercher un autre passage", "next_part": 239}
        }
    },
    
    # Partie finale pour l'exploration du grimoire
    213: {
        "text": "Luna invoque un esprit ancien qui lui révèle un secret caché dans les ruines.",
        "image": os.path.join(current_dir, "images", "image14.png"),
        "choices": {
            "1": {"text": "Suivre le secret révélé par l'esprit", "next_part": 250},
            "2": {"text": "Remercier l'esprit et retourner explorer", "next_part": 204},
            "3": {"text": "Détruire l'incantation pour éviter tout danger", "next_part": 251}
        }
    },
    
    214: {
        "text": "Luna garde le grimoire et décide de chercher un autre lieu pour explorer.",
        "image": os.path.join(current_dir, "images", "image15.png"),
        "choices": {
            "1": {"text": "Retourner à la vallée pour explorer de nouveaux lieux", "next_part": 1},
            "2": {"text": "Chercher dans les environs proches", "next_part": 202},
            "3": {"text": "Quitter l'aventure pour le moment", "next_part": 252}
        }
    },
    
    215: {
        "text": "Luna brûle le grimoire pour éviter qu'il ne tombe entre de mauvaises mains. La maison est maintenant complètement vide.",
        "image": os.path.join(current_dir, "images", "image16.png"),
        "choices": {
            "1": {"text": "Retourner à la vallée", "next_part": 1},
            "2": {"text": "Explorer d'autres lieux proches", "next_part": 206},
            "3": {"text": "Chercher d'autres secrets dans la maison", "next_part": 203}
        }
    },
    
    # Partie finale pour la carte ancienne
    216: {
        "text": "Luna suit la carte et découvre le temple oublié, où elle trouve un artefact puissant.",
        "image": os.path.join(current_dir, "images", "image17.png"),
        "choices": {
            "1": {"text": "Utiliser l'artefact pour ses propres fins", "next_part": 253},
            "2": {"text": "Ramener l'artefact à un sage local", "next_part": 254},
            "3": {"text": "Laisser l'artefact dans le temple et partir", "next_part": 255}
        }
    },
    
    217: {
        "text": "Luna cherche des indices dans la maison et découvre un message caché dans un livre ancien.",
        "image": os.path.join(current_dir, "images", "image18.png"),
        "choices": {
            "1": {"text": "Déchiffrer le message pour trouver la prochaine étape", "next_part": 256},
            "2": {"text": "Explorer d'autres pièces de la maison", "next_part": 205},
            "3": {"text": "Quitter la maison et retourner explorer la vallée", "next_part": 1}
        }
    },
    
    218: {
        "text": "Luna retourne à la vallée pour explorer d'autres lieux, mais découvre que le village a été envahi par des créatures étranges.",
        "image": os.path.join(current_dir, "images", "image19.png"),
        "choices": {
            "1": {"text": "Affronter les créatures pour libérer le village", "next_part": 257},
            "2": {"text": "Chercher un refuge et observer les créatures", "next_part": 258},
            "3": {"text": "Fuir le village et partir pour une autre destination", "next_part": 259}
        }
    },
    
    # Partie finale pour le village en ruines
    219: {
        "text": "Luna explore les ruines du village et trouve une ancienne relique qui pourrait être d'une grande valeur.",
        "image": os.path.join(current_dir, "images", "image20.png"),
        "choices": {
            "1": {"text": "Étudier la relique pour découvrir ses secrets", "next_part": 260},
            "2": {"text": "Vendre la relique à un marchand", "next_part": 261},
            "3": {"text": "Conserver la relique en sécurité pour plus tard", "next_part": 262}
        }
    },
    
    220: {
        "text": "Luna cherche des survivants et découvre un groupe de personnes cachées dans les ruines.",
        "image": os.path.join(current_dir, "images", "image21.png"),
        "choices": {
            "1": {"text": "Aider les survivants à se réinstaller ailleurs", "next_part": 263},
            "2": {"text": "Chercher à comprendre ce qui est arrivé au village", "next_part": 264},
            "3": {"text": "Laisser les survivants et continuer l'exploration", "next_part": 265}
        }
    },
    
    221: {
        "text": "Luna suit le sentier menant à une montagne lointaine et découvre une ancienne forteresse.",
        "image": os.path.join(current_dir, "images", "image22.png"),
        "choices": {
            "1": {"text": "Explorer la forteresse pour trouver des trésors", "next_part": 266},
            "2": {"text": "Examiner les fortifications pour des indices sur son histoire", "next_part": 267},
            "3": {"text": "Continuer l'ascension pour voir ce qui se trouve au sommet", "next_part": 268}
        }
    },
    
    # Partie finale pour la grotte
    222: {
        "text": "Luna étudie les fresques et découvre une prophétie ancienne concernant la vallée.",
        "image": os.path.join(current_dir, "images", "image23.png"),
        "choices": {
            "1": {"text": "Suivre la prophétie pour découvrir son sens", "next_part": 269},
            "2": {"text": "Chercher un trésor caché mentionné dans les fresques", "next_part": 270},
            "3": {"text": "Sortir de la grotte et revenir explorer ailleurs", "next_part": 271}
        }
    },
    
    223: {
        "text": "Luna cherche un trésor caché dans le temple mais trouve seulement des pièges dangereux.",
        "image": os.path.join(current_dir, "images", "image24.png"),
        "choices": {
            "1": {"text": "Désamorcer les pièges et continuer la recherche", "next_part": 272},
            "2": {"text": "Quitter le temple et chercher un autre lieu", "next_part": 273},
            "3": {"text": "Explorer d'autres grottes à proximité", "next_part": 274}
        }
    },
    
    224: {
        "text": "Luna sort de la grotte et continue l'exploration, découvrant une vallée cachée remplie de mystères.",
        "image": os.path.join(current_dir, "images", "image25.png"),
        "choices": {
            "1": {"text": "Explorer la vallée cachée", "next_part": 275},
            "2": {"text": "Chercher des indices dans les environs", "next_part": 276},
            "3": {"text": "Retourner à la cascade pour explorer d'autres endroits", "next_part": 277}
        }
    },
    
    # Partie finale pour la porte secrète
    225: {
        "text": "Luna entre par la porte secrète et trouve un laboratoire alchimique abandonné.",
        "image": os.path.join(current_dir, "images", "image26.png"),
        "choices": {
            "1": {"text": "Explorer le laboratoire pour trouver des potions", "next_part": 278},
            "2": {"text": "Chercher des indices sur les expériences menées ici", "next_part": 279},
            "3": {"text": "Quitter le laboratoire et revenir à la cascade", "next_part": 280}
        }
    },
    
    226: {
        "text": "Luna prend des échantillons d'eau et découvre que l'eau a des propriétés magiques.",
        "image": os.path.join(current_dir, "images", "image27.png"),
        "choices": {
            "1": {"text": "Utiliser l'eau magique pour des potions", "next_part": 281},
            "2": {"text": "Chercher d'autres sources d'eau magique", "next_part": 282},
            "3": {"text": "Retourner à la vallée pour explorer d'autres lieux", "next_part": 283}
        }
    },
    
    227: {
        "text": "Luna retourne à la vallée et découvre une carte ancienne qui semble mener à un trésor caché.",
        "image": os.path.join(current_dir, "images", "image28.png"),
        "choices": {
            "1": {"text": "Suivre la carte pour trouver le trésor", "next_part": 284},
            "2": {"text": "Chercher d'autres indices dans la vallée", "next_part": 285},
            "3": {"text": "Quitter la vallée et explorer d'autres régions", "next_part": 286}
        }
    },
    
    # Partie finale pour la chute de pierre
    228: {
        "text": "Luna explore les alentours de la chute de pierre et trouve un passage secret derrière la chute.",
        "image": os.path.join(current_dir, "images", "image29.png"),
        "choices": {
            "1": {"text": "Entrer dans le passage secret", "next_part": 287},
            "2": {"text": "Chercher d'autres secrets dans les environs", "next_part": 288},
            "3": {"text": "Suivre le chemin vers une autre destination", "next_part": 289}
        }
    },
    
    229: {
        "text": "Luna cherche des indices dans les environs et découvre un vieux campement abandonné.",
        "image": os.path.join(current_dir, "images", "image30.png"),
        "choices": {
            "1": {"text": "Explorer le campement pour trouver des indices", "next_part": 290},
            "2": {"text": "Chercher des traces de passage récent", "next_part": 291},
            "3": {"text": "Continuer l'exploration de la forêt", "next_part": 292}
        }
    },
    
    230: {
        "text": "Luna suit le chemin vers une montagne lointaine et trouve une ancienne tour de guet.",
        "image": os.path.join(current_dir, "images", "image31.png"), 
        "choices": {
            "1": {"text": "Explorer la tour de guet pour des indices", "next_part": 293},
            "2": {"text": "Monter au sommet de la montagne pour une vue panoramique", "next_part": 294},
            "3": {"text": "Chercher un autre chemin à travers la montagne", "next_part": 295}
        }
    },
    
    # Partie finale pour la découverte du puits
    231: {
        "text": "Luna descend dans le puits et découvre une chambre cachée avec un coffre ancien.",
        "image": os.path.join(current_dir, "images", "image32.png"),
        "choices": {
            "1": {"text": "Ouvrir le coffre pour découvrir son contenu", "next_part": 305},
            "2": {"text": "Examiner la chambre pour des indices supplémentaires", "next_part": 306},
            "3": {"text": "Remonter et chercher d'autres endroits à explorer", "next_part": 307}
        }
    },
    
    232: {
        "text": "Luna examine les inscriptions sur le mur du puits et découvre une prophétie ancienne.",
        "image": os.path.join(current_dir, "images", "image33.png"), 
        "choices": {
            "1": {"text": "Chercher à comprendre la prophétie", "next_part": 308},
            "2": {"text": "Remonter et explorer d'autres parties des ruines", "next_part": 309},
            "3": {"text": "Quitter les ruines et continuer l'exploration", "next_part": 310}
        }
    },
    
    233: {
        "text": "Luna retourne vers la vallée, trouvant un sentier menant à une nouvelle région inexplorée.",
        "image": os.path.join(current_dir, "images", "image34.png"),
        "choices": {
            "1": {"text": "Explorer la nouvelle région", "next_part": 311},
            "2": {"text": "Chercher des indices sur cette région", "next_part": 312},
            "3": {"text": "Retourner aux ruines pour explorer davantage", "next_part": 313}
        }
    },
    
    # Partie finale pour l'objet magique
    234: {
        "text": "Luna utilise l'objet magique et découvre qu'il a des pouvoirs surprenants qui l'aident dans son aventure.",
        "image": os.path.join(current_dir, "images", "image35.png"),
        "choices": {
            "1": {"text": "Utiliser les pouvoirs pour trouver un trésor", "next_part": 314},
            "2": {"text": "Utiliser les pouvoirs pour résoudre une énigme", "next_part": 315},
            "3": {"text": "Conserver l'objet pour des situations futures", "next_part": 316}
        }
    },
    
    235: {
        "text": "Luna conserve l'objet magique pour plus tard et continue son exploration.",
        "image": os.path.join(current_dir, "images", "image36.png"),
        "choices": {
            "1": {"text": "Explorer d'autres parties de la forêt", "next_part": 217},
            "2": {"text": "Chercher un autre artefact magique", "next_part": 237},
            "3": {"text": "Retourner vers la vallée pour explorer de nouveaux lieux", "next_part": 1}
        }
    },
    
    236: {
        "text": "Luna continue l'exploration dans la forêt et découvre un autre lieu mystérieux.",
        "image": os.path.join(current_dir, "images", "image37.png"),
        "choices": {
            "1": {"text": "Explorer le lieu mystérieux", "next_part": 317},
            "2": {"text": "Chercher des indices sur les environs", "next_part": 318},
            "3": {"text": "Retourner à la vallée pour explorer d'autres endroits", "next_part": 319}
        }
    },
    
    # Partie finale pour la caverne mystérieuse
    237: {
        "text": "Luna entre dans la caverne et découvre un artefact ancien gardé par un esprit protecteur.",
        "image": os.path.join(current_dir, "images", "image38.png"),
        "choices": {
            "1": {"text": "Affronter l'esprit pour obtenir l'artefact", "next_part": 320},
            "2": {"text": "Négocier avec l'esprit pour obtenir l'artefact", "next_part": 321},
            "3": {"text": "Fuir la caverne et chercher ailleurs", "next_part": 322}
        }
    },
    
    238: {
        "text": "Luna étudie les symboles à l'entrée de la caverne et découvre une énigme ancienne.",
        "image": os.path.join(current_dir, "images", "image39.png"),
        "choices": {
            "1": {"text": "Résoudre l'énigme pour entrer dans la caverne", "next_part": 323},
            "2": {"text": "Chercher des indices supplémentaires", "next_part": 324},
            "3": {"text": "Abandonner l'exploration de la caverne", "next_part": 325}
        }
    },
    
    239: {
        "text": "Luna cherche un autre passage et découvre une forêt enchantée remplie de créatures magiques.",
        "image": os.path.join(current_dir, "images", "image40.png"),
        "choices": {
            "1": {"text": "Explorer la forêt enchantée", "next_part": 326},
            "2": {"text": "Chercher des indices sur les créatures magiques", "next_part": 327},
            "3": {"text": "Revenir à la vallée pour explorer d'autres lieux", "next_part": 328}
        }
    },

    # Fin de l'histoire
    250: {
        "text": "Luna suit le secret révélé par l'esprit et découvre un trésor caché dans les ruines. L'aventure se termine avec une grande récompense et une nouvelle compréhension du passé.",
        "choices": {}
    },

    251: {
        "text": "Luna détruit l'incantation pour éviter tout danger et quitte les lieux en se sentant soulagée. Elle continue son voyage avec une nouvelle prudence.",
        "choices": {}
    },
    
    252: {
        "text": "Luna termine son aventure pour le moment, avec des souvenirs d'exploration et de mystères à raconter.",
        "choices": {}
    },
    
    253: {
        "text": "Luna utilise l'artefact et acquiert de grands pouvoirs, mais doit faire face aux responsabilités qui en découlent.",
        "choices": {}
    },
    
    254: {
        "text": "Luna ramène l'artefact à un sage local, qui le protège et lui révèle des secrets importants sur la région.",
        "choices": {}
    },
    
    255: {
        "text": "Luna laisse l'artefact dans le temple et part pour de nouvelles aventures, avec l'assurance que le trésor est en sécurité.",
        "choices": {}
    },
    
    256: {
        "text": "Luna déchiffre le message et découvre une nouvelle voie à explorer, menant à des mystères encore plus profonds.",
        "choices": {}
    },
    
    257: {
        "text": "Luna affronte les créatures et libère le village, gagnant respect et gratitude des survivants.",
        "choices": {}
    },
    
    258: {
        "text": "Luna trouve refuge et observe les créatures, apprenant à mieux comprendre leur nature et les mystères du village.",
        "choices": {}
    },
    
    259: {
        "text": "Luna fuit le village et continue ses explorations, se demandant ce qui est arrivé au village mystérieux.",
        "choices": {}
    },
    
    260: {
        "text": "Luna étudie la relique et découvre son importance dans la préservation de l'histoire et de la magie ancienne.",
        "choices": {}
    },
    
    261: {
        "text": "Luna vend la relique et utilise les fonds pour poursuivre de nouvelles aventures et explorations.",
        "choices": {}
    },
    
    262: {
        "text": "Luna conserve la relique en sécurité, prête à l'utiliser pour des moments critiques dans le futur.",
        "choices": {}
    },
    
    263: {
        "text": "Luna aide les survivants à se réinstaller ailleurs, apportant espoir et renouveau à ceux qui ont perdu leur foyer.",
        "choices": {}
    },
    
    264: {
        "text": "Luna enquête sur ce qui est arrivé au village et découvre des secrets qui changent sa perception des événements.",
        "choices": {}
    },
    
    265: {
        "text": "Luna quitte les survivants et continue son exploration, enrichie par ses découvertes dans les ruines.",
        "choices": {}
    },
    
    266: {
        "text": "Luna explore la forteresse et trouve des artefacts anciens qui révèlent l'histoire de la région.",
        "choices": {}
    },
    
    267: {
        "text": "Luna examine les fortifications de la forteresse et comprend leur rôle dans la défense contre les invasions passées.",
        "choices": {}
    },
    
    268: {
        "text": "Luna atteint le sommet de la montagne et découvre une vue imprenable, ainsi que des indices sur des aventures futures.",
        "choices": {}
    },
    
    269: {
        "text": "Luna suit la prophétie et découvre un secret qui change la destinée de la vallée et de ses habitants.",
        "choices": {}
    },
    
    270: {
        "text": "Luna cherche un trésor caché mentionné dans les fresques et trouve des artefacts précieux avec des pouvoirs anciens.",
        "choices": {}
    },
    
    271: {
        "text": "Luna sort de la grotte et retourne à l'exploration, avec une compréhension plus profonde des mystères de la vallée.",
        "choices": {}
    },
    
    272: {
        "text": "Luna désamorce les pièges et découvre un trésor caché dans le temple, avec des artefacts et des trésors anciens.",
        "choices": {}
    },
    
    273: {
        "text": "Luna quitte le temple et explore d'autres lieux, en quête de nouveaux mystères et trésors.",
        "choices": {}
    },
    
    274: {
        "text": "Luna explore d'autres grottes et découvre des secrets cachés et des trésors oubliés.",
        "choices": {}
    },
    
    275: {
        "text": "Luna explore la vallée cachée et découvre des secrets anciens qui révèlent une histoire oubliée.",
        "choices": {}
    },
    
    276: {
        "text": "Luna cherche des indices dans les environs et découvre des informations qui révèlent des mystères non résolus.",
        "choices": {}
    },
    
    277: {
        "text": "Luna retourne à la cascade et explore d'autres endroits, découvrant de nouveaux mystères et trésors.",
        "choices": {}
    },
    
    278: {
        "text": "Luna explore le laboratoire alchimique et trouve des potions et des ingrédients précieux pour ses aventures.",
        "choices": {}
    },
    
    279: {
        "text": "Luna cherche des indices sur les expériences menées dans le laboratoire et découvre des connaissances anciennes.",
        "choices": {}
    },
    
    280: {
        "text": "Luna quitte le laboratoire et retourne à la cascade, avec une meilleure compréhension des mystères de la région.",
        "choices": {}
    },
    
    281: {
        "text": "Luna utilise l'eau magique pour créer des potions puissantes qui l'aident dans ses aventures.",
        "choices": {}
    },
    
    282: {
        "text": "Luna cherche d'autres sources d'eau magique et découvre des ressources rares et précieuses.",
        "choices": {}
    },
    
    283: {
        "text": "Luna retourne à la vallée et explore de nouveaux lieux, enrichie par ses découvertes sur l'eau magique.",
        "choices": {}
    },
    
    284: {
        "text": "Luna suit la carte et trouve un trésor caché qui révèle des secrets sur la région.",
        "choices": {}
    },
    
    285: {
        "text": "Luna cherche d'autres indices dans la vallée et découvre des informations précieuses sur l'histoire locale.",
        "choices": {}
    },
    
    286: {
        "text": "Luna quitte la vallée et explore d'autres régions, en quête de nouvelles découvertes et aventures.",
        "choices": {}
    },
    
    287: {
        "text": "Luna entre dans le passage secret et découvre un trésor caché derrière la chute de pierre.",
        "choices": {}
    },
    
    288: {
        "text": "Luna cherche d'autres secrets dans les environs et découvre des indices sur des trésors cachés.",
        "choices": {}
    },
    
    289: {
        "text": "Luna suit un autre chemin et découvre de nouveaux lieux intéressants à explorer.",
        "choices": {}
    },
    
    290: {
        "text": "Luna explore le campement abandonné et trouve des indices sur des explorateurs passés.",
        "choices": {}
    },
    
    291: {
        "text": "Luna cherche des traces de passage récent et découvre des informations sur les voyageurs précédents.",
        "choices": {}
    },
    
    292: {
        "text": "Luna continue l'exploration de la forêt et découvre de nouveaux mystères et trésors cachés.",
        "choices": {}
    },
    
    293: {
        "text": "Luna explore la tour de guet et découvre des documents anciens qui révèlent des secrets sur la région.",
        "choices": {}
    },
    
    294: {
        "text": "Luna monte au sommet de la montagne et découvre une vue panoramique et des indices sur des aventures futures.",
        "choices": {}
    },
    
    295: {
        "text": "Luna cherche un autre chemin à travers la montagne et trouve des lieux inexplorés intéressants.",
        "choices": {}
    },
    
    296: {
        "text": "Luna affronte l'esprit protecteur et obtient l'artefact ancien, découvrant des pouvoirs et des secrets.",
        "choices": {}
    },
    
    297: {
        "text": "Luna négocie avec l'esprit et obtient l'artefact ancien, en apprenant des secrets précieux sur son utilisation.",
        "choices": {}
    },
    
    298: {
        "text": "Luna fuit la caverne et cherche ailleurs, avec de nouvelles perspectives sur son aventure.",
        "choices": {}
    },
    
    299: {
        "text": "Luna résout l'énigme et entre dans la caverne, découvrant des trésors et des secrets anciens.",
        "choices": {}
    },
    
    300: {
        "text": "Luna cherche des indices supplémentaires et découvre des informations cruciales pour résoudre l'énigme.",
        "choices": {}
    },
    
    301: {
        "text": "Luna abandonne l'exploration de la caverne et continue son aventure ailleurs, enrichie par ses découvertes.",
        "choices": {}
    },
    
    302: {
        "text": "Luna explore la forêt enchantée et découvre des créatures magiques et des trésors cachés.",
        "choices": {}
    },
    
    303: {
        "text": "Luna cherche des indices sur les créatures magiques et découvre des informations fascinantes sur leur nature.",
        "choices": {}
    },
    
    304: {
        "text": "Luna retourne à la vallée et explore de nouveaux lieux, en quête de nouvelles aventures et découvertes.",
        "choices": {}
    },
    
    305: {
        "text": "Luna ouvre le coffre et découvre des trésors anciens et des artefacts puissants.",
        "choices": {}
    },
    
    306: {
        "text": "Luna examine la chambre et découvre des indices importants sur l'histoire de la région.",
        "choices": {}
    },
    
    307: {
        "text": "Luna remonte du puits et continue son exploration, en quête de nouveaux mystères.",
        "choices": {}
    },
    
    308: {
        "text": "Luna comprend la prophétie et découvre des secrets qui changent son aventure et celle de la vallée.",
        "choices": {}
    },
    
    309: {
        "text": "Luna explore d'autres parties des ruines et découvre des informations supplémentaires sur l'histoire locale.",
        "choices": {}
    },
    
    310: {
        "text": "Luna quitte les ruines et continue son aventure, avec de nouvelles perspectives sur ses découvertes.",
        "choices": {}
    },
    
    311: {
        "text": "Luna explore la nouvelle région et découvre des trésors et des secrets inexplorés.",
        "choices": {}
    },
    
    312: {
        "text": "Luna cherche des indices sur la nouvelle région et découvre des informations fascinantes.",
        "choices": {}
    },
    
    313: {
        "text": "Luna retourne aux ruines et continue son exploration, découvrant de nouveaux mystères.",
        "choices": {}
    },
    
    314: {
        "text": "Luna utilise les pouvoirs de l'objet magique pour trouver un trésor caché et révèle des secrets précieux.",
        "choices": {}
    },
    
    315: {
        "text": "Luna utilise les pouvoirs de l'objet magique pour résoudre une énigme ancienne et découvre des trésors.",
        "choices": {}
    },
    
    316: {
        "text": "Luna conserve l'objet magique pour des situations futures, prête à l'utiliser dans ses aventures.",
        "choices": {}
    },
    
    317: {
        "text": "Luna explore le lieu mystérieux et découvre des secrets anciens et des trésors cachés.",
        "choices": {}
    },
    
    318: {
        "text": "Luna cherche des indices sur les environs et découvre des informations importantes pour ses aventures.",
        "choices": {}
    },
    
    319: {
        "text": "Luna retourne à la vallée et continue son exploration, enrichie par ses nouvelles découvertes.",
        "choices": {}
    },
    
    320: {
        "text": "Luna affronte l'esprit protecteur et obtient l'artefact ancien, découvrant des secrets et des pouvoirs.",
        "choices": {}
    },
    
    321: {
        "text": "Luna négocie avec l'esprit protecteur et obtient l'artefact ancien, révélant des connaissances anciennes.",
        "choices": {}
    },
    
    322: {
        "text": "Luna fuit la caverne et explore d'autres lieux, avec des nouvelles perspectives sur les mystères découverts.",
        "choices": {}
    },
    
    323: {
        "text": "Luna résout l'énigme et entre dans la caverne, découvrant des trésors et des secrets anciens.",
        "choices": {}
    },
    
    324: {
        "text": "Luna cherche des indices supplémentaires et découvre des informations cruciales pour résoudre l'énigme.",
        "choices": {}
    },
    
    325: {
        "text": "Luna abandonne l'exploration de la caverne et continue son aventure ailleurs, enrichie par ses découvertes.",
        "choices": {}
    },
    
    326: {
        "text": "Luna explore la forêt enchantée et découvre des créatures magiques et des trésors cachés.",
        "choices": {}
    },
    
    327: {
        "text": "Luna cherche des indices sur les créatures magiques et découvre des informations fascinantes sur leur nature.",
        "choices": {}
    },
    
    328: {
        "text": "Luna retourne à la vallée et explore de nouveaux lieux, en quête de nouvelles aventures et découvertes.",
        "choices": {}
    }
}


def get_story_part(part_id):
    """Retourne le texte, les choix et l'image de la partie de l'histoire spécifiée."""
    part = story.get(part_id)
    if part:
        text = part["text"]
        choices = part["choices"]
        image = part.get("image", None)  # Utilise None si l'image n'est pas définie
        return text, choices, image
    else:
        return None, None, None

def get_next_part(current_part_id, choice_key):
    """Retourne l'identifiant de la prochaine partie basée sur le choix de l'utilisateur."""
    part = story.get(current_part_id)
    if part and choice_key in part["choices"]:
        return part["choices"][choice_key]["next_part"]
    else:
        return None