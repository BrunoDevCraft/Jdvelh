# story.py
"""
Luna et la Vallée aux Murmures

Dix ans après la disparition de sa grand-mère Elira lors d'une expédition dans la
légendaire Vallée aux Murmures, Luna revient sur ses traces. Guidée par un pendentif
hérité d'elle, un grimoire à demi lisible et un vieux journal d'exploration, elle va
devoir percer le secret d'un peuple disparu, les Gardiens, et comprendre l'origine de
la brume grise qui ronge peu à peu la vallée et ses habitants.
"""

import os

# Déterminer le chemin du dossier actuel
current_dir = os.path.dirname(__file__)

# Les scènes de l'histoire
story = {
    1: {
        "text": "Dix ans après la disparition de sa grand-mère Elira, exploratrice partie enquêter sur la légendaire Vallée aux Murmures, Luna y revient enfin. Une brume tenace flotte entre les arbres, dont les feuilles bruissent comme si elles chuchotaient un avertissement. Le pendentif d'Elira, chaud contre sa peau, semble réagir à quelque chose de proche. Au loin, une maison de pierre solitaire brise le silence du paysage.",
        "image": os.path.join(current_dir, "images", "image1.png"),
        "choices": {
            "1": {"text": "Explorer la maison en pierre", "next_part": 201},
            "2": {"text": "Suivre le chemin sinueux qui serpente dans la forêt", "next_part": 202},
            "3": {"text": "Chercher un passage discret sous les racines des arbres", "next_part": 203},
        }
    },

    201: {
        "text": "La porte de la maison grince comme si elle n'avait pas été ouverte depuis des années. Sur une table couverte de poussière, Luna découvre un grimoire relié de cuir portant les initiales « E.D. » — celles de sa grand-mère.",
        "image": os.path.join(current_dir, "images", "image2.png"),
        "choices": {
            "1": {"text": "Lire le grimoire pour comprendre ce qu'Elira étudiait", "next_part": 204},
            "2": {"text": "Fouiller les autres pièces de la maison", "next_part": 205},
            "3": {"text": "Ressortir et retourner vers la vallée", "next_part": 206},
        }
    },

    202: {
        "text": "Le chemin débouche sur une cascade rugissante, dont l'écume dissimule l'entrée d'une grotte sombre. Le pendentif de Luna vibre plus fort à mesure qu'elle approche de l'eau.",
        "image": os.path.join(current_dir, "images", "image3.png"),
        "choices": {
            "1": {"text": "Entrer dans la grotte derrière le rideau d'eau", "next_part": 207},
            "2": {"text": "Observer la cascade avant de s'engager", "next_part": 208},
            "3": {"text": "Contourner et chercher un autre chemin", "next_part": 209},
        }
    },

    203: {
        "text": "Sous les racines noueuses d'un vieux chêne, Luna découvre un passage taillé dans la roche, menant à des ruines envahies par la végétation. Des symboles gravés, semblables à ceux du journal d'Elira, ornent les pierres effondrées.",
        "image": os.path.join(current_dir, "images", "image4.png"),
        "choices": {
            "1": {"text": "Fouiller les ruines à la recherche d'indices", "next_part": 210},
            "2": {"text": "S'arrêter pour reprendre des forces parmi les décombres", "next_part": 211},
            "3": {"text": "Continuer d'explorer sous les arbres", "next_part": 212},
        }
    },

    204: {
        "text": "Les pages du grimoire décrivent un rituel permettant d'invoquer les esprits protecteurs des Gardiens, l'ancien peuple qui veillait sur la vallée. En marge, une note griffonnée à la hâte : « S'il m'arrive quelque chose, ne détruis rien avant d'avoir écouté. »",
        "image": os.path.join(current_dir, "images", "image5.png"),
        "choices": {
            "1": {"text": "Tenter l'incantation pour invoquer un esprit", "next_part": 213},
            "2": {"text": "Garder le grimoire précieusement et poursuivre ailleurs", "next_part": 214},
            "3": {"text": "Brûler le grimoire, de peur qu'il ne tombe en de mauvaises mains", "next_part": 215},
        }
    },

    205: {
        "text": "Dans une chambre à l'étage, Luna trouve une carte à moitié brûlée — la même que celle mentionnée dans les carnets de sa grand-mère — indiquant l'emplacement d'un temple oublié au cœur de la vallée.",
        "image": os.path.join(current_dir, "images", "image6.png"),
        "choices": {
            "1": {"text": "Suivre la carte jusqu'au temple", "next_part": 216},
            "2": {"text": "Chercher d'autres indices dans la maison", "next_part": 217},
            "3": {"text": "Redescendre vers la vallée pour explorer ailleurs", "next_part": 218},
        }
    },

    206: {
        "text": "Luna quitte la maison silencieuse et redescend vers la vallée. Ce qu'elle découvre la glace : les ruines d'un village, autrefois prospère, aujourd'hui abandonné et rongé par une étrange brume grise.",
        "image": os.path.join(current_dir, "images", "image7.png"),
        "choices": {
            "1": {"text": "Explorer les ruines du village", "next_part": 219},
            "2": {"text": "Chercher des survivants ou des indices", "next_part": 220},
            "3": {"text": "Suivre un sentier qui grimpe vers une montagne lointaine", "next_part": 221},
        }
    },

    207: {
        "text": "Derrière le rideau d'eau, une grotte s'ouvre sur un temple ancien. Des fresques usées par le temps représentent des silhouettes encerclant un sceau lumineux — sans doute la source du mal qui ronge la vallée.",
        "image": os.path.join(current_dir, "images", "image8.png"),
        "choices": {
            "1": {"text": "Étudier les fresques pour comprendre leur signification", "next_part": 222},
            "2": {"text": "Chercher un trésor caché dans le temple", "next_part": 223},
            "3": {"text": "Ressortir et poursuivre l'exploration ailleurs", "next_part": 224},
        }
    },

    208: {
        "text": "En observant la cascade de plus près, Luna remarque un interstice dans la roche : une porte dissimulée derrière le rideau d'eau, presque invisible à l'œil nu.",
        "image": os.path.join(current_dir, "images", "image9.png"),
        "choices": {
            "1": {"text": "Franchir la porte secrète", "next_part": 225},
            "2": {"text": "Prélever un échantillon de l'eau, étrangement tiède", "next_part": 226},
            "3": {"text": "Rebrousser chemin vers la vallée", "next_part": 227},
        }
    },

    209: {
        "text": "En contournant la cascade, Luna tombe sur un éboulis étrange, comme si un pan de falaise s'était effondré récemment — révélant peut-être un passage resté caché pendant des siècles.",
        "image": os.path.join(current_dir, "images", "image10.png"),
        "choices": {
            "1": {"text": "Explorer les abords de l'éboulis", "next_part": 228},
            "2": {"text": "Chercher des indices sur ce qui l'a provoqué", "next_part": 229},
            "3": {"text": "Suivre le sentier qui monte vers la montagne", "next_part": 230},
        }
    },

    210: {
        "text": "Au centre des ruines, un puits de pierre porte des inscriptions identiques à celles du pendentif de Luna. L'air qui en remonte est étonnamment frais, comme si quelque chose respirait encore en dessous.",
        "image": os.path.join(current_dir, "images", "image11.png"),
        "choices": {
            "1": {"text": "Descendre explorer le puits", "next_part": 231},
            "2": {"text": "Examiner les inscriptions gravées sur la margelle", "next_part": 232},
            "3": {"text": "Revenir vers la vallée", "next_part": 233},
        }
    },

    211: {
        "text": "Luna s'assoit un instant parmi les pierres effondrées. En se relevant, elle remarque un éclat sous un bloc renversé : un petit objet gravé de runes, chaud au toucher — semblable à celui décrit dans le journal d'Elira.",
        "image": os.path.join(current_dir, "images", "image12.png"),
        "choices": {
            "1": {"text": "Essayer d'activer l'objet magique", "next_part": 234},
            "2": {"text": "Le ranger précieusement pour plus tard", "next_part": 235},
            "3": {"text": "Poursuivre l'exploration de la forêt", "next_part": 236},
        }
    },

    212: {
        "text": "Un peu plus loin, Luna découvre l'entrée d'une caverne dont le seuil est entièrement recouvert de symboles des Gardiens, semblables à ceux de la carte de sa grand-mère.",
        "image": os.path.join(current_dir, "images", "image13.png"),
        "choices": {
            "1": {"text": "Entrer directement dans la caverne", "next_part": 237},
            "2": {"text": "Étudier les symboles avant d'entrer", "next_part": 238},
            "3": {"text": "Chercher un autre chemin, par prudence", "next_part": 239},
        }
    },

    213: {
        "text": "Luna récite l'incantation. Une silhouette translucide apparaît devant elle — un esprit ancien qui la reconnaît étrangement bien et lui révèle l'emplacement d'un secret enfoui dans les ruines, lié à la disparition d'Elira.",
        "image": os.path.join(current_dir, "images", "image14.png"),
        "choices": {
            "1": {"text": "Suivre immédiatement le secret révélé", "next_part": 250},
            "2": {"text": "Remercier l'esprit et l'interroger davantage sur le grimoire", "next_part": 204},
            "3": {"text": "Détruire l'incantation, effrayée par ce contact", "next_part": 251},
        }
    },

    214: {
        "text": "Luna choisit de garder le grimoire contre elle, sentant qu'il pourrait encore lui être utile, et referme la maison derrière elle sans un bruit.",
        "image": os.path.join(current_dir, "images", "image15.png"),
        "choices": {
            "1": {"text": "Retourner vers la vallée pour explorer ailleurs", "next_part": 1},
            "2": {"text": "Repartir vers la cascade lointaine", "next_part": 202},
            "3": {"text": "S'accorder une pause avant de continuer l'aventure", "next_part": 252},
        }
    },

    215: {
        "text": "Les flammes dévorent le grimoire en silence, comme si la maison elle-même retenait son souffle. Quand tout est réduit en cendres, un calme étrange s'installe : la maison paraît enfin vide de son passé.",
        "image": os.path.join(current_dir, "images", "image16.png"),
        "choices": {
            "1": {"text": "Retourner vers la vallée", "next_part": 1},
            "2": {"text": "Explorer d'autres lieux proches", "next_part": 206},
            "3": {"text": "Chercher malgré tout d'autres secrets dans la maison", "next_part": 203},
        }
    },

    216: {
        "text": "En suivant la carte, Luna atteint le temple oublié. Au centre, sur un piédestal, repose un artefact pulsant d'une lumière douce — la même lumière que celle du pendentif d'Elira.",
        "image": os.path.join(current_dir, "images", "image17.png"),
        "choices": {
            "1": {"text": "S'emparer de l'artefact pour elle-même", "next_part": 253},
            "2": {"text": "Rapporter l'artefact à un sage du village voisin", "next_part": 254},
            "3": {"text": "Laisser l'artefact à sa place et repartir", "next_part": 255},
        }
    },

    217: {
        "text": "Dans un vieux livre annoté, Luna trouve un message codé, écrit de la main même de sa grand-mère, évoquant un « sceau à ne jamais briser sans les trois clés des Gardiens ».",
        "image": os.path.join(current_dir, "images", "image18.png"),
        "choices": {
            "1": {"text": "Déchiffrer entièrement le message", "next_part": 256},
            "2": {"text": "Continuer d'explorer les autres pièces", "next_part": 205},
            "3": {"text": "Quitter la maison, songeuse, pour retourner à la vallée", "next_part": 1},
        }
    },

    218: {
        "text": "En redescendant vers la vallée, Luna découvre le village de Pierreval envahi par des créatures difformes, nées de la brume grise. Leurs cris résonnent entre les ruines.",
        "image": os.path.join(current_dir, "images", "image19.png"),
        "choices": {
            "1": {"text": "Affronter les créatures pour libérer le village", "next_part": 257},
            "2": {"text": "Se mettre à l'abri et observer leur comportement", "next_part": 258},
            "3": {"text": "Fuir vers une autre destination", "next_part": 259},
        }
    },

    219: {
        "text": "Parmi les décombres de Pierreval, Luna déterre une relique frappée du même sceau que celui des fresques du temple — un fragment, peut-être, du sceau originel des Gardiens.",
        "image": os.path.join(current_dir, "images", "image20.png"),
        "choices": {
            "1": {"text": "Étudier la relique pour comprendre son rôle", "next_part": 260},
            "2": {"text": "La vendre à un marchand itinérant croisé en chemin", "next_part": 261},
            "3": {"text": "La conserver précieusement pour plus tard", "next_part": 262},
        }
    },

    220: {
        "text": "Sous une bâche effondrée, Luna découvre un petit groupe d'habitants de Pierreval, terrés là depuis que la brume a envahi leur village.",
        "image": os.path.join(current_dir, "images", "image21.png"),
        "choices": {
            "1": {"text": "Aider les survivants à se réinstaller en lieu sûr", "next_part": 263},
            "2": {"text": "Les interroger sur ce qui est arrivé au village", "next_part": 264},
            "3": {"text": "Les laisser et poursuivre seule l'exploration", "next_part": 265},
        }
    },

    221: {
        "text": "Le sentier grimpe jusqu'à une forteresse en ruine accrochée à la montagne, ancienne sentinelle veillant autrefois sur toute la vallée.",
        "image": os.path.join(current_dir, "images", "image22.png"),
        "choices": {
            "1": {"text": "Explorer la forteresse à la recherche de trésors", "next_part": 266},
            "2": {"text": "Examiner les fortifications pour comprendre son histoire", "next_part": 267},
            "3": {"text": "Poursuivre l'ascension jusqu'au sommet", "next_part": 268},
        }
    },

    222: {
        "text": "En étudiant les fresques, Luna comprend qu'une prophétie ancienne annonce le retour d'une « porteuse de lumière » capable de refermer le sceau — et reconnaît, avec un frisson, les traits du visage peint : ceux de sa propre lignée.",
        "image": os.path.join(current_dir, "images", "image23.png"),
        "choices": {
            "1": {"text": "Chercher à percer le sens complet de la prophétie", "next_part": 269},
            "2": {"text": "Chercher le trésor mentionné dans les fresques", "next_part": 270},
            "3": {"text": "Ressortir du temple, troublée, pour explorer ailleurs", "next_part": 271},
        }
    },

    223: {
        "text": "En cherchant un trésor, Luna déclenche une série de pièges anciens : dalles piégées, flèches rouillées, fumée toxique.",
        "image": os.path.join(current_dir, "images", "image24.png"),
        "choices": {
            "1": {"text": "Désamorcer les pièges avec prudence et continuer", "next_part": 272},
            "2": {"text": "Battre en retraite hors du temple", "next_part": 273},
            "3": {"text": "Explorer d'autres grottes voisines, plus sûres", "next_part": 274},
        }
    },

    224: {
        "text": "En sortant du temple, Luna découvre une vallée cachée, protégée par les falaises, où la brume grise ne semble pas avoir pénétré — un dernier sanctuaire préservé.",
        "image": os.path.join(current_dir, "images", "image25.png"),
        "choices": {
            "1": {"text": "Explorer cette vallée préservée", "next_part": 275},
            "2": {"text": "Chercher des indices sur pourquoi elle est épargnée", "next_part": 276},
            "3": {"text": "Retourner vers la cascade pour explorer ailleurs", "next_part": 277},
        }
    },

    225: {
        "text": "Derrière la porte secrète s'étend un laboratoire alchimique abandonné, ses tables couvertes de fioles brisées et de notes manuscrites — l'écriture d'Elira, encore une fois.",
        "image": os.path.join(current_dir, "images", "image26.png"),
        "choices": {
            "1": {"text": "Fouiller le laboratoire à la recherche de potions utilisables", "next_part": 278},
            "2": {"text": "Étudier les notes pour comprendre les expériences menées ici", "next_part": 279},
            "3": {"text": "Quitter le laboratoire et revenir vers la cascade", "next_part": 280},
        }
    },

    226: {
        "text": "L'échantillon d'eau prélevé scintille faiblement dans sa fiole : cette eau semble chargée d'une magie ancienne, capable peut-être de repousser la brume grise.",
        "image": os.path.join(current_dir, "images", "image27.png"),
        "choices": {
            "1": {"text": "Utiliser l'eau pour préparer une potion protectrice", "next_part": 281},
            "2": {"text": "Chercher d'autres sources de cette eau magique", "next_part": 282},
            "3": {"text": "Retourner vers la vallée avec cet échantillon précieux", "next_part": 283},
        }
    },

    227: {
        "text": "De retour dans la vallée, Luna trouve, glissée sous une pierre, une carte tracée à la main indiquant l'emplacement d'un trésor caché — encore une fois, l'écriture familière de sa grand-mère.",
        "image": os.path.join(current_dir, "images", "image28.png"),
        "choices": {
            "1": {"text": "Suivre cette nouvelle carte", "next_part": 284},
            "2": {"text": "Chercher d'autres indices dans la vallée avant de partir", "next_part": 285},
            "3": {"text": "Quitter la vallée pour explorer une autre région", "next_part": 286},
        }
    },

    228: {
        "text": "Aux abords de l'éboulis, Luna découvre un passage secret qui s'enfonce sous la roche, jusque-là dissimulé par les pierres tombées.",
        "image": os.path.join(current_dir, "images", "image29.png"),
        "choices": {
            "1": {"text": "S'engager dans le passage secret", "next_part": 287},
            "2": {"text": "Chercher d'autres indices dans les environs avant d'entrer", "next_part": 288},
            "3": {"text": "Suivre plutôt le sentier vers une autre destination", "next_part": 289},
        }
    },

    229: {
        "text": "Non loin de l'éboulis, Luna découvre un vieux campement abandonné à la hâte : tentes effondrées, gamelles rouillées, et un carnet resté ouvert sur une page à demi lisible.",
        "image": os.path.join(current_dir, "images", "image30.png"),
        "choices": {
            "1": {"text": "Fouiller le campement pour trouver des indices", "next_part": 290},
            "2": {"text": "Chercher des traces de passage plus récent", "next_part": 291},
            "3": {"text": "Poursuivre l'exploration de la forêt", "next_part": 292},
        }
    },

    230: {
        "text": "Le chemin mène jusqu'à une ancienne tour de guet, à moitié effondrée, offrant une vue dégagée sur toute la vallée brumeuse.",
        "image": os.path.join(current_dir, "images", "image31.png"),
        "choices": {
            "1": {"text": "Explorer la tour à la recherche d'indices", "next_part": 293},
            "2": {"text": "Grimper au sommet de la montagne pour une vue panoramique", "next_part": 294},
            "3": {"text": "Chercher un autre chemin à travers la montagne", "next_part": 295},
        }
    },

    231: {
        "text": "Au fond du puits, une chambre secrète s'ouvre, éclairée par une faible lueur bleutée. Au centre trône un coffre ancien, verrouillé par trois serrures distinctes.",
        "image": os.path.join(current_dir, "images", "image32.png"),
        "choices": {
            "1": {"text": "Tenter d'ouvrir le coffre", "next_part": 305},
            "2": {"text": "Examiner la chambre pour trouver d'autres indices", "next_part": 306},
            "3": {"text": "Remonter et poursuivre ailleurs", "next_part": 307},
        }
    },

    232: {
        "text": "Les inscriptions gravées sur la margelle du puits racontent, en langage ancien, la prophétie de la « porteuse de lumière » déjà entrevue dans les fresques du temple.",
        "image": os.path.join(current_dir, "images", "image33.png"),
        "choices": {
            "1": {"text": "Chercher à comprendre pleinement cette prophétie", "next_part": 308},
            "2": {"text": "Remonter et explorer une autre partie des ruines", "next_part": 309},
            "3": {"text": "Quitter les ruines pour poursuivre ailleurs", "next_part": 310},
        }
    },

    233: {
        "text": "En redescendant vers la vallée, Luna repère un sentier à peine visible menant vers une région qu'aucune carte, même celle d'Elira, ne mentionne.",
        "image": os.path.join(current_dir, "images", "image34.png"),
        "choices": {
            "1": {"text": "Explorer cette région inconnue", "next_part": 311},
            "2": {"text": "Chercher d'abord des indices à son sujet", "next_part": 312},
            "3": {"text": "Retourner aux ruines pour approfondir ses recherches", "next_part": 313},
        }
    },

    234: {
        "text": "L'objet gravé de runes s'illumine entre ses mains, révélant des pouvoirs inattendus : Luna sent la brume grise reculer légèrement autour d'elle.",
        "image": os.path.join(current_dir, "images", "image35.png"),
        "choices": {
            "1": {"text": "Utiliser ce pouvoir pour localiser un trésor", "next_part": 314},
            "2": {"text": "L'utiliser pour résoudre une énigme rencontrée plus tôt", "next_part": 315},
            "3": {"text": "Conserver son pouvoir pour un moment plus critique", "next_part": 316},
        }
    },

    235: {
        "text": "Luna range soigneusement l'objet magique dans son sac, décidant de ne l'utiliser qu'en cas de réel besoin, et poursuit son chemin.",
        "image": os.path.join(current_dir, "images", "image36.png"),
        "choices": {
            "1": {"text": "Retourner explorer d'autres pièces de la maison", "next_part": 217},
            "2": {"text": "Chercher un autre artefact ailleurs dans la vallée", "next_part": 237},
            "3": {"text": "Retourner vers la vallée pour explorer de nouveaux lieux", "next_part": 1},
        }
    },

    236: {
        "text": "En poursuivant son chemin dans la forêt, Luna débouche sur une clairière étrange, où l'air semble figé et où les murmures des arbres se taisent complètement.",
        "image": os.path.join(current_dir, "images", "image37.png"),
        "choices": {
            "1": {"text": "Explorer ce lieu silencieux et mystérieux", "next_part": 317},
            "2": {"text": "Chercher des indices sur ce qui a fait taire la forêt", "next_part": 318},
            "3": {"text": "Rebrousser chemin vers la vallée", "next_part": 319},
        }
    },

    237: {
        "text": "Dans la caverne, Luna découvre un artefact ancien veillé par un esprit gardien, dernier protecteur d'un fragment du sceau des Gardiens.",
        "image": os.path.join(current_dir, "images", "image38.png"),
        "choices": {
            "1": {"text": "Affronter l'esprit pour obtenir l'artefact", "next_part": 320},
            "2": {"text": "Tenter de négocier avec l'esprit", "next_part": 321},
            "3": {"text": "Renoncer et fuir la caverne", "next_part": 322},
        }
    },

    238: {
        "text": "À l'entrée de la caverne, les symboles gravés forment une énigme complexe, semblable à un verrou que seul un esprit rusé saurait déchiffrer.",
        "image": os.path.join(current_dir, "images", "image39.png"),
        "choices": {
            "1": {"text": "Résoudre l'énigme pour ouvrir le passage", "next_part": 323},
            "2": {"text": "Chercher des indices supplémentaires alentour", "next_part": 324},
            "3": {"text": "Renoncer à explorer cette caverne", "next_part": 325},
        }
    },

    239: {
        "text": "En cherchant un autre passage, Luna débouche sur une forêt enchantée où voltigent des créatures lumineuses, aussi curieuses d'elle qu'elle l'est d'elles.",
        "image": os.path.join(current_dir, "images", "image40.png"),
        "choices": {
            "1": {"text": "Explorer prudemment la forêt enchantée", "next_part": 326},
            "2": {"text": "Observer les créatures pour en apprendre plus sur leur nature", "next_part": 327},
            "3": {"text": "Revenir vers la vallée pour explorer ailleurs", "next_part": 328},
        }
    },

    250: {
        "text": "Luna suit le secret révélé par l'esprit et découvre, gravée dans la pierre, la dernière trace du passage d'Elira : un mot d'adieu et l'indication d'un lieu où elle pourrait enfin retrouver sa grand-mère. Son aventure continue, portée par un espoir retrouvé.",
        "choices": {}
    },

    251: {
        "text": "Effrayée par la puissance du rituel, Luna détruit l'incantation avant qu'elle ne cause plus de mal. Elle quitte la maison le cœur lourd, sans réponse sur le sort d'Elira, mais résolue à continuer sa quête autrement.",
        "choices": {}
    },

    252: {
        "text": "Épuisée par tant de découvertes, Luna s'accorde une pause bien méritée au bord de la vallée, le grimoire toujours serré contre elle. Son aventure reprendra, mais pour l'instant, elle savoure ce moment de calme.",
        "choices": {}
    },

    253: {
        "text": "Luna s'empare de l'artefact et sent aussitôt affluer en elle un pouvoir immense — mais aussi le poids d'une responsabilité qu'elle n'avait pas anticipée : celle de devenir, à son tour, gardienne du sceau.",
        "choices": {}
    },

    254: {
        "text": "Luna confie l'artefact à un sage du village voisin, qui le reconnaît aussitôt et lui révèle enfin la vérité : Elira n'a pas disparu, elle s'est sacrifiée pour retenir la brume grise.",
        "choices": {}
    },

    255: {
        "text": "Luna choisit de laisser l'artefact dans le temple, convaincue qu'il doit y rester en sécurité. Elle repart l'esprit apaisé, sachant que certains trésors valent mieux protégés qu'emportés.",
        "choices": {}
    },

    256: {
        "text": "En déchiffrant entièrement le message, Luna découvre l'existence des trois clés des Gardiens, indispensables pour refermer le sceau — une nouvelle quête, bien plus vaste, s'ouvre devant elle.",
        "choices": {}
    },

    257: {
        "text": "Luna affronte les créatures nées de la brume et libère Pierreval, gagnant la reconnaissance éternelle de ses habitants survivants. Son nom commence à se murmurer dans toute la vallée.",
        "choices": {}
    },

    258: {
        "text": "Cachée, Luna observe longuement les créatures et comprend qu'elles ne sont pas mauvaises, seulement égarées par la brume — une découverte qui changera sa façon d'affronter le mal qui ronge la vallée.",
        "choices": {}
    },

    259: {
        "text": "Luna fuit Pierreval sans se retourner, hantée par les cris qu'elle laisse derrière elle. Elle sait qu'elle devra un jour y revenir, mieux préparée.",
        "choices": {}
    },

    260: {
        "text": "En étudiant la relique, Luna comprend qu'elle est un fragment du sceau originel — une pièce du puzzle qui pourrait, un jour, aider à sauver toute la vallée.",
        "choices": {}
    },

    261: {
        "text": "Luna vend la relique à un marchand de passage, obtenant de quoi financer la suite de son voyage — mais elle se demande longtemps si elle n'a pas cédé un peu de l'histoire de sa grand-mère.",
        "choices": {}
    },

    262: {
        "text": "Luna conserve précieusement la relique, certaine qu'elle lui sera utile lorsqu'elle affrontera enfin la source de la brume grise.",
        "choices": {}
    },

    263: {
        "text": "Luna aide les survivants de Pierreval à trouver refuge dans une vallée voisine, leur offrant un nouveau départ loin de la brume.",
        "choices": {}
    },

    264: {
        "text": "En interrogeant les survivants, Luna apprend qu'une expédition, dix ans plus tôt, avait ouvert par erreur un sceau ancien — et qu'une femme aux cheveux gris, Elira, avait tenté seule de le refermer.",
        "choices": {}
    },

    265: {
        "text": "Luna laisse les survivants à leur sort et poursuit seule son exploration, un poids nouveau sur la conscience.",
        "choices": {}
    },

    266: {
        "text": "Dans la forteresse, Luna découvre des archives entières décrivant les Gardiens et leur lutte ancestrale contre la brume — un savoir perdu qu'elle est désormais seule à détenir.",
        "choices": {}
    },

    267: {
        "text": "En examinant les fortifications, Luna comprend que cette forteresse ne défendait pas la vallée contre des envahisseurs humains, mais contre quelque chose venu d'en dessous.",
        "choices": {}
    },

    268: {
        "text": "Du sommet de la montagne, Luna aperçoit toute l'étendue de la brume grise — et, en son centre, une lueur pulsante qu'elle sait devoir affronter tôt ou tard.",
        "choices": {}
    },

    269: {
        "text": "En perçant le sens de la prophétie, Luna comprend qu'elle seule, descendante d'Elira, peut refermer le sceau — son aventure prend un tournant décisif.",
        "choices": {}
    },

    270: {
        "text": "Le trésor mentionné dans les fresques se révèle être un miroir ancien, capable de montrer le passé — Luna y aperçoit, l'espace d'un instant, le visage de sa grand-mère.",
        "choices": {}
    },

    271: {
        "text": "Luna ressort du temple, l'esprit rempli de questions nouvelles, et reprend son exploration avec une détermination renforcée.",
        "choices": {}
    },

    272: {
        "text": "Après avoir désamorcé les pièges avec sang-froid, Luna découvre un trésor oublié : des instruments d'exploration ayant appartenu à Elira elle-même.",
        "choices": {}
    },

    273: {
        "text": "Prudente, Luna quitte le temple sans insister, préférant vivre pour continuer sa quête plutôt que risquer sa vie pour un trésor incertain.",
        "choices": {}
    },

    274: {
        "text": "En explorant des grottes voisines, Luna découvre un réseau de galeries entièrement gravées par les Gardiens — un vestige immense, resté intact depuis des siècles.",
        "choices": {}
    },

    275: {
        "text": "Luna explore la vallée cachée, épargnée par la brume, et y découvre les derniers descendants des Gardiens, vivant en secret loin du monde.",
        "choices": {}
    },

    276: {
        "text": "En cherchant des indices, Luna comprend que cette vallée est protégée par un sortilège tissé par Elira elle-même, des années plus tôt.",
        "choices": {}
    },

    277: {
        "text": "Luna retourne vers la cascade et poursuit son exploration, le cœur empli de nouvelles questions sur cette vallée aux mille secrets.",
        "choices": {}
    },

    278: {
        "text": "Dans le laboratoire, Luna trouve plusieurs potions encore utilisables, dont l'une, teintée d'argent, ressemble étrangement à celle décrite dans le journal de sa grand-mère.",
        "choices": {}
    },

    279: {
        "text": "En étudiant les notes du laboratoire, Luna comprend qu'Elira cherchait un remède à la brume grise, sans jamais l'achever.",
        "choices": {}
    },

    280: {
        "text": "Luna quitte le laboratoire avec la certitude renouvelée que sa grand-mère est peut-être encore quelque part, vivante, dans cette vallée.",
        "choices": {}
    },

    281: {
        "text": "Grâce à l'eau magique, Luna prépare une potion capable de repousser temporairement la brume grise — une arme précieuse pour la suite de son voyage.",
        "choices": {}
    },

    282: {
        "text": "En cherchant d'autres sources de cette eau, Luna découvre un réseau souterrain entier, alimenté par une source magique bien plus vaste qu'elle ne l'imaginait.",
        "choices": {}
    },

    283: {
        "text": "Luna retourne dans la vallée, son échantillon d'eau magique précieusement conservé, prête à en faire bon usage.",
        "choices": {}
    },

    284: {
        "text": "En suivant la nouvelle carte, Luna découvre un trésor modeste mais précieux : les carnets complets d'Elira, relatant chacune de ses découvertes dans la vallée.",
        "choices": {}
    },

    285: {
        "text": "En cherchant d'autres indices dans la vallée, Luna rassemble peu à peu les pièces d'un puzzle bien plus vaste qu'elle ne l'imaginait au départ.",
        "choices": {}
    },

    286: {
        "text": "Luna quitte la vallée pour explorer une région voisine, emportant avec elle toutes les questions restées sans réponse.",
        "choices": {}
    },

    287: {
        "text": "Le passage secret mène à une chambre scellée, où repose un dernier message d'Elira, gravé dans la pierre à la lueur d'une torche mourante.",
        "choices": {}
    },

    288: {
        "text": "En cherchant d'autres secrets autour de l'éboulis, Luna découvre des traces de fouilles récentes — quelqu'un d'autre s'intéresse à cette vallée.",
        "choices": {}
    },

    289: {
        "text": "Luna suit un autre chemin et débouche sur un panorama inattendu, loin des dangers rencontrés jusqu'ici.",
        "choices": {}
    },

    290: {
        "text": "En fouillant le campement abandonné, Luna reconnaît le matériel typique des expéditions d'Elira — la preuve qu'elle est bien passée par ici.",
        "choices": {}
    },

    291: {
        "text": "Les traces récentes découvertes par Luna suggèrent qu'elle n'est pas seule à explorer cette vallée en ce moment même.",
        "choices": {}
    },

    292: {
        "text": "Luna poursuit son exploration de la forêt, portée par un mélange grandissant d'excitation et d'appréhension.",
        "choices": {}
    },

    293: {
        "text": "Dans la tour de guet, Luna découvre des rapports anciens décrivant, siècle après siècle, la lente progression de la brume grise.",
        "choices": {}
    },

    294: {
        "text": "Du sommet, Luna contemple la vallée tout entière et comprend enfin l'ampleur de la tâche qui l'attend.",
        "choices": {}
    },

    295: {
        "text": "Luna trouve un autre chemin à travers la montagne, menant vers des contrées encore jamais explorées.",
        "choices": {}
    },

    305: {
        "text": "Le coffre s'ouvre enfin, révélant non pas un trésor matériel, mais les dernières volontés d'Elira, écrites pour quiconque saurait un jour ouvrir ce coffre.",
        "choices": {}
    },

    306: {
        "text": "En examinant la chambre secrète, Luna découvre des cartes gravées dans la pierre, indiquant l'emplacement exact du cœur du sceau.",
        "choices": {}
    },

    307: {
        "text": "Luna remonte du puits, pensive, et poursuit son exploration avec une longueur d'avance sur les mystères de la vallée.",
        "choices": {}
    },

    308: {
        "text": "En comprenant enfin la prophétie, Luna réalise qu'elle porte, sans le savoir, la même marque que celle décrite : elle est la « porteuse de lumière » annoncée.",
        "choices": {}
    },

    309: {
        "text": "En explorant davantage les ruines, Luna découvre les vestiges d'un ancien village des Gardiens, oublié de tous.",
        "choices": {}
    },

    310: {
        "text": "Luna quitte les ruines, songeuse, emportant avec elle un peu plus de la vérité sur cette vallée et sur sa propre famille.",
        "choices": {}
    },

    311: {
        "text": "Dans cette région inexplorée, Luna découvre un sanctuaire dédié aux Gardiens, resté intact depuis des siècles.",
        "choices": {}
    },

    312: {
        "text": "En cherchant des indices, Luna comprend que cette région a été délibérément effacée des cartes — quelqu'un voulait qu'elle reste secrète.",
        "choices": {}
    },

    313: {
        "text": "Luna retourne aux ruines pour approfondir ses recherches, refusant de laisser derrière elle la moindre question sans réponse.",
        "choices": {}
    },

    314: {
        "text": "Grâce aux pouvoirs de l'objet magique, Luna localise un trésor caché : un fragment du sceau des Gardiens, semblable à celui trouvé à Pierreval.",
        "choices": {}
    },

    315: {
        "text": "Luna utilise les pouvoirs de l'objet pour résoudre une énigme ancienne, révélant un passage jusqu'alors invisible.",
        "choices": {}
    },

    316: {
        "text": "Luna choisit de conserver le pouvoir de l'objet pour un moment plus décisif, sentant que la véritable épreuve reste à venir.",
        "choices": {}
    },

    317: {
        "text": "En explorant le lieu silencieux, Luna découvre l'origine exacte de la brume grise : une fissure dans le sceau, s'élargissant un peu plus chaque année.",
        "choices": {}
    },

    318: {
        "text": "En cherchant des indices, Luna trouve les restes d'un campement de fortune — celui, sans doute, d'Elira, dans les derniers jours de sa présence ici.",
        "choices": {}
    },

    319: {
        "text": "Luna retourne vers la vallée, le cœur lourd de ce qu'elle vient de découvrir, mais plus déterminée que jamais.",
        "choices": {}
    },

    320: {
        "text": "Luna affronte l'esprit gardien et remporte l'artefact, mais celui-ci lui murmure, avant de s'effacer, un dernier avertissement sur le prix à payer pour refermer le sceau.",
        "choices": {}
    },

    321: {
        "text": "En négociant avec l'esprit, Luna obtient l'artefact pacifiquement et apprend de précieux secrets sur la nature véritable des Gardiens.",
        "choices": {}
    },

    322: {
        "text": "Effrayée par la puissance de l'esprit, Luna fuit la caverne, certaine qu'elle devra revenir un jour, mieux préparée pour cette rencontre.",
        "choices": {}
    },

    323: {
        "text": "Luna résout l'énigme et pénètre dans la caverne, découvrant un trésor gardé depuis des siècles par les Gardiens eux-mêmes.",
        "choices": {}
    },

    324: {
        "text": "En cherchant des indices supplémentaires, Luna trouve la clé nécessaire pour résoudre l'énigme sans risquer d'éveiller ce qui dort dans la caverne.",
        "choices": {}
    },

    325: {
        "text": "Luna renonce à explorer cette caverne, préférant continuer son chemin plutôt que d'affronter un danger encore trop grand pour elle.",
        "choices": {}
    },

    326: {
        "text": "Luna explore prudemment la forêt enchantée et se lie d'amitié avec l'une des créatures lumineuses, qui accepte de la guider plus loin dans la vallée.",
        "choices": {}
    },

    327: {
        "text": "En observant les créatures, Luna comprend qu'elles fuient elles aussi la brume grise — un signe de plus que le mal qui ronge la vallée grandit.",
        "choices": {}
    },

    328: {
        "text": "Luna retourne à la vallée, songeuse, portant avec elle une nouvelle pièce du grand mystère qu'elle est venue résoudre.",
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
