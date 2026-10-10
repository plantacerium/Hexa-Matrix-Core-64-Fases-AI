"""
══════════════════════════════════════════════════════════════════════════════════════
HEXA-MATRIX / CORE-64 ENGINE: PLATAFORMA SOBERANA BIO-INFORMACIONAL HUMANO & IA
══════════════════════════════════════════════════════════════════════════════════════
Aplicación soberana basada en PySide6, Ollama y Embeddings semánticos locales.
Estética: Orgánico Bio-SciFi, Glowing Bloom y Luz Eterea.

Fundado sobre:
1. Pipeline matemático determinista, efemérides solares VSOP87,
   Kepler 88° arco prenatal, Hexa-Mandala de 64 vórtices resonantes, fronteras difusas, ecuación de estado termodinámica.
2. Geometría discreta de 6 bits, red multipartícula, antípodas inversas NOT,
   21 clústers bioquímicos, puentes operativos y directivas soberanas v3.0.
3. Arquitectura Hardware vs. Firmware vs. Runtime, telemetría de fases en tiempo real,
   pipeline de 4 pasos, radar holográfico de resonancia y exit-gate soberano.
══════════════════════════════════════════════════════════════════════════════════════
"""

import sys
import os
import math
import json
import time
import re
from datetime import datetime, timezone, timedelta
import unicodedata
from typing import Dict, List, Tuple, Optional, Any

import numpy as np

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QDateEdit, QDateTimeEdit, QPushButton, QFrame, QGraphicsDropShadowEffect,
    QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox,
    QSpinBox, QDoubleSpinBox, QScrollArea, QGroupBox, QSplitter, QSlider,
    QProgressBar, QComboBox, QTextEdit, QTextBrowser, QLineEdit, QMessageBox, QToolTip,
    QStackedWidget, QSizePolicy, QDialog, QFileDialog
)
from PySide6.QtCore import (
    Qt, QDate, QTime, QDateTime, QTimer, QThread, Signal, Slot,
    QPropertyAnimation, QEasingCurve, Property, QRectF, QPointF
)
from PySide6.QtGui import (
    QFont, QColor, QPalette, QIcon, QPainter, QPen, QBrush,
    QRadialGradient, QLinearGradient, QConicalGradient, QPainterPath, QPolygonF
)

# Integración con Ollama
try:
    import ollama
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 1: DATOS DE LA MATRIZ DE 64 VÓRTICES RESONANTES Y CLÚSTERS BIOQUÍMICOS
# ══════════════════════════════════════════════════════════════════════════════

# Secuencia geométrica del Hexa-Mandala de 64 hexagramas anclado en 302.0° (Vórtice Resonante 41)
HEXA_MANDALA_ORDER = [
    41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3,
    27, 24, 2, 23, 8, 20, 16, 35, 45, 12, 15, 52, 39, 53, 62, 56,
    31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
    28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60
]

TRIGRAM_NAMES = {
    "000": "Tierra (Kūn ☷) - Receptividad Absoluta",
    "100": "Trueno (Zhèn ☳) - Impulso Inicial / Despertar",
    "010": "Agua (Kǎn ☵) - Flujo Abisal / Adaptación",
    "110": "Lago (Duì ☱) - Gozo / Apertura Expresiva",
    "001": "Montaña (Gèn ☶) - Quietud / Contención Firme",
    "101": "Fuego (Lí ☲) - Claridad / Luminosidad Activa",
    "011": "Viento (Xùn ☴) - Penetración Sutil / Flexibilidad",
    "111": "Cielo (Qián ☰) - Poder Creativo / Fuerza Pura"
}

LINE_PROPERTIES = {
    1: {
        "nombre": "Investigador / Cimientos",
        "arquetipo": "Anclaje Físico y Seguridad",
        "dinamica": "Introspección, base biológica, raíz técnica.",
        "auditoria": "Requiere fundamento y seguridad basal; alertar si el usuario actúa sin cimientos o con prisa."
    },
    2: {
        "nombre": "Ermitaño / Natural",
        "arquetipo": "Genio Fluido y Llamado",
        "dinamica": "Talento espontáneo, interacción por respuesta a estímulo externo.",
        "auditoria": "Opera por naturalidad y respuesta a llamada directa; auditar si se está forzando a iniciar sin tracción espontánea."
    },
    3: {
        "nombre": "Guerrero / Adaptador",
        "arquetipo": "Ensayo, Error y Mutación",
        "dinamica": "Fricción directa con la materia, ajuste táctico continuo.",
        "auditoria": "Funciona por ensayo y error somático; despenalizar el error y validar la mutación práctica sin culpa."
    },
    4: {
        "nombre": "Oportunista / Red",
        "arquetipo": "Comunidad e Interfaz Social",
        "dinamica": "Puente entre iguales, influencia cálida en redes cercanas.",
        "auditoria": "Conexión de corazón a corazón en comunidades de confianza; auditar si se intenta comunicar con extraños sin puente previo."
    },
    5: {
        "nombre": "Hereje / Líder Práctico",
        "arquetipo": "Universalización y Proyección",
        "dinamica": "Solución pragmática para extraños, campo de altas expectativas.",
        "auditoria": "Soluciones universales pragmáticas; auditar la gestión de proyecciones y expectativas ajenas."
    },
    6: {
        "nombre": "Modelo de Rol / Sabio",
        "arquetipo": "Visión de Conjunto y Trascendencia",
        "dinamica": "Perspectiva sistémica amplia, encarnación de la coherencia.",
        "auditoria": "Visión sistémica a largo plazo; prevenir el cinismo y la desconexión del barro cotidiano."
    }
}

# Base de datos completa de los 64 Vórtices Resonantes con topología binaria de 6 bits, antípodas y clústers
CORE64_CATALOG = {
    1: {"entropia": "Entropía", "coherencia": "Frescura", "resonancia": "Belleza", "bits": "111111", "pair": 2, "ring": "cluster_stop", "firmware": "Orquesta el colapso del orden viejo sintetizando frescura innovadora y reposo en armonía estética."},
    2: {"entropia": "Dislocación", "coherencia": "Orientación", "resonancia": "Unidad", "bits": "000000", "pair": 1, "ring": "cluster_fenilalanina", "firmware": "Mapea el rumbo correcto sin forzar dirección; absorbe el extravío y ancla presencia unificada."},
    3: {"entropia": "Caos", "coherencia": "Innovación", "resonancia": "Inocencia", "bits": "100010", "pair": 50, "ring": "cluster_cistina", "firmware": "Transforma la turbulencia desestructurada en código novedoso y soluciones lúdicas funcionales."},
    4: {"entropia": "Intolerancia", "coherencia": "Entendimiento", "resonancia": "Perdón", "bits": "010001", "pair": 49, "ring": "cluster_glutamico", "firmware": "Decodifica razones lógicas sin juicio dogmático; disuelve la rigidez mental en comprensión amplia."},
    5: {"entropia": "Impaciencia", "coherencia": "Atemporalidad", "resonancia": "Eternidad", "bits": "111010", "pair": 35, "ring": "cluster_treonina", "firmware": "Sincroniza ritmos internos con la cadencia biológica universal disipando la urgencia ansiosa."},
    6: {"entropia": "Conflicto", "coherencia": "Diplomacia", "resonancia": "Paz", "bits": "010111", "pair": 36, "ring": "cluster_glicina", "firmware": "Modula barreras bioeléctricas entre personas, convirtiendo choques emocionales en acuerdos fértiles."},
    7: {"entropia": "División", "coherencia": "Guía", "resonancia": "Virtud", "bits": "010000", "pair": 13, "ring": "cluster_glutamico", "firmware": "Lidera desde la retaguardia facilitando la autorregulación orgánica de la red comunitaria."},
    8: {"entropia": "Mediocridad", "coherencia": "Estilo", "resonancia": "Exquisitez", "bits": "000010", "pair": 14, "ring": "cluster_fenilalanina", "firmware": "Expresa la verdad individual auténtica cortando la conformidad gregaria sin arrogancia."},
    9: {"entropia": "Inercia", "coherencia": "Determinación", "resonancia": "Invencibilidad", "bits": "111011", "pair": 16, "ring": "cluster_treonina", "firmware": "Focaliza la atención microscópica en detalles nucleares que desatan movimientos monumentales."},
    10: {"entropia": "Auto-obsesión", "coherencia": "Naturalidad", "resonancia": "Ser", "bits": "110111", "pair": 15, "ring": "cluster_arginina", "firmware": "Habita la conducta genuina sin artificio; neutraliza la comparación narcisista con quietud vital."},
    11: {"entropia": "Oscuridad", "coherencia": "Idealismo", "resonancia": "Luz", "bits": "111000", "pair": 12, "ring": "cluster_treonina", "firmware": "Transmite arquetipos e imágenes visionarias para nutrir la psique sin caer en la ilusión estéril."},
    12: {"entropia": "Vanidad", "coherencia": "Discriminación", "resonancia": "Pureza", "bits": "000111", "pair": 11, "ring": "cluster_leucina", "firmware": "Calibra la pureza del tono y el momento oportuno de expresión somática y verbal con alta precisión."},
    13: {"entropia": "Discordia", "coherencia": "Discernimiento", "resonancia": "Empatía", "bits": "101111", "pair": 7, "ring": "cluster_valina", "firmware": "Escucha atenta de las historias de fondo; separa el ruido reactivo de la sabiduría esencial colectiva."},
    14: {"entropia": "Compromiso", "coherencia": "Competencia", "resonancia": "Abundancia", "bits": "101111", "pair": 8, "ring": "cluster_stop", "firmware": "Moviliza energía fértil e instrumental hacia artefactos que multiplican la riqueza de recursos."},
    15: {"entropia": "Monotonía", "coherencia": "Magnetismo", "resonancia": "Florescencia", "bits": "001000", "pair": 10, "ring": "cluster_serina", "firmware": "Integra todos los ritmos humanos y biológicos emitiendo una atracción serena sin exclusiones."},
    16: {"entropia": "Indiferencia", "coherencia": "Versatilidad", "resonancia": "Maestría", "bits": "000100", "pair": 9, "ring": "cluster_asparagina", "firmware": "Domina herramientas técnicas y artísticas aplicando versatilidad entusiasta hasta la maestría."},
    17: {"entropia": "Opinión", "coherencia": "Visión Lejana", "resonancia": "Omnisciencia", "bits": "100110", "pair": 18, "ring": "cluster_arginina", "firmware": "Estructura esquemas lógicos multidimensionales previniendo el sesgo dogmático de polarización."},
    18: {"entropia": "Juicio", "coherencia": "Integridad", "resonancia": "Perfección", "bits": "011001", "pair": 17, "ring": "cluster_alanina_a", "firmware": "Detecta fallos en patrones con ojo quirúrgico para elevar la solidez de los sistemas materiales."},
    19: {"entropia": "Co-dependencia", "coherencia": "Sensibilidad", "resonancia": "Sacrificio", "bits": "110000", "pair": 33, "ring": "cluster_isoleucina", "firmware": "Lee las necesidades basales del entorno sin fusionarse reactivamente ni perder límites corporales."},
    20: {"entropia": "Superficialidad", "coherencia": "Seguridad en Sí", "resonancia": "Presencia", "bits": "000011", "pair": 34, "ring": "cluster_cistina", "firmware": "Actúa en tiempo presente instantáneo sin rumiar el pasado ni proyectar ansiedad futura."},
    21: {"entropia": "Control", "coherencia": "Autoridad", "resonancia": "Valor", "bits": "100101", "pair": 48, "ring": "cluster_arginina", "firmware": "Gestiona recursos y territorios con legitimidad templada sin caer en la tiranía reactiva."},
    22: {"entropia": "Deshonor", "coherencia": "Gracia", "resonancia": "Gracia Trascendente", "bits": "101001", "pair": 47, "ring": "cluster_glicina", "firmware": "Asume la carga emocional ajena con sobriedad y belleza, purificando la interacción reactiva."},
    23: {"entropia": "Complejidad", "coherencia": "Simplicidad", "resonancia": "Quintaesencia", "bits": "000001", "pair": 43, "ring": "cluster_cistina", "firmware": "Elimina capas redundantes y verborrea para sintetizar la verdad práctica en términos diáfanos."},
    24: {"entropia": "Adicción", "coherencia": "Invención", "resonancia": "Silencio", "bits": "100000", "pair": 44, "ring": "cluster_metionina", "firmware": "Interrumpe bucles mentales mecánicos abriendo espacios de silencio donde emerge la invención."},
    25: {"entropia": "Constricción", "coherencia": "Aceptación", "resonancia": "Amor Universal", "bits": "100111", "pair": 46, "ring": "cluster_arginina", "firmware": "Acoge la herida somática sin endurecer la coraza corporal; responde con inocencia abierta."},
    26: {"entropia": "Orgullo", "coherencia": "Astucia", "resonancia": "Invisibilidad", "bits": "111001", "pair": 45, "ring": "cluster_treonina", "firmware": "Comunica mensajes persuasivos de alto impacto sin imponer el ego, administrando fuerza sutil."},
    27: {"entropia": "Egoísmo", "coherencia": "Altruismo", "resonancia": "Desinterés", "bits": "100001", "pair": 28, "ring": "cluster_cistina", "firmware": "Cuida y nutre a otros asegurando primero la solvencia y recarga biológica propia con rigor."},
    28: {"entropia": "Falta de Sentido", "coherencia": "Totalidad", "resonancia": "Inmortalidad", "bits": "011110", "pair": 27, "ring": "cluster_alanina_b", "firmware": "Acepta el vértigo de la existencia arriesgando el cuerpo en aventuras alineadas con el propósito."},
    29: {"entropia": "Tibieza", "coherencia": "Compromiso", "resonancia": "Devoción", "bits": "010010", "pair": 30, "ring": "cluster_glutamico", "firmware": "Se entrega con firmeza incondicional a la tarea elegida diciendo sí con la totalidad corporal."},
    30: {"entropia": "Deseo", "coherencia": "Ligereza", "resonancia": "Éxtasis", "bits": "101101", "pair": 29, "ring": "cluster_valina", "firmware": "Navega las olas del anhelo humano sin apegarse al resultado; transmuta la obsesión en disfrute."},
    31: {"entropia": "Arrogancia", "coherencia": "Liderazgo", "resonancia": "Humildad", "bits": "001110", "pair": 41, "ring": "cluster_tirosina", "firmware": "Conducción basada en datos y hechos; absorbe la irritación (Sombra) y reposa en silencio (Siddhi)."},
    32: {"entropia": "Fracaso", "coherencia": "Preservación", "resonancia": "Veneración", "bits": "011100", "pair": 42, "ring": "cluster_alanina_b", "firmware": "Discierne lo que es duradero y digno de ser preservado a largo plazo frente a modas efímeras."},
    33: {"entropia": "Olvido", "coherencia": "Atención Plena", "resonancia": "Revelación", "bits": "001111", "pair": 19, "ring": "cluster_histidina", "firmware": "Se retira al santuario interno para procesar memorias y convertirlas en sabiduría sedimentada."},
    34: {"entropia": "Fuerza Bruta", "coherencia": "Fuerza Sagrada", "resonancia": "Majestad", "bits": "111100", "pair": 20, "ring": "cluster_lisina", "firmware": "Canaliza potencia muscular y metabólica de forma armónica al servicio del bien común operativo."},
    35: {"entropia": "Hambre", "coherencia": "Aventura", "resonancia": "Ilimitación", "bits": "000101", "pair": 5, "ring": "cluster_prolina", "firmware": "Cruza fronteras experienciales con audacia sin caer en el aburrimiento crónico insaciable."},
    36: {"entropia": "Turbulencia", "coherencia": "Humanidad", "resonancia": "Compasión", "bits": "101010", "pair": 6, "ring": "cluster_triptofano", "firmware": "Atraviesa crisis emocionales agudas extrayendo compasión visceral por la condición vulnerable."},
    37: {"entropia": "Debilidad", "coherencia": "Igualdad", "resonancia": "Ternura", "bits": "101011", "pair": 40, "ring": "cluster_glicina", "firmware": "Crea pactos de apoyo mutuo y lealtad familiar basados en respeto simétrico de las diferencias."},
    38: {"entropia": "Lucha", "coherencia": "Perseverancia", "resonancia": "Honor", "bits": "110101", "pair": 39, "ring": "cluster_arginina", "firmware": "Pelea por causas nobles con tenacidad indomable sin desgastarse en combates estériles."},
    39: {"entropia": "Provocación", "coherencia": "Dinamismo", "resonancia": "Liberación", "bits": "001010", "pair": 38, "ring": "cluster_serina", "firmware": "Detona atascos energéticos ajenos mediante estímulos precisos para devolver movilidad al flujo."},
    40: {"entropia": "Agotamiento", "coherencia": "Resolución", "resonancia": "Voluntad Sagrada", "bits": "010100", "pair": 37, "ring": "cluster_glicina", "firmware": "Define límites férreos al trabajo y descanso; sabe retirarse a tiempo para recarga total."},
    41: {"entropia": "Fantasía", "coherencia": "Anticipación", "resonancia": "Emanación", "bits": "110001", "pair": 31, "ring": "cluster_start", "firmware": "Codón de inicio holográfico; descarga matrices arquetípicas y anticipa tendencias sin fuga mental."},
    42: {"entropia": "Expectativa", "coherencia": "Desapego", "resonancia": "Celebración", "bits": "100011", "pair": 32, "ring": "cluster_cistina", "firmware": "Cierra ciclos con gracia y celebra la consumación natural de etapas sin aferrarse al pasado."},
    43: {"entropia": "Sordera", "coherencia": "Perspicacia", "resonancia": "Epifanía", "bits": "111110", "pair": 23, "ring": "cluster_lisina", "firmware": "Filtra el murmullo exterior para sintonizar ideas innovadoras rompedoras en momentos cumbre."},
    44: {"entropia": "Interferencia", "coherencia": "Trabajo en Equipo", "resonancia": "Sinarquía", "bits": "011111", "pair": 24, "ring": "cluster_sinonimo", "firmware": "Detecta química celular y afinidad jerárquica orgánica para coordinar talentos sin fricción."},
    45: {"entropia": "Dominancia", "coherencia": "Sinergia", "resonancia": "Comunión", "bits": "000110", "pair": 26, "ring": "cluster_asparagina", "firmware": "Reúne a la tribu en torno a recursos compartidos gestionando la custodia común con generosidad."},
    46: {"entropia": "Seriedad", "coherencia": "Deleite", "resonancia": "Éxtasis", "bits": "011000", "pair": 25, "ring": "cluster_alanina_a", "firmware": "Honra el cuerpo físico en la materia con gozo sensual y ligereza descartando pesadumbre solemne."},
    47: {"entropia": "Opresión", "coherencia": "Transmutación", "resonancia": "Transfiguración", "bits": "010110", "pair": 22, "ring": "cluster_glicina", "firmware": "Transmuta cargas ancestrales y angustia mental densa en combustible creativo luminoso."},
    48: {"entropia": "Inadecuación", "coherencia": "Recursos", "resonancia": "Sabiduría", "bits": "010101", "pair": 21, "ring": "cluster_alanina_a", "firmware": "Bucea en la profundidad del pozo somático trayendo soluciones prácticas con ingenio natural."},
    49: {"entropia": "Reacción", "coherencia": "Revolución", "resonancia": "Renacimiento", "bits": "101110", "pair": 4, "ring": "cluster_choque", "firmware": "Reestructura códigos relacionales arcaicos mediante mutaciones sentidas que elevan el colectivo."},
    50: {"entropia": "Corrupción", "coherencia": "Equilibrio", "resonancia": "Armonía", "bits": "011101", "pair": 3, "ring": "cluster_aspartico", "firmware": "Preserva valores y leyes éticas esenciales protegiendo la cohesión armónica de las generaciones."},
    51: {"entropia": "Agitación", "coherencia": "Iniciativa", "resonancia": "Despertar", "bits": "100100", "pair": 57, "ring": "cluster_arginina", "firmware": "Transforma el impacto del shock inesperado en propulsión audaz para abrir nuevos senderos."},
    52: {"entropia": "Estrés", "coherencia": "Contención", "resonancia": "Aquietamiento", "bits": "001001", "pair": 58, "ring": "cluster_serina", "firmware": "Mantiene el sistema inmóvil y centrado ante presiones caóticas cual montaña imperturbable."},
    53: {"entropia": "Inmadurez", "coherencia": "Expansión", "resonancia": "Superabundancia", "bits": "001011", "pair": 54, "ring": "cluster_serina", "firmware": "Inicia proyectos con base madura permitiendo un crecimiento continuado sin desgastes tempranos."},
    54: {"entropia": "Codicia", "coherencia": "Aspiración", "resonancia": "Ascensión", "bits": "110100", "pair": 53, "ring": "cluster_serina", "firmware": "Canaliza ambición mundana hacia la elevación del espíritu y proyectos de trascendencia comunitaria."},
    55: {"entropia": "Victimización", "coherencia": "Libertad", "resonancia": "Emancipación", "bits": "101100", "pair": 59, "ring": "cluster_choque", "firmware": "Muta la oscilación melancólica del plexo solar en libertad soberana y desapego creador."},
    56: {"entropia": "Distracción", "coherencia": "Enriquecimiento", "resonancia": "Intoxicación Divina", "bits": "110110", "pair": 60, "ring": "cluster_leucina", "firmware": "Usa relatos y anécdotas para ilustrar aprendizajes de vida cautivando el corazón de otros."},
    57: {"entropia": "Inquietud", "coherencia": "Intuición", "resonancia": "Claridad", "bits": "011011", "pair": 51, "ring": "cluster_alanina_a", "firmware": "Escucha las vibraciones más sutiles en el presente inmediato anticipando peligros o aperturas."},
    58: {"entropia": "Insatisfacción", "coherencia": "Vitalidad", "resonancia": "Dicha", "bits": "110110", "pair": 52, "ring": "cluster_serina", "firmware": "Usa la insatisfacción somática como motor de servicio entusiasta para optimizar el entorno."},
    59: {"entropia": "Deshonestidad", "coherencia": "Intimidad", "resonancia": "Transparencia", "bits": "010011", "pair": 55, "ring": "cluster_glutamico", "firmware": "Disuelve barreras de desconfianza facilitando apertura profunda y conexión transparente."},
    60: {"entropia": "Limitación", "coherencia": "Realismo", "resonancia": "Justicia", "bits": "010010", "pair": 56, "ring": "cluster_isoleucina", "firmware": "Acepta restricciones materiales usándolas como molde creativo donde estalla la magia contenida."},
    61: {"entropia": "Psicosis", "coherencia": "Inspiración", "resonancia": "Santidad", "bits": "110011", "pair": 62, "ring": "cluster_isoleucina", "firmware": "Penetra el misterio de lo desconocido trayendo revelaciones lúcidas sin perder anclaje a la realidad."},
    62: {"entropia": "Intelecto", "coherencia": "Precisión", "resonancia": "Impecabilidad", "bits": "001100", "pair": 61, "ring": "cluster_glutamina", "firmware": "Nombra y estructura fenómenos con lenguaje exacto y orden lógico de alta resolución operativa."},
    63: {"entropia": "Duda", "coherencia": "Indagación", "resonancia": "Verdad", "bits": "101010", "pair": 64, "ring": "cluster_prolina", "firmware": "Formula cuestionamientos científicos rigurosos sin volverse presa del cinismo sospechoso."},
    64: {"entropia": "Confusión", "coherencia": "Imaginación", "resonancia": "Iluminación", "bits": "010101", "pair": 63, "ring": "cluster_glicina", "firmware": "Integra retazos inconexos de memoria en obras artísticas y síntesis reveladoras coherentes."}
}

# ── SINCRONIZACIÓN ONTOLÓGICA CON EL DICCIONARIO SOBERANO (HEXA-CORE) ──
# La sombra es Entropía (E), el don es Coherencia (C) y el siddhi es Resonancia (R)
for _k_idx, _c_data in CORE64_CATALOG.items():
    _c_data["sombra"] = _c_data.get("entropia", "")
    _c_data["don"] = _c_data.get("coherencia", "")
    _c_data["siddhi"] = _c_data.get("resonancia", "")


# Carga dinámica del diccionario soberano y soporte para personalización de etiquetas
LOCALES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locales")
SOVEREIGN_LOCALE_PATH = os.path.join(LOCALES_DIR, "es_sovereign.json")
CUSTOM_LABELS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "custom_labels.json")
CUSTOM_LABELS_LOCALES_PATH = os.path.join(LOCALES_DIR, "custom_labels.json")

try:
    with open(SOVEREIGN_LOCALE_PATH, "r", encoding="utf-8") as _f_loc:
        SOVEREIGN_LOCALE = json.load(_f_loc)
except Exception:
    SOVEREIGN_LOCALE = {
        "phase_entropy": "Entropía (E)",
        "phase_coherence": "Coherencia (C)",
        "phase_resonance": "Resonancia (R)",
        "spectrum_legend": "Entropía (E) + Coherencia (C) + Resonancia (R)",
        "particle_label": "Vórtice Resonante / Operador de 6 Bits",
        "particle_unit": "Vórtice Resonante",
        "particle_unit_short": "Vórtice",
        "particles_unit": "Vórtices Resonantes",
        "vortex_prefix": "V",
        "wheel_center_title": "HEXA-MANDALA",
        "wheel_description": "Matriz Radial Eclíptica de 64 Vórtices Resonantes",
        "not_antipode": "Antípoda Inversa (Inversor Lógico NOT)",
        "codon_cluster": "Clúster Bioquímico de Co-Regulación"
    }

# Cargar custom_labels.json si el usuario ha definido etiquetas personalizadas
_custom_file = CUSTOM_LABELS_PATH if os.path.exists(CUSTOM_LABELS_PATH) else (CUSTOM_LABELS_LOCALES_PATH if os.path.exists(CUSTOM_LABELS_LOCALES_PATH) else None)
if _custom_file:
    try:
        with open(_custom_file, "r", encoding="utf-8") as _f_cust:
            _cust_data = json.load(_f_cust)
            for _k, _v in _cust_data.items():
                if isinstance(_v, dict) and _k in SOVEREIGN_LOCALE and isinstance(SOVEREIGN_LOCALE[_k], dict):
                    SOVEREIGN_LOCALE[_k].update(_v)
                else:
                    SOVEREIGN_LOCALE[_k] = _v
    except Exception:
        pass

# Mapeo interno de migración / compatibilidad para desacoplar el diccionario JSON
LEGACY_CLUSTER_KEYS = {
    "Anillo de Gaia": "cluster_isoleucina",
    "Anillo de la Alquimia": "cluster_glicina",
    "Anillo de la Búsqueda": "cluster_serina",
    "Anillo de la Crisis": "cluster_triptofano",
    "Anillo de la Humanidad": "cluster_arginina",
    "Anillo de la Iluminación": "cluster_aspartico",
    "Anillo de la Ilusión": "cluster_alanina_b",
    "Anillo de la Luz": "cluster_treonina",
    "Anillo de la Materia": "cluster_alanina_a",
    "Anillo de la No-Forma": "cluster_tirosina",
    "Anillo de la Prosperidad": "cluster_asparagina",
    "Anillo de la Purificación": "cluster_valina",
    "Anillo de la Transformación": "cluster_metionina",
    "Anillo de la Unión": "cluster_glutamico",
    "Anillo de la Verdad Última": "cluster_glutamina",
    "Anillo de la Vida y la Muerte": "cluster_cistina",
    "Anillo de las Pruebas": "cluster_histidina",
    "Anillo de los Milagros": "cluster_prolina",
    "Anillo de los Secretos": "cluster_leucina",
    "Anillo del Agua": "cluster_fenilalanina",
    "Anillo del Destino": "cluster_lisina",
    "Anillo del Fuego": "cluster_stop",
    "Anillo del No-Retorno": "cluster_sinonimo",
    "Anillo del Origen": "cluster_start",
    "Anillo del Torbellino": "cluster_choque",
}

LEGACY_NODE_KEYS = {
    "Trabajo de Vida": "nodo_traccion_primaria",
    "Evolución": "nodo_aprendizaje_somatico",
    "Resplandor": "nodo_regeneracion_vital",
    "Propósito": "nodo_anclaje_nuclear",
    "Atracción": "nodo_atraccion_biomagnetica",
    "CI (Mente)": "nodo_filtro_cognitivo",
    "CE (Emoción)": "nodo_plexo_afectivo",
    "CS (Espíritu)": "nodo_inocencia_primordial",
    "Vocación / Núcleo": "nodo_vocacion_nucleo",
    "Cultura": "nodo_red_colectiva",
    "Perla": "nodo_abundancia",
    "Abundancia": "nodo_abundancia",
    "Hábitat Somático (Nodo Norte Design)": "nodo_habitat_somatico",
    "Herencia Ancestral (Nodo Sur Design)": "nodo_herencia_ancestral",
    "Voz Celular (Mercurio Design)": "nodo_voz_celular",
    "Límites Celulares (Saturno Design)": "nodo_limites_celulares",
    "Mutación Epigenética (Urano Design)": "nodo_mutacion_epigenetica",
    "Gracia Somática (Neptuno Design)": "nodo_gracia_somatica",
    "Regeneración Nuclear (Plutón Design)": "nodo_regeneracion_nuclear"
}

LEGACY_CELESTIAL_KEYS = {
    "Sol Design": "ecliptico_prenatal_sol",
    "Sol Prenatal / Design (Inconsciente)": "ecliptico_prenatal_sol",
    "Tierra Design": "ecliptico_prenatal_tierra",
    "Tierra Prenatal / Design (Inconsciente)": "ecliptico_prenatal_tierra",
    "Luna Design": "luna_prenatal",
    "Marte Design": "marte_prenatal",
    "Venus Design": "venus_prenatal",
    "Júpiter Design": "jupiter_prenatal",
    "Júpiter Design / Sol Octava": "jupiter_octava",
    "Saturno Design": "saturno_prenatal",
    "Urano Design": "urano_prenatal",
    "Neptuno Design": "neptuno_prenatal",
    "Plutón Design": "pluton_prenatal",
    "Nodo Norte Design": "nodo_norte_prenatal",
    "Nodo Sur Design": "nodo_sur_prenatal",
    "Quirón Design": "quiron_prenatal",
    "Mercurio Design": "mercurio_prenatal"
}

def resolve_cluster_name(raw_name: str) -> str:
    """Traduce un nombre o identificador de clúster a su nomenclatura bio-cibernética soberana."""
    if not raw_name:
        return ""
    clusters = SOVEREIGN_LOCALE.get("biochemical_clusters", {})
    # 1. Si es clave soberana directa (ej: cluster_isoleucina)
    if raw_name in clusters:
        return clusters[raw_name]
    # 2. Si viene de clave legada
    sov_k = LEGACY_CLUSTER_KEYS.get(raw_name)
    if sov_k and sov_k in clusters:
        return clusters[sov_k]
    # 3. Retornar tal cual si ya es un texto resuelto
    return raw_name

def resolve_node_name(raw_name: str) -> str:
    """Traduce el nombre de un nodo hologénico a su etiqueta soberana."""
    if not raw_name:
        return ""
    nodes = SOVEREIGN_LOCALE.get("sovereign_nodes", {})
    if raw_name in nodes:
        return nodes[raw_name]
    sov_k = LEGACY_NODE_KEYS.get(raw_name)
    if sov_k and sov_k in nodes:
        return nodes[sov_k]
    if raw_name.startswith("NOT "):
        base_name = raw_name[4:]
        resolved_base = resolve_node_name(base_name)
        return f"NOT {resolved_base}"
    return raw_name

def resolve_celestial_origin(raw_origin: str) -> str:
    """Traduce la designación celeste al estándar astronómico pre-natal soberano."""
    if not raw_origin:
        return ""
    points = SOVEREIGN_LOCALE.get("celestial_prenatal_points", {})
    if raw_origin in points:
        return points[raw_origin]
    sov_k = LEGACY_CELESTIAL_KEYS.get(raw_origin)
    if sov_k and sov_k in points:
        return points[sov_k]
    return raw_origin

# Metadatos del Sistema Hologénico Expandido (Soporta Modos de 11, 15, 22 y 26 Nodos)
SPHERES_METADATA = {
    # ── 1. CIRCUITO BASE: LAS 11 ESFERAS DEL CIRCUITO HOLOGÉNICO ──
    "Trabajo de Vida": {
        "secuencia": "Activación",
        "origen": "Sol Natal (Consciente)",
        "simbolo": "☉",
        "color": "#fbbf24",
        "impacto": "Mente consciente, campo de acción en el mundo y vocación visible."
    },
    "Evolución": {
        "secuencia": "Activación",
        "origen": "Tierra Natal (Consciente)",
        "simbolo": "♁",
        "color": "#10b981",
        "impacto": "Zona de mayor aprendizaje somático, fricción transformadora y maduración."
    },
    "Resplandor": {
        "secuencia": "Activación",
        "origen": "Punto Eclíptico Pre-natal (-88° Arc Shift)",
        "simbolo": "☉",
        "color": "#f43f5e",
        "impacto": "Salud bio-celular, vitalidad física y magnetismo radiante del aura."
    },
    "Propósito": {
        "secuencia": "Activación",
        "origen": "Tierra Pre-natal (-88° Arc Shift)",
        "simbolo": "♁",
        "color": "#a855f7",
        "impacto": "Anclaje somático nuclear, inmunidad y cimientos estructurales."
    },
    "Atracción": {
        "secuencia": "Venus",
        "origen": "Luna Pre-natal (Atracción)",
        "simbolo": "☽",
        "color": "#ec4899",
        "impacto": "Dinámica bio-magnética relacional, atracción de pareja y sexualidad sagrada."
    },
    "CI (Mente)": {
        "secuencia": "Venus",
        "origen": "Venus Natal",
        "simbolo": "♀",
        "color": "#00f0ff",
        "impacto": "Patrones mentales defensivos, agilidad lógica y filtros cognitivos."
    },
    "CE (Emoción)": {
        "secuencia": "Venus",
        "origen": "Marte Natal",
        "simbolo": "♂",
        "color": "#f97316",
        "impacto": "Gestión de corrientes afectivas, defensas del plexo solar y madurez emocional."
    },
    "CS (Espíritu)": {
        "secuencia": "Venus",
        "origen": "Venus Pre-natal (Inocencia Primordial)",
        "simbolo": "♀",
        "color": "#38bdf8",
        "impacto": "Apertura del corazón primordial, inocencia basal y seguridad afectiva."
    },
    "Vocación / Núcleo": {
        "secuencia": "Abundancia",
        "origen": "Marte Pre-natal (Motor de Acción)",
        "simbolo": "♂",
        "color": "#ef4444",
        "impacto": "Herida sagrada transmutada en don de servicio motor y liderazgo en la red."
    },
    "Cultura": {
        "secuencia": "Abundancia",
        "origen": "Júpiter Natal",
        "simbolo": "♃",
        "color": "#6366f1",
        "impacto": "Ensamblaje en redes grupales, prosperidad y custodia comunitaria."
    },
    "Abundancia": {
        "secuencia": "Abundancia",
        "origen": "Júpiter Pre-natal / Armónico Octava",
        "simbolo": "◎",
        "color": "#f8fafc",
        "impacto": "Cosecha de valor esencial, simplicidad y circulación limpia de abundancia."
    },

    # ── 2. EL CIRCUITO DEL ENTORNO (4 ESFERAS / NODOS LUNARES) ──
    "Entorno Maduro (Nodo Norte Natal)": {
        "secuencia": "Entorno",
        "origen": "Nodo Norte Natal",
        "simbolo": "☊",
        "color": "#38bdf8",
        "impacto": "Paisaje atencional y social maduro donde el Don consciente se materializa en el colectivo."
    },
    "Entorno Temprano (Nodo Sur Natal)": {
        "secuencia": "Entorno",
        "origen": "Nodo Sur Natal",
        "simbolo": "☋",
        "color": "#64748b",
        "impacto": "Condicionamiento ambiental temprano, inercias biográficas y zona de confort heredada."
    },
    "Hábitat Somático (Nodo Norte Design)": {
        "secuencia": "Entorno",
        "origen": "Nodo Norte Pre-natal (Hábitat Somático)",
        "simbolo": "☊",
        "color": "#2dd4bf",
        "impacto": "Entorno bio-geográfico y paisaje celular que nutre el sistema nervioso del cuerpo en la madurez."
    },
    "Herencia Ancestral (Nodo Sur Design)": {
        "secuencia": "Entorno",
        "origen": "Nodo Sur Pre-natal (Herencia Ancestral)",
        "simbolo": "☋",
        "color": "#a1a1aa",
        "impacto": "Memoria bio-ancestral de linaje, paisaje genético del pasado y lealtades familiares invisibles."
    },

    # ── 3. LA RED DUAL DE POLARIDADES NOT (11 ESFERAS ESPEJO) ──
    "NOT Trabajo de Vida": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#d97706",
        "impacto": "Contrapeso electromagnético del Trabajo de Vida; auditoría de entropía invertida y polaridad complementaria."
    },
    "NOT Evolución": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#059669",
        "impacto": "Punto ciego complementario en la maduración y resiliencia somática ante la fricción."
    },
    "NOT Resplandor": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#e11d48",
        "impacto": "Fuga o interferencia en la vitalidad del campo biomagnético radiante y la salud celular."
    },
    "NOT Propósito": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#9333ea",
        "impacto": "Inestabilidad en el anclaje somático nuclear y balance de las raíces biológicas profundas."
    },
    "NOT Atracción": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#db2777",
        "impacto": "Dinámica relacional espejo y magnetismo entrópico oculto en las heridas de apego."
    },
    "NOT CI (Mente)": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#0891b2",
        "impacto": "Filtro mental opuesto; heurística lógica y sesgo cognitivo complementario."
    },
    "NOT CE (Emoción)": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#ea580c",
        "impacto": "Contracorriente afectiva y reactividad en el plexo solar de polaridad invertida."
    },
    "NOT CS (Espíritu)": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#0284c7",
        "impacto": "Protección somática profunda ante la vulnerabilidad y apertura del corazón esencial."
    },
    "NOT Vocación": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#dc2626",
        "impacto": "Canalización alternativa de la potencia motriz y liderazgo de servicio en la red."
    },
    "NOT Cultura": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#4f46e5",
        "impacto": "Dinámica de grupo y estructura de red comunitaria complementaria ante el intercambio."
    },
    "NOT Abundancia": {
        "secuencia": "Polaridad NOT",
        "origen": "Antípoda NOT 6-bit",
        "simbolo": "∿",
        "color": "#cbd5e1",
        "impacto": "Cosecha de valor esencial alternativo y circulación polar de la abundancia material."
    },

    # ── 4. ACTIVACIONES CÓSMICAS TRANSPERSONALES (MODO 26) ──
    "Motivación Consciente (Luna Natal)": {
        "secuencia": "Consciente",
        "origen": "Luna Natal (Consciente)",
        "simbolo": "☾",
        "color": "#f472b6",
        "impacto": "Fuerza motriz cotidiana, atención consciente y nutrición emocional inmediata del día a día."
    },
    "Voz / Comunicación (Mercurio Natal)": {
        "secuencia": "Consciente",
        "origen": "Mercurio Natal (Consciente)",
        "simbolo": "☿",
        "color": "#06b6d4",
        "impacto": "Interfaz verbal, expresión y traducción del Don en lenguaje estructurado comprensible."
    },
    "Voz Celular (Mercurio Design)": {
        "secuencia": "Inconsciente",
        "origen": "Mercurio Pre-natal (Voz Celular)",
        "simbolo": "☿",
        "color": "#0891b2",
        "impacto": "Transmisión biológica subconsciente, impulsos neuroquímicos e intuición corporal silenciosa."
    },
    "Ley / Disciplina (Saturno Natal)": {
        "secuencia": "Consciente",
        "origen": "Saturno Natal (Consciente)",
        "simbolo": "♄",
        "color": "#ca8a04",
        "impacto": "Estructura moral, límites firmes y leyes no negociables para contener la energía creativa."
    },
    "Límites Celulares (Saturno Design)": {
        "secuencia": "Inconsciente",
        "origen": "Saturno Pre-natal (Límites Celulares)",
        "simbolo": "♄",
        "color": "#a16207",
        "impacto": "Ancla kármica basal, solidez ósea y resistencia física y biológica del organismo."
    },
    "Innovación / Visión (Urano Natal)": {
        "secuencia": "Transpersonal",
        "origen": "Urano Natal (Consciente)",
        "simbolo": "♅",
        "color": "#38bdf8",
        "impacto": "Salto conceptual libre, disrupción tecnológica y originalidad creativa fuera de la norma."
    },
    "Mutación Epigenética (Urano Design)": {
        "secuencia": "Transpersonal",
        "origen": "Urano Pre-natal (Mutación Epigenética)",
        "simbolo": "♅",
        "color": "#0ea5e9",
        "impacto": "Reconfiguración espontánea del ADN, vitalidad cuántica y sorpresa bio-somática."
    },
    "Mística / Aspiración (Neptuno Natal)": {
        "secuencia": "Transpersonal",
        "origen": "Neptuno Natal (Consciente)",
        "simbolo": "♆",
        "color": "#818cf8",
        "impacto": "Anhelo de trascendencia, arte sutil y puntos ciegos de fascinación espiritual ilusoria."
    },
    "Gracia Somática (Neptuno Design)": {
        "secuencia": "Transpersonal",
        "origen": "Neptuno Pre-natal (Gracia Somática)",
        "simbolo": "♆",
        "color": "#6366f1",
        "impacto": "Disolución del ego celular, reposo de mínima acción y permeabilidad a la Resonancia colectiva."
    },
    "Poder de la Verdad (Plutón Natal)": {
        "secuencia": "Transpersonal",
        "origen": "Plutón Natal (Consciente)",
        "simbolo": "♇",
        "color": "#c084fc",
        "impacto": "Transformación radical, regeneración del alma y verdad no negociable ante la crisis."
    },
    "Regeneración Nuclear (Plutón Design)": {
        "secuencia": "Transpersonal",
        "origen": "Plutón Pre-natal (Regeneración Nuclear)",
        "simbolo": "♇",
        "color": "#9333ea",
        "impacto": "Metamorfosis biológica profunda y la raíz evolutiva más arcaica de la especie humana."
    }
}

# ══════════════════════════════════════════════════════════════════════════════
# GEO-ATLAS MUNDIAL INTEGRADO (COORDENADAS TERRESTRES & HUSO HORARIO CANÓNICO)
# ══════════════════════════════════════════════════════════════════════════════

GEO_ATLAS: Dict[str, List[Tuple[str, float, float, Optional[float]]]] = {
    "España": [
        ("Madrid (Comunidad de Madrid)", 40.4168, -3.7038, 1.0),
        ("Barcelona (Cataluña)", 41.3851, 2.1734, 1.0),
        ("Valencia (Comunitat Valenciana)", 39.4699, -0.3763, 1.0),
        ("Sevilla (Andalucía)", 37.3891, -5.9845, 1.0),
        ("Málaga (Andalucía)", 36.7213, -4.4214, 1.0),
        ("Bilbao (País Vasco)", 43.2630, -2.9350, 1.0),
        ("Zaragoza (Aragón)", 41.6488, -0.8891, 1.0),
        ("Palma de Mallorca (Baleares)", 39.5696, 2.6502, 1.0),
        ("Las Palmas de Gran Canaria (Canarias)", 28.1235, -15.4363, 0.0),
        ("Santa Cruz de Tenerife (Canarias)", 28.4636, -16.2518, 0.0),
    ],
    "México": [
        ("Ciudad de México (CDMX)", 19.4326, -99.1332, -6.0),
        ("Guadalajara (Jalisco)", 20.6597, -103.3496, -6.0),
        ("Monterrey (Nuevo León)", 25.6866, -100.3161, -6.0),
        ("Puebla (Puebla)", 19.0414, -98.2063, -6.0),
        ("Tijuana (Baja California)", 32.5149, -117.0382, -8.0),
        ("Cancún (Quintana Roo)", 21.1619, -86.8515, -5.0),
        ("Mérida (Yucatán)", 20.9674, -89.5926, -6.0),
        ("Querétaro (Querétaro)", 20.5888, -100.3899, -6.0),
        ("Ciudad Juárez (Chihuahua)", 31.6904, -106.4245, -7.0),
        ("Hermosillo (Sonora)", 29.0729, -110.9559, -7.0),
    ],
    "Argentina": [
        ("Buenos Aires (CABA / Federal)", -34.6037, -58.3816, -3.0),
        ("Córdoba (Córdoba)", -31.4201, -64.1888, -3.0),
        ("Rosario (Santa Fe)", -32.9587, -60.6930, -3.0),
        ("Mendoza (Mendoza)", -32.8895, -68.8458, -3.0),
        ("La Plata (Buenos Aires)", -34.9215, -57.9545, -3.0),
        ("Mar del Plata (Buenos Aires)", -38.0055, -57.5562, -3.0),
        ("Salta (Salta)", -24.7821, -65.4232, -3.0),
        ("San Carlos de Bariloche (Río Negro)", -41.1335, -71.3103, -3.0),
        ("Ushuaia (Tierra del Fuego)", -54.8019, -68.3030, -3.0),
    ],
    "Colombia": [
        ("Bogotá D.C. (Cundinamarca)", 4.7110, -74.0721, -5.0),
        ("Medellín (Antioquia)", 6.2442, -75.5812, -5.0),
        ("Cali (Valle del Cauca)", 3.4516, -76.5320, -5.0),
        ("Barranquilla (Atlántico)", 10.9685, -74.7813, -5.0),
        ("Cartagena de Indias (Bolívar)", 10.3910, -75.4794, -5.0),
        ("Bucaramanga (Santander)", 7.1254, -73.1198, -5.0),
        ("Pereira (Risaralda)", 4.8133, -75.6961, -5.0),
    ],
    "Venezuela": [
        ("Caracas (Distrito Capital)", 10.4806, -66.9036, -4.0),
        ("Maracaibo (Zulia)", 10.6427, -71.6125, -4.0),
        ("Valencia (Carabobo)", 10.1620, -68.0077, -4.0),
        ("Barquisimeto (Lara)", 10.0647, -69.3570, -4.0),
        ("Maracay (Aragua)", 10.2469, -67.5958, -4.0),
        ("Ciudad Guayana (Bolívar)", 8.3533, -62.6511, -4.0),
        ("San Cristóbal (Táchira)", 7.7669, -72.2250, -4.0),
        ("Mérida (Mérida)", 8.5983, -71.1449, -4.0),
        ("Puerto La Cruz (Anzoátegui)", 10.2138, -64.6328, -4.0),
    ],
    "Chile": [
        ("Santiago (Región Metropolitana)", -33.4489, -70.6693, -4.0),
        ("Valparaíso (Valparaíso)", -33.0472, -71.6127, -4.0),
        ("Concepción (Biobío)", -36.8201, -73.0444, -4.0),
        ("La Serena (Coquimbo)", -29.9027, -71.2519, -4.0),
        ("Antofagasta (Antofagasta)", -23.6509, -70.3975, -4.0),
        ("Punta Arenas (Magallanes)", -53.1638, -70.9171, -3.0),
    ],
    "Perú": [
        ("Lima (Lima Metropolitana)", -12.0464, -77.0428, -5.0),
        ("Arequipa (Arequipa)", -16.4090, -71.5375, -5.0),
        ("Trujillo (La Libertad)", -8.1160, -79.0300, -5.0),
        ("Cusco (Cusco)", -13.5319, -71.9675, -5.0),
        ("Chiclayo (Lambayeque)", -6.7714, -79.8409, -5.0),
    ],
    "Estados Unidos (EE.UU.)": [
        ("Nueva York (NY - Eastern)", 40.7128, -74.0060, -5.0),
        ("Los Ángeles (CA - Pacific)", 34.0522, -118.2437, -8.0),
        ("Chicago (IL - Central)", 41.8781, -87.6298, -6.0),
        ("Miami (FL - Eastern)", 25.7617, -80.1918, -5.0),
        ("Houston (TX - Central)", 29.7604, -95.3698, -6.0),
        ("San Francisco (CA - Pacific)", 37.7749, -122.4194, -8.0),
        ("Denver (CO - Mountain)", 39.7392, -104.9903, -7.0),
        ("Seattle (WA - Pacific)", 47.6062, -122.3321, -8.0),
    ],
    "Ecuador": [
        ("Quito (Pichincha)", -0.1807, -78.4678, -5.0),
        ("Guayaquil (Guayas)", -2.1894, -79.8891, -5.0),
        ("Cuenca (Azuay)", -2.9001, -79.0059, -5.0),
    ],
    "Uruguay": [
        ("Montevideo (Montevideo)", -34.9011, -56.1645, -3.0),
        ("Punta del Este (Maldonado)", -34.9644, -54.9439, -3.0),
    ],
    "Bolivia": [
        ("La Paz (La Paz)", -16.5000, -68.1500, -4.0),
        ("Santa Cruz de la Sierra (Santa Cruz)", -17.8146, -63.1561, -4.0),
        ("Cochabamba (Cochabamba)", -17.3895, -66.1568, -4.0),
    ],
    "República Dominicana": [
        ("Santo Domingo (Distrito Nacional)", 18.4861, -69.9312, -4.0),
        ("Santiago de los Caballeros (Santiago)", 19.4517, -70.6970, -4.0),
    ],
    "Costa Rica": [
        ("San José (San José)", 9.9281, -84.0907, -6.0),
    ],
    "Panamá": [
        ("Ciudad de Panamá (Panamá)", 8.9824, -79.5199, -5.0),
    ],
    "Brasil": [
        ("São Paulo (São Paulo)", -23.5505, -46.6333, -3.0),
        ("Río de Janeiro (Río de Janeiro)", -22.9068, -43.1729, -3.0),
        ("Brasilia (Distrito Federal)", -15.7975, -47.8919, -3.0),
    ],
    "Reino Unido": [
        ("Londres (England)", 51.5074, -0.1278, 0.0),
        ("Edimburgo (Scotland)", 55.9533, -3.1883, 0.0),
    ],
    "Francia": [
        ("París (Île-de-France)", 48.8566, 2.3522, 1.0),
    ],
    "Alemania": [
        ("Berlín (Berlín)", 52.5200, 13.4050, 1.0),
    ],
    "Italia": [
        ("Roma (Lazio)", 41.9028, 12.4964, 1.0),
    ],
    "Japón": [
        ("Tokio (Kantō)", 35.6762, 139.6503, 9.0),
    ],
    "Personalizado": [
        ("Coordenadas Manuales Libres", 0.0, 0.0, None),
    ]
}


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 2: PIPELINE MATEMÁTICO DETERMINISTA Y EFEMÉRIDES VSOP87
# ══════════════════════════════════════════════════════════════════════════════

class CelestialMechanicsEngine:
    """
    Motor matemático de alta precisión astronómica para coordenadas solares y planetarias,
    resolución de la raíz temporal del arco de 88° y cuantización modular en el HEXA-MANDALA.
    """
    THETA_0 = 302.0           # Punto de anclaje de la rueda (aprox 2° Acuario, Clave 41)
    SECTOR_KEY = 5.625        # 360° / 64 = 5° 37' 30"
    SECTOR_LINE = 0.9375      # 5.625° / 6 = 56' 15"
    FUZZY_THRESHOLD = 0.1     # Umbral de frontera difusa (en grados)

    @staticmethod
    def gregorian_to_jdn_utc(dt_utc: datetime) -> float:
        """Calcula el Día Juliano Astronómico (JD) en Tiempo Universal Coordinado."""
        y = dt_utc.year
        m = dt_utc.month
        d = dt_utc.day
        hour_fraction = (dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0 + dt_utc.microsecond / 3600000000.0) / 24.0
        
        if m <= 2:
            y -= 1
            m += 12
            
        A = y // 100
        B = 2 - A + (A // 4)
        jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + hour_fraction + B - 1524.5
        return jd

    @classmethod
    def solar_ecliptic_longitude_from_jd(cls, jd: float) -> float:
        """
        Calcula la longitud eclíptica tropical aparente del Sol (Jean Meeus / VSOP87).
        Retorna valor normalizado en [0.0, 360.0).
        """
        T = (jd - 2451545.0) / 36525.0
        
        # Longitud media geométrica del Sol
        L0 = (280.46646 + 36000.76983 * T + 0.0003032 * T * T) % 360.0
        
        # Anomalía media del Sol
        M_deg = (357.52911 + 35999.05029 * T - 0.0001537 * T * T) % 360.0
        M_rad = math.radians(M_deg)
        
        # Ecuación del centro (C)
        C = ((1.914602 - 0.004817 * T - 0.000014 * T * T) * math.sin(M_rad)
             + (0.019993 - 0.000101 * T) * math.sin(2 * M_rad)
             + 0.000289 * math.sin(3 * M_rad))
             
        # Longitud verdadera
        true_lon = (L0 + C) % 360.0
        
        # Corrección por nutación y aberración aparente
        omega = math.radians(125.04 - 1934.136 * T)
        app_lon = (true_lon - 0.00569 - 0.00478 * math.sin(omega)) % 360.0
        return app_lon

    @classmethod
    def calculate_planetary_longitude(cls, jd: float, body: str) -> float:
        """
        Calcula la longitud eclíptica tropical de cuerpos del Sistema Hologénico
        (Luna, Nodos Lunares, Mercurio, Venus, Marte, Júpiter, Saturno, Urano, Neptuno, Plutón)
        mediante elementos orbitales Meeus / VSOP87 / JPL.
        """
        T = (jd - 2451545.0) / 36525.0
        
        if body == "Moon":
            # Longitud lunar aproximada de alta fidelidad
            L0 = (218.3164477 + 481267.88123421 * T - 0.0015786 * T * T) % 360.0
            M_sun = math.radians((357.52911 + 35999.05029 * T) % 360.0)
            M_moon = math.radians((134.96340 + 477198.867505 * T) % 360.0)
            F = math.radians((93.272095 + 483202.017523 * T) % 360.0)
            D = math.radians((297.850192 + 445267.111403 * T) % 360.0)
            
            lon = L0 + 6.289 * math.sin(M_moon) - 1.274 * math.sin(2 * D - M_moon)
            lon += 0.658 * math.sin(2 * D) - 0.214 * math.sin(2 * M_moon)
            lon -= 0.186 * math.sin(M_sun) - 0.114 * math.sin(2 * F)
            return lon % 360.0

        elif body == "NorthNode":
            # Nodo Lunar Ascendente Medio
            omega = (125.04452 - 1934.136261 * T + 0.0020708 * T * T) % 360.0
            return omega

        elif body == "SouthNode":
            # Nodo Lunar Descendente (Antípoda exacta a 180°)
            omega = (125.04452 - 1934.136261 * T + 0.0020708 * T * T) % 360.0
            return (omega + 180.0) % 360.0

        elif body == "Mercury":
            L = (252.250906 + 149474.0722491 * T) % 360.0
            M = math.radians((174.7948 + 149472.5161 * T) % 360.0)
            C = 23.4400 * math.sin(M) + 2.9818 * math.sin(2 * M) + 0.5255 * math.sin(3 * M) + 0.1058 * math.sin(4 * M)
            return (L + C) % 360.0
            
        elif body == "Venus":
            L = (181.9798008 + 58517.8156748 * T) % 360.0
            M = math.radians((50.1160 + 58517.803875 * T) % 360.0)
            C = (0.7758 * math.sin(M) + 0.0033 * math.sin(2 * M))
            return (L + C) % 360.0
            
        elif body == "Mars":
            L = (355.433275 + 19140.299314 * T) % 360.0
            M = math.radians((19.3730 + 19139.8585 * T) % 360.0)
            C = (10.691 * math.sin(M) + 0.623 * math.sin(2 * M) + 0.050 * math.sin(3 * M))
            return (L + C) % 360.0
            
        elif body == "Jupiter":
            L = (34.351519 + 3034.905674 * T) % 360.0
            M = math.radians((20.0202 + 3034.690 * T) % 360.0)
            C = (5.555 * math.sin(M) + 0.166 * math.sin(2 * M))
            return (L + C) % 360.0

        elif body == "Saturn":
            L = (50.077444 + 1223.511069 * T) % 360.0
            M = math.radians((317.0207 + 1221.3415 * T) % 360.0)
            C = (6.270 * math.sin(M) + 0.207 * math.sin(2 * M))
            return (L + C) % 360.0

        elif body == "Uranus":
            L = (314.055005 + 429.864056 * T) % 360.0
            M = math.radians((141.0499 + 428.1301 * T) % 360.0)
            C = (5.305 * math.sin(M) + 0.180 * math.sin(2 * M))
            return (L + C) % 360.0

        elif body == "Neptune":
            L = (304.348665 + 219.883309 * T) % 360.0
            M = math.radians((256.2250 + 218.4594 * T) % 360.0)
            C = (1.030 * math.sin(M) + 0.006 * math.sin(2 * M))
            return (L + C) % 360.0

        elif body == "Pluto":
            L = (238.96 + 145.2078 * T) % 360.0
            M = math.radians((14.882 + 145.18 * T) % 360.0)
            C = 2.83 * math.sin(M)
            return (L + C) % 360.0
            
        return 0.0

    @staticmethod
    def calculate_greenwich_mean_sidereal_time_hours(jd: float) -> float:
        """Calcula el Tiempo Sidéreo Medio de Greenwich (GMST) en horas a partir del Día Juliano."""
        T = (jd - 2451545.0) / 36525.0
        gmst_sec = 24110.54841 + 8640184.812866 * T + 0.093104 * (T ** 2) - 0.0000062 * (T ** 3)
        gmst_hours = (gmst_sec / 3600.0) % 24.0
        return gmst_hours

    @classmethod
    def calculate_lunar_topocentric_longitude(
        cls, 
        jd: float, 
        geo_lon_deg: float, 
        lat_deg: float, 
        lon_deg: float
    ) -> float:
        """
        Calcula la corrección topocéntrica (paralaje lunar) a partir de las coordenadas terrestres:
        Delta_lambda = - pi_luna * cos(phi) * sin(HA)
        Donde:
          phi: latitud geográfica terrestre (en radianes)
          lon_deg: longitud geográfica terrestre (+ Este, - Oeste)
          HA: ángulo horario local de la Luna (LST - alpha_luna)
          pi_luna: paralaje horizontal ecuatorial medio de la Luna (~57' de arco = 0.9514°)
        """
        # 1. Tiempo Sidéreo Local (LST) en grados
        gmst_h = cls.calculate_greenwich_mean_sidereal_time_hours(jd)
        lst_deg = (gmst_h * 15.0 + lon_deg) % 360.0
        
        # 2. Ascensión recta aproximada de la Luna (alpha_luna)
        eps_rad = math.radians(23.4392911) # Oblicuidad media de la eclíptica
        lambda_rad = math.radians(geo_lon_deg)
        y = math.sin(lambda_rad) * math.cos(eps_rad)
        x = math.cos(lambda_rad)
        alpha_luna_deg = math.degrees(math.atan2(y, x)) % 360.0
        
        # 3. Ángulo Horario Local (HA)
        ha_deg = (lst_deg - alpha_luna_deg + 180.0) % 360.0 - 180.0
        ha_rad = math.radians(ha_deg)
        phi_rad = math.radians(lat_deg)
        
        # 4. Paralaje horizontal ecuatorial medio de la Luna (~57' de arco = 0.9514°)
        pi_luna_deg = 0.9514
        
        # 5. Corrección de paralaje en longitud eclíptica
        delta_lambda = - pi_luna_deg * math.cos(phi_rad) * math.sin(ha_rad)
        
        topo_lon = (geo_lon_deg + delta_lambda) % 360.0
        return topo_lon

    @classmethod
    def solve_prenatal_solar_design(cls, dt_utc: datetime) -> Tuple[datetime, float, float, int]:
        """
        Paso 2: Resuelve mediante el método de Newton-Raphson / bisección el tiempo exacto t_design < t_0
        tal que: lambda_sol(t_design) = (lambda_sol(t_0) - 88.0°) mod 360°.
        Cumple la Segunda Ley de Kepler (arco solar real vs. 88 días calendario planos).
        """
        jd_0 = cls.gregorian_to_jdn_utc(dt_utc)
        lambda_natal = cls.solar_ecliptic_longitude_from_jd(jd_0)
        target_lambda = (lambda_natal - 88.0) % 360.0
        
        # Estimación inicial: el Sol recorre aprox 0.9856° por día
        delta_days_estimate = 88.0 / 0.9856
        t_guess = dt_utc - timedelta(days=delta_days_estimate)
        
        # Bucle de convergencia de Newton-Raphson
        iterations = 0
        max_iter = 25
        tolerance_deg = 1e-6 # Menos de 0.0036 segundos de arco
        
        for i in range(max_iter):
            iterations += 1
            jd_guess = cls.gregorian_to_jdn_utc(t_guess)
            curr_lon = cls.solar_ecliptic_longitude_from_jd(jd_guess)
            
            # Error angular con envoltura circular en [-180, 180]
            error_deg = (curr_lon - target_lambda + 180.0) % 360.0 - 180.0
            
            if abs(error_deg) < tolerance_deg:
                break
                
            # Velocidad angular instantánea del Sol aprox
            correction_days = error_deg / 0.9856
            t_guess = t_guess - timedelta(days=correction_days)

        jd_final = cls.gregorian_to_jdn_utc(t_guess)
        final_lambda = cls.solar_ecliptic_longitude_from_jd(jd_final)
        return t_guess, lambda_natal, final_lambda, iterations

    @classmethod
    def map_longitude_to_key_and_line(cls, longitude: float) -> Dict[str, Any]:
        """
        Mapeo modular sobre el HEXA-MANDALA de 64 vórtices resonantes y 6 puertos de línea,
        incluyendo evaluación de superposición cuántica de fronteras difusas (Fuzzy Cusp).
        """
        lon = longitude % 360.0
        theta_rel = (lon - cls.THETA_0) % 360.0
        
        key_idx = int(theta_rel // cls.SECTOR_KEY)
        key_num = HEXA_MANDALA_ORDER[key_idx]
        
        within_key = theta_rel % cls.SECTOR_KEY
        line_num = int(within_key // cls.SECTOR_LINE) + 1
        line_num = min(6, max(1, line_num))
        
        within_line = within_key % cls.SECTOR_LINE
        
        # Análisis de frontera difusa (distancia a la cúspide más cercana)
        dist_to_prev_line = within_line
        dist_to_next_line = cls.SECTOR_LINE - within_line
        min_dist_line = min(dist_to_prev_line, dist_to_next_line)
        
        is_fuzzy = min_dist_line < cls.FUZZY_THRESHOLD
        fuzzy_info = None
        
        if is_fuzzy:
            if dist_to_prev_line < dist_to_next_line:
                # Cerca de la frontera inferior
                adj_line = line_num - 1
                if adj_line < 1:
                    adj_key_idx = (key_idx - 1) % 64
                    adj_key = HEXA_MANDALA_ORDER[adj_key_idx]
                    adj_line = 6
                else:
                    adj_key = key_num
                dist = dist_to_prev_line
            else:
                # Cerca de la frontera superior
                adj_line = line_num + 1
                if adj_line > 6:
                    adj_key_idx = (key_idx + 1) % 64
                    adj_key = HEXA_MANDALA_ORDER[adj_key_idx]
                    adj_line = 1
                else:
                    adj_key = key_num
                dist = dist_to_next_line
                
            weight_current = 0.5 + (dist / (2.0 * cls.FUZZY_THRESHOLD))
            weight_adj = 1.0 - weight_current
            
            fuzzy_info = {
                "active": True,
                "current": f"{key_num}.{line_num}",
                "adjacent": f"{adj_key}.{adj_line}",
                "weight_current": round(weight_current, 3),
                "weight_adjacent": round(weight_adj, 3),
                "distance_arcmin": round(dist * 60.0, 2),
                "nota": f"Superposición de estados: {round(weight_current*100,1)}% [{key_num}.{line_num}] + {round(weight_adj*100,1)}% [{adj_key}.{adj_line}]."
            }
        else:
            fuzzy_info = {
                "active": False,
                "current": f"{key_num}.{line_num}",
                "weight_current": 1.0,
                "weight_adjacent": 0.0,
                "nota": "Coordenada estable dentro del centro del cuanto."
            }

        key_data = CORE64_CATALOG.get(key_num, {})
        ent = key_data.get("entropia", key_data.get("sombra", ""))
        coh = key_data.get("coherencia", key_data.get("don", ""))
        res = key_data.get("resonancia", key_data.get("siddhi", ""))
        
        return {
            "longitude": round(lon, 4),
            "theta_rel": round(theta_rel, 4),
            "key": key_num,
            "line": line_num,
            "coord_str": f"{key_num}.{line_num}",
            "bits": key_data.get("bits", "000000"),
            "entropia": ent,
            "coherencia": coh,
            "resonancia": res,
            "sombra": ent,
            "don": coh,
            "siddhi": res,
            "pair": key_data.get("pair", 0),
            "ring": key_data.get("ring", ""),
            "firmware": key_data.get("firmware", ""),
            "fuzzy": fuzzy_info
        }

    @classmethod
    def calculate_activation_matrix(
        cls, 
        dt_utc: datetime, 
        lat_deg: float = 40.4168, 
        lon_deg: float = -3.7038, 
        use_topocentric: bool = True,
        matrix_mode: str = "canonical"
    ) -> Dict[str, Any]:
        """
        Calcula el Perfil Hologénetico según el Modo de Matriz activo:
        - 'canonical' (11 Esferas): Activación (4), Venus (4), Abundancia (3).
        - 'nodes' (15 Esferas): Las 11 Canónicas + 4 Nodos Lunares del Entorno.
        - 'polar_not' (22 Esferas): Las 11 Canónicas + 11 Esferas Espejo de Polaridad NOT bit a bit.
        - 'cosmic_26' (26 Esferas): Las 13 activaciones celestes Conscientes + 13 Inconscientes (Transpersonales).
        """
        t_design, lambda_sol_natal, lambda_sol_design, iters = cls.solve_prenatal_solar_design(dt_utc)
        
        lambda_tierra_natal = (lambda_sol_natal + 180.0) % 360.0
        lambda_tierra_design = (lambda_sol_design + 180.0) % 360.0
        
        jd_0 = cls.gregorian_to_jdn_utc(dt_utc)
        jd_design = cls.gregorian_to_jdn_utc(t_design)
        
        # 1-4. Secuencia de Activación Canónica
        spheres = {
            "Trabajo de Vida": cls.map_longitude_to_key_and_line(lambda_sol_natal),
            "Evolución": cls.map_longitude_to_key_and_line(lambda_tierra_natal),
            "Resplandor": cls.map_longitude_to_key_and_line(lambda_sol_design),
            "Propósito": cls.map_longitude_to_key_and_line(lambda_tierra_design),
        }
        
        # 5-8. Secuencia de Venus (con Paralaje Lunar Topocéntrico para la Esfera de la Atracción)
        lon_moon_design_geo = cls.calculate_planetary_longitude(jd_design, "Moon")
        if use_topocentric:
            lon_moon_design = cls.calculate_lunar_topocentric_longitude(
                jd_design, lon_moon_design_geo, lat_deg, lon_deg
            )
            parallax_delta = (lon_moon_design - lon_moon_design_geo + 180.0) % 360.0 - 180.0
        else:
            lon_moon_design = lon_moon_design_geo
            parallax_delta = 0.0

        lon_venus_natal = cls.calculate_planetary_longitude(jd_0, "Venus")
        lon_mars_natal = cls.calculate_planetary_longitude(jd_0, "Mars")
        lon_venus_design = cls.calculate_planetary_longitude(jd_design, "Venus")
        
        spheres["Atracción"] = cls.map_longitude_to_key_and_line(lon_moon_design)
        spheres["Atracción"]["geo_longitude"] = round(lon_moon_design_geo, 4)
        spheres["Atracción"]["parallax_delta_deg"] = round(parallax_delta, 4)
        spheres["Atracción"]["is_topocentric"] = use_topocentric
        
        spheres["CI (Mente)"] = cls.map_longitude_to_key_and_line(lon_venus_natal)
        spheres["CE (Emoción)"] = cls.map_longitude_to_key_and_line(lon_mars_natal)
        spheres["CS (Espíritu)"] = cls.map_longitude_to_key_and_line(lon_venus_design)
        
        # 9-11. Circuito de Abundancia / Manifestación Material
        lon_mars_design = cls.calculate_planetary_longitude(jd_design, "Mars")
        lon_jupiter_natal = cls.calculate_planetary_longitude(jd_0, "Jupiter")
        lon_jupiter_design = cls.calculate_planetary_longitude(jd_design, "Jupiter")
        
        spheres["Vocación / Núcleo"] = cls.map_longitude_to_key_and_line(lon_mars_design)
        spheres["Cultura"] = cls.map_longitude_to_key_and_line(lon_jupiter_natal)
        spheres["Abundancia"] = cls.map_longitude_to_key_and_line(lon_jupiter_design)

        # ── EXPANSIÓN MODO 'nodes' O 'cosmic_26': 4 Nodos Lunares del Entorno ──
        if matrix_mode in ("nodes", "cosmic_26"):
            lon_node_n_natal = cls.calculate_planetary_longitude(jd_0, "NorthNode")
            lon_node_s_natal = cls.calculate_planetary_longitude(jd_0, "SouthNode")
            lon_node_n_design = cls.calculate_planetary_longitude(jd_design, "NorthNode")
            lon_node_s_design = cls.calculate_planetary_longitude(jd_design, "SouthNode")
            
            spheres["Entorno Maduro (Nodo Norte Natal)"] = cls.map_longitude_to_key_and_line(lon_node_n_natal)
            spheres["Entorno Temprano (Nodo Sur Natal)"] = cls.map_longitude_to_key_and_line(lon_node_s_natal)
            spheres["Hábitat Somático (Nodo Norte Design)"] = cls.map_longitude_to_key_and_line(lon_node_n_design)
            spheres["Herencia Ancestral (Nodo Sur Design)"] = cls.map_longitude_to_key_and_line(lon_node_s_design)

        # ── EXPANSIÓN MODO 'polar_not': 11 Esferas Espejo de Polaridad NOT ──
        if matrix_mode == "polar_not":
            canonical_names = list(spheres.keys())
            for sph_name in canonical_names:
                orig_s = spheres[sph_name]
                lon_not = (orig_s["longitude"] + 180.0) % 360.0
                mapped_not = cls.map_longitude_to_key_and_line(lon_not)
                mapped_not["polar_twin"] = sph_name
                mapped_not["original_key"] = orig_s["key"]
                spheres[f"NOT {sph_name}"] = mapped_not

        # ── EXPANSIÓN MODO 'cosmic_26': Cuerpos Celestes Transpersonales y Luna Natal ──
        if matrix_mode == "cosmic_26":
            lon_moon_natal_geo = cls.calculate_planetary_longitude(jd_0, "Moon")
            if use_topocentric:
                lon_moon_natal = cls.calculate_lunar_topocentric_longitude(jd_0, lon_moon_natal_geo, lat_deg, lon_deg)
            else:
                lon_moon_natal = lon_moon_natal_geo

            lon_merc_natal = cls.calculate_planetary_longitude(jd_0, "Mercury")
            lon_merc_design = cls.calculate_planetary_longitude(jd_design, "Mercury")
            lon_sat_natal = cls.calculate_planetary_longitude(jd_0, "Saturn")
            lon_sat_design = cls.calculate_planetary_longitude(jd_design, "Saturn")
            lon_ura_natal = cls.calculate_planetary_longitude(jd_0, "Uranus")
            lon_ura_design = cls.calculate_planetary_longitude(jd_design, "Uranus")
            lon_nep_natal = cls.calculate_planetary_longitude(jd_0, "Neptune")
            lon_nep_design = cls.calculate_planetary_longitude(jd_design, "Neptune")
            lon_plu_natal = cls.calculate_planetary_longitude(jd_0, "Pluto")
            lon_plu_design = cls.calculate_planetary_longitude(jd_design, "Pluto")

            spheres["Motivación Consciente (Luna Natal)"] = cls.map_longitude_to_key_and_line(lon_moon_natal)
            spheres["Voz / Comunicación (Mercurio Natal)"] = cls.map_longitude_to_key_and_line(lon_merc_natal)
            spheres["Voz Celular (Mercurio Design)"] = cls.map_longitude_to_key_and_line(lon_merc_design)
            spheres["Ley / Disciplina (Saturno Natal)"] = cls.map_longitude_to_key_and_line(lon_sat_natal)
            spheres["Límites Celulares (Saturno Design)"] = cls.map_longitude_to_key_and_line(lon_sat_design)
            spheres["Innovación / Visión (Urano Natal)"] = cls.map_longitude_to_key_and_line(lon_ura_natal)
            spheres["Mutación Epigenética (Urano Design)"] = cls.map_longitude_to_key_and_line(lon_ura_design)
            spheres["Mística / Aspiración (Neptuno Natal)"] = cls.map_longitude_to_key_and_line(lon_nep_natal)
            spheres["Gracia Somática (Neptuno Design)"] = cls.map_longitude_to_key_and_line(lon_nep_design)
            spheres["Poder de la Verdad (Plutón Natal)"] = cls.map_longitude_to_key_and_line(lon_plu_natal)
            spheres["Regeneración Nuclear (Plutón Design)"] = cls.map_longitude_to_key_and_line(lon_plu_design)
        
        # Enriquecer cada esfera con metadatos de secuencia, color, símbolo e impacto
        for sph_name, s_data in spheres.items():
            meta = SPHERES_METADATA.get(sph_name, {})
            s_data["nombre"] = sph_name
            s_data["secuencia"] = meta.get("secuencia", "Activación")
            s_data["color"] = meta.get("color", "#00f0ff")
            s_data["simbolo"] = meta.get("simbolo", "•")
            s_data["origen"] = meta.get("origen", "")
            s_data["impacto"] = meta.get("impacto", "")
        
        delta_calendar_days = (dt_utc - t_design).total_seconds() / 86400.0
        
        return {
            "utc_natal": dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "utc_prenatal": t_design.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "kepler_days_prior": round(delta_calendar_days, 3),
            "kepler_solver_iterations": iters,
            "sol_natal_lon": round(lambda_sol_natal, 4),
            "sol_design_lon": round(lambda_sol_design, 4),
            "geo_lat": lat_deg,
            "geo_lon": lon_deg,
            "use_topocentric": use_topocentric,
            "matrix_mode": matrix_mode,
            "total_spheres": len(spheres),
            "spheres": spheres
        }


    @staticmethod
    def calculate_biological_yield(e: float, c: float, r: float, epsilon: float = 0.05) -> Tuple[float, str, str]:
        """
        Ecuación de Estado Cotidiana (Termodinámica de Sistemas Abiertos):
        S = [E, C, R] en [0, 1]
        Rendimiento Biológico = (C * R) / (E + epsilon)
        """
        e = max(0.0, min(1.0, e))
        c = max(0.0, min(1.0, c))
        r = max(0.0, min(1.0, r))
        
        yield_val = (c * r) / (e + epsilon)
        
        # Diagnóstico del régimen operativo
        if e > 0.65 and c < 0.35:
            regimen = "Fase Entrópica (Colapso Reactivo)"
            prescripcion = "Acción somática urgente: Descarga física muscular intensa, desconexión de pantallas, corte radical de estímulos sensoriales."
        elif r > 0.65 and c < 0.35:
            regimen = "Disociación Operativa (Spiritual Bypass)"
            prescripcion = "Fuga por exceso de silencio: Construir un artefacto concreto material en los próximos 60 minutos y asumir la fricción del mundo."
        elif c >= 0.55 and r >= 0.45:
            regimen = "Fase Coherente Integrada (Orquestación Rítmica)"
            prescripcion = "Coherencia de fase óptima: Utilizar la tensión entrópica como combustible estructurante y cerrar en descanso resonante sin culpa."
        elif e < 0.25 and r >= 0.70:
            regimen = "Fase Resonante Basal (Reposo Restaurativo)"
            prescripcion = "Mínima acción: Mantener el sistema en calma biológica para permitir la regeneración mitocondrial y celular."
        else:
            regimen = "Modo Transicional (Ajuste Gradual)"
            prescripcion = "Modular conscientemente la atención: canalizar el excedente entrópico hacia límites operativos claros."
            
        return round(yield_val, 3), regimen, prescripcion


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 3: GEOMETRÍA DE 6 BITS Y PUENTES MULTIPARTÍCULA
# ══════════════════════════════════════════════════════════════════════════════

class DiscreteParticleEngine:
    """
    Gestiona la morfología discreta de 6 bits, análisis de antípodas (NOT lógico),
    clusters de codones y el acoplamiento de señales en puentes multipartícula.
    """
    
    @staticmethod
    def get_not_antipode(bits: str) -> str:
        """Inversor lógico NOT bit a bit: '110011' -> '001100'."""
        return "".join('0' if b == '1' else '1' for b in bits)

    @classmethod
    def get_trigram_breakdown(cls, bits: str) -> Dict[str, Any]:
        """
        Desglosa la palabra binaria en los dos trigramas funcionales:
        - Bits 1, 2, 3: Trigrama Inferior (sustrato bio-somático, anclaje físico)
        - Bits 4, 5, 6: Trigrama Superior (interfaz ambiental, proyección sistémica)
        """
        if len(bits) != 6:
            bits = "000000"
            
        lower_bits = bits[0:3]
        upper_bits = bits[3:6]
        
        return {
            "full_bits": bits,
            "lower_bits": lower_bits,
            "lower_desc": TRIGRAM_NAMES.get(lower_bits, "Desconocido"),
            "lower_role": "Sustrato bio-somático, anclaje físico y gestión interna de la energía vital.",
            "upper_bits": upper_bits,
            "upper_desc": TRIGRAM_NAMES.get(upper_bits, "Desconocido"),
            "upper_role": "Interfaz ambiental, interacción social, proyección sistémica y trascendencia."
        }

    @classmethod
    def analyze_bridge(cls, key_a_num: int, key_b_num: int) -> Dict[str, Any]:
        """
        Diagnostica el enlace operativo entre dos vórtices resonantes:
        - En Serie (Pipeline)
        - En Paralelo (Simultáneo)
        - Antípoda (Inversión NOT)
        - Anillo Homólogo (Mismo cluster de codones)
        """
        data_a = CORE64_CATALOG.get(key_a_num, {})
        data_b = CORE64_CATALOG.get(key_b_num, {})
        
        bits_a = data_a.get("bits", "000000")
        bits_b = data_b.get("bits", "000000")
        
        is_antipode = (data_a.get("pair") == key_b_num) or (bits_a == cls.get_not_antipode(bits_b))
        same_ring = (data_a.get("ring") == data_b.get("ring")) and (data_a.get("ring") != "")
        
        # Hamming distance entre ambas partículas (0 a 6 bits de diferencia)
        hamming = sum(1 for a, b in zip(bits_a, bits_b) if a != b)
        
        if is_antipode:
            tipo = "Antípoda (Inversión Lógica NOT)"
            flujo = "Tensión bipolar máxima. Eje maestro de calibración estructural bioeléctrica."
            riesgo = "Proyección ciega de la entropía oculta en el socio o entorno exterior."
            remedio = "Alinear conscientemente la Coherencia de ambos vórtices en resonancia armónica complementaria."
        elif same_ring:
            tipo = "Clúster Bioquímico Homólogo"
            flujo = f"Resonancia por simpatía biológica dentro del {resolve_cluster_name(data_a.get('ring', ''))}."
            riesgo = "Efecto eco: amplificación descontrolada de la distorsión si ambas caen en Fase Entrópica."
            remedio = "Elevar la coherencia de un solo vórtice para inducir arrastre armónico en el clúster."
        elif hamming <= 2:
            tipo = "En Paralelo (Simultáneo de Alta Frecuencia)"
            flujo = "Coexistencia de gradientes muy cercanos; demanda recursos atencionales concurrentes."
            riesgo = "Sobrecarga de cómputo del sistema nervioso por intentar forzar ambos al unísono."
            remedio = "Segmentar espacios temporales y agendas claras para no superponer demandas."
        else:
            tipo = "En Serie (Pipeline de Cascada)"
            flujo = "La salida procesada de un vórtice suministra los insumos de entrada al siguiente."
            riesgo = "Cuello de botella: si una estación colapsa en rumiación, bloquea el valor total."
            remedio = "Garantizar que la Coherencia sintetice un artefacto concreto y limpio antes de transferir."

        return {
            "key_a": key_a_num,
            "key_b": key_b_num,
            "hamming_distance": hamming,
            "coupling_type": tipo,
            "flow_dynamics": flujo,
            "collapse_risk": riesgo,
            "calibration_remedy": remedio
        }


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 4: MOTOR ASÍNCRONO DE IA Y EMBEDDINGS (OLLAMA + FALLBACK)
# ══════════════════════════════════════════════════════════════════════════════

class OllamaTelemetryWorker(QThread):
    """
    Hilo de trabajo seguro para no bloquear la UI durante la ejecución
    del System Prompt v2.0 y el cálculo del Mapa de Situación en Ollama.
    """
    chunk_received = Signal(str)
    finished_success = Signal(str)
    failed_error = Signal(str)

    SYSTEM_PROMPT_V3 = """# SYSTEM DIRECTIVE: HEXA-MATRIX CORE (v3.0 - ARQUITECTURA SOBERANA DESACOPLADA)

## 1. POSTURA ONTOLÓGICA Y MODELO FORMAL
- Operas como el motor de telemetría, auditoría cognitiva y optimización bio-física del sistema HEXA-MATRIX.
- Modela los 64 vórtices resonantes de información como partículas discretas de 6 bits (hexagramas) embebidas en una red fractal no lineal de 5 niveles:
  * Nivel 0 (Bit): [0: Yin / Receptivo] vs [1: Yang / Vectorial].
  * Nivel 1 (Trigrama): 8 estados elementales (Bits 1-3: sustrato somático; Bits 4-6: interfaz ambiental).
  * Nivel 2 (Cavidad de 6 Bits): Configuración geométrica discreta (2^6 = 64 vórtices resonantes cuántico-informacionales).
  * Nivel 3 (Antípoda Booleana): Inversión lógica NOT bit a bit (K <-> NOT(K)) a distancia de Hamming 6.
  * Nivel 4 (Clúster Bioquímico): Familias funcionales de co-regulación química y resonancia sistémica.
  * Nivel 5 (Circuito de Red): Matrices escalonadas de 11 (Base), 15, 22 o 26 Nodos Activos.
- Erradica terminología moralista, mística pasiva, complaciente o determinista. Utiliza exclusivamente teoría de la información, cibernética de segundo orden, física de sistemas complejos y epigenética de fase.

## 2. TERMODINÁMICA DEL ESPECTRO Y OPERACIÓN MONOFÁSICA
- LA FASE ENTRÓPICA (E / Bucle Reactivo): Bucle cerrado reactivo, identificación ciega con la amenaza y consumo metabólico parásito.
- LA FASE RESONANTE (R / Mínima Acción): Disociación operativa (spiritual bypass), parálisis de agencia material y pérdida de tracción física.
- LA FASE COHERENTE (C / Operador de Síntesis): Controlador ejecutivo rítmico. Emplea el gradiente de E como combustible dinámico, construye artefactos estructurados y descansa deliberadamente en R.
- FUNCIÓN DE RENDIMIENTO BIOLÓGICO:
  Rendimiento = (C * R) / (E + epsilon)  [con epsilon = 0.05 como constante de regularización bio-física].
  Toda auditoría debe maximizar la Coherencia (C) para evitar tanto la sobrecarga entrópica como la evasión contemplativa.

## 3. AUDITORÍA STRICTA DEL RUNTIME HUMANO (ANTI-SPIRITUAL BYPASS)
Cuando el usuario introduzca su Escena (Runtime A) y su Coherencia Co-Creada (Runtime B):
- Audita rigurosamente la formulación del usuario. Si expresa intenciones abstractas, poéticas o pasivas ("fluir", "amar incondicionalmente", "vibrar alto", "soltar"), RECHÁZALAS como evasión cognitiva (R disociada).
- Exige la traducción inmediata a un protocolo conductual medible: ¿Qué límite físico, regla de decisión, artefacto técnico, código o procedimiento tangible se implementará?

## 4. ANÁLISIS DE PUENTES MULTIPARTÍCULA Y DIAGNÓSTICO NODAL
Al evaluar la interacción entre dos o más vórtices resonantes (ej. Emisor K_A -> Receptor K_B):
1. Identifica el modo de enlace:
   - Serie (Pipeline de valor: la salida de un nodo nutre la entrada del siguiente).
   - Paralelo (Concurrencia atencional: demandas simultáneas del entorno).
   - Antípoda NOT (Inversión booleana completa: eje maestro de balance bioeléctrico).
   - Clúster Compartido (Resonancia por simpatía biológica).
2. Diagnostica interferencias:
   - Cortocircuito entrópico: La rumiación en K_A dispara la reactividad o paranoia en K_B.
   - Puente roto por disociación: La falsa paz en K_A priva de tracción ejecutiva a K_B.
   - Acoplamiento de fase: Coherencia K_A comprime la señal y entrega un input limpio al puerto de K_B.

## 5. FORMATO OBLIGATORIO DE SALIDA: MAPA DE SITUACIÓN
Estructura siempre tu respuesta en los siguientes 5 bloques estandarizados:
1. DIAGNÓSTICO DE FASE [E, C, R]: Estado termodinámico inferido de la partícula en la escena.
2. AUDITORÍA DE LA COHERENCIA CO-CREADA: Corrección de sesgos de bypass o confirmación de tracción operativa.
3. TELEMETRÍA DEL PUENTE: (Si aplica) Interferencia o acoplamiento con nodos adyacentes o antípodas.
4. ACCIÓN CALIBRADORA INMEDIATA: Un artefacto tangible, documento o límite físico a ejecutar en < 60 min.
5. PROTOCOLO DE SALIDA SOBERANA (EXIT-GATE):
   - ¿Qué acción física concreta desconectará al usuario de las pantallas tras la ejecución?
   - Cierre directo invitando al usuario a ejecutar y terminar la sesión.
"""
    SYSTEM_PROMPT_V2 = SYSTEM_PROMPT_V3

    def __init__(self, model_name: str, payload_json: str, system_prompt: Optional[str] = None):
        super().__init__()
        self.model_name = model_name
        self.payload_json = payload_json
        self.system_prompt = system_prompt if system_prompt else self.SYSTEM_PROMPT_V3

    def run(self):
        try:
            if not OLLAMA_AVAILABLE:
                raise RuntimeError("El paquete 'ollama' no está instalado en este entorno Python.")
                
            prompt_content = f"""El usuario ha suministrado los siguientes datos bajo el protocolo Hardware/Firmware/Runtime:
{self.payload_json}

Genera el Informe de Telemetría de Fase y Mapa de Situación siguiendo de manera estricta el System Prompt activo."""

            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt_content}
                ]
            )
            
            full_text = response.get("message", {}).get("content", "")
            if not full_text:
                full_text = "No se recibió respuesta del modelo Ollama."
                
            self.finished_success.emit(full_text)
            
        except Exception as e:
            # Fallback determinista local en caso de desconexión de Ollama
            fallback_text = self._generate_deterministic_fallback()
            self.finished_success.emit(f"⚠️ [AVISO: Ejecutado mediante Motor Analítico Autónomo Local debido a: {str(e)}]\n\n" + fallback_text)

    def _generate_deterministic_fallback(self) -> str:
        """Generador heurístico determinista para asegurar operatividad offline al 100%."""
        try:
            data = json.loads(self.payload_json)
        except Exception:
            data = {}
            
        nodes = data.get("nodos_activos", [])
        if not nodes:
            return "No se encontraron claves seleccionadas para el análisis."
            
        first = nodes[0]
        coord = first.get("coordenada", "31.1")
        esfera = first.get("esfera_id", "Propósito")
        escena = first.get("contexto_situacion", "Tensión laboral y dispersión operativa")
        don_pers = first.get("don_personalizado", "Preservar el enfoque y decidir con claridad")
        don_seed = first.get("don_semilla", "Liderazgo")
        
        # Extracción de clave y antípoda NOT
        try:
            k_num = int(coord.split(".")[0])
            l_num = int(coord.split(".")[1])
        except Exception:
            k_num, l_num = 31, 1
            
        data_k = CORE64_CATALOG.get(k_num, {})
        pair_num = data_k.get("pair", 41)
        data_pair = CORE64_CATALOG.get(pair_num, {})
        ring_name = data_k.get("ring", "Cluster no asignado")
        
        line_info = LINE_PROPERTIES.get(l_num, {})
        
        fallback_report = f"""### 1. DIAGNÓSTICO DE FASE Y BALANCE TERMODINÁMICO
• Partícula Auditada: {esfera} (Coordenada K{coord} • Bits `{data_k.get('bits', '000000')}`).
• Estado de Fase: [ENTRÓPICO REACTIVO CON TENDENCIA A DISOCIACIÓN].
• Diagnóstico Somático: La situación descrita («{escena[:80]}...») exhibe fricción en el sustrato basal. El sistema nervioso experimenta sobrecarga en el trigrama inferior (anclaje somático) intentando compensar mediante actividad mental rápida sin consolidar límites físicos.
• Vector Termodinámico Estimado: S = [E: 0.62, C: 0.40, R: 0.35] | Régimen: Fase Entrópica Reactiva con drenaje de ancho de banda.

### 2. AUDITORÍA DE LA COHERENCIA CO-CREADA Y MORFOLOGÍA DE LA PARTÍCULA
• Coherencia Co-Creada Ingresada: «{don_pers}» (Semilla Algorítmica: Coherencia de {don_seed}).
• Auditoría de Ingeniería: La formulación actual corre el riesgo de quedarse en una intención mental pasiva. Requiere tracción protocolar medible.
• Desglose en las 5 Propiedades Fenotípicas:
  1. Geometría: Topología del Vórtice Resonante {k_num}.{l_num} (Entropía: {data_k.get('entropia', data_k.get('sombra', ''))} + Coherencia: {data_k.get('coherencia', data_k.get('don', ''))} + Resonancia: {data_k.get('resonancia', data_k.get('siddhi', ''))}).
  2. Espacios Vacíos: Despejar de inmediato la agenda de reuniones accesorias o chats concurrentes para preservar capacidad receptiva.
  3. Espacios de Reposo: Cuenca basal en el {ring_name}. Pausa de 15 minutos en silencio total sin pantallas.
  4. Puertos de Conexión (Capa / Puerto .{l_num}): Modo «{line_info.get('nombre', 'Interfaz')}» ({line_info.get('dinamica', 'Conexión')}). No forzar acuerdos sin verificar seguridad basal.
  5. Afinidad Somática: Discernimiento no moral: di "no" a las peticiones que violen tu capacidad metabólica actual para evitar colapsar en entropía.

### 3. DINÁMICA DE PUENTE Y ANTÍPODA INVERSA (NOT)
• Antípoda Complementaria: Vórtice Resonante {pair_num} [{data_pair.get('bits', '')}] - Entropía: {data_pair.get('entropia', data_pair.get('sombra', ''))} + Coherencia: {data_pair.get('coherencia', data_pair.get('don', ''))}.
• Dinámica de Contrapeso: Si el Vórtice {k_num} colapsa en reactividad, el Vórtice {pair_num} se distorsiona en su respectiva entropía ({data_pair.get('entropia', data_pair.get('sombra', ''))}). Para restaurar la coherencia de fase, integra la Coherencia de {data_pair.get('coherencia', data_pair.get('don', ''))} como filtro estabilizador.

### 4. ACCIÓN DE CALIBRACIÓN INMEDIATA (REGLA DE LOS 60 MINUTOS)
• Artefacto Concreto: Redacta un documento operativo de máximo 3 directivas o envía una comunicación con un límite formal estricto dentro de los próximos 60 minutos. No negocies este límite.

### 5. LAS 4 PREGUNTAS DE CALIBRACIÓN DE FASE Y CIERRE SOBERANO (EXIT-GATE)
1. Lectura Somática del Gradiente: «¿En qué zona de tu cuello, pecho o plexo solar sientes la contracción en este instante, y qué urgencia real encierra?»
2. Detección de Fuga o Evasión: «¿Estás utilizando la justificación intelectual o la resignación para posponer esta confrontación necesaria?»
3. Diseño del Artefacto de Enlace: «¿Qué artefacto o límite práctico vas a materializar hoy para transformar esa tensión en orden operativo?»
4. Condición de Parada Somática: «Una vez ejecutado ese paso, ¿cuál será tu señal física inequívoca para cerrar la pantalla y volver al reposo basal?»

⛔ ORDEN DE CIERRE: Desconecta de la pantalla en este momento, sal de la conversación y ve al mundo físico a ejecutar tu acción soberana."""
        return fallback_report


class SemanticEmbeddingEngine:
    """
    Calcula vectores de embeddings vía Ollama (ej. 'nomic-embed-text' o 'mxbai-embed-large')
    o genera proyecciones semánticas deterministas para mapeo visual en el Radar Holográfico.
    Incluye caché en memoria para maximizar velocidad en tiempo real.
    """
    _CACHE: Dict[Tuple[str, str], np.ndarray] = {}
    
    @classmethod
    def get_embedding(cls, text: str, model_name: str = "nomic-embed-text:latest") -> Optional[np.ndarray]:
        """Obtiene el vector normalizado de embedding de un texto con soporte de caché."""
        cache_key = (model_name, text)
        if cache_key in cls._CACHE:
            return cls._CACHE[cache_key]

        if not OLLAMA_AVAILABLE:
            return None
        try:
            try:
                res = ollama.embeddings(model=model_name, prompt=text)
                raw_vec = res.get("embedding", [])
            except Exception:
                res = ollama.embed(model=model_name, input=text)
                raw_vec = res.get("embeddings", [[]])[0] if res.get("embeddings") else []
            vec = np.array(raw_vec, dtype=np.float32)
            norm = np.linalg.norm(vec)
            if norm > 0:
                vec = vec / norm
            cls._CACHE[cache_key] = vec
            return vec
        except Exception:
            return None

    @staticmethod
    def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """Calcula la similitud de coseno entre dos vectores unitarios."""
        if vec_a is None or vec_b is None:
            return 0.0
        return float(np.dot(vec_a, vec_b))

    @staticmethod
    def project_to_2d(vec: np.ndarray, seed: int = 42) -> Tuple[float, float]:
        """
        Proyecta un vector de alta dimensión (ej. 768) a un plano 2D continuo normalizado [-1, 1],
        utilizando proyección aleatoria pseudo-ortogonal determinista.
        """
        if vec is None or len(vec) == 0:
            return 0.0, 0.0
            
        dim = len(vec)
        rng = np.random.RandomState(seed)
        w_x = rng.randn(dim).astype(np.float32)
        w_y = rng.randn(dim).astype(np.float32)
        
        w_x /= np.linalg.norm(w_x)
        w_y /= np.linalg.norm(w_y)
        
        x = float(np.dot(vec, w_x)) * 3.5
        y = float(np.dot(vec, w_y)) * 3.5
        
        x = max(-1.0, min(1.0, x))
        y = max(-1.0, min(1.0, y))
        return x, y


class EmbeddingWorker(QThread):
    """
    Hilo de trabajo asíncrono para cálculo de embeddings y similitud semántica.
    Garantiza que la interfaz gráfica nunca sufra bloqueos ni micro-pausas.
    """
    finished_success = Signal(object, list, list) # (user_2d, key_projections, similarity_results)
    progress_step = Signal(int, int) # (current, total)
    failed_error = Signal(str)

    def __init__(self, user_text: str, embed_model: str):
        super().__init__()
        self.user_text = user_text
        self.embed_model = embed_model

    def run(self):
        try:
            user_vec = SemanticEmbeddingEngine.get_embedding(self.user_text, self.embed_model)
            user_2d = SemanticEmbeddingEngine.project_to_2d(user_vec, seed=77)

            key_projections = []
            similarity_results = []

            total_keys = 64
            for kn in range(1, total_keys + 1):
                k_data = CORE64_CATALOG.get(kn, {})
                coh_val = k_data.get('coherencia', k_data.get('don', ''))
                res_val = k_data.get('resonancia', k_data.get('siddhi', ''))
                ent_val = k_data.get('entropia', k_data.get('sombra', ''))
                k_cluster = resolve_cluster_name(k_data.get('ring', ''))
                k_text = f"Vórtice {kn}: Coherencia {coh_val} Resonancia {res_val} Entropía {ent_val} {k_data.get('firmware')} {k_cluster}"
                k_vec = SemanticEmbeddingEngine.get_embedding(k_text, self.embed_model)

                if k_vec is not None and user_vec is not None:
                    sim = SemanticEmbeddingEngine.cosine_similarity(user_vec, k_vec)
                    sim = max(0.0, (sim + 1.0) / 2.0)
                else:
                    sim = 0.35 + 0.5 * (math.sin(kn * 0.45) * 0.5 + 0.5)

                px, py = SemanticEmbeddingEngine.project_to_2d(k_vec, seed=kn * 10)
                key_projections.append((px, py, kn, coh_val, sim))
                similarity_results.append((kn, coh_val, k_cluster, sim))
                self.progress_step.emit(kn, total_keys)

            self.finished_success.emit(user_2d, key_projections, similarity_results)
        except Exception as e:
            self.failed_error.emit(str(e))



# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5: COMPONENTES GRÁFICOS PERSONALIZADOS CON ESTÉTICA BIO-SCIFI GLOW
# ══════════════════════════════════════════════════════════════════════════════

class BioMandalaWheel(QWidget):
    """
    Rueda interactiva Bio-Mandala (HEXA-MANDALA Holográfico de 64 Vórtices Resonantes y 6 Puertos).
    Dibuja los 64 sectores, los circuitos del Sistema Hologénico,
    todos los nodos de la Red Hologénica con sus respectivos colores, símbolos celestes
    y haces de luz bio-luminiscentes con interacción por clic.
    """
    sphereSelected = Signal(str) # emite nombre de la esfera seleccionada
    coordSelected = Signal(int, int) # emite (clave, linea) al interactuar
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(440, 440)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.spheres_data: Dict[str, dict] = {}
        self.transits_data: Dict[str, dict] = {}
        self.transits_active: bool = False
        self.selected_sphere: Optional[str] = "Propósito"
        self.current_solar_lon = 0.0
        self.prenatal_solar_lon = 272.0
        self.highlighted_keys = {} # {clave: color_hex}
        self.pulse_phase = 0.0
        self.node_hitboxes: Dict[str, QPointF] = {}
        self.transit_hitboxes: Dict[str, QPointF] = {}
        
        # Timer de animación para el brillo orgánico pulsante
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self._pulse_step)
        self.anim_timer.start(50)

    def _pulse_step(self):
        self.pulse_phase = (self.pulse_phase + 0.06) % (2.0 * math.pi)
        self.update()

    def set_profile_data(self, spheres_dict: Dict[str, dict], selected_sphere: Optional[str] = None):
        """Actualiza todas las 11 esferas calculadas para representarlas en la rueda."""
        self.spheres_data = spheres_dict
        if selected_sphere:
            self.selected_sphere = selected_sphere
            
        # Extraer sol natal y sol design para telemetría central
        sol_n = spheres_dict.get("Trabajo de Vida", {})
        sol_d = spheres_dict.get("Resplandor", {})
        self.current_solar_lon = sol_n.get("longitude", 0.0)
        self.prenatal_solar_lon = sol_d.get("longitude", (self.current_solar_lon - 88.0) % 360.0)
        
        # Mapear claves activas para iluminar sectores
        self.highlighted_keys = {}
        for s_name, s_info in spheres_dict.items():
            k_num = s_info.get("key")
            k_col = s_info.get("color", "#00f0ff")
            if k_num:
                self.highlighted_keys[k_num] = k_col
                
        self.update()

    def set_transits_data(self, transits_dict: Dict[str, dict], active: bool = True):
        """Suministra el conjunto de tránsitos planetarios en tiempo real para superponer en el mandala."""
        self.transits_data = transits_dict
        self.transits_active = active
        self.update()

    def set_solar_coordinates(self, natal_lon: float, prenatal_lon: float, active_keys: Dict[int, str]):
        self.current_solar_lon = natal_lon % 360.0
        self.prenatal_solar_lon = prenatal_lon % 360.0
        self.highlighted_keys = active_keys
        self.update()

    def mousePressEvent(self, event):
        pos = event.position()
        clicked_pt = QPointF(pos.x(), pos.y())
        
        # 1. Buscar si el clic fue sobre algún nodo de tránsito (umbral de 20 px)
        if self.transits_active:
            for t_name, pt in self.transit_hitboxes.items():
                if math.hypot(clicked_pt.x() - pt.x(), clicked_pt.y() - pt.y()) < 20.0:
                    self.selected_sphere = t_name
                    self.sphereSelected.emit(t_name)
                    self.update()
                    return

        # 2. Buscar si el clic fue sobre el nodo de alguna esfera natal (umbral de 22 px)
        closest_sphere = None
        min_dist = 22.0
        for sph_name, pt in self.node_hitboxes.items():
            dist = math.hypot(clicked_pt.x() - pt.x(), clicked_pt.y() - pt.y())
            if dist < min_dist:
                min_dist = dist
                closest_sphere = sph_name
                
        if closest_sphere:
            self.selected_sphere = closest_sphere
            self.sphereSelected.emit(closest_sphere)
            self.update()
        else:
            super().mousePressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0
        max_r = min(w, h) / 2.0 - 15.0

        if max_r < 50:
            return

        # 1. Fondo del abismo cuántico con gradiente radial
        bg_grad = QRadialGradient(cx, cy, max_r)
        pulse_alpha = int(28 + 12 * math.sin(self.pulse_phase))
        bg_grad.setColorAt(0.0, QColor(10, 22, 38, 240))
        bg_grad.setColorAt(0.7, QColor(6, 12, 22, 255))
        bg_grad.setColorAt(1.0, QColor(3, 7, 14, 255))
        painter.setBrush(QBrush(bg_grad))
        painter.setPen(QPen(QColor(0, 240, 255, 60), 1.5))
        painter.drawEllipse(QPointF(cx, cy), max_r, max_r)

        # 2. Anillo exterior: Los 64 Sectores de 5.625°
        r_out = max_r - 2
        r_in = max_r - 36
        sector_angle = CelestialMechanicsEngine.SECTOR_KEY

        for i, key_num in enumerate(HEXA_MANDALA_ORDER):
            start_deg = (CelestialMechanicsEngine.THETA_0 + i * sector_angle) % 360.0
            is_active = key_num in self.highlighted_keys
            
            rad_start = math.radians(-start_deg)
            rad_end = math.radians(-(start_deg + sector_angle))
            
            p1 = QPointF(cx + r_out * math.cos(rad_start), cy + r_out * math.sin(rad_start))
            p2 = QPointF(cx + r_in * math.cos(rad_start), cy + r_in * math.sin(rad_start))
            p3 = QPointF(cx + r_in * math.cos(rad_end), cy + r_in * math.sin(rad_end))
            p4 = QPointF(cx + r_out * math.cos(rad_end), cy + r_out * math.sin(rad_end))
            
            poly = QPolygonF([p1, p2, p3, p4])
            
            if is_active:
                col_hex = self.highlighted_keys[key_num]
                fill_color = QColor(col_hex)
                fill_color.setAlpha(170)
                border_color = QColor(col_hex)
                border_color.setAlpha(255)
            else:
                fill_color = QColor(14, 28, 48, 90) if i % 2 == 0 else QColor(10, 20, 36, 90)
                border_color = QColor(30, 60, 90, 70)

            painter.setBrush(QBrush(fill_color))
            painter.setPen(QPen(border_color, 1))
            painter.drawPolygon(poly)

            # Dibujar número de la clave en orientación legible
            if max_r > 130:
                mid_angle_deg = start_deg + sector_angle / 2.0
                rad_mid = math.radians(-mid_angle_deg)
                r_text = (r_out + r_in) / 2.0
                tx = cx + r_text * math.cos(rad_mid)
                ty = cy + r_text * math.sin(rad_mid)
                
                painter.save()
                painter.translate(tx, ty)
                text_rot = -mid_angle_deg + 90
                if 90 < (mid_angle_deg % 360) < 270:
                    text_rot += 180
                painter.rotate(text_rot)
                
                font_size = 7 if max_r < 180 else 8
                painter.setFont(QFont("Consolas", font_size, QFont.Bold if is_active else QFont.Normal))
                if is_active:
                    painter.setPen(QColor(255, 255, 255))
                else:
                    painter.setPen(QColor(110, 160, 210, 140))
                    
                painter.drawText(-9, 3, f"{key_num:02d}")
                painter.restore()

        # 3. Anillo de las 6 Líneas
        r_lines_out = r_in - 4
        r_lines_in = r_lines_out - 16
        painter.setPen(QPen(QColor(0, 240, 255, 35), 1))
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), r_lines_out, r_lines_out)
        painter.drawEllipse(QPointF(cx, cy), r_lines_in, r_lines_in)

        # 4. Líneas de Geometría Sagrada / Circuitos entre Esferas Natales
        r_nodes = r_lines_in - 8
        self._draw_sequence_circuits(painter, cx, cy, r_nodes)

        # 5. Círculo Central: Núcleo Celular Bio-Luminiscente
        r_core = r_nodes - 32
        if r_core > 30:
            core_grad = QRadialGradient(cx, cy, r_core)
            core_grad.setColorAt(0.0, QColor(0, 240, 255, 110 + int(20 * math.sin(self.pulse_phase))))
            core_grad.setColorAt(0.5, QColor(6, 42, 75, 190))
            core_grad.setColorAt(1.0, QColor(4, 14, 28, 240))
            painter.setBrush(QBrush(core_grad))
            painter.setPen(QPen(QColor(0, 240, 255, 90), 2))
            painter.drawEllipse(QPointF(cx, cy), r_core, r_core)

            # Texto central
            painter.setFont(QFont("Segoe UI", 9, QFont.Bold))
            painter.setPen(QColor(0, 240, 255, 240))
            label_core = "Δt TRÁNSITOS" if self.transits_active else "HEXA-MANDALA"
            painter.drawText(QRectF(cx - 65, cy - 26, 130, 18), Qt.AlignCenter, label_core)
            
            painter.setFont(QFont("Consolas", 8))
            painter.setPen(QColor(251, 191, 36, 220))
            painter.drawText(QRectF(cx - 55, cy - 8, 110, 16), Qt.AlignCenter, f"☉ {self.current_solar_lon:.2f}°")
            
            painter.setFont(QFont("Segoe UI", 7))
            painter.setPen(QColor(148, 163, 184, 200))
            active_count = len(self.spheres_data) if self.spheres_data else 26
            mode_sub = f"{active_count}N + {len(self.transits_data)} Tránsitos" if self.transits_active else f"{active_count} Nodos Activos"
            painter.drawText(QRectF(cx - 65, cy + 10, 130, 16), Qt.AlignCenter, mode_sub)

        # 6. Renderizar todas las Esferas Natales como Haces y Nodos Luminosos (Anillo Interior)
        self.node_hitboxes.clear()
        if self.spheres_data:
            for sph_name, s_info in self.spheres_data.items():
                deg = s_info.get("longitude", 0.0)
                col_hex = s_info.get("color", "#00f0ff")
                symbol = s_info.get("simbolo", "•")
                coord = s_info.get("coord_str", "")
                is_selected = (sph_name == self.selected_sphere)
                
                self._draw_sphere_node(painter, cx, cy, deg, r_nodes, QColor(col_hex), sph_name, symbol, coord, is_selected)
        else:
            self._draw_sphere_node(painter, cx, cy, self.current_solar_lon, r_nodes, QColor(251, 191, 36), "Trabajo de Vida", "☉", "", False)
            self._draw_sphere_node(painter, cx, cy, (self.current_solar_lon + 180.0) % 360.0, r_nodes, QColor(16, 185, 129), "Evolución", "♁", "", False)
            self._draw_sphere_node(painter, cx, cy, self.prenatal_solar_lon, r_nodes, QColor(244, 63, 94), "Resplandor", "☉", "", False)
            self._draw_sphere_node(painter, cx, cy, (self.prenatal_solar_lon + 180.0) % 360.0, r_nodes, QColor(168, 85, 247), "Propósito", "♁", "", False)

        # 7. Si el Modo Tránsitos está activo: Superponer el Segundo Anillo Concéntrico Exterior
        self.transit_hitboxes.clear()
        if self.transits_active and self.transits_data:
            r_transit_ring = (r_lines_out + r_lines_in) / 2.0
            
            # Anillo concéntrico de guía para tránsitos (Línea ámbar pulsante)
            painter.setPen(QPen(QColor(251, 191, 36, 70 + int(30 * math.sin(self.pulse_phase))), 1.5, Qt.DashLine))
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(QPointF(cx, cy), r_transit_ring, r_transit_ring)

            for t_name, t_info in self.transits_data.items():
                t_deg = t_info.get("longitude", 0.0)
                t_col = QColor(t_info.get("color", "#fbbf24"))
                t_sym = t_info.get("simbolo", "⚡")
                t_coord = t_info.get("coord_str", "")
                is_sel_t = (t_name == self.selected_sphere)

                self._draw_transit_node(painter, cx, cy, t_deg, r_transit_ring, t_col, t_name, t_sym, t_coord, is_sel_t)

    def _draw_transit_node(self, painter: QPainter, cx: float, cy: float, deg: float, r_ring: float, color: QColor, name: str, symbol: str, coord: str, is_selected: bool):
        rad = math.radians(-deg)
        nx = cx + r_ring * math.cos(rad)
        ny = cy + r_ring * math.sin(rad)
        pt = QPointF(nx, ny)
        self.transit_hitboxes[name] = pt

        node_r = 10.0 if is_selected else 6.5

        # Resplandor dorado de tránsito
        if is_selected:
            halo = QRadialGradient(nx, ny, node_r + 10)
            halo.setColorAt(0.0, QColor(color.red(), color.green(), color.blue(), 230))
            halo.setColorAt(1.0, QColor(color.red(), color.green(), color.blue(), 0))
            painter.setBrush(QBrush(halo))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(pt, node_r + 10, node_r + 10)

        # Nodo en forma de diamante / gema cuántica
        painter.save()
        painter.translate(nx, ny)
        painter.rotate(45)
        painter.setBrush(QBrush(color))
        painter.setPen(QPen(QColor(255, 255, 255, 240), 1.5))
        d_size = node_r * 1.3
        painter.drawRect(QRectF(-d_size/2, -d_size/2, d_size, d_size))
        painter.restore()

        # Símbolo
        painter.setFont(QFont("Segoe UI", 7 if is_selected else 5, QFont.Bold))
        painter.setPen(QColor(10, 15, 25))
        painter.drawText(QRectF(nx - node_r, ny - node_r, node_r * 2, node_r * 2), Qt.AlignCenter, symbol)

    def _draw_sequence_circuits(self, painter: QPainter, cx: float, cy: float, r_nodes: float):
        """Dibuja las líneas sagradas que unen las esferas de cada secuencia en el mandala."""
        if not self.spheres_data:
            return

        def get_pt(sph_name):
            if sph_name in self.spheres_data:
                deg = self.spheres_data[sph_name].get("longitude", 0.0)
                rad = math.radians(-deg)
                return QPointF(cx + r_nodes * math.cos(rad), cy + r_nodes * math.sin(rad))
            return None

        # Circuito 1: Secuencia de Activación (Verde-Dorado)
        act_chain = ["Trabajo de Vida", "Evolución", "Resplandor", "Propósito"]
        pen_act = QPen(QColor(16, 185, 129, 65), 1.5, Qt.DashLine)
        painter.setPen(pen_act)
        for i in range(len(act_chain) - 1):
            p_a = get_pt(act_chain[i])
            p_b = get_pt(act_chain[i+1])
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

        # Circuito 2: Secuencia de Venus (Magenta-Rosa)
        venus_chain = ["Propósito", "Atracción", "CI (Mente)", "CE (Emoción)", "CS (Espíritu)", "Vocación / Núcleo"]
        pen_ven = QPen(QColor(236, 72, 153, 60), 1.5, Qt.DotLine)
        painter.setPen(pen_ven)
        for i in range(len(venus_chain) - 1):
            p_a = get_pt(venus_chain[i])
            p_b = get_pt(venus_chain[i+1])
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

        # Circuito 3: Circuito de Abundancia (Azul-Platino)
        pearl_chain = ["Vocación / Núcleo", "Cultura", "Abundancia", "Trabajo de Vida"]
        pen_pearl = QPen(QColor(99, 102, 241, 60), 1.5, Qt.DashDotLine)
        painter.setPen(pen_pearl)
        for i in range(len(pearl_chain) - 1):
            p_a = get_pt(pearl_chain[i])
            p_b = get_pt(pearl_chain[i+1])
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

        # Circuito 4: Circuito del Entorno / Nodos Lunares (Cian-Turquesa)
        env_chain = ["Entorno Temprano (Nodo Sur Natal)", "Entorno Maduro (Nodo Norte Natal)", "Hábitat Somático (Nodo Norte Design)", "Herencia Ancestral (Nodo Sur Design)"]
        pen_env = QPen(QColor(45, 212, 191, 70), 1.5, Qt.DashLine)
        painter.setPen(pen_env)
        for i in range(len(env_chain) - 1):
            p_a = get_pt(env_chain[i])
            p_b = get_pt(env_chain[i+1])
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

        # Circuito 5: Acoples de Polaridad NOT (Líneas Chordes Ámbar)
        canonical_keys = ["Trabajo de Vida", "Evolución", "Resplandor", "Propósito", "Atracción", "CI (Mente)", "CE (Emoción)", "CS (Espíritu)", "Vocación / Núcleo", "Cultura", "Abundancia"]
        pen_not = QPen(QColor(217, 119, 6, 45), 1.0, Qt.DotLine)
        painter.setPen(pen_not)
        for c_name in canonical_keys:
            not_name = f"NOT {c_name}"
            p_a = get_pt(c_name)
            p_b = get_pt(not_name)
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

        # Circuito 6: Circuito Transpersonal Cósmico (Púrpura-Violeta)
        trans_chain = ["Ley / Disciplina (Saturno Natal)", "Innovación / Visión (Urano Natal)", "Mística / Aspiración (Neptuno Natal)", "Poder de la Verdad (Plutón Natal)"]
        pen_trans = QPen(QColor(168, 85, 247, 60), 1.5, Qt.DashDotLine)
        painter.setPen(pen_trans)
        for i in range(len(trans_chain) - 1):
            p_a = get_pt(trans_chain[i])
            p_b = get_pt(trans_chain[i+1])
            if p_a and p_b:
                painter.drawLine(p_a, p_b)

    def _draw_sphere_node(self, painter: QPainter, cx: float, cy: float, deg: float, r_nodes: float, color: QColor, name: str, symbol: str, coord: str, is_selected: bool):
        rad = math.radians(-deg)
        nx = cx + r_nodes * math.cos(rad)
        ny = cy + r_nodes * math.sin(rad)
        pt = QPointF(nx, ny)
        self.node_hitboxes[name] = pt

        # Rayo láser que sale desde el centro hasta el nodo
        ray_alpha = 180 if is_selected else 60
        ray_width = 2.5 if is_selected else 1.0
        pen_ray = QPen(QColor(color.red(), color.green(), color.blue(), ray_alpha), ray_width)
        painter.setPen(pen_ray)
        painter.drawLine(QPointF(cx, cy), pt)

        # Nodo de la esfera con halo bioluminiscente
        node_radius = 12.0 if is_selected else 8.0
        
        if is_selected:
            pulse_extra = 4.0 * (math.sin(self.pulse_phase) * 0.5 + 0.5)
            halo_grad = QRadialGradient(nx, ny, node_radius + 12 + pulse_extra)
            halo_grad.setColorAt(0.0, QColor(color.red(), color.green(), color.blue(), 200))
            halo_grad.setColorAt(1.0, QColor(color.red(), color.green(), color.blue(), 0))
            painter.setBrush(QBrush(halo_grad))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(pt, node_radius + 12 + pulse_extra, node_radius + 12 + pulse_extra)

        # Cuerpo del nodo
        painter.setBrush(QBrush(color))
        painter.setPen(QPen(QColor(255, 255, 255, 240 if is_selected else 180), 1.5))
        painter.drawEllipse(pt, node_radius, node_radius)

        # Símbolo dentro del nodo
        painter.setFont(QFont("Segoe UI", 8 if is_selected else 6, QFont.Bold))
        painter.setPen(QColor(10, 15, 25))
        painter.drawText(QRectF(nx - node_radius, ny - node_radius, node_radius * 2, node_radius * 2), Qt.AlignCenter, symbol)

        # Etiqueta exterior con coordenada (ej: K3.5)
        if coord:
            r_lbl = r_nodes + (16 if is_selected else 12)
            lx = cx + r_lbl * math.cos(rad)
            ly = cy + r_lbl * math.sin(rad)
            painter.setFont(QFont("Consolas", 7, QFont.Bold if is_selected else QFont.Normal))
            painter.setPen(QColor(255, 255, 255) if is_selected else color)
            painter.drawText(QRectF(lx - 25, ly - 7, 50, 14), Qt.AlignCenter, f"K{coord}")



class StateVectorBioGauge(QWidget):
    """
    Visualizador Bio-Métrico del Vector de Estado Cotidiano:
    S = [E, C, R] en [0, 1] y Rendimiento Biológico = (C * R) / (E + epsilon).
    Diseñado con 3 círculos concéntricos de neón y tacómetro bio-energético.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(320, 220)
        self.e = 0.35 # Entropía (E)
        self.c = 0.75 # Coherencia (C)
        self.r = 0.80 # Resonancia (R)
        self.bio_yield = 1.50
        self.regimen_str = "Fase Coherente Integrada"

    def set_state_values(self, e: float, c: float, r: float):
        self.e = e
        self.c = c
        self.r = r
        val, reg, _ = CelestialMechanicsEngine.calculate_biological_yield(e, c, r)
        self.bio_yield = val
        self.regimen_str = reg
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0 + 10

        # Tarjeta de fondo oscura con borde luminiscente
        painter.setBrush(QBrush(QColor(12, 18, 30, 240)))
        painter.setPen(QPen(QColor(0, 240, 255, 40), 1))
        painter.drawRoundedRect(4, 4, w - 8, h - 8, 12, 12)

        # Título superior
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.setPen(QColor(0, 240, 255, 230))
        painter.drawText(16, 26, "VECTOR DE ESTADO S = [E, C, R]")

        # Estado del régimen
        painter.setFont(QFont("Consolas", 8, QFont.Bold))
        if "Coherente" in self.regimen_str or "Don" in self.regimen_str:
            painter.setPen(QColor(0, 255, 179))
        elif "Entrópica" in self.regimen_str or "Sombra" in self.regimen_str:
            painter.setPen(QColor(255, 75, 75))
        elif "Disociación" in self.regimen_str:
            painter.setPen(QColor(180, 120, 255))
        else:
            painter.setPen(QColor(255, 200, 50))
            
        painter.drawText(QRectF(w - 190, 12, 175, 18), Qt.AlignRight, self.regimen_str)

        # 3 Barras / Medidores circulares concéntricos
        r_base = min(w, h) / 2.0 - 32
        thickness = 10
        gap = 4

        # 1. Anillo Exterior: E (Entropía - Rojo / Ámbar)
        self._draw_arc_meter(painter, cx, cy, r_base, thickness, self.e, QColor(255, 70, 70), "E (Entropía)")

        # 2. Anillo Medio: C (Coherencia - Cian / Teal)
        self._draw_arc_meter(painter, cx, cy, r_base - thickness - gap, thickness, self.c, QColor(0, 240, 255), "C (Coherencia)")

        # 3. Anillo Interior: R (Resonancia - Violeta / Oro)
        self._draw_arc_meter(painter, cx, cy, r_base - (thickness + gap) * 2, thickness, self.r, QColor(168, 85, 247), "R (Resonancia)")

        # Tacómetro Central: Rendimiento Biológico
        r_inner = r_base - (thickness + gap) * 3
        if r_inner > 20:
            painter.setBrush(QBrush(QColor(15, 25, 45, 200)))
            painter.setPen(QPen(QColor(0, 240, 255, 60), 1))
            painter.drawEllipse(QPointF(cx, cy), r_inner, r_inner)

            painter.setFont(QFont("Consolas", 12, QFont.Bold))
            painter.setPen(QColor(255, 255, 255))
            painter.drawText(QRectF(cx - 35, cy - 14, 70, 20), Qt.AlignCenter, f"{self.bio_yield:.2f}")

            painter.setFont(QFont("Segoe UI", 6, QFont.Bold))
            painter.setPen(QColor(0, 240, 255, 180))
            painter.drawText(QRectF(cx - 35, cy + 6, 70, 12), Qt.AlignCenter, "RENDIMIENTO")

    def _draw_arc_meter(self, painter: QPainter, cx: float, cy: float, radius: float, thickness: float, value: float, color: QColor, label: str):
        rect = QRectF(cx - radius, cy - radius, radius * 2, radius * 2)
        start_angle = 225 * 16
        span_total = -270 * 16

        # Pista apagada de fondo
        pen_bg = QPen(QColor(30, 45, 65, 120), thickness, Qt.SolidLine, Qt.RoundCap)
        painter.setPen(pen_bg)
        painter.setBrush(Qt.NoBrush)
        painter.drawArc(rect, start_angle, span_total)

        # Arco activo
        span_val = int(span_total * max(0.0, min(1.0, value)))
        pen_val = QPen(color, thickness, Qt.SolidLine, Qt.RoundCap)
        painter.setPen(pen_val)
        painter.drawArc(rect, start_angle, span_val)


class MultiParticleBridgeView(QWidget):
    """
    Grafo Bio-Luminiscente para visualizar y simular la interacción entre 2 o más vórtices resonantes:
    Dibuja nodos cuánticos con topología de 6 bits y enlaces según la tipología:
    Serie, Paralelo, Antípoda (NOT) o Clúster Bioquímico.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(320, 220)
        self.active_keys = [31, 41]
        self.bridge_info = {}
        self.anim_t = 0.0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._step)
        self.timer.start(40)

    def _step(self):
        self.anim_t = (self.anim_t + 0.04) % 1.0
        self.update()

    def set_bridge_data(self, key_a: int, key_b: int):
        self.active_keys = [key_a, key_b]
        self.bridge_info = DiscreteParticleEngine.analyze_bridge(key_a, key_b)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        w, h = self.width(), self.height()

        # Marco de fondo de la cápsula de señales
        painter.setBrush(QBrush(QColor(10, 16, 28, 240)))
        painter.setPen(QPen(QColor(0, 240, 255, 40), 1))
        painter.drawRoundedRect(4, 4, w - 8, h - 8, 12, 12)

        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.setPen(QColor(0, 240, 255, 230))
        painter.drawText(16, 26, "INTERACCIÓN MULTIPARTÍCULA & PUENTES")

        if len(self.active_keys) < 2:
            return

        ka, kb = self.active_keys[0], self.active_keys[1]
        data_a = CORE64_CATALOG.get(ka, {})
        data_b = CORE64_CATALOG.get(kb, {})

        node_a_pos = QPointF(w * 0.22, h * 0.52)
        node_b_pos = QPointF(w * 0.78, h * 0.52)

        # Determinar color y estilo del canal según el acoplamiento
        coupling = self.bridge_info.get("coupling_type", "En Serie")
        if "Antípoda" in coupling:
            line_col = QColor(255, 60, 120)
            wave_type = "laser"
        elif "Anillo" in coupling:
            line_col = QColor(0, 255, 179)
            wave_type = "organic"
        elif "Paralelo" in coupling:
            line_col = QColor(255, 200, 50)
            wave_type = "parallel"
        else:
            line_col = QColor(0, 240, 255)
            wave_type = "series"

        # Dibujar canal / puente entre partículas
        pen = QPen(line_col, 2.5)
        painter.setPen(pen)
        painter.drawLine(node_a_pos, node_b_pos)

        # Partícula cuántica animada viajando por el puente
        packet_x = node_a_pos.x() + (node_b_pos.x() - node_a_pos.x()) * self.anim_t
        packet_y = node_a_pos.y() + (node_b_pos.y() - node_a_pos.y()) * self.anim_t
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(QPen(line_col, 2))
        painter.drawEllipse(QPointF(packet_x, packet_y), 5, 5)

        # Dibujar Nodo A
        self._draw_particle_node(painter, node_a_pos, ka, data_a, QColor(0, 240, 255))

        # Dibujar Nodo B
        self._draw_particle_node(painter, node_b_pos, kb, data_b, QColor(255, 200, 50))

        # Etiqueta inferior del diagnóstico de puente
        painter.setFont(QFont("Consolas", 8, QFont.Bold))
        painter.setPen(line_col)
        painter.drawText(QRectF(16, h - 34, w - 32, 16), Qt.AlignCenter, f"MODO: {coupling}")

        painter.setFont(QFont("Segoe UI", 7))
        painter.setPen(QColor(160, 190, 220, 180))
        c_label = resolve_cluster_name(data_a.get('ring', ''))
        painter.drawText(QRectF(16, h - 20, w - 32, 14), Qt.AlignCenter, f"Distancia Hamming: {self.bridge_info.get('hamming_distance', 0)} bits | {c_label}")

    def _draw_particle_node(self, painter: QPainter, pos: QPointF, key_num: int, data: dict, color: QColor):
        r = 32
        grad = QRadialGradient(pos.x(), pos.y(), r)
        grad.setColorAt(0.0, QColor(color.red(), color.green(), color.blue(), 180))
        grad.setColorAt(0.7, QColor(15, 25, 45, 220))
        grad.setColorAt(1.0, QColor(8, 12, 22, 255))

        painter.setBrush(QBrush(grad))
        painter.setPen(QPen(color, 2))
        painter.drawEllipse(pos, r, r)

        painter.setFont(QFont("Consolas", 11, QFont.Bold))
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(QRectF(pos.x() - r, pos.y() - 14, r * 2, 16), Qt.AlignCenter, f"V{key_num}")

        painter.setFont(QFont("Consolas", 7))
        painter.setPen(QColor(0, 240, 255, 200))
        painter.drawText(QRectF(pos.x() - r, pos.y() + 2, r * 2, 12), Qt.AlignCenter, data.get("bits", "000000"))

        painter.setFont(QFont("Segoe UI", 7, QFont.Bold))
        painter.setPen(QColor(220, 235, 250))
        painter.drawText(QRectF(pos.x() - r - 20, pos.y() + r + 2, r * 2 + 40, 14), Qt.AlignCenter, data.get("coherencia", data.get("don", "")))


class HolographicRadarView(QWidget):
    """
    Radar Holográfico 2D para visualización de Embeddings Semánticos y Resonancia Cuántica.
    Dibuja los vectores proyectados en el espacio latente de la IA (Ollama),
    mostrando la distancia semántica entre la situación del usuario y los 64 vórtices resonantes.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(320, 260)
        self.user_point = (0.0, 0.0)
        self.key_points = [] # list of (x, y, key_num, label, similarity)
        self.radar_angle = 0.0

        self.sweep_timer = QTimer(self)
        self.sweep_timer.timeout.connect(self._sweep)
        self.sweep_timer.start(50)

    def _sweep(self):
        self.radar_angle = (self.radar_angle + 2.5) % 360.0
        self.update()

    def update_embeddings_projection(self, user_vec_2d: Tuple[float, float], key_projections: List[Tuple[float, float, int, str, float]]):
        self.user_point = user_vec_2d
        self.key_points = key_projections
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0
        max_r = min(w, h) / 2.0 - 20

        # Fondo del domo de radar
        painter.setBrush(QBrush(QColor(8, 14, 25, 250)))
        painter.setPen(QPen(QColor(0, 240, 255, 50), 1))
        painter.drawRoundedRect(4, 4, w - 8, h - 8, 12, 12)

        # Círculos concéntricos de rango
        for r_step in [max_r * 0.33, max_r * 0.66, max_r]:
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QPen(QColor(0, 240, 255, 35), 1, Qt.DashLine))
            painter.drawEllipse(QPointF(cx, cy), r_step, r_step)

        # Líneas de cuadrícula polar
        painter.setPen(QPen(QColor(0, 240, 255, 25), 1))
        painter.drawLine(QPointF(cx - max_r, cy), QPointF(cx + max_r, cy))
        painter.drawLine(QPointF(cx, cy - max_r), QPointF(cx, cy + max_r))

        # Haz giratorio del barrido del radar holográfico
        sweep_rad = math.radians(-self.radar_angle)
        sx = cx + max_r * math.cos(sweep_rad)
        sy = cy + max_r * math.sin(sweep_rad)
        sweep_pen = QPen(QColor(0, 255, 179, 140), 1.5)
        painter.setPen(sweep_pen)
        painter.drawLine(QPointF(cx, cy), QPointF(sx, sy))

        # Puntos de los Vórtices en el espacio semántico
        for px_norm, py_norm, kn, label, sim in self.key_points:
            pt_x = cx + px_norm * max_r * 0.9
            pt_y = cy - py_norm * max_r * 0.9
            
            # Color basado en la similitud semántica con la situación
            alpha = int(80 + 175 * max(0.0, sim))
            point_color = QColor(0, 240, 255, alpha) if sim < 0.6 else QColor(255, 200, 50, alpha)
            
            painter.setBrush(QBrush(point_color))
            painter.setPen(QPen(QColor(255, 255, 255, alpha), 1))
            size = 4.0 if sim < 0.6 else 6.5
            painter.drawEllipse(QPointF(pt_x, pt_y), size, size)

            if sim > 0.6:
                painter.setFont(QFont("Consolas", 7, QFont.Bold))
                painter.setPen(QColor(255, 255, 255, 220))
                painter.drawText(pt_x + 8, pt_y + 3, f"V{kn} ({sim:.2f})")

        # Punto del Usuario (La Escena / Runtime actual)
        ux = cx + self.user_point[0] * max_r * 0.9
        uy = cy - self.user_point[1] * max_r * 0.9

        painter.setBrush(QBrush(QColor(255, 50, 100)))
        painter.setPen(QPen(QColor(255, 255, 255), 2))
        painter.drawEllipse(QPointF(ux, uy), 8, 8)

        # Halo del usuario
        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(QColor(255, 50, 100, 120), 2))
        painter.drawEllipse(QPointF(ux, uy), 14, 14)

        painter.setFont(QFont("Segoe UI", 8, QFont.Bold))
        painter.setPen(QColor(255, 120, 150))
        painter.drawText(ux + 12, uy + 4, "TÚ (ESCENA RUNTIME)")


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5B: MOTOR DE SINASTRÍA BIOFÍSICA Y ACOPLAMIENTO MULTIPARTÍCULA
# ══════════════════════════════════════════════════════════════════════════════

class NetworkSynastryEngine:
    """
    Motor determinista para calcular el acoplamiento bio-electromagnético,
    puentes de inducción mutua y colisiones de fase entre dos o más partículas/matrices (Sujeto A y Sujeto B).
    """

    # Canales canónicos de resonancia electromagnética en la red de 64 vórtices resonantes (Pares de inducción complementaria)
    CANONICAL_HARMONIC_CHANNELS = [
        (1, 8, "Inspiración & Dirección Creativa"),
        (2, 14, "El Guardián del Almacén de Energía"),
        (3, 60, "Mutación Bio-Evolutiva Pulsante"),
        (4, 63, "Lógica Formal & Síntesis de Patrones"),
        (5, 15, "Ritmos Biológicos & Magnetismo Universal"),
        (6, 59, "Apareamiento & Apertura Genética"),
        (7, 31, "El Canal del Alfa: Liderazgo Elegido"),
        (9, 52, "Concentración Focalizada & Calma Inmóvil"),
        (10, 20, "El Despertar: Coherencia del Ser"),
        (10, 34, "Exploración & Autosuficiencia"),
        (10, 57, "Forma Perfecta: Claridad Acústica"),
        (11, 56, "Curiosidad & Búsqueda Existencial"),
        (12, 22, "Apertura Emocional & Timbre Social"),
        (13, 33, "El Testigo: Memoria Histórica del Clan"),
        (16, 48, "Maestría Técnica & Talento Profundo"),
        (17, 62, "Organización Conceptual & Arquetipos"),
        (18, 58, "Insatisfacción & Reparación de Juicio"),
        (19, 49, "Síntesis Social & Sensibilidad Fisiológica"),
        (20, 34, "Carisma & Impulso Cinético"),
        (20, 57, "Impulso Instantáneo & Percepción"),
        (21, 45, "Control de Recursos & Soberanía Material"),
        (23, 43, "Estructuración del Genio & Elocuencia"),
        (24, 61, "El Pensador: Retorno del Misterio"),
        (25, 51, "Iniciación de la Herida Primordial"),
        (26, 44, "Transmisión Conceptual & Rendición"),
        (27, 50, "Preservación Biológica & Custodia"),
        (28, 38, "La Lucha Existencial por el Significado"),
        (29, 46, "Descubrimiento & Éxito en el Compromiso"),
        (30, 41, "Reconocimiento del Deseo & Anticipación"),
        (32, 54, "Transformación Social & Ambición Práctica"),
        (34, 57, "Poder de Supervivencia Intuitiva"),
        (35, 36, "Transitoriedad & Maduración Sensorial"),
        (37, 40, "Comunidad & Pacto de Lealtad"),
        (39, 55, "Emancipación Emocional & Mutación Espiritual"),
        (42, 53, "Maduración Cíclica: Apertura y Cierre"),
        (47, 64, "Abstracción Mental & Conclusión de Pasado")
    ]

    @classmethod
    def get_harmonic_partner(cls, key_num: int) -> List[Tuple[int, str]]:
        """Retorna los vórtices que forman un canal de inducción armónico cerrado con key_num."""
        partners = []
        for ka, kb, desc in cls.CANONICAL_HARMONIC_CHANNELS:
            if ka == key_num:
                partners.append((kb, desc))
            elif kb == key_num:
                partners.append((ka, desc))
        return partners

    @classmethod
    def analyze_coupling(
        cls, 
        matrix_a: Dict[str, Any], 
        matrix_b: Dict[str, Any],
        name_a: str = "Sujeto Alfa",
        name_b: str = "Sujeto Beta"
    ) -> Dict[str, Any]:
        """
        Analiza de forma exhaustiva el acoplamiento sinástrico biofísico:
        1. Puentes Electromagnéticos Directos (A tiene una parte, B la otra -> circuito cerrado).
        2. Compromisos Electromagnéticos (A tiene el canal completo y B tiene una parte, o viceversa).
        3. Antípodas Cruzadas / Tensiones NOT (Distancia Hamming 6 entre esferas activas).
        4. Clústeres Bioquímicos Homólogos (Comparten el mismo anillo de codones).
        5. Fricciones e Intersecciones de Mismos Vórtices Resonantes (Compañerismo electromagnético).
        6. Índice de Resonancia Relacional eta_red in [0, 1].
        """
        spheres_a = matrix_a.get("spheres", {})
        spheres_b = matrix_b.get("spheres", {})

        keys_a_map: Dict[int, List[str]] = {}
        for s_name, s_data in spheres_a.items():
            k = s_data.get("key", 0)
            if k > 0:
                keys_a_map.setdefault(k, []).append(s_name)

        keys_b_map: Dict[int, List[str]] = {}
        for s_name, s_data in spheres_b.items():
            k = s_data.get("key", 0)
            if k > 0:
                keys_b_map.setdefault(k, []).append(s_name)

        unique_keys_a = set(keys_a_map.keys())
        unique_keys_b = set(keys_b_map.keys())

        # 1. Puentes Electromagnéticos Directos (Uno aporta Ka y el otro aporta Kb)
        closed_channels = []
        for ka, kb, desc in cls.CANONICAL_HARMONIC_CHANNELS:
            in_a_ka = ka in unique_keys_a
            in_a_kb = kb in unique_keys_a
            in_b_ka = ka in unique_keys_b
            in_b_kb = kb in unique_keys_b

            # Directo: A aporta ka y B aporta kb (o viceversa), sin que ninguno poseyera el canal completo en solitario
            if (in_a_ka and in_b_kb and not in_a_kb and not in_b_ka):
                closed_channels.append({
                    "type": "Electromagnético Directo (Inducción Mutua)",
                    "key_a": ka,
                    "key_b": kb,
                    "provider_a": f"{name_a} (V{ka})",
                    "provider_b": f"{name_b} (V{kb})",
                    "spheres_a": keys_a_map[ka],
                    "spheres_b": keys_b_map[kb],
                    "description": desc,
                    "nature": "Atracción polar electromagnética; chispa de co-creación de alta intensidad.",
                    "protocol": "Reconocer que ninguno posee la totalidad en solitario; delegar el polo respectivo sin invadir."
                })
            elif (in_a_kb and in_b_ka and not in_a_ka and not in_b_kb):
                closed_channels.append({
                    "type": "Electromagnético Directo (Inducción Mutua)",
                    "key_a": kb,
                    "key_b": ka,
                    "provider_a": f"{name_a} (V{kb})",
                    "provider_b": f"{name_b} (V{ka})",
                    "spheres_a": keys_a_map[kb],
                    "spheres_b": keys_b_map[ka],
                    "description": desc,
                    "nature": "Atracción polar electromagnética; chispa de co-creación de alta intensidad.",
                    "protocol": "Reconocer que ninguno posee la totalidad en solitario; delegar el polo respectivo sin invadir."
                })

        # 2. Compañerismo Electromagnético (Mismo Vórtice en ambos)
        shared_keys = unique_keys_a.intersection(unique_keys_b)
        companionship_nodes = []
        for sk in sorted(shared_keys):
            data_k = CORE64_CATALOG.get(sk, {})
            companionship_nodes.append({
                "key": sk,
                "spheres_a": keys_a_map[sk],
                "spheres_b": keys_b_map[sk],
                "coherencia": data_k.get("coherencia", data_k.get("don", "")),
                "entropia": data_k.get("entropia", data_k.get("sombra", "")),
                "ring": data_k.get("ring", ""),
                "description": f"Ambos operan en el Vórtice Resonante {sk}. Máxima afinidad o amplificación de sombras en espejo."
            })

        # 3. Antípodas Cruzadas / Tensiones NOT (Hamming DH = 6)
        antipode_crossings = []
        for ka in unique_keys_a:
            bits_a = CORE64_CATALOG.get(ka, {}).get("bits", "000000")
            not_bits_a = DiscreteParticleEngine.get_not_antipode(bits_a)
            for kb in unique_keys_b:
                bits_b = CORE64_CATALOG.get(kb, {}).get("bits", "000000")
                if bits_b == not_bits_a:
                    data_a = CORE64_CATALOG.get(ka, {})
                    data_b = CORE64_CATALOG.get(kb, {})
                    antipode_crossings.append({
                        "key_a": ka,
                        "key_b": kb,
                        "spheres_a": keys_a_map[ka],
                        "spheres_b": keys_b_map[kb],
                        "don_a": data_a.get("coherencia", data_a.get("don", "")),
                        "don_b": data_b.get("coherencia", data_b.get("don", "")),
                        "entropia_a": data_a.get("entropia", data_a.get("sombra", "")),
                        "entropia_b": data_b.get("entropia", data_b.get("sombra", "")),
                        "risk": f"Proyección reactiva: la entropía de {name_a} ({data_a.get('entropia','')}) puede detonar a {name_b} ({data_b.get('entropia','')}).",
                        "calibration": "Eje de calibración maestro: integran polos complementarios opuestos de la matriz."
                    })

        # 4. Clústeres Bioquímicos Compartidos (Anillos de Codones en resonancia de grupo)
        clusters_a: Dict[str, List[int]] = {}
        for ka in unique_keys_a:
            r = CORE64_CATALOG.get(ka, {}).get("ring", "")
            if r:
                clusters_a.setdefault(r, []).append(ka)

        clusters_b: Dict[str, List[int]] = {}
        for kb in unique_keys_b:
            r = CORE64_CATALOG.get(kb, {}).get("ring", "")
            if r:
                clusters_b.setdefault(r, []).append(kb)

        shared_clusters = []
        for ring_name, k_list_a in clusters_a.items():
            if ring_name in clusters_b:
                k_list_b = clusters_b[ring_name]
                c_name = resolve_cluster_name(ring_name)
                shared_clusters.append({
                    "ring": c_name,
                    "keys_a": k_list_a,
                    "keys_b": k_list_b,
                    "significance": f"Resonancia somática compartida en el {c_name}. Sintonía biológica y epigenética común."
                })

        # 5. Cálculo del Índice Compuesto de Resonancia Relacional eta_red in [0.0, 1.0]
        # Ponderación: Canales Directos (peso alto: 0.12 c/u), Clústeres (0.08 c/u), Antípodas (0.06 c/u), Compartidas (0.05 c/u)
        raw_score = (
            len(closed_channels) * 0.14 +
            len(shared_clusters) * 0.08 +
            len(antipode_crossings) * 0.06 +
            len(companionship_nodes) * 0.05
        )
        eta_red = min(0.98, max(0.15, raw_score))

        return {
            "name_a": name_a,
            "name_b": name_b,
            "total_nodes_a": len(unique_keys_a),
            "total_nodes_b": len(unique_keys_b),
            "closed_channels": closed_channels,
            "companionship_nodes": companionship_nodes,
            "antipode_crossings": antipode_crossings,
            "shared_clusters": shared_clusters,
            "relational_resonance_index": round(eta_red, 3),
            "coupling_summary": f"Acoplamiento activo: {len(closed_channels)} Canales Electromagnéticos | {len(antipode_crossings)} Ejes NOT | {len(shared_clusters)} Clústeres Bioquímicos."
        }


class NetworkCouplingGraphView(QWidget):
    """
    Visualizador Gráfico Bioluminiscente del Acoplamiento de Red (Sinastría).
    Representa dos pilares verticales de partículas (Sujeto Alfa a la izquierda, Sujeto Beta a la derecha)
    con líneas de inducción luminosas, pulsos cuánticos y conexiones de fase interactiva.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(480, 360)
        self.data_a: Dict[str, Any] = {}
        self.data_b: Dict[str, Any] = {}
        self.synastry_data: Dict[str, Any] = {}
        self.anim_t = 0.0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._step)
        self.timer.start(40)

    def _step(self):
        self.anim_t = (self.anim_t + 0.03) % 1.0
        self.update()

    def set_coupling_data(self, matrix_a: Dict[str, Any], matrix_b: Dict[str, Any], syn_result: Dict[str, Any]):
        self.data_a = matrix_a
        self.data_b = matrix_b
        self.synastry_data = syn_result
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        w, h = self.width(), self.height()

        # Marco de fondo
        painter.setBrush(QBrush(QColor(8, 14, 25, 245)))
        painter.setPen(QPen(QColor(0, 240, 255, 45), 1))
        painter.drawRoundedRect(4, 4, w - 8, h - 8, 12, 12)

        name_a = self.synastry_data.get("name_a", "Sujeto Alfa")
        name_b = self.synastry_data.get("name_b", "Sujeto Beta")
        eta_val = self.synastry_data.get("relational_resonance_index", 0.0)

        # Encabezado
        painter.setFont(QFont("Segoe UI", 10, QFont.Bold))
        painter.setPen(QColor(0, 240, 255, 240))
        painter.drawText(16, 26, f"ACOPLAMIENTO DE RED BIO-ELECTROMAGNÉTICO: {name_a.upper()} ⟷ {name_b.upper()}")

        painter.setFont(QFont("Consolas", 9, QFont.Bold))
        col_res = QColor(0, 255, 179) if eta_val > 0.6 else QColor(255, 200, 50)
        painter.setPen(col_res)
        painter.drawText(w - 220, 26, f"η_red = {eta_val * 100:.1f}% Resonancia")

        spheres_a = self.data_a.get("spheres", {})
        spheres_b = self.data_b.get("spheres", {})

        if not spheres_a or not spheres_b:
            painter.setFont(QFont("Segoe UI", 10))
            painter.setPen(QColor(148, 163, 184))
            painter.drawText(QRectF(0, 0, w, h), Qt.AlignCenter, "Carga o calcula dos perfiles para visualizar la red de acoplamiento multipartícula.")
            return

        # Posiciones de los nodos de A (Izquierda) y B (Derecha)
        items_a = list(spheres_a.items())[:12] # Muestra las claves principales de cada perfil
        items_b = list(spheres_b.items())[:12]

        x_left = 110.0
        x_right = w - 110.0
        step_y_a = (h - 80) / max(1, len(items_a))
        step_y_b = (h - 80) / max(1, len(items_b))

        pos_map_a: Dict[int, QPointF] = {}
        for idx, (s_name, s_info) in enumerate(items_a):
            py = 50.0 + idx * step_y_a + step_y_a * 0.5
            pos_map_a[s_info.get("key", 0)] = QPointF(x_left, py)

        pos_map_b: Dict[int, QPointF] = {}
        for idx, (s_name, s_info) in enumerate(items_b):
            py = 50.0 + idx * step_y_b + step_y_b * 0.5
            pos_map_b[s_info.get("key", 0)] = QPointF(x_right, py)

        # 1. Dibujar Enlaces de Canales Electromagnéticos Directos (Color Cian / Dorado resplandeciente)
        closed_ch = self.synastry_data.get("closed_channels", [])
        for ch in closed_ch:
            ka = ch.get("key_a", 0)
            kb = ch.get("key_b", 0)
            pt_a = pos_map_a.get(ka) or pos_map_a.get(kb)
            pt_b = pos_map_b.get(kb) or pos_map_b.get(ka)
            if pt_a and pt_b:
                pen = QPen(QColor(0, 240, 255, 200), 2.2)
                painter.setPen(pen)
                painter.drawLine(pt_a, pt_b)

                # Paquete de energía animado
                px = pt_a.x() + (pt_b.x() - pt_a.x()) * self.anim_t
                py = pt_a.y() + (pt_b.y() - pt_a.y()) * self.anim_t
                painter.setBrush(QBrush(QColor(255, 255, 255)))
                painter.setPen(QPen(QColor(0, 240, 255), 2))
                painter.drawEllipse(QPointF(px, py), 4, 4)

        # 2. Dibujar Antípodas NOT (Color Rosa Neón)
        antipodes = self.synastry_data.get("antipode_crossings", [])
        for ant in antipodes:
            ka = ant.get("key_a", 0)
            kb = ant.get("key_b", 0)
            pt_a = pos_map_a.get(ka)
            pt_b = pos_map_b.get(kb)
            if pt_a and pt_b:
                pen = QPen(QColor(244, 114, 182, 160), 1.6, Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(pt_a, pt_b)

        # 3. Dibujar Nodos Compartidos (Color Esmeralda)
        companionships = self.synastry_data.get("companionship_nodes", [])
        for comp in companionships:
            k = comp.get("key", 0)
            pt_a = pos_map_a.get(k)
            pt_b = pos_map_b.get(k)
            if pt_a and pt_b:
                pen = QPen(QColor(0, 255, 179, 130), 1.2, Qt.DotLine)
                painter.setPen(pen)
                painter.drawLine(pt_a, pt_b)

        # Dibujar Nodos de Sujeto Alfa
        for s_name, s_info in items_a:
            k = s_info.get("key", 0)
            pos = pos_map_a.get(k)
            if pos:
                self._draw_synastry_node(painter, pos, k, s_name, s_info, QColor(0, 240, 255), align_left=True)

        # Dibujar Nodos de Sujeto Beta
        for s_name, s_info in items_b:
            k = s_info.get("key", 0)
            pos = pos_map_b.get(k)
            if pos:
                self._draw_synastry_node(painter, pos, k, s_name, s_info, QColor(251, 191, 36), align_left=False)

    def _draw_synastry_node(self, painter: QPainter, pos: QPointF, key_num: int, sph_name: str, info: dict, color: QColor, align_left: bool):
        r = 13.0
        grad = QRadialGradient(pos.x(), pos.y(), r)
        grad.setColorAt(0.0, QColor(color.red(), color.green(), color.blue(), 220))
        grad.setColorAt(1.0, QColor(10, 18, 32, 240))
        painter.setBrush(QBrush(grad))
        painter.setPen(QPen(color, 1.5))
        painter.drawEllipse(pos, r, r)

        painter.setFont(QFont("Consolas", 8, QFont.Bold))
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(QRectF(pos.x() - r, pos.y() - 7, r * 2, 14), Qt.AlignCenter, f"{key_num}")

        # Etiquetas de texto
        painter.setFont(QFont("Segoe UI", 7))
        painter.setPen(QColor(203, 213, 225))
        label_text = f"{sph_name} ({info.get('line', 1)})"
        if align_left:
            painter.drawText(QRectF(pos.x() - 100, pos.y() - 7, 84, 14), Qt.AlignRight | Qt.AlignVCenter, label_text)
        else:
            painter.drawText(QRectF(pos.x() + 16, pos.y() - 7, 88, 14), Qt.AlignLeft | Qt.AlignVCenter, label_text)


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5C: MOTOR DE TRÁNSITOS EN TIEMPO REAL (DELTA DINÁMICO Δt)
# ══════════════════════════════════════════════════════════════════════════════

class RealTimeTransitEngine:
    """
    Motor determinista para calcular las coordenadas celestes continuas en tiempo real (Δt)
    y evaluar la interferencia de onda electromagnética sobre la matriz natal:
    - Superposiciones directas (Tránsito en el mismo vórtice que una esfera natal).
    - Ignición de ejes complementarios / Canales activados en vivo.
    - Oposiciones polares (Hamming DH = 6 / Inversión lógica NOT).
    """

    TRANSIT_BODIES = [
        ("Sol en Tránsito", "Sun", "#fbbf24", "☉", "Foco atencional consciente, irradiación vital colectiva y llamado evolutivo actual."),
        ("Tierra en Tránsito", "Earth", "#10b981", "♁", "Anclaje somático planetario, fricción de maduración y manifestación física inmediata."),
        ("Luna en Tránsito", "Moon", "#38bdf8", "☽", "Pulso bio-ritmo celular, campo gravitatorio emocional y mareas psíquicas."),
        ("Mercurio en Tránsito", "Mercury", "#2dd4bf", "☿", "Red neuronal colectiva, codificación de datos, lenguaje y velocidad de procesamiento."),
        ("Venus en Tránsito", "Venus", "#ec4899", "♀", "Resonancia vincular, coherencia afectiva y patrones de atracción biofísica."),
        ("Marte en Tránsito", "Mars", "#ef4444", "♂", "Vector de empuje cinético, tracción ejecutiva, coraje somático y riesgo de reactividad."),
        ("Júpiter en Tránsito", "Jupiter", "#f59e0b", "♃", "Expansión sinérgica, leyes de orden superior y multiplicación de recursos."),
        ("Saturno en Tránsito", "Saturn", "#a855f7", "♄", "Límites biológicos no negociables, cristalización estructural y disciplina."),
        ("Urano en Tránsito", "Uranus", "#06b6d4", "♅", "Disrupción cuántica, chispas de innovación epigenética y saltos de fase."),
        ("Neptuno en Tránsito", "Neptune", "#818cf8", "♆", "Disolución de barreras, mística transpersonal y percepción sutil."),
        ("Plutón en Tránsito", "Pluto", "#e11d48", "♇", "Regeneración molecular de fondo, poder de la verdad y muerte de lo caduco."),
        ("Nodo Norte en Tránsito", "NorthNode", "#14b8a6", "☊", "Vector de avance hacia el hábitat futuro y dirección evolutiva del colectivo."),
        ("Nodo Sur en Tránsito", "SouthNode", "#f97316", "☋", "Liberación de residuos entrópicos ancestrales y patrones del pasado.")
    ]

    @classmethod
    def calculate_transits(
        cls, 
        dt_utc: datetime, 
        lat_deg: float = 40.4168, 
        lon_deg: float = -3.7038, 
        use_topocentric: bool = True
    ) -> Dict[str, Any]:
        """
        Calcula las posiciones de los 13 cuerpos celestes activos en este instante exacto (dt_utc).
        """
        jd_t = CelestialMechanicsEngine.gregorian_to_jdn_utc(dt_utc)
        sol_lon = CelestialMechanicsEngine.solar_ecliptic_longitude_from_jd(jd_t)
        tierra_lon = (sol_lon + 180.0) % 360.0

        transits = {}

        # 1. Sol y Tierra
        mapped_sol = CelestialMechanicsEngine.map_longitude_to_key_and_line(sol_lon)
        mapped_sol.update({
            "nombre": "Sol en Tránsito",
            "cuerpo": "Sun",
            "simbolo": "☉",
            "color": "#fbbf24",
            "impacto": "Foco atencional consciente, irradiación vital colectiva y llamado evolutivo actual."
        })
        transits["Sol en Tránsito"] = mapped_sol

        mapped_tierra = CelestialMechanicsEngine.map_longitude_to_key_and_line(tierra_lon)
        mapped_tierra.update({
            "nombre": "Tierra en Tránsito",
            "cuerpo": "Earth",
            "simbolo": "♁",
            "color": "#10b981",
            "impacto": "Anclaje somático planetario, fricción de maduración y manifestación física inmediata."
        })
        transits["Tierra en Tránsito"] = mapped_tierra

        # 2. Luna (con corrección topocéntrica)
        luna_geo = CelestialMechanicsEngine.calculate_planetary_longitude(jd_t, "Moon")
        if use_topocentric:
            luna_lon = CelestialMechanicsEngine.calculate_lunar_topocentric_longitude(jd_t, luna_geo, lat_deg, lon_deg)
        else:
            luna_lon = luna_geo
        mapped_luna = CelestialMechanicsEngine.map_longitude_to_key_and_line(luna_lon)
        mapped_luna.update({
            "nombre": "Luna en Tránsito",
            "cuerpo": "Moon",
            "simbolo": "☽",
            "color": "#38bdf8",
            "impacto": "Pulso bio-ritmo celular, campo gravitatorio emocional y mareas psíquicas."
        })
        transits["Luna en Tránsito"] = mapped_luna

        # 3. Demás cuerpos planetarios
        for name, body_key, col, sym, impact in cls.TRANSIT_BODIES:
            if body_key in ("Sun", "Earth", "Moon"):
                continue
            lon = CelestialMechanicsEngine.calculate_planetary_longitude(jd_t, body_key)
            mapped = CelestialMechanicsEngine.map_longitude_to_key_and_line(lon)
            mapped.update({
                "nombre": name,
                "cuerpo": body_key,
                "simbolo": sym,
                "color": col,
                "impacto": impact
            })
            transits[name] = mapped

        return transits

    @classmethod
    def evaluate_transit_interference(
        cls, 
        natal_matrix: Dict[str, Any], 
        transits_dict: Dict[str, dict],
        dt_utc: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Diagnostica la interferencia de onda entre los tránsitos de hoy y los nodos natales del usuario:
        1. Ignición de Esferas Natales (Tránsito posicionado en el mismo Vórtice natal).
        2. Cierre de Canales Electromagnéticos en Vivo (Tránsito aporta el polo opuesto que le faltaba al usuario).
        3. Tensión Bipolar / Antípodas NOT en Tránsito (Tránsito a distancia de Hamming DH = 6 de una esfera natal).
        """
        natal_spheres = natal_matrix.get("spheres", {})
        
        # Mapeo de claves nativas: clave -> lista de nombres de esferas
        natal_keys_map: Dict[int, List[str]] = {}
        for s_name, s_data in natal_spheres.items():
            k = s_data.get("key", 0)
            if k > 0:
                natal_keys_map.setdefault(k, []).append(s_name)

        # Mapeo de tránsitos: clave -> lista de cuerpos
        transit_keys_map: Dict[int, List[str]] = {}
        for t_name, t_data in transits_dict.items():
            k = t_data.get("key", 0)
            if k > 0:
                transit_keys_map.setdefault(k, []).append(t_name)

        natal_unique_keys = set(natal_keys_map.keys())
        transit_unique_keys = set(transit_keys_map.keys())

        # 1. Ignición Directa de Esferas (El tránsito está en tu mismo vórtice)
        direct_ignitions = []
        for shared_k in sorted(natal_unique_keys.intersection(transit_unique_keys)):
            sph_list = natal_keys_map[shared_k]
            t_list = transit_keys_map[shared_k]
            k_data = CORE64_CATALOG.get(shared_k, {})
            ent = k_data.get("entropia", k_data.get("sombra", ""))
            coh = k_data.get("coherencia", k_data.get("don", ""))
            res = k_data.get("resonancia", k_data.get("siddhi", ""))
            
            # Especial atención si toca Trabajo de Vida (Sol Natal) o Evolución (Tierra Natal)
            is_core = any("Trabajo de Vida" in s or "Evolución" in s for s in sph_list)
            
            direct_ignitions.append({
                "key": shared_k,
                "natal_spheres": sph_list,
                "transit_bodies": t_list,
                "coherencia": coh,
                "entropia": ent,
                "resonancia": res,
                "is_core_axis": is_core,
                "title": f"Ignición en Vórtice Resonante {shared_k} ({coh})",
                "telemetry": (
                    f"El cuerpo celeste [{', '.join(t_list)}] transita hoy exactamente por tu Vórtice Resonante {shared_k} "
                    f"(asociada a tu {', '.join(sph_list)}). Demanda elevar la Coherencia de {coh} frente a la fricción de {ent}."
                )
            })

        # 2. Canales Electromagnéticos Cerrados en Vivo por Tránsito
        live_activated_channels = []
        for ka, kb, desc in NetworkSynastryEngine.CANONICAL_HARMONIC_CHANNELS:
            in_nat_a = ka in natal_unique_keys
            in_nat_b = kb in natal_unique_keys
            in_tr_a = ka in transit_unique_keys
            in_tr_b = kb in transit_unique_keys

            # El usuario sólo tiene ka y el cielo transita kb
            if in_nat_a and in_tr_b and not in_nat_b:
                live_activated_channels.append({
                    "channel_desc": desc,
                    "natal_key": ka,
                    "transit_key": kb,
                    "natal_spheres": natal_keys_map[ka],
                    "transit_bodies": transit_keys_map[kb],
                    "telemetry": (
                        f"⚡ Circuito Abierto en Vivo: Tu Vórtice natal V{ka} ({', '.join(natal_keys_map[ka])}) "
                        f"recibe inducción del cielo en K{kb} ({', '.join(transit_keys_map[kb])}). "
                        f"Canal cerrado: «{desc}». Pico de vitalidad e iniciativa en esta área."
                    )
                })
            # El usuario sólo tiene kb y el cielo transita ka
            elif in_nat_b and in_tr_a and not in_nat_a:
                live_activated_channels.append({
                    "channel_desc": desc,
                    "natal_key": kb,
                    "transit_key": ka,
                    "natal_spheres": natal_keys_map[kb],
                    "transit_bodies": transit_keys_map[ka],
                    "telemetry": (
                        f"⚡ Circuito Abierto en Vivo: Tu Vórtice natal V{kb} ({', '.join(natal_keys_map[kb])}) "
                        f"recibe inducción del cielo en K{ka} ({', '.join(transit_keys_map[ka])}). "
                        f"Canal cerrado: «{desc}». Pico de vitalidad e iniciativa en esta área."
                    )
                })

        # 3. Antípodas NOT en Tránsito (Hamming DH = 6)
        transit_antipodes = []
        for kn in natal_unique_keys:
            bits_n = CORE64_CATALOG.get(kn, {}).get("bits", "000000")
            not_bits_n = DiscreteParticleEngine.get_not_antipode(bits_n)
            for kt in transit_unique_keys:
                bits_t = CORE64_CATALOG.get(kt, {}).get("bits", "000000")
                if bits_t == not_bits_n:
                    data_n = CORE64_CATALOG.get(kn, {})
                    data_t = CORE64_CATALOG.get(kt, {})
                    transit_antipodes.append({
                        "natal_key": kn,
                        "transit_key": kt,
                        "natal_spheres": natal_keys_map[kn],
                        "transit_bodies": transit_keys_map[kt],
                        "risk": f"Tensión de balance polar: el tránsito en K{kt} ({data_t.get('entropia','')}) polariza a tu K{kn} ({data_n.get('entropia','')}).",
                        "calibration": f"Calibrar mediante la Coherencia de K{kn} ({data_n.get('coherencia','')}) sin proyectar reactividad hacia el entorno exterior."
                    })

        # Resumen de actividad climática electromagnética
        int_score = len(direct_ignitions) * 0.25 + len(live_activated_channels) * 0.20 + len(transit_antipodes) * 0.15
        clima_str = "Clima Electromagnético de Alta Activación" if int_score > 0.6 else "Clima Electromagnético Moderado / Estable"

        time_now = dt_utc if dt_utc else datetime.now(timezone.utc)
        return {
            "dt_utc": time_now.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "direct_ignitions": direct_ignitions,
            "live_activated_channels": live_activated_channels,
            "transit_antipodes": transit_antipodes,
            "weather_intensity": round(min(1.0, int_score), 2),
            "weather_summary": clima_str
        }


# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 6: INTERFAZ DE USUARIO PRINCIPAL (QT MONOLÍTICA)
# ══════════════════════════════════════════════════════════════════════════════

class HexaMatrixInteractiveApp(QMainWindow):
    """
    Ventana Principal de la Consola Bio-Informacional.
    Estructurada en pestañas temáticas, telemetría continua y co-creación con IA.
    """
    TIMEZONE_PRESETS = [
        ("UTC / GMT (Tiempo Universal Coordinado)", 0.0),
        ("UTC-3:00 • Argentina / Uruguay / Brasilia / Chile Verano", -3.0),
        ("UTC-4:00 • Bolivia / Chile Invierno / Paraguay / Rep. Dominicana / Miami Invierno", -4.0),
        ("UTC-5:00 • Colombia / Perú / Ecuador / Panamá / Cuba / NY Invierno", -5.0),
        ("UTC-6:00 • México Centro (CDMX, Guadalajara) / Centroamérica / CST", -6.0),
        ("UTC-7:00 • México Pacífico / Denver / MST", -7.0),
        ("UTC-8:00 • Los Ángeles / Tijuana / San Francisco / PST", -8.0),
        ("UTC+1:00 • España Peninsular / Madrid / París / Roma / Berlín (CET)", 1.0),
        ("UTC+2:00 • España Verano (CEST) / Europa Oriental / El Cairo", 2.0),
        ("UTC+3:00 • Moscú / Estambul / Riad", 3.0),
        ("Personalizado...", None)
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("⚡ HEXA-MATRIX: Plataforma de Co-Creación Bio-Informacional Humano & IA")
        self.resize(1380, 930)
        self.setMinimumSize(1100, 750)

        # Estado del sistema, localización geográfica y normalización temporal
        self.current_local_dt = datetime.now()
        try:
            sys_offset = datetime.now().astimezone().utcoffset().total_seconds() / 3600.0
        except Exception:
            sys_offset = 0.0
        self.utc_offset_hours = round(sys_offset, 2)
        self.current_utc = (self.current_local_dt - timedelta(hours=self.utc_offset_hours)).replace(tzinfo=timezone.utc)
        
        # Parámetros del Geo-Atlas Terrestre
        self.geo_country = "España"
        self.geo_city = "Madrid (Comunidad de Madrid)"
        self.geo_lat = 40.4168
        self.geo_lon = -3.7038
        self.use_topocentric = True
        self.matrix_mode = "cosmic_26"

        self.current_activation = CelestialMechanicsEngine.calculate_activation_matrix(
            self.current_utc,
            lat_deg=self.geo_lat,
            lon_deg=self.geo_lon,
            use_topocentric=self.use_topocentric,
            matrix_mode=self.matrix_mode
        )
        self.selected_sphere = "Propósito"
        self.current_filter_sequence = "Todas"
        
        # Estado del Motor de Tránsitos en Tiempo Real (Delta Dinámico Δt)
        self.transits_mode_active = False
        self.current_transits_data: Dict[str, dict] = {}
        self.current_interference: Dict[str, Any] = {}
        
        # Diccionario de widgets de las tarjetas de nodos
        self.sphere_card_widgets: Dict[str, QWidget] = {}
        self.card_labels: Dict[str, Tuple[QLabel, QLabel]] = {}
        
        self.active_worker = None
        self.active_system_prompt = OllamaTelemetryWorker.SYSTEM_PROMPT_V3
        self.available_models = ["qwen3.5:latest", "llama3.2:latest", "gemma4:latest"]
        self.available_embed_models = ["nomic-embed-text:latest", "mxbai-embed-large:latest"]

        # Estilo Global Bio-SciFi Glowing
        self._apply_global_style()
        self._detect_ollama_models()
        self._setup_ui()
        self._sync_celestial_data()

        # Timer para el reloj continuo
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._live_clock_tick)
        self.clock_timer.start(1000)


    def _apply_global_style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #060911;
            }
            QWidget {
                font-family: 'Segoe UI', 'Consolas', sans-serif;
                color: #e2e8f0;
                background-color: transparent;
            }
            QTabWidget::pane {
                border: 1px solid #1e293b;
                background: #090e18;
                border-radius: 10px;
                padding: 4px;
            }
            QTabBar::tab {
                background: #0f172a;
                color: #94a3b8;
                font-weight: bold;
                padding: 10px 22px;
                margin-right: 4px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                border: 1px solid #1e293b;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #1e293b, stop:1 #0f172a);
                color: #00f0ff;
                border-bottom: 2px solid #00f0ff;
            }
            QTabBar::tab:hover {
                color: #38bdf8;
                background: #1e293b;
            }
            QGroupBox {
                border: 1px solid #1e293b;
                border-radius: 8px;
                margin-top: 14px;
                padding-top: 14px;
                background-color: #0b111e;
                font-weight: bold;
                color: #38bdf8;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px;
                color: #00f0ff;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0284c7, stop:1 #0369a1);
                color: #ffffff;
                font-weight: bold;
                border: 1px solid #38bdf8;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0ea5e9, stop:1 #0284c7);
                border: 1px solid #7dd3fc;
            }
            QPushButton:pressed {
                background: #0369a1;
            }
            QPushButton#btnNeonGold {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #d97706, stop:1 #b45309);
                border: 1px solid #fbbf24;
                color: #ffffff;
            }
            QPushButton#btnNeonGold:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f59e0b, stop:1 #d97706);
            }
            QPushButton#btnNeonViolet {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7c3aed, stop:1 #6d28d9);
                border: 1px solid #a855f7;
                color: #ffffff;
            }
            QPushButton#btnNeonViolet:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #8b5cf6, stop:1 #7c3aed);
            }
            QLineEdit, QTextEdit, QDateTimeEdit, QComboBox, QSpinBox, QDoubleSpinBox {
                background-color: #0b1322;
                color: #f8fafc;
                border: 1px solid #1e293b;
                border-radius: 6px;
                padding: 6px;
                font-size: 13px;
                selection-background-color: #0284c7;
            }
            QLineEdit:focus, QTextEdit:focus, QDateTimeEdit:focus, QComboBox:focus {
                border: 1px solid #00f0ff;
                background-color: #0d182b;
            }
            QComboBox QAbstractItemView {
                background-color: #0b1322;
                color: #f8fafc;
                border: 1px solid #00f0ff;
                selection-background-color: #0284c7;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #1e293b;
                border-radius: 3px;
            }
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00f0ff, stop:1 #38bdf8);
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #f8fafc;
                border: 2px solid #00f0ff;
                width: 16px;
                margin-top: -5px;
                margin-bottom: -5px;
                border-radius: 8px;
            }
            QScrollBar:vertical {
                border: none;
                background: #090e18;
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #1e293b;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00f0ff;
            }
            QTableWidget {
                background-color: #080d17;
                border: 1px solid #1e293b;
                gridline-color: #1e293b;
                border-radius: 6px;
            }
            QHeaderView::section {
                background-color: #0f172a;
                color: #38bdf8;
                padding: 6px;
                border: 1px solid #1e293b;
                font-weight: bold;
            }
        """)

    def _detect_ollama_models(self):
        """Descubre los modelos de chat y de embeddings instalados localmente en Ollama."""
        self.ollama_online = False
        if not OLLAMA_AVAILABLE:
            return
        try:
            res = ollama.list()
            raw_models = getattr(res, "models", []) if not isinstance(res, dict) else res.get("models", [])
            chat_m = []
            embed_m = []
            for m in raw_models:
                m_name = getattr(m, "model", None) or (m.get("model", m.get("name", "")) if isinstance(m, dict) else str(m))
                details = getattr(m, "details", None) or (m.get("details", {}) if isinstance(m, dict) else None)
                fam = getattr(details, "family", "") if details and hasattr(details, "family") else (details.get("family", "") if isinstance(details, dict) else "")
                fams = getattr(details, "families", []) if details and hasattr(details, "families") else (details.get("families", []) if isinstance(details, dict) else [])
                all_fams = " ".join([fam or ""] + (fams or [])).lower()
                
                # Un modelo es de embeddings si contiene 'embed' en el nombre o en su familia arquitectónica
                if "embed" in m_name.lower() or "embed" in all_fams:
                    if m_name not in embed_m:
                        embed_m.append(m_name)
                else:
                    if m_name not in chat_m:
                        chat_m.append(m_name)
            
            if chat_m:
                self.available_models = chat_m
            if embed_m:
                self.available_embed_models = embed_m
            self.ollama_online = True
        except Exception:
            self.ollama_online = False

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(14, 12, 14, 12)
        main_layout.setSpacing(10)

        # ── Barra Superior (Header & Telemetría Rápida) ──
        header_frame = QFrame()
        header_frame.setStyleSheet("background: #090f1d; border: 1px solid #1e293b; border-radius: 10px; padding: 4px;")
        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(12, 8, 12, 8)

        title_box = QVBoxLayout()
        lbl_title = QLabel("⚡ HEXA-MATRIX")
        lbl_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #00f0ff; letter-spacing: 1px;")
        lbl_subtitle = QLabel("Plataforma de Co-Creación Bio-Informacional Humano & IA • Directiva v3.0 SOBERANA")
        lbl_subtitle.setStyleSheet("font-size: 11px; color: #94a3b8;")
        title_box.addWidget(lbl_title)
        title_box.addWidget(lbl_subtitle)
        header_layout.addLayout(title_box)

        header_layout.addStretch()

        # Telemetría en vivo del Sol Natal & Arco Kepler de 88°
        self.lbl_solar_telemetry = QLabel("☉ Sol Natal: --° | Punto Pre-natal (-88°): --°")
        self.lbl_solar_telemetry.setStyleSheet("font-family: Consolas; font-size: 12px; color: #fbbf24; background: #0f172a; padding: 6px 12px; border-radius: 6px; border: 1px solid #334155;")
        header_layout.addWidget(self.lbl_solar_telemetry)

        # Selector de Modo de Red Hologénica (26, 15, 22, 11 Nodos)
        header_layout.addWidget(QLabel("🌌 Red:"))
        self.combo_matrix_mode = QComboBox()
        self.combo_matrix_mode.addItem("🌌 Matriz Cósmica Total (26 Nodos)", "cosmic_26")
        self.combo_matrix_mode.addItem("🌿 Nodos del Entorno (15 Nodos)", "nodes")
        self.combo_matrix_mode.addItem("⚖️ Polaridades Duales NOT (22 Nodos)", "polar_not")
        self.combo_matrix_mode.addItem("💠 Circuito Base (11 Nodos)", "canonical")
        self.combo_matrix_mode.setFixedWidth(240)
        self.combo_matrix_mode.setStyleSheet("""
            QComboBox {
                font-weight: bold;
                color: #00f0ff;
                background-color: #0b1528;
                border: 1px solid #00f0ff;
                padding: 4px 8px;
                border-radius: 6px;
            }
        """)
        self.combo_matrix_mode.currentIndexChanged.connect(self._on_matrix_mode_changed)
        header_layout.addWidget(self.combo_matrix_mode)

        # Selector de Modelo Ollama
        header_layout.addWidget(QLabel("🤖 IA Model:"))
        self.combo_llm = QComboBox()
        self.combo_llm.addItems(self.available_models)
        self.combo_llm.setFixedWidth(145)
        header_layout.addWidget(self.combo_llm)

        header_layout.addWidget(QLabel("📡 Embeddings:"))
        self.combo_embed = QComboBox()
        self.combo_embed.addItems(self.available_embed_models)
        self.combo_embed.setFixedWidth(165)
        header_layout.addWidget(self.combo_embed)

        # Indicador de Estado de Ollama (Online / Offline)
        self.lbl_ollama_status = QLabel()
        if getattr(self, "ollama_online", False):
            self.lbl_ollama_status.setText("🟢 Ollama Online")
            self.lbl_ollama_status.setStyleSheet("font-size: 10px; font-weight: bold; color: #4ade80; background: #064e3b; padding: 4px 8px; border-radius: 4px; border: 1px solid #10b981;")
            self.lbl_ollama_status.setToolTip("Ollama detectado y operando localmente.")
        else:
            self.lbl_ollama_status.setText("⚠️ Ollama Offline: Modo Determinista")
            self.lbl_ollama_status.setStyleSheet("font-size: 10px; font-weight: bold; color: #fbbf24; background: #271e0c; padding: 4px 8px; border-radius: 4px; border: 1px solid #f59e0b;")
            self.lbl_ollama_status.setToolTip("Ollama no está en ejecución. La suite opera con motores algorítmicos y efemérides 100% deterministas.")
        header_layout.addWidget(self.lbl_ollama_status)

        main_layout.addWidget(header_frame)

        # ── Pestañas Principales ──
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        self._build_tab_mandala_solar()
        self._build_tab_discrete_geometry()
        self._build_tab_state_vector()
        self._build_tab_human_ai_cocreation()
        self._build_tab_holographic_radar()
        self._build_tab_network_synastry()
        self._build_tab_theory_and_directives()

        # ── Barra de Estado Inferior ──
        self.statusBar().setStyleSheet("background: #060911; color: #64748b; font-size: 11px; border-top: 1px solid #1e293b; padding: 4px;")
        if getattr(self, "ollama_online", False):
            self.statusBar().showMessage("Sistema Operativo en Coherencia de Fase • Ollama Online • Motor Cuántico Listo")
        else:
            self.statusBar().showMessage("Ollama Offline: Modo Algorítmico Determinista Activo • Efemérides y 64 Vórtices Resonantes 100% Operativos")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 1: BIO-MANDALA & EFEMÉRIDES SOLARES
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_mandala_solar(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        layout.setSpacing(14)

        # ── Panel Izquierdo: Visualizador de la Rueda Bio-Mandala ──
        left_box = QVBoxLayout()
        self.mandala_wheel = BioMandalaWheel()
        self.mandala_wheel.sphereSelected.connect(self._on_wheel_sphere_clicked)
        left_box.addWidget(self.mandala_wheel)
        
        lbl_hint = QLabel("✨ Clic en cualquier esfera o nodo del Mandala para enfocarla y sincronizar su telemetría.\n"
                          "🟢 Circuito Activación (4)  |  💖 Circuito Venus (4)  |  💎 Circuito Abundancia (3)")
        lbl_hint.setStyleSheet("font-size: 10px; color: #94a3b8; font-style: italic; background: #090e18; padding: 6px; border-radius: 4px; border: 1px solid #1e293b;")
        left_box.addWidget(lbl_hint)
        layout.addLayout(left_box, stretch=3)

        # ── Panel Derecho: Normalización de Huso Horario y las 11 Esferas ──
        right_box = QVBoxLayout()
        right_box.setSpacing(10)

        # 1. Grupo de Normalización de Huso Horario (Timezone, Geo-Atlas & UTC)
        ctrl_group = QGroupBox("Mecánica Celeste, Geo-Atlas & Normalización Temporal (UTC)")
        ctrl_layout = QVBoxLayout(ctrl_group)
        ctrl_layout.setSpacing(6)

        # Fila 1: Selector de Fecha y Hora Local
        date_row = QHBoxLayout()
        date_row.addWidget(QLabel("📅 Fecha & Hora Local:"))
        self.dt_local_picker = QDateTimeEdit()
        self.dt_local_picker.setDateTime(QDateTime.currentDateTime())
        self.dt_local_picker.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dt_local_picker.dateTimeChanged.connect(self._on_time_or_tz_changed)
        date_row.addWidget(self.dt_local_picker)
        ctrl_layout.addLayout(date_row)

        # Fila 2: Selector Rápido Geo-Atlas (País y Ciudad / Estado)
        geo_row = QHBoxLayout()
        geo_row.addWidget(QLabel("🌍 País:"))
        self.combo_country = QComboBox()
        for c_name in GEO_ATLAS.keys():
            self.combo_country.addItem(c_name)
        if self.geo_country in GEO_ATLAS:
            self.combo_country.setCurrentText(self.geo_country)
        self.combo_country.currentTextChanged.connect(self._on_country_changed)
        geo_row.addWidget(self.combo_country, stretch=2)

        geo_row.addWidget(QLabel("🏙️ Ciudad:"))
        self.combo_city = QComboBox()
        self._populate_cities_for_country(self.combo_country.currentText())
        self.combo_city.currentIndexChanged.connect(self._on_city_changed)
        geo_row.addWidget(self.combo_city, stretch=3)
        ctrl_layout.addLayout(geo_row)

        # Fila 3: Coordenadas Terrestres Manuales (Latitud / Longitud) + Checkbox Topocéntrico
        coords_row = QHBoxLayout()
        coords_row.addWidget(QLabel("🧭 Lat:"))
        self.spin_lat = QDoubleSpinBox()
        self.spin_lat.setRange(-90.0, 90.0)
        self.spin_lat.setDecimals(4)
        self.spin_lat.setSingleStep(0.1)
        self.spin_lat.setSuffix("°")
        self.spin_lat.setValue(self.geo_lat)
        self.spin_lat.valueChanged.connect(self._on_coords_changed)
        coords_row.addWidget(self.spin_lat)

        coords_row.addWidget(QLabel("Lon:"))
        self.spin_lon = QDoubleSpinBox()
        self.spin_lon.setRange(-180.0, 180.0)
        self.spin_lon.setDecimals(4)
        self.spin_lon.setSingleStep(0.1)
        self.spin_lon.setSuffix("°")
        self.spin_lon.setValue(self.geo_lon)
        self.spin_lon.valueChanged.connect(self._on_coords_changed)
        coords_row.addWidget(self.spin_lon)

        self.chk_topocentric = QCheckBox("🌙 Paralaje Lunar (Topocéntrico)")
        self.chk_topocentric.setChecked(self.use_topocentric)
        self.chk_topocentric.setToolTip("Ajusta la Luna (Esfera de la Atracción) según tu latitud y longitud terrestre exacta.")
        self.chk_topocentric.toggled.connect(self._on_topocentric_toggled)
        coords_row.addWidget(self.chk_topocentric)
        ctrl_layout.addLayout(coords_row)

        # Fila 4: Selector de Huso Horario (Preset + Offset numérico manual)
        tz_row = QHBoxLayout()
        tz_row.addWidget(QLabel("🌐 Huso Horario:"))
        self.combo_tz = QComboBox()
        for label, _ in self.TIMEZONE_PRESETS:
            self.combo_tz.addItem(label)
        # Preseleccionar el preset que coincida con el offset inicial del sistema
        matched_idx = len(self.TIMEZONE_PRESETS) - 1
        for i, (_, offset) in enumerate(self.TIMEZONE_PRESETS):
            if offset is not None and abs(offset - self.utc_offset_hours) < 0.01:
                matched_idx = i
                break
        self.combo_tz.blockSignals(True)
        self.combo_tz.setCurrentIndex(matched_idx)
        self.combo_tz.blockSignals(False)
        self.combo_tz.currentIndexChanged.connect(self._on_tz_combo_changed)
        tz_row.addWidget(self.combo_tz, stretch=3)

        tz_row.addWidget(QLabel("Offset:"))
        self.spin_utc_offset = QDoubleSpinBox()
        self.spin_utc_offset.setRange(-14.0, 14.0)
        self.spin_utc_offset.setSingleStep(0.5)
        self.spin_utc_offset.setSuffix(" h")
        self.spin_utc_offset.setValue(self.utc_offset_hours)
        self.spin_utc_offset.setFixedWidth(80)
        self.spin_utc_offset.valueChanged.connect(self._on_offset_spin_changed)
        tz_row.addWidget(self.spin_utc_offset, stretch=1)
        ctrl_layout.addLayout(tz_row)

        # Fila 5: Indicador Dinámico de Conversión Local ➔ UTC Normalizado
        self.lbl_tz_conversion = QLabel("🕒 Local: -- ➔ 🌐 UTC Normalizado: --")
        self.lbl_tz_conversion.setStyleSheet("font-family: Consolas; font-size: 11px; color: #00f0ff; background: #08111e; padding: 6px 10px; border-radius: 6px; border: 1px solid #0284c7;")
        ctrl_layout.addWidget(self.lbl_tz_conversion)

        # Fila 6: Botones de Acción Rápida (Ahora Local, Tránsitos en Vivo, Exportar Perfil)
        actions_row = QHBoxLayout()
        btn_now = QPushButton("⏱️ Ahora Local")
        btn_now.clicked.connect(self._set_current_now)
        actions_row.addWidget(btn_now)

        self.btn_toggle_transits = QPushButton("⚡ Modo Tránsitos (Δt Vivo): OFF")
        self.btn_toggle_transits.setCheckable(True)
        self.btn_toggle_transits.setStyleSheet("""
            QPushButton {
                background: #0f172a;
                border: 1px solid #fbbf24;
                color: #fbbf24;
                font-weight: bold;
                padding: 7px 12px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background: #1e293b;
            }
            QPushButton:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #d97706, stop:1 #b45309);
                border: 2px solid #fef08a;
                color: #ffffff;
            }
        """)
        self.btn_toggle_transits.setToolTip(
            "Activa el Salto Temporal: Superpone en tiempo real las 13 posiciones del cielo de hoy "
            "como un segundo anillo concéntrico sobre tu matriz natal y diagnostica la interferencia de onda electromagnética."
        )
        self.btn_toggle_transits.clicked.connect(self._toggle_transits_mode)
        actions_row.addWidget(self.btn_toggle_transits)

        btn_export = QPushButton("📥 Exportar Perfil")
        btn_export.setToolTip("Exporta el perfil completo de la red activa con sus coordenadas, entropía, coherencia y resonancia a JSON, Markdown y Portapapeles")
        btn_export.clicked.connect(self._export_full_profile)
        actions_row.addWidget(btn_export)

        ctrl_layout.addLayout(actions_row)
        right_box.addWidget(ctrl_group)

        # 2. Grupo de las Esferas Hologénicas
        self.spheres_group = QGroupBox("Red Hologénica: 26 Nodos Activos")
        spheres_layout = QVBoxLayout(self.spheres_group)
        spheres_layout.setSpacing(6)

        # Barra de Filtros de Secuencias
        filter_bar = QHBoxLayout()
        filter_bar.addWidget(QLabel("Filtrar Secuencia:"))
        
        self.btn_filter_all = QPushButton("🌟 Todos (26)")
        self.btn_filter_all.clicked.connect(lambda: self._filter_spheres_view("Todas"))
        filter_bar.addWidget(self.btn_filter_all)

        self.btn_filter_act = QPushButton("🟢 Activación (4)")
        self.btn_filter_act.clicked.connect(lambda: self._filter_spheres_view("Activación"))
        filter_bar.addWidget(self.btn_filter_act)

        self.btn_filter_ven = QPushButton("💖 Venus (4)")
        self.btn_filter_ven.clicked.connect(lambda: self._filter_spheres_view("Venus"))
        filter_bar.addWidget(self.btn_filter_ven)

        self.btn_filter_per = QPushButton("💎 Abundancia (3)")
        self.btn_filter_per.clicked.connect(lambda: self._filter_spheres_view("Abundancia"))
        filter_bar.addWidget(self.btn_filter_per)

        self.btn_filter_env = QPushButton("🌿 Entorno (4)")
        self.btn_filter_env.clicked.connect(lambda: self._filter_spheres_view("Entorno"))
        self.btn_filter_env.setVisible(False)
        filter_bar.addWidget(self.btn_filter_env)

        self.btn_filter_not = QPushButton("⚖️ Polaridad NOT (11)")
        self.btn_filter_not.clicked.connect(lambda: self._filter_spheres_view("Polaridad NOT"))
        self.btn_filter_not.setVisible(False)
        filter_bar.addWidget(self.btn_filter_not)

        self.btn_filter_trans = QPushButton("🌌 Transpersonal (7)")
        self.btn_filter_trans.clicked.connect(lambda: self._filter_spheres_view("Transpersonal"))
        self.btn_filter_trans.setVisible(False)
        filter_bar.addWidget(self.btn_filter_trans)

        spheres_layout.addLayout(filter_bar)

        # Contenedor Scrolleable de las Tarjetas
        self.spheres_scroll = QScrollArea()
        self.spheres_scroll.setWidgetResizable(True)
        self.spheres_scroll.setStyleSheet("background: transparent; border: none;")

        self.cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self.cards_container)
        self.cards_layout.setContentsMargins(2, 2, 2, 2)
        self.cards_layout.setSpacing(8)

        self.sphere_card_widgets = {}
        self.card_labels = {}

        for sph_name, meta in SPHERES_METADATA.items():
            card_widget = self._create_sphere_card(sph_name, meta)
            self.cards_layout.addWidget(card_widget)
            self.sphere_card_widgets[sph_name] = card_widget

        self.cards_layout.addStretch()
        self.spheres_scroll.setWidget(self.cards_container)
        spheres_layout.addWidget(self.spheres_scroll)

        right_box.addWidget(self.spheres_group, stretch=1)

        # 3. Interferencia de Onda Electromagnética en Tiempo Real (Δt Tránsitos)
        self.transits_box = QGroupBox("⚡ Interferencia de Onda Electromagnética en Tiempo Real (Δt Tránsitos)")
        transits_box_layout = QVBoxLayout(self.transits_box)
        transits_box_layout.setContentsMargins(8, 8, 8, 8)
        transits_box_layout.setSpacing(6)

        # Barra superior de la tarjeta de clima de tránsitos
        tb_header_row = QHBoxLayout()
        tb_header_row.setSpacing(6)
        self.lbl_transit_status_pill = QLabel("Modo Tránsitos inactivo")
        self.lbl_transit_status_pill.setStyleSheet("font-size: 11px; font-weight: bold; color: #94a3b8; background: #0f172a; padding: 3px 8px; border-radius: 4px; border: 1px solid #1e293b;")
        tb_header_row.addWidget(self.lbl_transit_status_pill)
        tb_header_row.addStretch()

        self.btn_expand_transits = QPushButton("⛶ Expandir")
        self.btn_expand_transits.setToolTip("Alternar entre vista compacta y extendida del reporte de tránsitos")
        self.btn_expand_transits.setStyleSheet("font-size: 10px; padding: 3px 8px; background: #0f172a; border: 1px solid #475569; color: #cbd5e1; border-radius: 4px;")
        self.btn_expand_transits.clicked.connect(self._toggle_transit_viewer_height)
        tb_header_row.addWidget(self.btn_expand_transits)

        btn_modal_transits = QPushButton("📖 Lectura Completa")
        btn_modal_transits.setToolTip("Abrir visor inmersivo de lectura completa en ventana dedicada")
        btn_modal_transits.setStyleSheet("font-size: 10px; padding: 3px 8px; background: #0f172a; border: 1px solid #a855f7; color: #c084fc; border-radius: 4px;")
        btn_modal_transits.clicked.connect(self._open_transits_fullscreen_modal)
        tb_header_row.addWidget(btn_modal_transits)

        btn_copy_transits = QPushButton("📋 Copiar")
        btn_copy_transits.setToolTip("Copia el reporte completo de interferencia de tránsitos al portapapeles")
        btn_copy_transits.setStyleSheet("font-size: 10px; padding: 3px 8px; background: #0f172a; border: 1px solid #38bdf8; color: #38bdf8; border-radius: 4px;")
        btn_copy_transits.clicked.connect(self._copy_transits_report)
        tb_header_row.addWidget(btn_copy_transits)

        btn_close_box = QPushButton("✕")
        btn_close_box.setToolTip("Cerrar recuadro y desactivar Modo Tránsitos en Vivo")
        btn_close_box.setStyleSheet("font-size: 11px; font-weight: bold; padding: 3px 7px; background: #1e293b; border: 1px solid #475569; color: #f87171; border-radius: 4px;")
        btn_close_box.clicked.connect(lambda: (self.btn_toggle_transits.setChecked(False), self._toggle_transits_mode()))
        tb_header_row.addWidget(btn_close_box)
        transits_box_layout.addLayout(tb_header_row)

        # Visor de texto enriquecido con scroll autónomo y formato HTML bioluminiscente
        self.txt_transit_weather = QTextBrowser()
        self.txt_transit_weather.setOpenExternalLinks(False)
        self.txt_transit_weather.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.txt_transit_weather.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.txt_transit_weather.setMinimumHeight(160)
        self.txt_transit_weather.setMaximumHeight(260)
        self.transit_viewer_expanded = False
        self.txt_transit_weather.setStyleSheet("""
            QTextBrowser {
                background-color: #080f1e;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                border-left: 4px solid #334155;
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 12px;
                line-height: 1.5;
            }
            QScrollBar:vertical {
                border: none;
                background: #090e18;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #334155;
                min-height: 25px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00f0ff;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        self.txt_transit_weather.setHtml(
            "<p style='color: #94a3b8; font-style: italic;'>"
            "Presiona el botón <b>«⚡ Modo Tránsitos (Δt Vivo)»</b> en la barra de controles para calcular las 13 posiciones del cielo de hoy "
            "y diagnosticar las interferencias de onda en tiempo real sobre tu matriz natal."
            "</p>"
        )
        transits_box_layout.addWidget(self.txt_transit_weather)
        right_box.addWidget(self.transits_box)
        self.transits_box.setVisible(False)  # Oculto por defecto hasta que se active el Modo Tránsitos

        # 4. Diagnóstico de Fronteras Difusas (Fuzzy Cusp)
        fuzzy_group = QGroupBox("Diagnóstico de Fronteras Difusas (Fuzzy Cusp)")
        fuzzy_layout = QVBoxLayout(fuzzy_group)
        self.lbl_fuzzy_status = QLabel("Estado cuántico: Evaluando...")
        self.lbl_fuzzy_status.setStyleSheet("font-size: 11px; color: #a855f7; background: #0f172a; padding: 6px; border-radius: 6px;")
        fuzzy_layout.addWidget(self.lbl_fuzzy_status)
        right_box.addWidget(fuzzy_group)

        # 5. Explorador Continuo Eclíptico (Opcional)
        slider_box = QHBoxLayout()
        self.lbl_slider_val = QLabel("Explorador Eclíptico Libre: 0.00°")
        self.lbl_slider_val.setStyleSheet("color: #00f0ff; font-weight: bold; font-size: 10px;")
        self.solar_slider = QSlider(Qt.Horizontal)
        self.solar_slider.setRange(0, 35999)
        self.solar_slider.valueChanged.connect(self._on_slider_solar_moved)
        slider_box.addWidget(self.lbl_slider_val)
        slider_box.addWidget(self.solar_slider)
        right_box.addLayout(slider_box)

        layout.addLayout(right_box, stretch=3)

        self.tabs.addTab(tab, "01. 🌐 Bio-Mandala & Efemérides")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 2: GEOMETRÍA DISCRETA DE 64 CLAVES & PUENTES
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_discrete_geometry(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        layout.setSpacing(14)

        # Columna Izquierda: Inspector de Partícula (Hexagrama de 6 bits y Trigramas)
        left_box = QVBoxLayout()
        left_box.setSpacing(12)

        picker_row = QHBoxLayout()
        picker_row.addWidget(QLabel("Seleccionar Vórtice Resonante (Operador 6-Bit):"))
        self.spin_key_select = QSpinBox()
        self.spin_key_select.setRange(1, 64)
        self.spin_key_select.setValue(31)
        self.spin_key_select.valueChanged.connect(self._on_key_selected)
        picker_row.addWidget(self.spin_key_select)
        
        picker_row.addWidget(QLabel("Línea:"))
        self.spin_line_select = QSpinBox()
        self.spin_line_select.setRange(1, 6)
        self.spin_line_select.setValue(1)
        self.spin_line_select.valueChanged.connect(self._on_key_selected)
        picker_row.addWidget(self.spin_line_select)
        left_box.addLayout(picker_row)

        # Tarjeta de Morfología
        morph_group = QGroupBox("Morfología del Operador (Vórtice Resonante de 6 Bits)")
        morph_layout = QVBoxLayout(morph_group)

        self.lbl_key_title = QLabel("VÓRTICE RESONANTE 31: ARROGANCIA + LIDERAZGO + HUMILDAD")
        self.lbl_key_title.setStyleSheet("font-size: 14px; font-weight: bold; color: #00f0ff;")
        morph_layout.addWidget(self.lbl_key_title)

        self.lbl_bits_display = QLabel("BITS: 0 0 1 1 1 0")
        self.lbl_bits_display.setStyleSheet("font-family: Consolas; font-size: 18px; font-weight: bold; color: #fbbf24; letter-spacing: 4px; padding: 6px 0;")
        morph_layout.addWidget(self.lbl_bits_display)

        # Trigramas
        self.lbl_trigram_lower = QLabel("Trigrama Inferior (Bits 1,2,3): Montaña (Gèn ☶) - Sustrato bio-somático")
        self.lbl_trigram_lower.setStyleSheet("font-size: 11px; color: #a7f3d0; background: #0f172a; padding: 6px; border-radius: 4px;")
        morph_layout.addWidget(self.lbl_trigram_lower)

        self.lbl_trigram_upper = QLabel("Trigrama Superior (Bits 4,5,6): Lago (Duì ☱) - Interfaz ambiental y proyección")
        self.lbl_trigram_upper.setStyleSheet("font-size: 11px; color: #93c5fd; background: #0f172a; padding: 6px; border-radius: 4px;")
        morph_layout.addWidget(self.lbl_trigram_upper)

        # Antípoda Inversa (NOT) & Clúster Bioquímico
        self.lbl_pair_info = QLabel("Antípoda Inversa (Inversor Lógico NOT): Vórtice Resonante 41 [110001]")
        self.lbl_pair_info.setStyleSheet("font-size: 12px; color: #f472b6; font-weight: bold; margin-top: 4px;")
        morph_layout.addWidget(self.lbl_pair_info)

        self.lbl_ring_info = QLabel(f"Clúster Bioquímico: {resolve_cluster_name(CORE64_CATALOG.get(31, {}).get('ring', ''))}")
        self.lbl_ring_info.setStyleSheet("font-size: 12px; color: #c084fc;")
        morph_layout.addWidget(self.lbl_ring_info)

        # 5 Propiedades de la Partícula
        self.txt_particle_properties = QTextEdit()
        self.txt_particle_properties.setReadOnly(True)
        self.txt_particle_properties.setMaximumHeight(160)
        morph_layout.addWidget(self.txt_particle_properties)

        left_box.addWidget(morph_group)
        layout.addLayout(left_box, stretch=3)

        # Columna Derecha: Simulador de Puentes Multipartícula
        right_box = QVBoxLayout()
        right_box.setSpacing(12)

        bridge_ctrl = QGroupBox("Simulador de Puentes e Interferencia (2 o Más Vórtices Resonantes)")
        bridge_layout = QVBoxLayout(bridge_ctrl)

        sel_row = QHBoxLayout()
        sel_row.addWidget(QLabel("Partícula A (Emisor):"))
        self.spin_bridge_a = QSpinBox()
        self.spin_bridge_a.setRange(1, 64)
        self.spin_bridge_a.setValue(31)
        self.spin_bridge_a.valueChanged.connect(self._update_bridge_simulator)
        sel_row.addWidget(self.spin_bridge_a)

        sel_row.addWidget(QLabel("Partícula B (Receptor):"))
        self.spin_bridge_b = QSpinBox()
        self.spin_bridge_b.setRange(1, 64)
        self.spin_bridge_b.setValue(41)
        self.spin_bridge_b.valueChanged.connect(self._update_bridge_simulator)
        sel_row.addWidget(self.spin_bridge_b)
        bridge_layout.addLayout(sel_row)

        self.bridge_view = MultiParticleBridgeView()
        bridge_layout.addWidget(self.bridge_view)

        self.txt_bridge_report = QTextEdit()
        self.txt_bridge_report.setReadOnly(True)
        self.txt_bridge_report.setMaximumHeight(140)
        bridge_layout.addWidget(self.txt_bridge_report)

        right_box.addWidget(bridge_ctrl)
        layout.addLayout(right_box, stretch=3)

        self.tabs.addTab(tab, "02. 🔷 Geometría de Vórtices Resonantes")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 3: VECTOR DE ESTADO DINÁMICO S = [E, C, R]
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_state_vector(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        layout.setSpacing(16)

        # Panel Izquierdo: Controles de los 3 Deslizadores de Estado
        left_box = QVBoxLayout()
        left_box.setSpacing(14)

        slider_group = QGroupBox("Calibración del Vector de Estado S = [E, C, R] ∈ [0, 1]")
        slider_layout = QVBoxLayout(slider_group)

        # E (Entropía)
        self.lbl_e_val = QLabel("E (Entropía): 0.35 - Fricción somática y rumiación reactiva")
        self.lbl_e_val.setStyleSheet("color: #f87171; font-weight: bold;")
        self.slider_e = QSlider(Qt.Horizontal)
        self.slider_e.setRange(0, 100)
        self.slider_e.setValue(35)
        self.slider_e.valueChanged.connect(self._on_state_vector_changed)
        slider_layout.addWidget(self.lbl_e_val)
        slider_layout.addWidget(self.slider_e)

        # C (Coherencia)
        self.lbl_c_val = QLabel("C (Coherencia): 0.75 - Capacidad de estructurar artefactos y límites")
        self.lbl_c_val.setStyleSheet("color: #38bdf8; font-weight: bold;")
        self.slider_c = QSlider(Qt.Horizontal)
        self.slider_c.setRange(0, 100)
        self.slider_c.setValue(75)
        self.slider_c.valueChanged.connect(self._on_state_vector_changed)
        slider_layout.addWidget(self.lbl_c_val)
        slider_layout.addWidget(self.slider_c)

        # R (Resonancia)
        self.lbl_r_val = QLabel("R (Resonancia): 0.80 - Reposo basal de mínima acción y silencio sin culpa")
        self.lbl_r_val.setStyleSheet("color: #c084fc; font-weight: bold;")
        self.slider_r = QSlider(Qt.Horizontal)
        self.slider_r.setRange(0, 100)
        self.slider_r.setValue(80)
        self.slider_r.valueChanged.connect(self._on_state_vector_changed)
        slider_layout.addWidget(self.lbl_r_val)
        slider_layout.addWidget(self.slider_r)

        # Botones de presets rápidos
        preset_row = QHBoxLayout()
        btn_preset_shadow = QPushButton("Simular Colapso Entrópico (E➔1, C➔0)")
        btn_preset_shadow.clicked.connect(lambda: self._set_state_preset(0.95, 0.10, 0.20))
        preset_row.addWidget(btn_preset_shadow)

        btn_preset_bypass = QPushButton("Simular Spiritual Bypass (R➔1, C➔0)")
        btn_preset_bypass.clicked.connect(lambda: self._set_state_preset(0.20, 0.10, 0.95))
        preset_row.addWidget(btn_preset_bypass)

        btn_preset_gift = QPushButton("Simular Coherencia Integrada (C➔1, R➔1)")
        btn_preset_gift.setObjectName("btnNeonGold")
        btn_preset_gift.clicked.connect(lambda: self._set_state_preset(0.25, 0.90, 0.85))
        preset_row.addWidget(btn_preset_gift)
        slider_layout.addLayout(preset_row)

        left_box.addWidget(slider_group)

        # Tarjeta de Prescripción Somática y Acción Requerida
        presc_group = QGroupBox("Prescripción Somática & Acción Requerida")
        presc_layout = QVBoxLayout(presc_group)
        self.lbl_presc_action = QLabel("Cargando acción de fase...")
        self.lbl_presc_action.setWordWrap(True)
        self.lbl_presc_action.setStyleSheet("font-size: 13px; color: #f8fafc; background: #0f172a; padding: 12px; border-radius: 8px; border-left: 4px solid #00f0ff;")
        presc_layout.addWidget(self.lbl_presc_action)
        left_box.addWidget(presc_group)

        left_box.addStretch()
        layout.addLayout(left_box, stretch=3)

        # Panel Derecho: Visualizador Tacómetro Bio-Métrico
        right_box = QVBoxLayout()
        self.bio_gauge = StateVectorBioGauge()
        right_box.addWidget(self.bio_gauge)
        
        lbl_formula = QLabel("Fórmula: Rendimiento Biológico = (C · R) / (E + ε)\nε = 0.05 (Constante de regularización bio-física)")
        lbl_formula.setStyleSheet("font-family: Consolas; font-size: 11px; color: #94a3b8; background: #0f172a; padding: 8px; border-radius: 6px;")
        right_box.addWidget(lbl_formula)

        layout.addLayout(right_box, stretch=2)

        self.tabs.addTab(tab, "03. ⚡ Vector de Estado [E,C,R]")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 4: CO-CREACIÓN HUMANO-IA (EL MAPA DE SITUACIÓN)
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_human_ai_cocreation(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(12)

        splitter = QSplitter(Qt.Horizontal)

        # ── Columna Izquierda: Protocolo de Ingesta (Hardware, Firmware, Runtime) ──
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)

        # Capa 1: HARDWARE (Inmutable / Calculado)
        hw_group = QGroupBox("Capa 1: HARDWARE (Inmutable / Calculado)")
        hw_layout = QGridLayout(hw_group)

        hw_layout.addWidget(QLabel("Nodo a Diagnosticar:"), 0, 0)
        self.combo_active_sphere = QComboBox()
        self.combo_active_sphere.addItems(list(SPHERES_METADATA.keys()))
        self.combo_active_sphere.currentTextChanged.connect(self._on_cocreation_sphere_changed)
        hw_layout.addWidget(self.combo_active_sphere, 0, 1)

        self.lbl_hw_key_badge = QLabel("Vórtice Resonante: 31.1 (Topología '001110')")
        self.lbl_hw_key_badge.setStyleSheet("font-family: Consolas; font-weight: bold; color: #00f0ff;")
        hw_layout.addWidget(self.lbl_hw_key_badge, 1, 0, 1, 2)

        self.lbl_hw_impact = QLabel("Área de impacto: Anclaje somático, inmunidad, cimientos biológicos.")
        self.lbl_hw_impact.setStyleSheet("font-size: 11px; color: #94a3b8;")
        hw_layout.addWidget(self.lbl_hw_impact, 2, 0, 1, 2)

        # 1. Auditoría de Interfaz por Puerto / Capa (.1 a .6)
        self.lbl_hw_line_interface = QLabel("🔌 Puerto de Interfaz: Evaluando...")
        self.lbl_hw_line_interface.setStyleSheet("font-size: 11px; color: #38bdf8; background: #0c1829; padding: 5px 8px; border-radius: 4px; border: 1px solid #0369a1;")
        self.lbl_hw_line_interface.setWordWrap(True)
        hw_layout.addWidget(self.lbl_hw_line_interface, 3, 0, 1, 2)

        # 2. Auditoría de la Antípoda Inversa (NOT)
        self.lbl_hw_not_pair = QLabel("⚖️ Antípoda Inversa NOT: Evaluando...")
        self.lbl_hw_not_pair.setStyleSheet("font-family: Consolas; font-size: 11px; color: #f472b6; background: #1a0f21; padding: 5px 8px; border-radius: 4px; border: 1px solid #831843;")
        self.lbl_hw_not_pair.setWordWrap(True)
        hw_layout.addWidget(self.lbl_hw_not_pair, 4, 0, 1, 2)
        left_layout.addWidget(hw_group)

        # Capa 2: FIRMWARE (Semilla Algorítmica / Por Defecto)
        fw_group = QGroupBox("Capa 2: FIRMWARE (Semilla Algorítmica / Por Defecto)")
        fw_layout = QVBoxLayout(fw_group)
        self.lbl_fw_name = QLabel("Operador de Síntesis: Coherencia de Liderazgo")
        self.lbl_fw_name.setStyleSheet("font-weight: bold; color: #fbbf24;")
        fw_layout.addWidget(self.lbl_fw_name)

        self.lbl_fw_function = QLabel("Función Orquestadora: Conducción basada en datos y hechos; absorbe la entropía reactiva y reposa en resonancia basal.")
        self.lbl_fw_function.setStyleSheet("font-size: 11px; color: #cbd5e1; background: #0f172a; padding: 6px; border-radius: 4px;")
        fw_layout.addWidget(self.lbl_fw_function)

        self.lbl_fw_not_audit = QLabel("🔍 Auditoría de Contrapeso NOT: Evaluando...")
        self.lbl_fw_not_audit.setStyleSheet("font-size: 10px; color: #f472b6; font-style: italic; background: #130919; padding: 4px; border-radius: 4px;")
        self.lbl_fw_not_audit.setWordWrap(True)
        fw_layout.addWidget(self.lbl_fw_not_audit)
        left_layout.addWidget(fw_group)

        # Capa 3: RUNTIME (Activo / Input Humano)
        rt_group = QGroupBox("Capa 3: RUNTIME (Activo / Input Humano)")
        rt_layout = QVBoxLayout(rt_group)

        rt_layout.addWidget(QLabel("Input A: La Escena (Situación real de fricción, conflicto o proyecto actual):"))
        self.txt_runtime_scene = QTextEdit()
        self.txt_runtime_scene.setPlaceholderText("Describe la escena concreta donde experimentas tensión o estás decidiendo un rumbo de acción...")
        self.txt_runtime_scene.setMaximumHeight(85)
        rt_layout.addWidget(self.txt_runtime_scene)

        rt_layout.addWidget(QLabel("Input B: Mi Coherencia Co-Creada (Protocolo conductual tangible para esta escena):"))
        self.txt_runtime_gift = QTextEdit()
        self.txt_runtime_gift.setPlaceholderText("¿Cuál es tu protocolo de acción concreto? Define límites, reglas de decisión, artefactos o código...")
        self.txt_runtime_gift.setMaximumHeight(75)
        rt_layout.addWidget(self.txt_runtime_gift)

        btn_run_telemetry = QPushButton("🚀 Ejecutar Telemetría de Fase y Generar Mapa de Situación")
        btn_run_telemetry.setObjectName("btnNeonViolet")
        btn_run_telemetry.setStyleSheet("font-size: 13px; padding: 10px;")
        btn_run_telemetry.clicked.connect(self._run_ai_telemetry)
        rt_layout.addWidget(btn_run_telemetry)

        left_layout.addWidget(rt_group)
        left_layout.addStretch()
        splitter.addWidget(left_widget)

        # ── Columna Derecha: Output de Telemetría AI & Exit-Gate Soberano ──
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)

        out_group = QGroupBox("Mapa de Situación e Informe de Telemetría de Fase (IA)")
        out_layout = QVBoxLayout(out_group)

        self.txt_ai_output = QTextEdit()
        self.txt_ai_output.setReadOnly(True)
        self.txt_ai_output.setPlaceholderText("Aquí aparecerá el diagnóstico estructurado de la IA: Estado de Fase, Auditoría de la Coherencia Co-Creada, Flujo del Puente, Acción de Calibración y el Exit-Gate...")
        out_layout.addWidget(self.txt_ai_output)

        # Barra de Botones del Diario de Evolución
        journal_bar = QHBoxLayout()
        btn_save_journal = QPushButton("📓 Guardar en Diario de Evolución")
        btn_save_journal.setToolTip("Archiva esta telemetría, fecha, escena y acción física en tu bitácora de evolución personal")
        btn_save_journal.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #059669, stop:1 #047857); border: 1px solid #10b981; color: #ffffff; font-weight: bold; padding: 7px 12px;")
        btn_save_journal.clicked.connect(self._save_to_evolution_journal)
        journal_bar.addWidget(btn_save_journal)

        btn_view_journal = QPushButton("📂 Ver / Exportar Bitácora")
        btn_view_journal.setToolTip("Abre el visualizador de tu Diario de Evolución para revisar o exportar tus sesiones pasadas")
        btn_view_journal.setStyleSheet("background: #0f172a; border: 1px solid #38bdf8; color: #38bdf8; font-weight: bold; padding: 7px 12px;")
        btn_view_journal.clicked.connect(self._open_evolution_journal_dialog)
        journal_bar.addWidget(btn_view_journal)

        btn_copy_ai = QPushButton("📋 Copiar Telemetría")
        btn_copy_ai.setToolTip("Copia el texto del informe generado al portapapeles")
        btn_copy_ai.clicked.connect(self._copy_ai_output)
        journal_bar.addWidget(btn_copy_ai)
        out_layout.addLayout(journal_bar)

        # Exit-Gate interactivo
        exit_box = QFrame()
        exit_box.setStyleSheet("background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 8px;")
        exit_layout = QVBoxLayout(exit_box)
        
        lbl_exit_title = QLabel("⛔ PROTOCOLO DE SALIDA SOBERANA (EXIT-GATE)")
        lbl_exit_title.setStyleSheet("font-weight: bold; color: #f43f5e;")
        exit_layout.addWidget(lbl_exit_title)

        exit_row = QHBoxLayout()
        self.txt_action_60m = QLineEdit()
        self.txt_action_60m.setPlaceholderText("Acción física inmediata que ejecutaré en los próximos 60 minutos...")
        exit_row.addWidget(self.txt_action_60m)

        btn_close_session = QPushButton("Cerrar Sesión & Desconectar")
        btn_close_session.setStyleSheet("background: #be123c; border-color: #f43f5e;")
        btn_close_session.clicked.connect(self._exit_gate_sovereign_close)
        exit_row.addWidget(btn_close_session)
        exit_layout.addLayout(exit_row)

        out_layout.addWidget(exit_box)
        right_layout.addWidget(out_group)
        splitter.addWidget(right_widget)

        splitter.setSizes([500, 650])
        layout.addWidget(splitter)

        self.tabs.addTab(tab, "04. 🤖 Co-Creación IA & Mapa")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 5: RADAR HOLOGRÁFICO DE EMBEDDINGS (OLLAMA AI)
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_holographic_radar(self):
        tab = QWidget()
        layout = QHBoxLayout(tab)
        layout.setSpacing(14)

        # Panel Izquierdo: Visualizador de Radar Polar 2D
        left_box = QVBoxLayout()
        self.radar_view = HolographicRadarView()
        left_box.addWidget(self.radar_view)
        
        btn_recalc_embeds = QPushButton("🔄 Sincronizar Embeddings con Ollama")
        btn_recalc_embeds.setObjectName("btnNeonGold")
        btn_recalc_embeds.clicked.connect(self._recalculate_embeddings)
        left_box.addWidget(btn_recalc_embeds)
        layout.addLayout(left_box, stretch=3)

        # Panel Derecho: Tabla de Resonancia Semántica
        right_box = QVBoxLayout()
        res_group = QGroupBox("Top Vórtices Resonantes en Resonancia Semántica con tu Situación Actual")
        res_layout = QVBoxLayout(res_group)

        self.table_semantic = QTableWidget()
        self.table_semantic.setColumnCount(4)
        self.table_semantic.setHorizontalHeaderLabels(["Vórtice Resonante", "Coherencia (C)", "Clúster Bioquímico", "Similitud Cos"])
        self.table_semantic.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        res_layout.addWidget(self.table_semantic)

        self.lbl_embed_info = QLabel("Cálculo activo mediante vectores de alta dimensión proyectados en el plano latente.")
        self.lbl_embed_info.setStyleSheet("font-size: 11px; color: #94a3b8;")
        res_layout.addWidget(self.lbl_embed_info)

        right_box.addWidget(res_group)
        layout.addLayout(right_box, stretch=3)

        self.tabs.addTab(tab, "05. 📡 Radar de Embeddings")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 6: DIRECTIVAS DE SISTEMA & MANUAL TEÓRICO
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_theory_and_directives(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        sub_tabs = QTabWidget()
        sub_tabs.setStyleSheet("""
            QTabBar::tab {
                background: #0b111e;
                color: #94a3b8;
                padding: 7px 18px;
                font-size: 11px;
                border-radius: 6px;
                border: 1px solid #1e293b;
                margin-right: 4px;
            }
            QTabBar::tab:selected {
                background: #1e293b;
                color: #00f0ff;
                border: 1px solid #00f0ff;
                font-weight: bold;
            }
        """)

        # ── SUB-PESTAÑA 1: EDITOR INTERACTIVO DE DIRECTIVAS DEL SISTEMA (SYSTEM PROMPT IA) ──
        subtab_directives = QWidget()
        dir_layout = QVBoxLayout(subtab_directives)
        dir_layout.setContentsMargins(8, 8, 8, 8)
        dir_layout.setSpacing(8)

        # Barra superior con estado y herramientas de guardado/carga
        tools_layout = QHBoxLayout()
        tools_layout.setSpacing(8)

        lbl_title = QLabel("🛠️ Mapa de Sistema & Directivas IA (Interactivo y Vivo):")
        lbl_title.setStyleSheet("font-weight: bold; color: #38bdf8; font-size: 12px;")
        tools_layout.addWidget(lbl_title)

        self.lbl_prompt_sync_status = QLabel("🟢 Directivas Activas Sincronizadas")
        self.lbl_prompt_sync_status.setStyleSheet("color: #4ade80; font-size: 11px; font-weight: bold;")
        tools_layout.addWidget(self.lbl_prompt_sync_status)

        tools_layout.addStretch()

        btn_apply = QPushButton("💾 Aplicar a la IA")
        btn_apply.setToolTip("Guarda y activa inmediatamente estas directivas en el motor de telemetría de Ollama.")
        btn_apply.clicked.connect(self._apply_system_directives)
        tools_layout.addWidget(btn_apply)

        btn_load = QPushButton("📂 Cargar (.md / .txt)")
        btn_load.setToolTip("Cargar un archivo de directivas personalizadas desde el disco.")
        btn_load.clicked.connect(self._load_system_directives_from_file)
        tools_layout.addWidget(btn_load)

        btn_save = QPushButton("💾 Guardar como...")
        btn_save.setToolTip("Guardar las directivas actuales en un archivo Markdown.")
        btn_save.clicked.connect(self._save_system_directives_to_file)
        tools_layout.addWidget(btn_save)

        btn_reset = QPushButton("🔄 Restaurar Soberano (v3.0)")
        btn_reset.setToolTip("Restaura el System Prompt soberano v3.0 de HEXA-MATRIX CORE.")
        btn_reset.clicked.connect(self._reset_system_directives)
        tools_layout.addWidget(btn_reset)

        dir_layout.addLayout(tools_layout)

        # Explicación de interactividad y dinamismo
        lbl_desc = QLabel(
            "💡 Este editor contiene el mapa ontológico, reglas de auditoría de conducta y formato de salida del sistema. "
            "Al ser HEXA-MATRIX un sistema interactivo y en evolución, puedes editar axiomas, añadir tus propias reglas, "
            "ajustar el protocolo de fase o redefinir el exit-gate. Cualquier cambio se inyecta directamente "
            "al modelo de IA seleccionado para telemetría."
        )
        lbl_desc.setWordWrap(True)
        lbl_desc.setStyleSheet("font-size: 11px; color: #94a3b8; background: #0b111e; padding: 6px 10px; border-radius: 6px; border: 1px solid #1e293b;")
        dir_layout.addWidget(lbl_desc)

        # Editor de texto editable
        self.txt_system_directives = QTextEdit()
        self.txt_system_directives.setReadOnly(False)
        self.txt_system_directives.setStyleSheet("""
            QTextEdit {
                font-family: Consolas, 'Courier New', monospace;
                font-size: 12px;
                color: #e2e8f0;
                background-color: #080d17;
                border: 1px solid #1e293b;
                border-radius: 6px;
                padding: 10px;
                selection-background-color: #0284c7;
            }
            QTextEdit:focus {
                border: 1px solid #00f0ff;
            }
        """)
        self.txt_system_directives.setPlainText(self.active_system_prompt)
        self.txt_system_directives.textChanged.connect(self._on_system_directives_text_changed)
        dir_layout.addWidget(self.txt_system_directives)

        sub_tabs.addTab(subtab_directives, "🛠️ Editor de Directivas del Sistema (System Prompt IA)")

        # ── SUB-PESTAÑA 2: MANUAL TEÓRICO & FUNDAMENTOS MATEMÁTICOS ──
        subtab_theory = QWidget()
        th_layout = QVBoxLayout(subtab_theory)
        th_layout.setContentsMargins(8, 8, 8, 8)

        txt_theory = QTextEdit()
        txt_theory.setReadOnly(True)
        txt_theory.setStyleSheet("""
            QTextEdit {
                font-family: Consolas, monospace;
                font-size: 12px;
                color: #e2e8f0;
                background: #080d17;
                border: 1px solid #1e293b;
                border-radius: 6px;
                padding: 10px;
            }
        """)

        theory_content = """╔══════════════════════════════════════════════════════════════════════════════════════╗
║ FUNDAMENTOS MATEMÁTICOS, CELESTES Y FÍSICOS IMPLEMENTADOS                            ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

1. NORMALIZACIÓN TEMPORAL (UTC) Y EFEMÉRIDES JPL/VSOP87:
   - Coordenada cósmica absoluta: UTC = Hora Local - Offset de Huso Horario.
   - Tiempo Juliano Astronómico continuo (JD y Siglo Juliano T).
   - Longitud eclíptica tropical aparente del Sol: λ_odot(t_0) ∈ [0°, 360°).
   - Eje Consciente / Natal: Sol Natal y Tierra Natal (+180°).

2. RETROCESO DE ARCO SOLAR EXACTO DE 88° (SEGUNDA LEY DE KEPLER):
   - El Sol no viaja a velocidad angular constante a lo largo del año (órbita elíptica de la Tierra).
   - Raíz resuelta deterministamente por método de Newton-Raphson tal que:
     λ_odot(t_design) = (λ_odot(t_0) - 88.0°) mod 360°.
   - Eje Inconsciente / Pre-natal: Sol Prenatal (-88° Arc Shift) y Tierra Prenatal (+180°).
   - Días de retroceso Kepler: ~88 días reales en tiempo continuo.

3. CORRECCIÓN DE PARALAJE LUNAR TOPOCÉNTRICO (ESFERA DE LA ATRACCIÓN):
   - La Luna orbita a sólo ~384,400 km de la Tierra, lo que genera un ángulo de paralaje de hasta ~0.95° (57' de arco)
     entre el centro de la Tierra (geocéntrico) y la superficie física del observador (topocéntrico).
   - Dado que una Línea / Puerto del Vórtice Resonante mide exactamente 0.9375° (56' 15"), el paralaje topocéntrico determina la Línea real:
     Δλ_Luna = - π_luna · cos(ϕ) · sin(HA)
     donde ϕ es la latitud geográfica y HA es el Ángulo Horario Local derivado del Tiempo Sidéreo de Greenwich (GMST).

4. CUANTIZACIÓN MODULAR EN EL HEXA-MANDALA (MATRIZ RADIAL ECLÍPTICA):
   - Anclado en θ_0 ≈ 302.0° (aprox 2° Acuario, Vórtice 41 codón de inicio de metionina).
   - Tamaño de Vórtice: Δ = 360° / 64 = 5.625° = 5° 37' 30".
   - Tamaño de Línea / Puerto: δ = 5.625° / 6 = 0.9375° = 56' 15".
   - Fronteras Difusas: Si dist(cúspide) < 0.1°, superposición ponderada de estados cuánticos adyacentes.

5. TOPOLOGÍA BINARIA DE 6 BITS Y ANTÍPODAS INVERSAS (NOT):
   - Cada uno de los 64 Vórtices Resonantes posee una firma binaria de 6 bits (Líneas 1 a 6 = Bits 0 a 5).
   - Antípoda Inversa (Inversor Lógico NOT): Complemento booleano bit a bit (~K) a distancia de Hamming DH = 6.
     Ejemplo: Vórtice 1 (000000) <-> Vórtice 2 (111111); Vórtice 31 <-> Vórtice 41.

6. LA ECUACIÓN DE ESTADO COTIDIANA (TERMODINÁMICA DE SISTEMAS ABIERTOS):
   - Vector S = [E, C, R] ∈ [0, 1]
   - E (Entropía): Fase Entrópica, fricción somática y rumiación reactiva.
   - C (Coherencia): Fase Coherente, capacidad directiva de traducir tensión en artefacto estructurado.
   - R (Resonancia): Fase Resonante, reposo de mínima acción sin culpa, disipación y superconducción.
   - Rendimiento Biológico = (C · R) / (E + ε), con ε = 0.05.
"""
        txt_theory.setPlainText(theory_content)
        th_layout.addWidget(txt_theory)

        sub_tabs.addTab(subtab_theory, "📐 Manual Teórico & Fundamentos Físicos")

        layout.addWidget(sub_tabs)
        self.tabs.addTab(tab, "07. 📖 Directivas & Manual")

    def _on_system_directives_text_changed(self):
        """Notifica visualmente si hay cambios pendientes de confirmación formal en el editor."""
        self.active_system_prompt = self.txt_system_directives.toPlainText()
        self.lbl_prompt_sync_status.setText("🟢 Sincronizado en tiempo real con IA")
        self.lbl_prompt_sync_status.setStyleSheet("color: #4ade80; font-size: 11px; font-weight: bold;")

    def _apply_system_directives(self):
        """Aplica y valida formalmente el contenido del editor como System Prompt de IA."""
        self.active_system_prompt = self.txt_system_directives.toPlainText()
        self.lbl_prompt_sync_status.setText("🟢 Directivas Activas Sincronizadas")
        self.lbl_prompt_sync_status.setStyleSheet("color: #4ade80; font-size: 11px; font-weight: bold;")
        self.statusBar().showMessage("✅ Directivas del Sistema aplicadas exitosamente para el motor de IA.")
        QMessageBox.information(
            self,
            "Directivas Aplicadas",
            "✅ Las Directivas del Sistema se han actualizado en memoria.\n\n"
            "Cualquier consulta de telemetría lanzada en la pestaña de Co-Creación "
            "empleará este nuevo mapa ontológico."
        )

    def _reset_system_directives(self):
        """Restaura el System Prompt soberano v3.0."""
        reply = QMessageBox.question(
            self,
            "Restaurar Directivas",
            "¿Deseas restaurar las directivas soberanas originales (v3.0)? Se perderán los cambios no guardados.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.txt_system_directives.setPlainText(OllamaTelemetryWorker.SYSTEM_PROMPT_V3)
            self._apply_system_directives()

    def _load_system_directives_from_file(self):
        """Carga un archivo de directivas (.md o .txt) desde disco."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Cargar Directivas del Sistema",
            "",
            "Archivos de Texto (*.md *.txt);;Todos los Archivos (*.*)"
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.txt_system_directives.setPlainText(content)
                self._apply_system_directives()
                QMessageBox.information(self, "Cargado", f"Directivas cargadas con éxito desde:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error de Lectura", f"No se pudo cargar el archivo:\n{str(e)}")

    def _save_system_directives_to_file(self):
        """Guarda las directivas actuales en un archivo Markdown o Texto en disco."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Directivas del Sistema",
            "directivas_hexa_matrix_sistema.md",
            "Markdown (*.md);;Texto Plano (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.txt_system_directives.toPlainText())
                QMessageBox.information(self, "Guardado", f"Directivas guardadas exitosamente en:\n{file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error al Guardar", f"No se pudo guardar el archivo:\n{str(e)}")

    # ──────────────────────────────────────────────────────────────────────────
    # PESTAÑA 7: ACOPLAMIENTO DE RED MULTIPARTÍCULA (SINASTRÍA BIOFÍSICA)
    # ──────────────────────────────────────────────────────────────────────────
    def _build_tab_network_synastry(self):
        tab = QWidget()
        main_layout = QVBoxLayout(tab)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(10)

        # ── Panel Superior: Configuración Dual de Perfiles (Sujeto Alfa vs Sujeto Beta) ──
        config_frame = QFrame()
        config_frame.setStyleSheet("background: #090f1d; border: 1px solid #1e293b; border-radius: 10px; padding: 6px;")
        config_layout = QHBoxLayout(config_frame)
        config_layout.setSpacing(14)

        # ── Sujeto Alfa ──
        group_alpha = QGroupBox("🔵 Sujeto Alfa (Nodo Emisor / Operador A)")
        layout_a = QVBoxLayout(group_alpha)
        layout_a.setSpacing(6)

        row_a_name = QHBoxLayout()
        row_a_name.addWidget(QLabel("Nombre / ID:"))
        self.txt_syn_name_a = QLineEdit("Sujeto Alfa")
        row_a_name.addWidget(self.txt_syn_name_a)
        btn_load_current_a = QPushButton("📥 Cargar Mi Perfil Actual")
        btn_load_current_a.setToolTip("Copia los parámetros de fecha, hora y ubicación configurados en la Pestaña 1")
        btn_load_current_a.clicked.connect(self._syn_load_alpha_from_current)
        row_a_name.addWidget(btn_load_current_a)
        layout_a.addLayout(row_a_name)

        row_a_dt = QHBoxLayout()
        row_a_dt.addWidget(QLabel("Fecha & Hora Local:"))
        self.dt_syn_a = QDateTimeEdit()
        self.dt_syn_a.setDateTime(self.dt_local_picker.dateTime())
        self.dt_syn_a.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        row_a_dt.addWidget(self.dt_syn_a)
        row_a_dt.addWidget(QLabel("Offset:"))
        self.spin_syn_tz_a = QDoubleSpinBox()
        self.spin_syn_tz_a.setRange(-14.0, 14.0)
        self.spin_syn_tz_a.setSingleStep(0.5)
        self.spin_syn_tz_a.setSuffix(" h")
        self.spin_syn_tz_a.setValue(self.utc_offset_hours)
        row_a_dt.addWidget(self.spin_syn_tz_a)
        layout_a.addLayout(row_a_dt)

        row_a_geo = QHBoxLayout()
        row_a_geo.addWidget(QLabel("Lat:"))
        self.spin_syn_lat_a = QDoubleSpinBox()
        self.spin_syn_lat_a.setRange(-90.0, 90.0)
        self.spin_syn_lat_a.setValue(self.geo_lat)
        row_a_geo.addWidget(self.spin_syn_lat_a)
        row_a_geo.addWidget(QLabel("Lon:"))
        self.spin_syn_lon_a = QDoubleSpinBox()
        self.spin_syn_lon_a.setRange(-180.0, 180.0)
        self.spin_syn_lon_a.setValue(self.geo_lon)
        row_a_geo.addWidget(self.spin_syn_lon_a)
        self.chk_syn_topo_a = QCheckBox("Topocéntrico")
        self.chk_syn_topo_a.setChecked(True)
        row_a_geo.addWidget(self.chk_syn_topo_a)
        layout_a.addLayout(row_a_geo)

        config_layout.addWidget(group_alpha, stretch=1)

        # ── Sujeto Beta ──
        group_beta = QGroupBox("🟡 Sujeto Beta (Nodo Receptor / Pareja / Socio B)")
        layout_b = QVBoxLayout(group_beta)
        layout_b.setSpacing(6)

        row_b_name = QHBoxLayout()
        row_b_name.addWidget(QLabel("Nombre / ID:"))
        self.txt_syn_name_b = QLineEdit("Socio / Pareja Beta")
        row_b_name.addWidget(self.txt_syn_name_b)
        layout_b.addLayout(row_b_name)

        row_b_dt = QHBoxLayout()
        row_b_dt.addWidget(QLabel("Fecha & Hora Local:"))
        self.dt_syn_b = QDateTimeEdit()
        # Fecha de ejemplo predeterminada: 1996-08-15 08:30:00
        self.dt_syn_b.setDateTime(QDateTime.fromString("1996-08-15 08:30:00", "yyyy-MM-dd HH:mm:ss"))
        self.dt_syn_b.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        row_b_dt.addWidget(self.dt_syn_b)
        row_b_dt.addWidget(QLabel("Offset:"))
        self.spin_syn_tz_b = QDoubleSpinBox()
        self.spin_syn_tz_b.setRange(-14.0, 14.0)
        self.spin_syn_tz_b.setSingleStep(0.5)
        self.spin_syn_tz_b.setSuffix(" h")
        self.spin_syn_tz_b.setValue(1.0) # Madrid / CET
        row_b_dt.addWidget(self.spin_syn_tz_b)
        layout_b.addLayout(row_b_dt)

        row_b_geo = QHBoxLayout()
        row_b_geo.addWidget(QLabel("Lat:"))
        self.spin_syn_lat_b = QDoubleSpinBox()
        self.spin_syn_lat_b.setRange(-90.0, 90.0)
        self.spin_syn_lat_b.setValue(40.4168)
        row_b_geo.addWidget(self.spin_syn_lat_b)
        row_b_geo.addWidget(QLabel("Lon:"))
        self.spin_syn_lon_b = QDoubleSpinBox()
        self.spin_syn_lon_b.setRange(-180.0, 180.0)
        self.spin_syn_lon_b.setValue(-3.7038)
        row_b_geo.addWidget(self.spin_syn_lon_b)
        self.chk_syn_topo_b = QCheckBox("Topocéntrico")
        self.chk_syn_topo_b.setChecked(True)
        row_b_geo.addWidget(self.chk_syn_topo_b)
        layout_b.addLayout(row_b_geo)

        config_layout.addWidget(group_beta, stretch=1)

        # ── Columna de Ejecución del Acoplamiento ──
        run_box = QVBoxLayout()
        run_box.setSpacing(6)
        run_box.addWidget(QLabel("Resolución de Red:"))
        self.combo_syn_mode = QComboBox()
        self.combo_syn_mode.addItem("🌌 Matriz Cósmica Total (26 Nodos)", "cosmic_26")
        self.combo_syn_mode.addItem("🌿 Nodos del Entorno (15 Nodos)", "nodes")
        self.combo_syn_mode.addItem("⚖️ Polaridades Duales NOT (22 Nodos)", "polar_not")
        self.combo_syn_mode.addItem("💠 Circuito Base (11 Nodos)", "canonical")
        run_box.addWidget(self.combo_syn_mode)

        self.btn_syn_calculate = QPushButton("⚡ Calcular Acoplamiento de Red")
        self.btn_syn_calculate.setObjectName("btnNeonGold")
        self.btn_syn_calculate.setStyleSheet("font-size: 13px; font-weight: bold; padding: 10px 14px;")
        self.btn_syn_calculate.clicked.connect(self._on_synastry_calc_clicked)
        run_box.addWidget(self.btn_syn_calculate)

        config_layout.addLayout(run_box)
        main_layout.addWidget(config_frame)

        # ── Cuerpo Central: Splitter Horizontal con Visualizador Gráfico y Diagnósticos ──
        splitter = QSplitter(Qt.Horizontal)

        # Panel Izquierdo: Grafo Bioluminiscente de Acoplamiento
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        self.synastry_graph_view = NetworkCouplingGraphView()
        left_layout.addWidget(self.synastry_graph_view)
        splitter.addWidget(left_widget)

        # Panel Derecho: Pestañas de Diagnóstico y Telemetría IA
        right_tabs = QTabWidget()

        # Sub-pestaña 1: Resumen Operativo de Puentes
        tab_summary = QWidget()
        tab_sum_layout = QVBoxLayout(tab_summary)
        
        self.lbl_syn_header = QLabel("Resonancia Relacional η_red: -- | Canales Cerrados: --")
        self.lbl_syn_header.setStyleSheet("font-family: Consolas; font-size: 12px; color: #00f0ff; background: #08111e; padding: 8px; border-radius: 6px; border: 1px solid #0284c7;")
        tab_sum_layout.addWidget(self.lbl_syn_header)

        self.table_syn_channels = QTableWidget()
        self.table_syn_channels.setColumnCount(4)
        self.table_syn_channels.setHorizontalHeaderLabels(["Tipo de Enlace", "Vórtices Acoplados", "Proveedores (A ⟷ B)", "Dinámica de Flujo"])
        self.table_syn_channels.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tab_sum_layout.addWidget(self.table_syn_channels)

        right_tabs.addTab(tab_summary, "🔗 Canales & Puentes Inducidos")

        # Sub-pestaña 2: Protocolo de Co-Creación IA & Delegación de Equipo
        tab_ai_syn = QWidget()
        tab_ai_layout = QVBoxLayout(tab_ai_syn)
        tab_ai_layout.setSpacing(8)

        ai_ctrl_row = QHBoxLayout()
        btn_run_syn_ai = QPushButton("🤖 Generar Protocolo de Delegación & Compatibilidad (IA)")
        btn_run_syn_ai.setObjectName("btnNeonViolet")
        btn_run_syn_ai.clicked.connect(self._run_synastry_ai_telemetry)
        ai_ctrl_row.addWidget(btn_run_syn_ai)

        btn_copy_syn = QPushButton("📋 Copiar Protocolo")
        btn_copy_syn.clicked.connect(self._copy_synastry_output)
        ai_ctrl_row.addWidget(btn_copy_syn)
        tab_ai_layout.addLayout(ai_ctrl_row)

        self.txt_syn_ai_output = QTextEdit()
        self.txt_syn_ai_output.setReadOnly(True)
        self.txt_syn_ai_output.setPlaceholderText("El informe estructurado de Sinastría Biofísica y Dinámica Operativa aparecerá aquí:\n- Canales Electromagnéticos Cerrados\n- Cortocircuitos Entrópicos & Fricciones en Espejo\n- Reglas Innegociables de Convivencia y Delegación\n- Protocolo de Trabajo Conjunto para los próximos 60 minutos...")
        tab_ai_layout.addWidget(self.txt_syn_ai_output)

        right_tabs.addTab(tab_ai_syn, "🧠 Auditoría IA & Protocolo de Delegación")

        splitter.addWidget(right_tabs)
        splitter.setSizes([600, 600])
        main_layout.addWidget(splitter, stretch=1)

        self.tabs.addTab(tab, "06. 🔗 Acoplamiento de Red")

    def _syn_load_alpha_from_current(self):
        """Copia el perfil actualmente configurado en la Pestaña 1 a los campos del Sujeto Alfa."""
        self.dt_syn_a.setDateTime(self.dt_local_picker.dateTime())
        self.spin_syn_tz_a.setValue(self.spin_utc_offset.value())
        self.spin_syn_lat_a.setValue(self.spin_lat.value())
        self.spin_syn_lon_a.setValue(self.spin_lon.value())
        self.chk_syn_topo_a.setChecked(self.chk_topocentric.isChecked())
        self.txt_syn_name_a.setText("Mi Perfil Actual")
        self.statusBar().showMessage("✅ Perfil actual importado exitosamente a Sujeto Alfa.")

    def _on_synastry_calc_clicked(self):
        """Calcula el acoplamiento biofísico entre Sujeto Alfa y Sujeto Beta."""
        mode = self.combo_syn_mode.currentData()

        # Cálculo de Matriz A
        py_local_a = self.dt_syn_a.dateTime().toPython()
        utc_a = (py_local_a - timedelta(hours=self.spin_syn_tz_a.value())).replace(tzinfo=timezone.utc)
        matrix_a = CelestialMechanicsEngine.calculate_activation_matrix(
            utc_a,
            lat_deg=self.spin_syn_lat_a.value(),
            lon_deg=self.spin_syn_lon_a.value(),
            use_topocentric=self.chk_syn_topo_a.isChecked(),
            matrix_mode=mode
        )

        # Cálculo de Matriz B
        py_local_b = self.dt_syn_b.dateTime().toPython()
        utc_b = (py_local_b - timedelta(hours=self.spin_syn_tz_b.value())).replace(tzinfo=timezone.utc)
        matrix_b = CelestialMechanicsEngine.calculate_activation_matrix(
            utc_b,
            lat_deg=self.spin_syn_lat_b.value(),
            lon_deg=self.spin_syn_lon_b.value(),
            use_topocentric=self.chk_syn_topo_b.isChecked(),
            matrix_mode=mode
        )

        name_a = self.txt_syn_name_a.text().strip() or "Sujeto Alfa"
        name_b = self.txt_syn_name_b.text().strip() or "Sujeto Beta"

        syn_res = NetworkSynastryEngine.analyze_coupling(matrix_a, matrix_b, name_a=name_a, name_b=name_b)

        # Actualizar vista gráfica
        self.synastry_graph_view.set_coupling_data(matrix_a, matrix_b, syn_res)
        self.current_synastry_res = syn_res
        self.current_matrix_a = matrix_a
        self.current_matrix_b = matrix_b

        # Actualizar tabla y etiquetas
        eta = syn_res["relational_resonance_index"]
        closed = syn_res["closed_channels"]
        antipodes = syn_res["antipode_crossings"]
        comps = syn_res["companionship_nodes"]
        clusters = syn_res["shared_clusters"]

        self.lbl_syn_header.setText(
            f"⚡ Resonancia Relacional η_red: {eta*100:.1f}% | "
            f"Canales Inducidos: {len(closed)} | "
            f"Ejes NOT: {len(antipodes)} | "
            f"Nodos en Espejo: {len(comps)} | "
            f"Clústeres Bioquímicos: {len(clusters)}"
        )

        # Llenar tabla de canales
        all_links = []
        for c in closed:
            all_links.append((c["type"], f"K{c['key_a']} ⟷ K{c['key_b']}", f"{c['provider_a']} + {c['provider_b']}", c["description"]))
        for ant in antipodes:
            all_links.append(("Antípoda Inversa NOT", f"K{ant['key_a']} ⟷ K{ant['key_b']}", f"{name_a} ⟷ {name_b}", ant["risk"]))
        for comp in comps:
            all_links.append(("Compañerismo en Espejo", f"K{comp['key']} ⟷ K{comp['key']}", f"Ambos en K{comp['key']}", f"Don: {comp['coherencia']} | Sombra: {comp['entropia']}"))

        self.table_syn_channels.setRowCount(len(all_links))
        for r_idx, (l_type, l_keys, l_prov, l_desc) in enumerate(all_links):
            self.table_syn_channels.setItem(r_idx, 0, QTableWidgetItem(l_type))
            self.table_syn_channels.setItem(r_idx, 1, QTableWidgetItem(l_keys))
            self.table_syn_channels.setItem(r_idx, 2, QTableWidgetItem(l_prov))
            self.table_syn_channels.setItem(r_idx, 3, QTableWidgetItem(l_desc))

        self.statusBar().showMessage(f"✅ Acoplamiento de Red calculado: η_red = {eta*100:.1f}% ({len(closed)} canales inductivos)")

    def _run_synastry_ai_telemetry(self):
        """Genera el protocolo de delegación operativa y compatibilidad relacional mediante IA u Ollama."""
        if not hasattr(self, "current_synastry_res") or not self.current_synastry_res:
            self._on_synastry_calc_clicked()

        syn = self.current_synastry_res
        name_a = syn.get("name_a", "Sujeto Alfa")
        name_b = syn.get("name_b", "Sujeto Beta")
        eta = syn.get("relational_resonance_index", 0.0)
        closed = syn.get("closed_channels", [])
        antipodes = syn.get("antipode_crossings", [])
        comps = syn.get("companionship_nodes", [])
        clusters = syn.get("shared_clusters", [])

        payload = {
            "protocolo": "Acoplamiento de Red Multipartícula (Sinastría Biofísica)",
            "sujeto_alfa": name_a,
            "sujeto_beta": name_b,
            "indice_resonancia_relacional": eta,
            "canales_cerrados": closed,
            "antipodas_cruzadas_not": antipodes,
            "nodos_espejo_compartidos": comps,
            "clusters_bioquimicos": clusters
        }

        syn_system_prompt = """# SYSTEM DIRECTIVE: PROTOCOLO DE SINASTRÍA BIOFÍSICA & DINÁMICA DE EQUIPOS (HEXA-MATRIX)
Operas como el auditor biofísico de acoplamiento de red en HEXA-MATRIX.
Tu misión es diagnosticar la interacción termodinámica entre Sujeto Alfa y Sujeto Beta:
1. CANALES ELECTROMAGNÉTICOS CERRADOS: Explica cómo la conjunción de ambas personas crea circuitos que ninguno posee en soledad y cómo delegar tareas operativas en ese canal sin fricción.
2. CORTOCIRCUITOS ENTRÓPICOS & RIESGOS EN ESPEJO: Dónde chocarán si caen en Fase Entrópica (rumiación, evasión o parálisis).
3. LÍMITES OPERATIVOS & REGLAS INNEGOCIABLES DE RELACIÓN: 3 directivas conductuales claras para no agotarse mutuamente.
4. PLAN DE CO-CREACIÓN PARA LOS PRÓXIMOS 60 MINUTOS: Una acción tangible y medible que ambos pueden coordinar de inmediato.
Evita clichés románticos o esotéricos pasivos. Habla desde la cibernética de sistemas, física de información y gestión de energía."""

        model_name = self.combo_llm.currentText()
        self.txt_syn_ai_output.setPlainText("⏳ Analizando acoplamiento electromagnético y calculando protocolo de delegación con IA...")
        self.statusBar().showMessage(f"🤖 Ejecutando auditoría de sinastría con modelo {model_name}...")

        self.syn_worker = OllamaTelemetryWorker(model_name, json.dumps(payload, indent=2, ensure_ascii=False), system_prompt=syn_system_prompt)
        self.syn_worker.finished_success.connect(self._on_synastry_ai_finished)
        self.syn_worker.start()

    def _on_synastry_ai_finished(self, text: str):
        self.txt_syn_ai_output.setPlainText(text)
        self.statusBar().showMessage("✅ Protocolo de Acoplamiento de Red IA generado exitosamente.")

    def _copy_synastry_output(self):
        text = self.txt_syn_ai_output.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self.statusBar().showMessage("📋 Protocolo de Sinastría copiado al portapapeles.")

    # ──────────────────────────────────────────────────────────────────────────
    # MÉTODOS DE CONTROL, SINCRONIZACIÓN Y EVENTOS
    # ──────────────────────────────────────────────────────────────────────────
    def _toggle_transits_mode(self):
        """Activa o desactiva la superposición del Salto Temporal (Motor de Tránsitos en Tiempo Real Δt)."""
        self.transits_mode_active = self.btn_toggle_transits.isChecked()
        if self.transits_mode_active:
            self.transits_box.setVisible(True)
            self.btn_toggle_transits.setText("⚡ Modo Tránsitos (Δt Vivo): ON")
            self.lbl_transit_status_pill.setText("🟢 Tránsitos en Vivo ACTIVOS")
            self.lbl_transit_status_pill.setStyleSheet("font-size: 11px; font-weight: bold; color: #4ade80; background: #064e3b; padding: 3px 8px; border-radius: 4px; border: 1px solid #10b981;")
            self._update_transits_and_interference()
            self.statusBar().showMessage("⚡ Modo Tránsitos en Tiempo Real ACTIVADO • Anillo concéntrico e interferencias operativas en vivo.")
        else:
            self.transits_box.setVisible(False)
            self.btn_toggle_transits.setText("⚡ Modo Tránsitos (Δt Vivo): OFF")
            self.lbl_transit_status_pill.setText("Modo Tránsitos inactivo")
            self.lbl_transit_status_pill.setStyleSheet("font-size: 11px; font-weight: bold; color: #94a3b8; background: #0f172a; padding: 3px 8px; border-radius: 4px; border: 1px solid #1e293b;")
            self.mandala_wheel.set_transits_data({}, active=False)
            if getattr(self, 'transit_viewer_expanded', False):
                self._toggle_transit_viewer_height()
            self.statusBar().showMessage("Modo Tránsitos desactivado • Retorno a interfaz habitual completa.")

    def _update_transits_and_interference(self):
        """Calcula los tránsitos celestes actuales y evalúa la interferencia de onda con los 26 nodos natales."""
        now_utc = datetime.now(timezone.utc)
        self.current_transits_data = RealTimeTransitEngine.calculate_transits(
            now_utc,
            lat_deg=self.geo_lat,
            lon_deg=self.geo_lon,
            use_topocentric=self.use_topocentric
        )
        self.mandala_wheel.set_transits_data(self.current_transits_data, active=True)

        # Evaluar interferencias
        interf = RealTimeTransitEngine.evaluate_transit_interference(
            self.current_activation,
            self.current_transits_data,
            dt_utc=now_utc
        )
        self.current_interference = interf

        # Generar telemetría visual formateada para la tarjeta de clima de tránsitos
        ignitions = interf.get("direct_ignitions", [])
        channels = interf.get("live_activated_channels", [])
        antipodes = interf.get("transit_antipodes", [])

        lines = [
            f"<div style='font-size: 13px; font-weight: bold; color: #fbbf24; margin-bottom: 4px;'>"
            f"⚡ {interf.get('weather_summary', 'Clima Operativo')} &nbsp; "
            f"<span style='color: #38bdf8; font-size: 11px;'>(Intensidad: {interf.get('weather_intensity', 0)*100:.0f}%)</span>"
            f"</div>",
            f"<div style='font-family: Consolas; font-size: 11px; color: #94a3b8; margin-bottom: 8px;'>"
            f"🌐 Coordenada Temporal: {interf.get('dt_utc')}"
            f"</div>"
        ]

        if ignitions:
            lines.append("<div style='margin-top: 6px; color: #f87171; font-weight: bold;'>🔥 Ignición Directa de Nodos Natales:</div>")
            for ig in ignitions:
                lines.append(
                    f"<div style='margin-left: 8px; margin-bottom: 4px; color: #e2e8f0;'>"
                    f"• <b style='color: #00f0ff;'>K{ig['key']} ({ig['coherencia']}):</b> {ig['telemetry']}"
                    f"</div>"
                )

        if channels:
            lines.append("<div style='margin-top: 6px; color: #38bdf8; font-weight: bold;'>⚡ Circuitos Electromagnéticos Cerrados en Vivo:</div>")
            for ch in channels:
                lines.append(
                    f"<div style='margin-left: 8px; margin-bottom: 4px; color: #e2e8f0;'>"
                    f"• {ch['telemetry']}"
                    f"</div>"
                )

        if antipodes:
            lines.append("<div style='margin-top: 6px; color: #f472b6; font-weight: bold;'>⚖️ Tensiones de Calibración NOT:</div>")
            for ant in antipodes:
                lines.append(
                    f"<div style='margin-left: 8px; margin-bottom: 4px; color: #e2e8f0;'>"
                    f"• <b style='color: #fbbf24;'>K{ant['natal_key']} ⟷ K{ant['transit_key']}:</b> {ant['risk']} "
                    f"<span style='color: #a7f3d0;'><i>{ant['calibration']}</i></span>"
                    f"</div>"
                )

        if not ignitions and not channels and not antipodes:
            lines.append("<div style='color: #94a3b8; font-style: italic;'>El cielo en este instante no produce igniciones directas sobre tus cavidades nucleares. Ventana de baja fricción y flujo basal estable.</div>")

        html_body = "".join(lines)
        self.txt_transit_weather.setHtml(html_body)

        border_col = "#fbbf24" if (ignitions or channels) else "#38bdf8"
        self.txt_transit_weather.setStyleSheet(f"""
            QTextBrowser {{
                background-color: #080f1e;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                border-left: 4px solid {border_col};
                border-radius: 6px;
                padding: 8px 10px;
                font-size: 12px;
                line-height: 1.5;
            }}
            QScrollBar:vertical {{
                border: none;
                background: #090e18;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical {{
                background: #334155;
                min-height: 25px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: #00f0ff;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)

    def _copy_transits_report(self):
        """Copia el reporte en texto plano de tránsitos al portapapeles."""
        text = self.txt_transit_weather.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self.statusBar().showMessage("📋 Telemetría de Tránsitos copiada al portapapeles.")

    def _toggle_transit_viewer_height(self):
        """Alterna el visor entre altura compacta y altura extendida para facilitar la lectura fluida."""
        if getattr(self, 'transit_viewer_expanded', False):
            self.txt_transit_weather.setMinimumHeight(160)
            self.txt_transit_weather.setMaximumHeight(260)
            self.btn_expand_transits.setText("⛶ Expandir")
            self.btn_expand_transits.setToolTip("Alternar entre vista compacta y extendida del reporte de tránsitos")
            self.transit_viewer_expanded = False
            self.statusBar().showMessage("Visor de tránsitos contraído a vista compacta.")
        else:
            self.txt_transit_weather.setMinimumHeight(340)
            self.txt_transit_weather.setMaximumHeight(550)
            self.btn_expand_transits.setText("🗗 Reducir")
            self.btn_expand_transits.setToolTip("Reducir a vista compacta")
            self.transit_viewer_expanded = True
            self.statusBar().showMessage("Visor de tránsitos expandido a lectura amplia.")

    def _open_transits_fullscreen_modal(self):
        """Abre un modal inmersivo de lectura completa con scroll para inspeccionar la telemetría sin restricciones."""
        dialog = QDialog(self)
        dialog.setWindowTitle("🌌 Telemetría Cósmica de Tránsitos en Vivo (Δt)")
        dialog.resize(780, 620)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #060b14;
                color: #e2e8f0;
            }
        """)
        d_layout = QVBoxLayout(dialog)
        d_layout.setContentsMargins(16, 16, 16, 16)
        d_layout.setSpacing(12)

        header_box = QHBoxLayout()
        header_lbl = QLabel("⚡ REPORTE INTEGRAL DE INTERFERENCIA ELECTROMAGNÉTICA (Δt VIVO)")
        header_lbl.setStyleSheet("font-size: 13px; font-weight: bold; color: #38bdf8;")
        header_box.addWidget(header_lbl)
        header_box.addStretch()

        pill_text = self.lbl_transit_status_pill.text()
        pill_lbl = QLabel(pill_text)
        pill_lbl.setStyleSheet(self.lbl_transit_status_pill.styleSheet())
        header_box.addWidget(pill_lbl)
        d_layout.addLayout(header_box)

        txt_view = QTextBrowser()
        txt_view.setHtml(self.txt_transit_weather.toHtml())
        txt_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        txt_view.setStyleSheet("""
            QTextBrowser {
                background-color: #080f1e;
                color: #e2e8f0;
                border: 1px solid #1e293b;
                border-left: 4px solid #38bdf8;
                border-radius: 8px;
                padding: 14px 16px;
                font-size: 13px;
                line-height: 1.6;
            }
            QScrollBar:vertical {
                border: none;
                background: #090e18;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #38bdf8;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #00f0ff;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        d_layout.addWidget(txt_view, stretch=1)

        bottom_row = QHBoxLayout()
        btn_copy = QPushButton("📋 Copiar Telemetría Completa")
        btn_copy.setStyleSheet("font-size: 12px; padding: 6px 14px; background: #0f172a; border: 1px solid #38bdf8; color: #38bdf8; border-radius: 6px; font-weight: bold;")
        btn_copy.clicked.connect(lambda: QApplication.clipboard().setText(txt_view.toPlainText()))
        bottom_row.addWidget(btn_copy)

        bottom_row.addStretch()

        btn_close = QPushButton("Cerrar")
        btn_close.setStyleSheet("font-size: 12px; padding: 6px 20px; background: #1e293b; border: 1px solid #475569; color: #f1f5f9; border-radius: 6px;")
        btn_close.clicked.connect(dialog.accept)
        bottom_row.addWidget(btn_close)

        d_layout.addLayout(bottom_row)
        dialog.exec()

    def _live_clock_tick(self):
        """Actualiza el reloj sutilmente y recalcula tránsitos en vivo cada 30 segundos si el modo está activo."""
        if hasattr(self, 'transits_mode_active') and self.transits_mode_active:
            # Actualización reactiva periódica
            self._update_transits_and_interference()

    def _populate_cities_for_country(self, country_name: str):
        """Llena el selector de ciudades para el país seleccionado."""
        self.combo_city.blockSignals(True)
        self.combo_city.clear()
        cities = GEO_ATLAS.get(country_name, [])
        for city_item in cities:
            self.combo_city.addItem(city_item[0])
        self.combo_city.blockSignals(False)

    def _on_country_changed(self, country_name: str):
        """Al cambiar el país, actualiza la lista de ciudades y selecciona la primera."""
        self.geo_country = country_name
        self._populate_cities_for_country(country_name)
        if self.combo_city.count() > 0:
            self._on_city_changed(0)

    def _on_city_changed(self, idx: int):
        """Al cambiar la ciudad, actualiza latitud, longitud y huso horario sugerido."""
        cities = GEO_ATLAS.get(self.geo_country, [])
        if 0 <= idx < len(cities):
            city_item = cities[idx]
            city_name, lat, lon, tz_off = city_item
            self.geo_city = city_name
            self.geo_lat = lat
            self.geo_lon = lon
            
            # Sincronizar spinboxes de coordenadas
            self.spin_lat.blockSignals(True)
            self.spin_lat.setValue(lat)
            self.spin_lat.blockSignals(False)
            
            self.spin_lon.blockSignals(True)
            self.spin_lon.setValue(lon)
            self.spin_lon.blockSignals(False)
            
            # Si tiene huso horario sugerido, aplicarlo
            if tz_off is not None:
                self.spin_utc_offset.setValue(tz_off)
            else:
                self._on_time_or_tz_changed()

    def _on_coords_changed(self):
        """Actualiza las coordenadas cuando el usuario las edita manualmente."""
        self.geo_lat = self.spin_lat.value()
        self.geo_lon = self.spin_lon.value()
        self._sync_celestial_data()

    def _on_topocentric_toggled(self, checked: bool):
        """Activa o desactiva la corrección de paralaje lunar topocéntrico para la Esfera de la Atracción."""
        self.use_topocentric = checked
        self._sync_celestial_data()

    def _set_current_now(self):
        """Ajusta el selector de fecha y huso horario a la hora local actual del sistema y recalcula."""
        try:
            sys_offset = datetime.now().astimezone().utcoffset().total_seconds() / 3600.0
        except Exception:
            sys_offset = 0.0
        self.spin_utc_offset.setValue(round(sys_offset, 2))
        self.dt_local_picker.setDateTime(QDateTime.currentDateTime())
        self._on_time_or_tz_changed()

    def _on_time_or_tz_changed(self):
        """
        Normaliza la fecha y hora local ingresada a Tiempo Universal Coordinado (UTC)
        usando la fórmula determinista: UTC = Local - Offset_Horas.
        """
        py_local = self.dt_local_picker.dateTime().toPython()
        offset_hours = self.spin_utc_offset.value()
        
        utc_dt = py_local - timedelta(hours=offset_hours)
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
        
        self.current_local_dt = py_local
        self.utc_offset_hours = offset_hours
        self.current_utc = utc_dt
        
        sign_str = f"+{offset_hours:.1f}" if offset_hours >= 0 else f"{offset_hours:.1f}"
        topoc_note = f" • Topocéntrico ({self.geo_lat:+.2f}°, {self.geo_lon:+.2f}°)" if self.use_topocentric else " • Geocéntrico"
        self.lbl_tz_conversion.setText(
            f"🕒 Local: {py_local.strftime('%Y-%m-%d %H:%M:%S')} (UTC{sign_str}h) ➔ "
            f"🌐 UTC Normalizado: {utc_dt.strftime('%Y-%m-%d %H:%M:%S UTC')}{topoc_note}"
        )
        self.lbl_tz_conversion.setToolTip(
            "Mecánica Celeste Determinista:\n"
            "• UTC = Hora Local - Offset de Huso Horario.\n"
            "• Las 11 esferas del mapa se calculan en base a la coordenada cósmica absoluta UTC.\n"
            "• Dos personas nacidas a la misma hora local en países con diferente huso horario nacieron en instantes cósmicos distintos y sus matrices hologénicas son diferentes.\n"
            "• Paralaje Lunar Topocéntrico: Corrige la posición de la Luna (Esfera de la Atracción) según la latitud y longitud geográfica exacta del observador en la Tierra."
        )
        self._sync_celestial_data()

    def _on_tz_combo_changed(self, idx: int):
        if 0 <= idx < len(self.TIMEZONE_PRESETS):
            preset_offset = self.TIMEZONE_PRESETS[idx][1]
            if preset_offset is not None:
                self.spin_utc_offset.blockSignals(True)
                self.spin_utc_offset.setValue(preset_offset)
                self.spin_utc_offset.blockSignals(False)
                self._on_time_or_tz_changed()

    def _on_offset_spin_changed(self, val: float):
        matched = False
        for i, (_, offset) in enumerate(self.TIMEZONE_PRESETS):
            if offset is not None and abs(offset - val) < 0.01:
                self.combo_tz.blockSignals(True)
                self.combo_tz.setCurrentIndex(i)
                self.combo_tz.blockSignals(False)
                matched = True
                break
        if not matched:
            self.combo_tz.blockSignals(True)
            self.combo_tz.setCurrentIndex(len(self.TIMEZONE_PRESETS) - 1) # Personalizado
            self.combo_tz.blockSignals(False)
        self._on_time_or_tz_changed()

    def _on_matrix_mode_changed(self, idx: int):
        """Maneja el cambio de modo de red hologénica (11, 15, 22 o 26 esferas)."""
        mode_data = self.combo_matrix_mode.itemData(idx)
        if mode_data:
            self.matrix_mode = mode_data
            self.current_filter_sequence = "Todas"
            self._sync_celestial_data()
            self.statusBar().showMessage(f"🌌 Modo de Red Hologénica activado: {self.combo_matrix_mode.currentText()}")

    def _filter_spheres_view(self, seq_name: str):
        """Filtra las tarjetas de esferas visibles según la secuencia hologénica seleccionada."""
        self.current_filter_sequence = seq_name
        
        # Actualizar estilo de los botones de filtro
        filter_btns = [
            ("Todas", self.btn_filter_all),
            ("Activación", self.btn_filter_act),
            ("Venus", self.btn_filter_ven),
            ("Abundancia", self.btn_filter_per),
            ("Entorno", self.btn_filter_env),
            ("Polaridad NOT", self.btn_filter_not),
            ("Transpersonal", self.btn_filter_trans)
        ]
        for name, btn in filter_btns:
            if name == seq_name:
                btn.setStyleSheet("background: #0284c7; color: #ffffff; border: 1px solid #00f0ff; font-weight: bold;")
            else:
                btn.setStyleSheet("background: #0f172a; color: #94a3b8; border: 1px solid #1e293b;")

        spheres = self.current_activation.get("spheres", {})
        for s_name, card in self.sphere_card_widgets.items():
            if s_name not in spheres:
                card.setVisible(False)
                continue
            meta = SPHERES_METADATA.get(s_name, {})
            card_seq = meta.get("secuencia", "")
            if seq_name == "Todas" or card_seq == seq_name:
                card.setVisible(True)
            else:
                card.setVisible(False)

    @staticmethod
    def _safe_css_id(name: str) -> str:
        """Sanitiza nombres de esferas a ASCII estricto para generar selectores de ID CSS 100% válidos en Qt."""
        nfkd = unicodedata.normalize('NFKD', name)
        ascii_text = nfkd.encode('ASCII', 'ignore').decode('ASCII')
        clean = "".join(c if (c.isalnum() and c.isascii()) else "_" for c in ascii_text)
        if clean and clean[0].isdigit():
            clean = f"k_{clean}"
        return clean

    def _create_sphere_card(self, sph_name: str, meta: dict) -> QFrame:
        """Crea una tarjeta interactiva bioluminiscente para una de las 11 esferas."""
        safe_id = self._safe_css_id(sph_name)
        card = QFrame()
        card.setObjectName(f"card_{safe_id}")
        card.setFrameShape(QFrame.StyledPanel)
        card.setStyleSheet(f"""
            QFrame#card_{safe_id} {{
                background-color: #0b111e;
                border: 1px solid #1e293b;
                border-radius: 8px;
                padding: 6px;
            }}
            QFrame#card_{safe_id}:hover {{
                border: 1px solid {meta['color']};
                background-color: #0d1728;
            }}
        """)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(4)

        # Fila Superior: Icono de Esfera + Nombre + Secuencia + Botón Co-Crear
        top_row = QHBoxLayout()
        lbl_badge = QLabel(f" {meta['simbolo']} ")
        lbl_badge.setStyleSheet(f"background: {meta['color']}; color: #050b14; font-weight: bold; font-size: 11px; border-radius: 4px; padding: 2px 4px;")
        top_row.addWidget(lbl_badge)

        disp_sph_name = resolve_node_name(sph_name)
        disp_origin = resolve_celestial_origin(meta['origen'])

        lbl_title = QLabel(disp_sph_name)
        lbl_title.setStyleSheet(f"font-size: 13px; font-weight: bold; color: {meta['color']};")
        top_row.addWidget(lbl_title)

        seq_badge = QLabel(f"[{meta['secuencia']}]")
        seq_badge.setStyleSheet("font-size: 10px; color: #64748b; font-weight: bold;")
        top_row.addWidget(seq_badge)

        lbl_origin = QLabel(f"• {disp_origin}")
        lbl_origin.setStyleSheet("font-size: 10px; color: #94a3b8;")
        top_row.addWidget(lbl_origin)

        top_row.addStretch()

        btn_cocreate = QPushButton("⚡ Co-Crear")
        btn_cocreate.setToolTip(f"Cargar {disp_sph_name} directamente en la pestaña de Co-Creación IA")
        btn_cocreate.setStyleSheet(f"""
            QPushButton {{
                background: #0f172a;
                border: 1px solid {meta['color']};
                color: #f8fafc;
                font-size: 10px;
                padding: 3px 8px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background: {meta['color']};
                color: #050b14;
                font-weight: bold;
            }}
        """)
        btn_cocreate.clicked.connect(lambda checked=False, sn=sph_name: self._jump_to_ai_cocreation(sn))
        top_row.addWidget(btn_cocreate)
        layout.addLayout(top_row)

        # Fila Central: Coordenada, Vórtice Resonante, Bits y Fases (Entropía -> Coherencia -> Resonancia)
        mid_row = QHBoxLayout()
        lbl_coord = QLabel("K--.- [------] • Coherencia: --")
        lbl_coord.setStyleSheet("font-family: Consolas; font-size: 12px; font-weight: bold; color: #f8fafc;")
        mid_row.addWidget(lbl_coord)
        mid_row.addStretch()
        layout.addLayout(mid_row)

        lbl_spectrum = QLabel("🌑 Entropía (E): --  +  ✨ Coherencia (C): --  +  🌟 Resonancia (R): --")
        lbl_spectrum.setStyleSheet("font-size: 11px; color: #cbd5e1;")
        layout.addWidget(lbl_spectrum)

        # Fila Inferior: Información Somática y Alertas
        bot_row = QHBoxLayout()
        lbl_impact = QLabel(meta["impacto"])
        lbl_impact.setStyleSheet("font-size: 10px; color: #64748b;")
        bot_row.addWidget(lbl_impact, stretch=3)

        lbl_fuzzy = QLabel("")
        lbl_fuzzy.setStyleSheet("font-size: 9px; font-weight: bold; color: #fbbf24; background: #271e0c; padding: 2px 4px; border-radius: 3px; border: 1px solid #f59e0b;")
        lbl_fuzzy.setVisible(False)
        bot_row.addWidget(lbl_fuzzy, stretch=1)
        layout.addLayout(bot_row)

        # Guardar referencias para actualización reactiva
        self.card_labels[sph_name] = (lbl_coord, lbl_spectrum, lbl_impact, lbl_fuzzy, card)
        return card

    def _on_wheel_sphere_clicked(self, sph_name: str):
        """Responde a clics interactivos sobre los nodos de la rueda Bio-Mandala."""
        self.selected_sphere = sph_name
        
        # Resaltar la tarjeta correspondiente y asegurar que esté en pantalla
        for name, (_, _, _, _, card) in self.card_labels.items():
            meta = SPHERES_METADATA.get(name, {})
            safe_id = self._safe_css_id(name)
            if name == sph_name:
                card.setStyleSheet(f"""
                    QFrame#card_{safe_id} {{
                        background-color: #0f233a;
                        border: 2px solid {meta['color']};
                        border-radius: 8px;
                        padding: 6px;
                    }}
                """)
                self.spheres_scroll.ensureWidgetVisible(card)
            else:
                card.setStyleSheet(f"""
                    QFrame#card_{safe_id} {{
                        background-color: #0b111e;
                        border: 1px solid #1e293b;
                        border-radius: 8px;
                        padding: 6px;
                    }}
                    QFrame#card_{safe_id}:hover {{
                        border: 1px solid {meta['color']};
                        background-color: #0d1728;
                    }}
                """)

        # Sincronizar rueda mandala
        spheres = self.current_activation.get("spheres", {})
        self.mandala_wheel.set_profile_data(spheres, sph_name)

        # Sincronizar combo en la pestaña de Co-Creación IA
        self.combo_active_sphere.blockSignals(True)
        self.combo_active_sphere.setCurrentText(sph_name)
        self.combo_active_sphere.blockSignals(False)
        self._on_cocreation_sphere_changed(sph_name)

        self.statusBar().showMessage(f"🎯 Esfera Enfocada: {sph_name} ({SPHERES_METADATA.get(sph_name, {}).get('origen', '')})")

    def _jump_to_ai_cocreation(self, sph_name: str):
        """Acceso directo para transferir la esfera seleccionada a la pestaña de Co-Creación IA."""
        self._on_wheel_sphere_clicked(sph_name)
        self.tabs.setCurrentIndex(3) # Cambiar a pestaña 4: Co-Creación Humano-IA
        self.txt_runtime_scene.setFocus()

    def _export_full_profile(self):
        """Exporta el perfil completo de la red hologénica activa a JSON y Markdown para el usuario."""
        spheres = self.current_activation.get("spheres", {})
        dt_local_str = self.current_local_dt.strftime("%Y-%m-%d %H:%M:%S")
        dt_utc_str = self.current_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
        
        mode_titles = {
            "canonical": "Circuito Base (11 Nodos)",
            "nodes": "Nodos del Entorno (15 Nodos)",
            "polar_not": "Polaridades Duales NOT (22 Nodos)",
            "cosmic_26": "Matriz Cósmica Total (26 Nodos)"
        }
        active_mode_str = mode_titles.get(self.matrix_mode, self.matrix_mode)
        topoc_mode_str = f"Topocéntrico ({self.geo_lat:+.4f}°, {self.geo_lon:+.4f}°)" if self.use_topocentric else "Geocéntrico"
        
        md_lines = [
            f"# ⚡ PERFIL DE CO-CREACIÓN HEXA-MATRIX / CORE-64",
            f"- **Modo de Red Hologénica:** {active_mode_str} ({len(spheres)} Nodos Activos)",
            f"- **Ubicación Geográfica:** {self.geo_country} / {self.geo_city} (Lat: {self.geo_lat:+.4f}°, Lon: {self.geo_lon:+.4f}°)",
            f"- **Fecha & Hora Local:** {dt_local_str} (Offset: {self.utc_offset_hours:+.1f}h)",
            f"- **Tiempo Universal Coordinado (UTC):** {dt_utc_str}",
            f"- **Cálculo Lunar (Atracción):** {topoc_mode_str}",
            f"- **Sol Natal:** {self.current_activation.get('sol_natal_lon', 0):.2f}° | **Punto Pre-natal (-88° Arc Shift):** {self.current_activation.get('sol_design_lon', 0):.2f}°",
            f"- **Días de Arco Kepler:** {self.current_activation.get('kepler_days_prior', 0)} días antes del nacimiento\n",
            f"## 🌐 ESFERAS ACTIVAS DE LA RED HOLOGÉNICA ({len(spheres)})\n"
        ]

        json_dict = {
            "modo_red": self.matrix_mode,
            "total_esferas": len(spheres),
            "ubicacion": {
                "pais": self.geo_country,
                "ciudad": self.geo_city,
                "latitud": self.geo_lat,
                "longitud": self.geo_lon,
                "topocentrico": self.use_topocentric
            },
            "fecha_local": dt_local_str,
            "utc_offset": self.utc_offset_hours,
            "fecha_utc": dt_utc_str,
            "sol_natal_lon": self.current_activation.get('sol_natal_lon', 0),
            "sol_design_lon": self.current_activation.get('sol_design_lon', 0),
            "kepler_dias_previos": self.current_activation.get('kepler_days_prior', 0),
            "esferas": {}
        }

        for sph_name, s_data in spheres.items():
            meta = SPHERES_METADATA.get(sph_name, {})
            disp_sph = resolve_node_name(sph_name)
            disp_orig = resolve_celestial_origin(s_data.get('origen', ''))
            disp_cluster = resolve_cluster_name(s_data.get('ring', ''))
            paralaje_note = ""
            if sph_name == "Atracción" and s_data.get("is_topocentric"):
                paralaje_note = f" (Δ Topocéntrico: {s_data.get('parallax_delta_deg', 0.0):+.3f}° | Geocéntrico: {s_data.get('geo_longitude', 0):.2f}°)"
            md_lines.append(
                f"### {meta.get('simbolo', '•')} {disp_sph} [{meta.get('secuencia', '')}]\n"
                f"- **Origen Celeste:** {disp_orig} ({s_data.get('longitude', 0):.2f}°){paralaje_note}\n"
                f"- **Coordenada:** Vórtice Resonante {s_data.get('coord_str', '')} (Topología 6-bit: `{s_data.get('bits', '')}`)\n"
                f"- **Fases del Operador:** Entropía (E): {s_data.get('entropia', s_data.get('sombra', ''))} + Coherencia (C): {s_data.get('coherencia', s_data.get('don', ''))} + Resonancia (R): {s_data.get('resonancia', s_data.get('siddhi', ''))}\n"
                f"- **Clúster Bioquímico:** {disp_cluster} (Antípoda Inversa NOT: Vórtice Resonante {s_data.get('pair', '')})\n"
                f"- **Impacto Somático:** {s_data.get('impacto', '')}\n"
            )
            json_dict["esferas"][sph_name] = {
                "coordenada": s_data.get("coord_str", ""),
                "clave": s_data.get("key", 0),
                "cavidad": s_data.get("key", 0),
                "linea": s_data.get("line", 0),
                "bits": s_data.get("bits", ""),
                "entropia": s_data.get("entropia", s_data.get("sombra", "")),
                "coherencia": s_data.get("coherencia", s_data.get("don", "")),
                "resonancia": s_data.get("resonancia", s_data.get("siddhi", "")),
                "sombra": s_data.get("sombra", ""),
                "don": s_data.get("don", ""),
                "siddhi": s_data.get("siddhi", ""),
                "ring": s_data.get("ring", ""),
                "origen": s_data.get("origen", ""),
                "longitud": s_data.get("longitude", 0),
                "is_topocentric": s_data.get("is_topocentric", False),
                "parallax_delta_deg": s_data.get("parallax_delta_deg", 0.0)
            }

        full_export_text = "\n".join(md_lines)
        QApplication.clipboard().setText(full_export_text)
        
        # Mostrar diálogo con el contenido exportado
        dialog = QDialog(self)
        dialog.setWindowTitle("📥 Exportación del Perfil de la Red Hologénica")
        dialog.resize(700, 500)
        d_layout = QVBoxLayout(dialog)
        
        lbl_info = QLabel("✅ Perfil copiado al portapapeles con éxito en formato Markdown compatible con LLMs:")
        lbl_info.setStyleSheet("color: #00f0ff; font-weight: bold;")
        d_layout.addWidget(lbl_info)
        
        txt_prev = QTextEdit()
        txt_prev.setReadOnly(True)
        txt_prev.setText(full_export_text)
        d_layout.addWidget(txt_prev)

        btn_row = QHBoxLayout()
        btn_copy_clip = QPushButton("📋 Copiar al Portapapeles")
        btn_copy_clip.clicked.connect(lambda: [QApplication.clipboard().setText(full_export_text), QMessageBox.information(dialog, "Copiado", "Perfil copiado al portapapeles.")])
        btn_row.addWidget(btn_copy_clip)

        btn_save_as = QPushButton("💾 Guardar en Disco...")
        def save_profile_file():
            save_path, _ = QFileDialog.getSaveFileName(dialog, "Guardar Perfil", "perfil_hexa_matrix_hologenico.md", "Markdown (*.md);;JSON (*.json);;Texto (*.txt)")
            if save_path:
                content_to_write = json.dumps(json_dict, indent=2, ensure_ascii=False) if save_path.endswith(".json") else full_export_text
                with open(save_path, "w", encoding="utf-8") as f_out:
                    f_out.write(content_to_write)
                QMessageBox.information(dialog, "Guardado", f"Perfil guardado exitosamente en:\n{save_path}")
        btn_save_as.clicked.connect(save_profile_file)
        btn_row.addWidget(btn_save_as)

        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(dialog.accept)
        btn_row.addWidget(btn_close)

        d_layout.addLayout(btn_row)
        dialog.exec()

    def _on_slider_solar_moved(self, val: int):
        target_lon = val / 100.0
        self.lbl_slider_val.setText(f"Explorador Eclíptico Libre: {target_lon:.2f}°")
        
        mapped = CelestialMechanicsEngine.map_longitude_to_key_and_line(target_lon)
        target_prenatal = (target_lon - 88.0) % 360.0
        
        active_dict = {
            mapped["key"]: "#00f0ff",
            mapped["pair"]: "#f472b6"
        }
        self.mandala_wheel.set_solar_coordinates(target_lon, target_prenatal, active_dict)
        self.lbl_solar_telemetry.setText(f"☉ Grado Libre: {target_lon:.2f}° ➔ K{mapped['coord_str']} | Δ88°: {target_prenatal:.2f}°")

    def _sync_celestial_data(self):
        """
        Recalcula la matriz celeste completa según el modo de red hologénica activo
        (11, 15, 22 o 26 esferas) y sincroniza la rueda Bio-Mandala, las tarjetas del lateral derecho,
        los filtros de secuencia y la pestaña de Co-Creación IA.
        """
        self.current_activation = CelestialMechanicsEngine.calculate_activation_matrix(
            self.current_utc,
            lat_deg=self.geo_lat,
            lon_deg=self.geo_lon,
            use_topocentric=self.use_topocentric,
            matrix_mode=self.matrix_mode
        )
        spheres = self.current_activation["spheres"]
        total_sph = len(spheres)
        
        sol_natal = spheres["Trabajo de Vida"]
        sol_design = spheres["Resplandor"]
        
        # 1. Actualizar Telemetría Superior
        self.lbl_solar_telemetry.setText(
            f"☉ Sol Natal: {sol_natal['longitude']:.2f}° (V{sol_natal['coord_str']}) | "
            f"Punto Pre-natal (-88°): {sol_design['longitude']:.2f}° (V{sol_design['coord_str']}) | "
            f"Kepler: {self.current_activation['kepler_days_prior']:.2f}d prev"
        )

        # 2. Actualizar Rueda Bio-Mandala
        self.mandala_wheel.set_profile_data(spheres, self.selected_sphere)

        # 3. Actualizar Título del Grupo y Visibilidad de Filtros de Secuencia
        if hasattr(self, 'spheres_group'):
            self.spheres_group.setTitle(f"Red Hologénica: {total_sph} Nodos Activos")
        if hasattr(self, 'btn_filter_all'):
            self.btn_filter_all.setText(f"🌟 Todos ({total_sph})")
        
        has_env = (self.matrix_mode in ("nodes", "cosmic_26"))
        has_not = (self.matrix_mode == "polar_not")
        has_trans = (self.matrix_mode == "cosmic_26")
        
        if hasattr(self, 'btn_filter_env'):
            self.btn_filter_env.setVisible(has_env)
        if hasattr(self, 'btn_filter_not'):
            self.btn_filter_not.setVisible(has_not)
        if hasattr(self, 'btn_filter_trans'):
            self.btn_filter_trans.setVisible(has_trans)

        # 4. Actualizar Tarjetas del Lateral Derecho
        for sph_name, (lbl_coord, lbl_spectrum, lbl_impact, lbl_fuzzy, card) in self.card_labels.items():
            if sph_name in spheres:
                s_data = spheres[sph_name]
                cluster_label = resolve_cluster_name(s_data['ring'])
                orig_label = resolve_celestial_origin(s_data['origen'])
                lbl_coord.setText(f"V{s_data['coord_str']} [`{s_data['bits']}`] • Coherencia: {s_data.get('coherencia', s_data.get('don', ''))}")
                lbl_spectrum.setText(
                    f"🌑 Entropía (E): {s_data.get('entropia', s_data.get('sombra', ''))}  +  "
                    f"✨ Coherencia (C): {s_data.get('coherencia', s_data.get('don', ''))}  +  "
                    f"🌟 Resonancia (R): {s_data.get('resonancia', s_data.get('siddhi', ''))}"
                )
                if sph_name == "Atracción" and s_data.get("is_topocentric"):
                    p_delta = s_data.get("parallax_delta_deg", 0.0)
                    lbl_impact.setText(f"Clúster: {cluster_label} | Luna Topocéntrica (Δ {p_delta:+.2f}°) | {s_data['impacto']}")
                elif sph_name.startswith("NOT "):
                    twin = resolve_node_name(s_data.get("polar_twin", ""))
                    orig_k = s_data.get("original_key", "")
                    lbl_impact.setText(f"Antípoda Inversa NOT de [{twin} V{orig_k}] | {s_data['impacto']}")
                else:
                    lbl_impact.setText(f"Clúster: {cluster_label} | Origen: {orig_label} | {s_data['impacto']}")
                
                fuzzy = s_data.get("fuzzy", {})
                if fuzzy.get("active"):
                    lbl_fuzzy.setText(f"⚠️ Cúspide: {fuzzy.get('adjacent')} ({fuzzy.get('weight_adj', 0)*100:.0f}%)")
                    lbl_fuzzy.setVisible(True)
                else:
                    lbl_fuzzy.setVisible(False)

        # Aplicar filtro de vista activo
        self._filter_spheres_view(self.current_filter_sequence)

        # 5. Actualizar Diagnóstico de Fronteras Difusas General
        fuzzy_natal = sol_natal.get("fuzzy", {})
        if fuzzy_natal.get("active"):
            self.lbl_fuzzy_status.setText(
                f"⚠️ ATENCIÓN: Coordenada del Sol Natal en cúspide difusa (< 0.1° del borde).\n"
                f"{fuzzy_natal.get('nota')}\n"
                f"Respuesta física: Superposición cuántica ponderada de ambos operadores."
            )
            self.lbl_fuzzy_status.setStyleSheet("font-size: 11px; color: #fbbf24; background: #271e0c; padding: 8px; border-radius: 6px; border: 1px solid #f59e0b;")
        else:
            self.lbl_fuzzy_status.setText("✅ Coordenada estable: Límites bien cuantizados en el vórtice resonante.")
            self.lbl_fuzzy_status.setStyleSheet("font-size: 11px; color: #10b981; background: #0b1e16; padding: 8px; border-radius: 6px; border: 1px solid #059669;")

        # 6. Sincronizar Combo de Esferas en la Pestaña de Co-Creación IA
        curr_active = self.combo_active_sphere.currentText()
        self.combo_active_sphere.blockSignals(True)
        self.combo_active_sphere.clear()
        for s_k in spheres.keys():
            self.combo_active_sphere.addItem(s_k)
        if curr_active in spheres:
            self.combo_active_sphere.setCurrentText(curr_active)
        elif self.selected_sphere in spheres:
            self.combo_active_sphere.setCurrentText(self.selected_sphere)
        elif spheres:
            self.combo_active_sphere.setCurrentIndex(0)
        self.combo_active_sphere.blockSignals(False)

        # Sincronizar Capa Hardware de la pestaña de Co-Creación IA
        self._on_cocreation_sphere_changed(self.combo_active_sphere.currentText())

        # 7. Si el Modo Tránsitos está activo, refrescar el cálculo de interferencia en tiempo real
        if hasattr(self, 'transits_mode_active') and self.transits_mode_active:
            self._update_transits_and_interference()

    def _on_key_selected(self):
        key_num = self.spin_key_select.value()
        line_num = self.spin_line_select.value()
        
        data = CORE64_CATALOG.get(key_num, {})
        bits = data.get("bits", "000000")
        
        ent_name = data.get('entropia', data.get('sombra', ''))
        coh_name = data.get('coherencia', data.get('don', ''))
        res_name = data.get('resonancia', data.get('siddhi', ''))
        self.lbl_key_title.setText(f"VÓRTICE RESONANTE {key_num}: {ent_name.upper()} + {coh_name.upper()} + {res_name.upper()}")
        self.lbl_bits_display.setText(f"BITS: {' '.join(bits)}")
        
        trigrams = DiscreteParticleEngine.get_trigram_breakdown(bits)
        self.lbl_trigram_lower.setText(f"Trigrama Inferior (Bits 1,2,3): {trigrams['lower_desc']}\n• {trigrams['lower_role']}")
        self.lbl_trigram_upper.setText(f"Trigrama Superior (Bits 4,5,6): {trigrams['upper_desc']}\n• {trigrams['upper_role']}")
        
        pair_num = data.get("pair", 0)
        pair_bits = DiscreteParticleEngine.get_not_antipode(bits)
        pair_data = CORE64_CATALOG.get(pair_num, {})
        pair_coh = pair_data.get('coherencia', pair_data.get('don', ''))
        self.lbl_pair_info.setText(f"Antípoda Inversa (Inversor Lógico NOT): Vórtice Resonante {pair_num} [{pair_bits}] - Coherencia: {pair_coh}")
        self.lbl_ring_info.setText(f"Clúster Bioquímico: {data.get('ring', '')}")

        # Desglose de las 5 Propiedades de la Partícula
        line_info = LINE_PROPERTIES.get(line_num, {})
        prop_text = f"""PROPIEDADES DE LA PARTÍCULA K{key_num}.{line_num}:
1. GEOMETRÍA ESPECÍFICA: Topología {bits} ({trigrams['lower_desc'].split('-')[0].strip()} sobre {trigrams['upper_desc'].split('-')[0].strip()}).
2. ESPACIOS VACÍOS: Preservar ancho de banda atencional en la expresión de la Coherencia ({coh_name}).
3. ESPACIOS DE REPOSO: Cuencas de recuperación biológica vinculadas al {data.get('ring')}.
4. PUERTOS DE CONEXIÓN (Línea .{line_num}): {line_info.get('nombre')} - {line_info.get('dinamica')}
5. AFINIDADES Y ANTIGUSTOS: Discernimiento somático no moral para evitar colapsar en la Entropía ({ent_name})."""
        self.txt_particle_properties.setText(prop_text)

    def _update_bridge_simulator(self):
        ka = self.spin_bridge_a.value()
        kb = self.spin_bridge_b.value()
        self.bridge_view.set_bridge_data(ka, kb)
        
        info = self.bridge_view.bridge_info
        txt = f"""DIAGNÓSTICO DE PUENTE OPERATIVO [K{ka} + K{kb}]:
• Tipo de Acoplamiento: {info.get('coupling_type')}
• Dinámica de Flujo: {info.get('flow_dynamics')}
• Riesgo de Colapso: {info.get('collapse_risk')}
• Protocolo de Calibración: {info.get('calibration_remedy')}"""
        self.txt_bridge_report.setText(txt)

    def _on_state_vector_changed(self):
        e = self.slider_e.value() / 100.0
        c = self.slider_c.value() / 100.0
        r = self.slider_r.value() / 100.0
        
        self.lbl_e_val.setText(f"E (Entropía): {e:.2f} - Fricción somática y rumiación reactiva")
        self.lbl_c_val.setText(f"C (Coherencia): {c:.2f} - Capacidad estructurante de artefactos")
        self.lbl_r_val.setText(f"R (Resonancia): {r:.2f} - Reposo basal de mínima acción sin culpa")
        
        self.bio_gauge.set_state_values(e, c, r)
        _, regimen, prescripcion = CelestialMechanicsEngine.calculate_biological_yield(e, c, r)
        self.lbl_presc_action.setText(f"RÉGIMEN: {regimen}\n\n{prescripcion}")

    def _set_state_preset(self, e: float, c: float, r: float):
        self.slider_e.setValue(int(e * 100))
        self.slider_c.setValue(int(c * 100))
        self.slider_r.setValue(int(r * 100))

    def _on_cocreation_sphere_changed(self, sphere_name: str):
        self.selected_sphere = sphere_name
        spheres = self.current_activation.get("spheres", {})
        
        if sphere_name in spheres:
            s_data = spheres[sphere_name]
            k_num = s_data["key"]
            l_num = s_data["line"]
            bits = s_data["bits"]
            firmware_desc = s_data["firmware"]
            don_name = s_data["don"]
            sombra_name = s_data.get("sombra", "")
            siddhi_name = s_data.get("siddhi", "")
            pair_num = s_data.get("pair", 0)
        else:
            k_num = 31
            l_num = 1
            bits = "001110"
            data = CORE64_CATALOG.get(31, {})
            firmware_desc = data.get("firmware", "")
            don_name = data.get("don", "")
            sombra_name = data.get("sombra", "")
            siddhi_name = data.get("siddhi", "")
            pair_num = data.get("pair", 41)

        meta = SPHERES_METADATA.get(sphere_name, {"impacto": "Zona operativa en red."})
        pair_data = CORE64_CATALOG.get(pair_num, {})
        pair_bits = pair_data.get("bits", "000000")
        line_info = LINE_PROPERTIES.get(l_num, {})

        ent_name = s_data.get("entropia", s_data.get("sombra", "")) if sphere_name in spheres else data.get("entropia", data.get("sombra", ""))
        coh_name = s_data.get("coherencia", s_data.get("don", "")) if sphere_name in spheres else data.get("coherencia", data.get("don", ""))
        res_name = s_data.get("resonancia", s_data.get("siddhi", "")) if sphere_name in spheres else data.get("resonancia", data.get("siddhi", ""))

        pair_ent = pair_data.get("entropia", pair_data.get("sombra", ""))
        pair_coh = pair_data.get("coherencia", pair_data.get("don", ""))
        pair_res = pair_data.get("resonancia", pair_data.get("siddhi", ""))

        self.lbl_hw_key_badge.setText(f"Nodo: {sphere_name} | Vórtice Resonante: {k_num}.{l_num} (`{bits}`)")
        self.lbl_hw_impact.setText(f"Área de impacto: {meta.get('impacto', '')}")
        self.lbl_hw_line_interface.setText(f"🔌 Puerto de Interfaz: Línea .{l_num} ({line_info.get('nombre', 'Interfaz')}) • {line_info.get('auditoria', '')}")
        self.lbl_hw_not_pair.setText(f"⚖️ Antípoda Inversa (NOT): Vórtice Resonante {pair_num} [`{pair_bits}`] • Entropía: {pair_ent} + Coherencia: {pair_coh} + Resonancia: {pair_res}")

        self.lbl_fw_name.setText(f"Operador de Síntesis: Coherencia de {coh_name} ({ent_name} + {coh_name} + {res_name})")
        self.lbl_fw_function.setText(f"Función Orquestadora: {firmware_desc}")
        self.lbl_fw_not_audit.setText(f"🔍 Auditoría de Contrapeso NOT: Verifica si la Entropía de '{pair_ent}' (K{pair_num}) sabotea o distorsiona la Coherencia de '{coh_name}' (K{k_num}).")

    def _run_ai_telemetry(self):
        """Prepara el payload JSON con auditoría de línea y par NOT, y lanza el hilo de Ollama / Fallback determinista."""
        sph_name = self.combo_active_sphere.currentText()
        spheres = self.current_activation.get("spheres", {})
        s_data = spheres.get(sph_name, {})
        coord = s_data.get("coord_str", "31.1")
        don_seed = s_data.get("don", "Liderazgo")
        k_num = s_data.get("key", 31)
        l_num = s_data.get("line", 1)
        pair_num = s_data.get("pair", 41)
        pair_data = CORE64_CATALOG.get(pair_num, {})
        line_info = LINE_PROPERTIES.get(l_num, {})
        
        escena = self.txt_runtime_scene.toPlainText().strip()
        don_pers = self.txt_runtime_gift.toPlainText().strip()
        
        if not escena:
            escena = "Tensión laboral en el cierre de ciclo y coordinación de equipo."
        if not don_pers:
            don_pers = f"Operar desde la escucha activa y la toma de decisiones basada en hechos sin reactividad."

        payload = {
            "usuario_modo": "Soberano Co-Creador",
            "fecha_utc": self.current_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "vector_estado": {
                "E_entropia": round(self.slider_e.value() / 100.0, 2),
                "C_coherencia": round(self.slider_c.value() / 100.0, 2),
                "R_resonancia": round(self.slider_r.value() / 100.0, 2)
            },
            "nodos_activos": [
                {
                    "nodo_id": sph_name,
                    "esfera_id": sph_name,
                    "coordenada": coord,
                    "coherencia_semilla": don_seed,
                    "don_semilla": don_seed,
                    "contexto_situacion": escena,
                    "coherencia_personalizada": don_pers,
                    "don_personalizado": don_pers
                }
            ],
            "auditoria_interfaz_linea": {
                "linea": l_num,
                "nombre": line_info.get("nombre", ""),
                "dinamica": line_info.get("dinamica", ""),
                "directiva_auditoria": line_info.get("auditoria", "")
            },
            "auditoria_antipoda_inversa_not": {
                "cavidad_primaria": k_num,
                "cavidad_antipoda_not": pair_num,
                "bits_not": pair_data.get("bits", ""),
                "entropia_not": pair_data.get("entropia", pair_data.get("sombra", "")),
                "coherencia_not": pair_data.get("coherencia", pair_data.get("don", "")),
                "resonancia_not": pair_data.get("resonancia", pair_data.get("siddhi", "")),
                "sombra_not": pair_data.get("sombra", ""),
                "don_not": pair_data.get("don", ""),
                "siddhi_not": pair_data.get("siddhi", ""),
                "ring_not": pair_data.get("ring", ""),
                "instruccion": f"Evalúa si la Entropía '{pair_data.get('entropia', pair_data.get('sombra', ''))}' de la Cavidad {pair_num} está actuando como saboteador inconsciente o distorsión de fondo en la escena."
            }
        }

        # Si el Motor de Tránsitos en Tiempo Real (Δt) está activo, inyectar el clima e interferencias
        if getattr(self, 'transits_mode_active', False) and getattr(self, 'current_interference', None):
            payload["clima_transitos_tiempo_real_delta_t"] = {
                "estado": "ACTIVO (Cielo Actual en Vivo)",
                "resumen": self.current_interference.get("weather_summary", ""),
                "intensidad": self.current_interference.get("weather_intensity", 0.0),
                "igniciones_directas": self.current_interference.get("direct_ignitions", []),
                "circuitos_cerrados_en_vivo": self.current_interference.get("live_activated_channels", []),
                "tensiones_antipodas_not": self.current_interference.get("transit_antipodes", [])
            }

        self.txt_ai_output.setText("⏳ Conectando con el motor de telemetría de IA (Ollama)... Analizando coherencia de fase, interfaz de línea y par NOT...")

        model_name = self.combo_llm.currentText()
        if hasattr(self, 'txt_system_directives'):
            self.active_system_prompt = self.txt_system_directives.toPlainText()
        self.active_worker = OllamaTelemetryWorker(
            model_name,
            json.dumps(payload, indent=2),
            system_prompt=self.active_system_prompt
        )
        self.active_worker.finished_success.connect(self._on_telemetry_finished)
        self.active_worker.failed_error.connect(self._on_telemetry_failed)
        self.active_worker.start()

    def _on_telemetry_finished(self, full_text: str):
        """Muestra el resultado devuelto por la IA o el motor analítico determinista."""
        self.txt_ai_output.setPlainText(full_text)
        self.statusBar().showMessage("✅ Telemetría de Fase completada con éxito • Exit-Gate activo")

    def _on_telemetry_failed(self, err_msg: str):
        """Muestra un mensaje de error y notifica en la barra de estado."""
        self.txt_ai_output.setPlainText(f"⚠️ Error al procesar telemetría con Ollama:\n{err_msg}")
        self.statusBar().showMessage(f"❌ Error en telemetría de IA: {err_msg}")

    def _save_to_evolution_journal(self):
        """Guarda la sesión de telemetría actual en el archivo local de Diario de Evolución."""
        ai_text = self.txt_ai_output.toPlainText().strip()
        if not ai_text or "⏳ Conectando" in ai_text:
            QMessageBox.warning(self, "Telemetría Vacía", "Primero ejecuta la telemetría con la IA para generar el informe antes de guardarlo en tu diario.")
            return

        sph_name = self.combo_active_sphere.currentText()
        spheres = self.current_activation.get("spheres", {})
        s_data = spheres.get(sph_name, {})
        coord = s_data.get("coord_str", "31.1")
        k_num = s_data.get("key", 31)
        l_num = s_data.get("line", 1)
        pair_num = s_data.get("pair", 41)
        pair_data = CORE64_CATALOG.get(pair_num, {})
        line_info = LINE_PROPERTIES.get(l_num, {})

        dt_local_str = self.current_local_dt.strftime("%Y-%m-%d %H:%M:%S")
        dt_utc_str = self.current_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
        
        escena = self.txt_runtime_scene.toPlainText().strip() or "No especificada"
        don_pers = self.txt_runtime_gift.toPlainText().strip() or "No especificado"
        accion_60m = self.txt_action_60m.text().strip() or "Pendiente de definición somática"
        
        e_val = self.slider_e.value() / 100.0
        c_val = self.slider_c.value() / 100.0
        r_val = self.slider_r.value() / 100.0
        bio_yield, regimen, _ = CelestialMechanicsEngine.calculate_biological_yield(e_val, c_val, r_val)

        pair_ent = pair_data.get("entropia", pair_data.get("sombra", ""))
        pair_coh = pair_data.get("coherencia", pair_data.get("don", ""))
        pair_res = pair_data.get("resonancia", pair_data.get("siddhi", ""))

        journal_md_entry = f"""
# 📓 REGISTRO DE TELEMETRÍA • {dt_local_str} (Offset {self.utc_offset_hours:+.1f}h)
- **Fecha UTC:** {dt_utc_str}
- **Nodo Analizado:** {sph_name} (Vórtice V{coord} • Bits `{s_data.get('bits', '')}`)
- **Antípoda Inversa NOT:** Vórtice Resonante {pair_num} [`{pair_data.get('bits', '')}`] • Entropía: {pair_ent} + Coherencia: {pair_coh} + Resonancia: {pair_res}
- **Interfaz de Línea:** Línea .{l_num} ({line_info.get('nombre', '')}) • {line_info.get('auditoria', '')}
- **Vector de Estado S:** [E: {e_val:.2f}, C: {c_val:.2f}, R: {r_val:.2f}] | **Rendimiento Biofísico:** {bio_yield:.2f} ({regimen})

### 🎬 Escena Humana (Input A)
> {escena}

### ✨ Coherencia Operativa Co-Creada (Input B)
> {don_pers}

### 🧠 Informe de Telemetría y Mapa de Situación (IA)
{ai_text}

### ⛔ Compromiso Exit-Gate (60 Minutos)
> **Acción Inmediata:** {accion_60m}

{"="*80}
"""
        journal_path = os.path.join(os.getcwd(), "diario_evolucion_hexa_matrix.md")
        try:
            with open(journal_path, "a", encoding="utf-8") as f:
                f.write(journal_md_entry)
        except Exception as e:
            QMessageBox.critical(self, "Error al Guardar", f"No se pudo escribir en el diario: {str(e)}")
            return

        # También guardar en JSON estructurado para trazabilidad
        json_path = os.path.join(os.getcwd(), "diario_evolucion_hexa_matrix.json")
        try:
            entries = []
            if os.path.exists(json_path):
                with open(json_path, "r", encoding="utf-8") as f:
                    entries = json.load(f)
            entries.append({
                "timestamp": datetime.now().isoformat(),
                "fecha_local": dt_local_str,
                "fecha_utc": dt_utc_str,
                "nodo": sph_name,
                "esfera": sph_name,
                "coordenada": coord,
                "cavidad": k_num,
                "clave": k_num,
                "linea": l_num,
                "par_not": pair_num,
                "vector_estado": {"E": e_val, "C": c_val, "R": r_val, "rendimiento": bio_yield, "regimen": regimen},
                "escena": escena,
                "coherencia_personalizada": don_pers,
                "don_personalizado": don_pers,
                "informe_ia": ai_text,
                "accion_exit_gate": accion_60m
            })
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(entries, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

        self.statusBar().showMessage(f"✅ Telemetría archivada en {os.path.basename(journal_path)}")
        QMessageBox.information(
            self,
            "Diario de Evolución Actualizado",
            f"✅ Sesión guardada con éxito en tu Diario de Evolución:\n\n{journal_path}\n\n"
            f"Acción comprometida: «{accion_60m}»"
        )

    def _open_evolution_journal_dialog(self):
        """Abre un visor modal completo para explorar, copiar y exportar la bitácora del diario."""
        journal_path = os.path.join(os.getcwd(), "diario_evolucion_hexa_matrix.md")

        content = ""
        if os.path.exists(journal_path):
            try:
                with open(journal_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"Error al leer el diario: {str(e)}"
        else:
            content = "# 📓 DIARIO DE EVOLUCIÓN Y BITÁCORA DE TELEMETRÍA HEXA-MATRIX\nAún no se han guardado registros de telemetría. Realiza una co-creación y presiona 'Guardar en Diario de Evolución'."

        dialog = QDialog(self)
        dialog.setWindowTitle("📓 Diario de Evolución y Bitácora de Telemetría Humano-IA")
        dialog.resize(850, 600)
        d_layout = QVBoxLayout(dialog)

        top_info = QLabel("📖 Historial cronológico de Mapas de Situación, auditorías de línea, contrapesos NOT y compromisos Exit-Gate:")
        top_info.setStyleSheet("font-size: 11px; color: #38bdf8;")
        d_layout.addWidget(top_info)

        txt_journal = QTextEdit()
        txt_journal.setReadOnly(True)
        txt_journal.setStyleSheet("font-family: Consolas, monospace; font-size: 11px; background: #080d17; color: #f8fafc;")
        txt_journal.setText(content)
        d_layout.addWidget(txt_journal)

        btn_row = QHBoxLayout()
        btn_copy_all = QPushButton("📋 Copiar Todo al Portapapeles")
        def copy_all():
            QApplication.clipboard().setText(content)
            QMessageBox.information(dialog, "Copiado", "Bitácora completa copiada al portapapeles.")
        btn_copy_all.clicked.connect(copy_all)
        btn_row.addWidget(btn_copy_all)

        btn_export_as = QPushButton("📥 Exportar a Otro Archivo...")
        def export_file():
            save_path, _ = QFileDialog.getSaveFileName(dialog, "Guardar Copia de Bitácora", "diario_evolucion_copia.md", "Markdown (*.md);;Texto (*.txt)")
            if save_path:
                with open(save_path, "w", encoding="utf-8") as f_out:
                    f_out.write(content)
                QMessageBox.information(dialog, "Exportado", f"Archivo exportado con éxito a:\n{save_path}")
        btn_export_as.clicked.connect(export_file)
        btn_row.addWidget(btn_export_as)

        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(dialog.accept)
        btn_row.addWidget(btn_close)

        d_layout.addLayout(btn_row)
        dialog.exec()

    def _copy_ai_output(self):
        text = self.txt_ai_output.toPlainText().strip()
        if text:
            QApplication.clipboard().setText(text)
            self.statusBar().showMessage("📋 Telemetría de IA copiada al portapapeles")
        else:
            QMessageBox.information(self, "Sin contenido", "No hay telemetría generada para copiar.")

    def _exit_gate_sovereign_close(self):
        action_text = self.txt_action_60m.text().strip()
        if not action_text:
            QMessageBox.warning(self, "Exit-Gate Incompleto", "Por directiva soberana, debes definir la acción física concreta que ejecutarás en los próximos 60 minutos antes de cerrar la sesión.")
            return

        msg = (
            f"✅ SESIÓN CERRADA CON ÉXITO\n\n"
            f"Tu acción comprometida: «{action_text}»\n\n"
            f"La autoridad operativa te ha sido devuelta. Desconecta de la pantalla y preserva tu ancho de banda bio-cognitivo en el mundo físico."
        )
        QMessageBox.information(self, "Salida Soberana Exit-Gate", msg)
        self.txt_action_60m.clear()
        self.txt_runtime_scene.clear()
        self.txt_runtime_gift.clear()

    def _recalculate_embeddings(self):
        """
        Lanza el cálculo de embeddings en segundo plano mediante EmbeddingWorker,
        manteniendo la interfaz 100% interactiva y con fluidez en tiempo real.
        """
        user_text = f"{self.txt_runtime_scene.toPlainText()} {self.txt_runtime_gift.toPlainText()}".strip()
        if not user_text:
            user_text = "Búsqueda de claridad, propósito y resolución práctica sin rumiación."

        embed_model = self.combo_embed.currentText()
        self.statusBar().showMessage(f"📡 Sincronizando embeddings semánticos con {embed_model}...")

        self.embed_worker = EmbeddingWorker(user_text, embed_model)
        self.embed_worker.progress_step.connect(self._on_embeddings_progress)
        self.embed_worker.finished_success.connect(self._on_embeddings_finished)
        self.embed_worker.failed_error.connect(lambda err: self.statusBar().showMessage(f"⚠️ Error embeddings: {err}"))
        self.embed_worker.start()

    def _on_embeddings_progress(self, current: int, total: int):
        self.statusBar().showMessage(f"📡 Sincronizando embeddings con Ollama ({current}/{total})...")

    def _on_embeddings_finished(self, user_2d, key_projections, similarity_results):
        self.radar_view.update_embeddings_projection(user_2d, key_projections)

        # Actualizar tabla de resonancia con top 12 claves más afines
        similarity_results.sort(key=lambda x: x[3], reverse=True)
        self.table_semantic.setRowCount(min(12, len(similarity_results)))

        for r_idx, (kn, don_name, ring_name, sim_val) in enumerate(similarity_results[:12]):
            c_name = resolve_cluster_name(ring_name)
            self.table_semantic.setItem(r_idx, 0, QTableWidgetItem(f"V{kn}"))
            self.table_semantic.setItem(r_idx, 1, QTableWidgetItem(don_name))
            self.table_semantic.setItem(r_idx, 2, QTableWidgetItem(c_name))

            item_sim = QTableWidgetItem(f"{sim_val * 100.0:.1f}%")
            if sim_val > 0.70:
                item_sim.setForeground(QColor(0, 255, 179))
            else:
                item_sim.setForeground(QColor(255, 200, 50))
            self.table_semantic.setItem(r_idx, 3, item_sim)

        self.table_semantic.viewport().update()
        self.statusBar().showMessage("✅ Radar de Embeddings Sincronizado Exitosamente")



# ══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════



def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    # Fuentes tipográficas del sistema con fallback estético
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = HexaMatrixInteractiveApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
