# -*- coding: utf-8 -*-
"""
GUI_Image_jdvelh.py
--------------------
"Luna et la Vallée aux Murmures" — un jeu dont vous êtes le héros.

Cette version reprend exactement la logique du programme original
(story.py n'est pas modifié : mêmes fonctions get_story_part / get_next_part,
même façon de parcourir l'histoire) mais habille l'interface pour recréer
l'ambiance d'un vrai livre-jeu d'aventure : parchemin vieilli, filets dorés,
numéros de passage façon "paragraphe", typographies à empattements et
boutons de choix stylisés.

Aucune dépendance externe n'est nécessaire : uniquement la bibliothèque
standard tkinter (comme dans la version d'origine).
"""

import os
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, ttk

from story import get_story_part, get_next_part


# ---------------------------------------------------------------------------
#  PALETTE — ambiance "vallée brumeuse à la nuit tombée"
# ---------------------------------------------------------------------------
PALETTE = {
    "bg_top":        "#100c08",   # ciel nocturne, haut du dégradé
    "bg_bottom":      "#231a10",   # brume dorée, bas du dégradé
    "panel":          "#241b13",   # panneau "bois sombre"
    "panel_border":   "#c9a227",   # liseré doré du cadre
    "parchment":      "#ede0c3",   # papier vieilli
    "parchment_edge": "#8a7550",   # ombre du parchemin
    "ink":            "#3a2c18",   # encre / texte sur parchemin
    "gold":           "#d9b04c",   # titres, filets décoratifs
    "gold_soft":      "#b3924e",
    "button":         "#3a2c1c",   # boutons de choix (au repos)
    "button_hover":   "#5c4527",   # boutons de choix (survol)
    "button_text":    "#ecdcb8",
    "danger":         "#5c2323",
    "danger_hover":   "#7a2e2e",
}

# Candidats de polices, du plus "livre-jeu médiéval" au plus universel.
TITLE_FONTS = [
    "Cinzel Decorative", "Cinzel", "Trajan Pro", "Copperplate Gothic Bold",
    "Papyrus", "Big Caslon", "Georgia", "Times New Roman",
]
BODY_FONTS = [
    "Cormorant Garamond", "EB Garamond", "Garamond", "Palatino Linotype",
    "Book Antiqua", "Baskerville", "Georgia", "Times New Roman",
]

CIRCLED_DIGITS = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩"]


def _pick_font(candidates, fallback="Times New Roman"):
    """Retourne le premier nom de police disponible sur la machine."""
    try:
        available = set(tkfont.families())
    except Exception:
        return fallback
    for name in candidates:
        if name in available:
            return name
    return fallback


class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Luna et la Vallée aux Murmures — Vous êtes le Héros")
        self.root.geometry("780x760")
        self.root.minsize(620, 620)
        self.root.configure(bg=PALETTE["bg_bottom"])

        self.current_part_id = 1

        # Polices résolues une seule fois au démarrage.
        title_family = _pick_font(TITLE_FONTS)
        body_family = _pick_font(BODY_FONTS)
        self.fonts = {
            "banner": tkfont.Font(family=title_family, size=30, weight="bold"),
            "subtitle": tkfont.Font(family=body_family, size=14, slant="italic"),
            "chapter": tkfont.Font(family=body_family, size=11, weight="bold"),
            "body": tkfont.Font(family=body_family, size=14),
            "button": tkfont.Font(family=body_family, size=13, weight="bold"),
            "small": tkfont.Font(family=body_family, size=10, slant="italic"),
        }

        # Icône de fenêtre : on réutilise la toute première illustration.
        self._try_set_icon()

        # Ascenseur du texte : on force le thème ttk "clam", qui est dessiné
        # par Tk lui-même (pas délégué à l'OS), afin que nos couleurs et
        # notre épaisseur soient bien appliquées sur toutes les plateformes
        # (contrairement à tk.Scrollbar, souvent "écrasé" par le rendu
        # natif du système, notamment sur macOS).
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure(
            "Story.Vertical.TScrollbar",
            gripcount=0,
            background=PALETTE["gold_soft"],   # couleur du curseur
            troughcolor=PALETTE["panel"],       # couleur du rail
            bordercolor=PALETTE["panel"],
            arrowcolor=PALETTE["parchment"],
            relief="flat",
            arrowsize=22,
            width=22,
        )
        style.map(
            "Story.Vertical.TScrollbar",
            background=[("active", PALETTE["gold"]), ("pressed", PALETTE["gold"])],
        )

        # Toile de fond en dégradé, redessinée à chaque redimensionnement.
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0, bd=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_canvas.bind("<Configure>", self._draw_background)

        # Panneau central façon "reliure" contenant tout le jeu.
        self.panel = tk.Frame(
            self.root, bg=PALETTE["panel"],
            highlightbackground=PALETTE["panel_border"],
            highlightcolor=PALETTE["panel_border"], highlightthickness=2,
        )
        self.panel.place(relx=0.5, rely=0.5, anchor="center",
                          relwidth=0.88, relheight=0.92)

        self.image_ref = None  # anti garbage-collection pour l'illustration
        self.start_screen()

    # ------------------------------------------------------------------
    #  Décor
    # ------------------------------------------------------------------
    def _try_set_icon(self):
        icon_path = os.path.join(os.path.dirname(__file__), "images", "image1.png")
        if os.path.exists(icon_path):
            try:
                self._icon_img = tk.PhotoImage(file=icon_path)
                self.root.iconphoto(True, self._icon_img)
            except Exception:
                pass

    def _draw_background(self, event=None):
        """Dégradé vertical nuit -> brume dorée + léger grain de texture."""
        c = self.bg_canvas
        c.delete("bg")
        w = c.winfo_width() or self.root.winfo_width()
        h = c.winfo_height() or self.root.winfo_height()
        if w <= 1 or h <= 1:
            return

        top = self._hex_to_rgb(PALETTE["bg_top"])
        bottom = self._hex_to_rgb(PALETTE["bg_bottom"])
        steps = 60
        for i in range(steps):
            t = i / (steps - 1)
            r = round(top[0] + (bottom[0] - top[0]) * t)
            g = round(top[1] + (bottom[1] - top[1]) * t)
            b = round(top[2] + (bottom[2] - top[2]) * t)
            color = f"#{r:02x}{g:02x}{b:02x}"
            y0 = int(h * i / steps)
            y1 = int(h * (i + 1) / steps) + 1
            c.create_rectangle(0, y0, w, y1, fill=color, outline="", tags="bg")

        # Grain léger (vieux papier / pénombre) via un pointillé discret.
        c.create_rectangle(0, 0, w, h, fill="", outline="",
                            stipple="gray25", tags="bg")
        c.tag_lower("bg")

    @staticmethod
    def _hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def _separator(self, parent, symbol="✦"):
        tk.Label(
            parent, text=f"─────  {symbol}  ─────",
            bg=parent["bg"], fg=PALETTE["gold_soft"], font=self.fonts["small"],
        ).pack(pady=(2, 10))

    # ------------------------------------------------------------------
    #  Écran de titre
    # ------------------------------------------------------------------
    def start_screen(self):
        self.clear_screen()

        wrapper = tk.Frame(self.panel, bg=PALETTE["panel"])
        wrapper.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            wrapper, text="⚜", bg=PALETTE["panel"], fg=PALETTE["gold"],
            font=(self.fonts["banner"].actual("family"), 26),
        ).pack(pady=(0, 6))

        tk.Label(
            wrapper, text="L E   J E U   D O N T   V O U S\nÊ T E S   L E   H É R O S",
            bg=PALETTE["panel"], fg=PALETTE["gold"], font=self.fonts["banner"],
            justify="center",
        ).pack()

        self._separator(wrapper, "❦")

        tk.Label(
            wrapper, text="Luna et la Vallée aux Murmures",
            bg=PALETTE["panel"], fg=PALETTE["parchment"],
            font=self.fonts["subtitle"], justify="center",
        ).pack(pady=(0, 4))

        tk.Label(
            wrapper,
            text="Dix ans après la disparition de sa grand-mère,\n"
                 "Luna revient percer le secret de la vallée brumeuse.",
            bg=PALETTE["panel"], fg=PALETTE["gold_soft"],
            font=self.fonts["small"], justify="center",
        ).pack(pady=(0, 26))

        self._make_button(wrapper, "Commencer l'aventure", self.start_story,
                           width=28).pack(pady=6)
        self._make_button(wrapper, "Fermer le grimoire", self.root.quit,
                           width=28, danger=True).pack(pady=6)

    # ------------------------------------------------------------------
    #  Boutons stylisés (choix, actions)
    # ------------------------------------------------------------------
    def _make_button(self, parent, text, command, width=None, danger=False):
        bg = PALETTE["danger"] if danger else PALETTE["button"]
        hover = PALETTE["danger_hover"] if danger else PALETTE["button_hover"]

        btn = tk.Button(
            parent, text=text, command=command, font=self.fonts["button"],
            bg=bg, fg=PALETTE["button_text"], activebackground=hover,
            activeforeground=PALETTE["gold"], relief="flat", bd=0,
            padx=16, pady=10, cursor="hand2",
            highlightbackground=PALETTE["gold_soft"], highlightthickness=1,
            justify="left", anchor="w" if width else "center",
        )
        if width:
            btn.configure(width=width)

        def on_enter(_e):
            btn.configure(bg=hover, fg=PALETTE["gold"])

        def on_leave(_e):
            btn.configure(bg=bg, fg=PALETTE["button_text"])

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # ------------------------------------------------------------------
    #  Déroulé de l'histoire
    # ------------------------------------------------------------------
    def start_story(self):
        self.clear_screen()
        self.display_story(self.current_part_id)

    def display_story(self, part_id):
        text, choices, image_path = get_story_part(part_id)

        if text is None or choices is None:
            messagebox.showerror("Erreur", "Partie d'histoire non valide.")
            return

        self.clear_screen()

        # -- en-tête façon manuscrit : numéro de passage ------------------
        header = tk.Frame(self.panel, bg=PALETTE["panel"])
        header.pack(fill="x", padx=24, pady=(18, 6))
        tk.Label(
            header, text=f"§ Passage n° {part_id}", bg=PALETTE["panel"],
            fg=PALETTE["gold_soft"], font=self.fonts["chapter"],
        ).pack(side="left")
        tk.Label(
            header, text="Luna et la Vallée aux Murmures", bg=PALETTE["panel"],
            fg=PALETTE["gold_soft"], font=self.fonts["chapter"],
        ).pack(side="right")

        body = tk.Frame(self.panel, bg=PALETTE["panel"])
        body.pack(fill="both", expand=True, padx=24, pady=(0, 18))

        # -- illustration, encadrée comme une enluminure -------------------
        if image_path and os.path.exists(image_path):
            try:
                image = tk.PhotoImage(file=image_path)
                self.image_ref = image
                frame_img = tk.Frame(
                    body, bg=PALETTE["gold_soft"], padx=3, pady=3,
                )
                frame_img.pack(pady=(4, 14))
                inner = tk.Frame(frame_img, bg="black", padx=2, pady=2)
                inner.pack()
                tk.Label(inner, image=image, bg="black").pack()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de charger l'image : {e}")

        # -- choix ou fin de chapitre ---------------------------------------
        # On packe d'abord les choix, ancrés en bas ("side=bottom") : ils
        # réservent ainsi toujours la place dont ils ont besoin et restent
        # visibles en entier, quel que soit leur nombre (2 ou 3 choix, ou le
        # bloc de fin de chapitre).
        choices_frame = tk.Frame(body, bg=PALETTE["panel"])
        choices_frame.pack(side="bottom", fill="x")

        # -- texte, sur un encart "parchemin" -------------------------------
        # Le cadre de texte occupe tout l'espace restant entre l'image et
        # les choix : sa taille est donc uniforme d'une vignette à l'autre
        # (elle dépend de la mise en page, pas de la longueur du texte). Si
        # le texte est trop long pour tenir dans cet espace, un ascenseur
        # apparaît pour le lire en entier, sans jamais empiéter sur les
        # choix ci-dessous, qui restent toujours entièrement visibles.
        parch_outer = tk.Frame(body, bg=PALETTE["parchment_edge"])
        parch_outer.pack(fill="both", expand=True, pady=(0, 18))
        parch_inner = tk.Frame(parch_outer, bg=PALETTE["parchment"])
        parch_inner.pack(fill="both", expand=True, padx=2, pady=2)

        text_wrapper = tk.Frame(parch_inner, bg=PALETTE["parchment"])
        text_wrapper.pack(fill="both", expand=True)

        self.text_label = tk.Text(
            text_wrapper, font=self.fonts["body"], height=5, width=1,
            bg=PALETTE["parchment"], fg=PALETTE["ink"], wrap="word",
            relief="flat", bd=0, padx=18, pady=16,
            highlightthickness=0, cursor="arrow",
        )
        # Ascenseur stylisé (thème ttk "clam" forcé plus haut) : rail sombre,
        # curseur doré large de 22 px, bien visible sur le parchemin clair.
        text_scroll = ttk.Scrollbar(
            text_wrapper, orient="vertical", command=self.text_label.yview,
            style="Story.Vertical.TScrollbar",
        )
        self.text_label.configure(yscrollcommand=text_scroll.set)

        self.text_label.pack(side="left", fill="both", expand=True)
        text_scroll.pack(side="right", fill="y", padx=(6, 0))

        self.text_label.insert("1.0", text)
        self.text_label.configure(state="disabled")  # lecture seule

        # Confort : la molette de la souris fait défiler le texte même
        # sans cliquer précisément sur l'ascenseur (Windows/Mac + Linux).
        def _on_mousewheel(event):
            if event.num == 4:          # Linux, molette vers le haut
                delta = -1
            elif event.num == 5:        # Linux, molette vers le bas
                delta = 1
            else:                       # Windows / macOS
                delta = -1 if event.delta > 0 else 1
            self.text_label.yview_scroll(delta, "units")
            return "break"

        for seq in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
            self.text_label.bind(seq, _on_mousewheel)

        if choices:
            for i, (key, value) in enumerate(choices.items()):
                marker = CIRCLED_DIGITS[i] if i < len(CIRCLED_DIGITS) else f"({i + 1})"
                label = f"{marker}  {value['text']}"
                btn = self._make_button(
                    choices_frame, label,
                    lambda k=key: self.make_choice(k), width=52,
                )
                btn.pack(fill="x", pady=5)
        else:
            self._separator(choices_frame, "❖")
            tk.Label(
                choices_frame, text="F I N   D E   C E   C H E M I N",
                bg=PALETTE["panel"], fg=PALETTE["gold"],
                font=self.fonts["subtitle"],
            ).pack(pady=(0, 14))
            self._make_button(choices_frame, "Reprendre l'aventure depuis le début",
                               self.restart_story, width=40).pack(pady=5)
            self._make_button(choices_frame, "Fermer le grimoire", self.root.quit,
                               width=40, danger=True).pack(pady=5)

    def make_choice(self, choice_key):
        next_part_id = get_next_part(self.current_part_id, choice_key)
        if next_part_id is not None:
            self.current_part_id = next_part_id
            self.display_story(next_part_id)
        else:
            messagebox.showerror("Erreur", "Choix non valide. Veuillez essayer à nouveau.")

    def restart_story(self):
        self.current_part_id = 1
        self.start_story()

    def clear_screen(self):
        for widget in self.panel.winfo_children():
            widget.destroy()
        self.text_label = None


if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()
