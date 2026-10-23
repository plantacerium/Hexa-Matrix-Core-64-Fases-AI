#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
══════════════════════════════════════════════════════════════════════════════
HEXA-MATRIX CORE-64 • MODEL CONTEXT PROTOCOL (MCP) SERVER
══════════════════════════════════════════════════════════════════════════════
Servidor MCP determinista para conectar la suite Hexa-Matrix Core-64 Fases AI
con agentes de inteligencia artificial (Antigravity, Claude, Cursor, etc.).

Expone:
  • Efemérides astronómicas VSOP87 y Jean Meeus para cálculo natal y diseño.
  • Solver Newton-Raphson de arco solar prenatal de 88°.
  • Corrección de paralaje lunar topocéntrico.
  • Álgebra booleana de 6 bits e hipercubo de 64 vórtices (Hamming DH=0..6).
  • Ecuación de estado termodinámico no-lineal (Rendimiento Biológico).
  • Sinastría bio-electromagnética de red y cierre de canales armónicos.
  • Telemetría de tránsitos planetarios en tiempo real e interferencia.
  • Escaneo predictivo de ventanas temporales de tránsitos.
  • Sinastría de grupo / topología colectiva (Penta / Equipos multicuerpo).
  • Puente biomolecular de codones de ARN y aminoácidos estándar IUPAC.
  • Bóveda persistente de perfiles natales (profiles_vault.json).
  • Generación y exportación de Dossiers Ejecutivos Bio-SciFi (HTML y PDF).
══════════════════════════════════════════════════════════════════════════════
"""

import sys
import os
import json
import base64
import html
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Union, Tuple

# ── Fix A: Protección estricta del canal stdio para protocolo JSON-RPC ──
# Evitar que PySide6 intente abrir contexto gráfico y capturar prints al importar
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

_orig_stdout = sys.stdout
try:
    sys.stdout = sys.stderr
    import hexa_matrix_core_64_fases_ai as hm
finally:
    sys.stdout = _orig_stdout

# Importar ReportLab para generación nativa de PDF
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors as rl_colors
    from reportlab.lib.units import mm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

# Importar el SDK de Model Context Protocol (soporte mcp 2.x y 1.x)
try:
    from mcp.server.mcpserver import MCPServer
except ImportError:
    try:
        from mcp.server.fastmcp import FastMCP as MCPServer
    except ImportError as e:
        sys.stderr.write(f"Error importando MCP SDK: {e}\nInstala mcp con: pip install mcp\n")
        raise

# Instancia del servidor MCP
mcp = MCPServer("hexamatrix-core-64")


# ══════════════════════════════════════════════════════════════════════════════
# DICCIONARIO BIOMOLECULAR: AMINOÁCIDOS IUPAC Y CODONES DE ARN
# ══════════════════════════════════════════════════════════════════════════════

AMINO_ACID_MAP = {
    "cluster_triptofano": {"name_es": "Triptófano", "name_en": "Tryptophan", "iupac_3": "Trp", "iupac_1": "W", "codons": ["UGG"], "chem_class": "Aromático no polar"},
    "cluster_metionina": {"name_es": "Metionina", "name_en": "Methionine", "iupac_3": "Met", "iupac_1": "M", "codons": ["AUG"], "chem_class": "No polar alifático azufrado"},
    "cluster_start": {"name_es": "Codón Start (Metionina)", "name_en": "Start Codon (Met)", "iupac_3": "Met", "iupac_1": "M", "codons": ["AUG"], "chem_class": "Iniciador transcripcional"},
    "cluster_stop": {"name_es": "Codones Stop (Terminación)", "name_en": "Stop Codons", "iupac_3": "STOP", "iupac_1": "*", "codons": ["UAA", "UAG", "UGA"], "chem_class": "Terminación de cadena peptídica"},
    "cluster_tirosina": {"name_es": "Tirosina", "name_en": "Tyrosine", "iupac_3": "Tyr", "iupac_1": "Y", "codons": ["UAU", "UAC"], "chem_class": "Aromático polar neutro"},
    "cluster_histidina": {"name_es": "Histidina", "name_en": "Histidine", "iupac_3": "His", "iupac_1": "H", "codons": ["CAU", "CAC"], "chem_class": "Básico aromático con carga positiva"},
    "cluster_glutamina": {"name_es": "Glutamina", "name_en": "Glutamine", "iupac_3": "Gln", "iupac_1": "Q", "codons": ["CAA", "CAG"], "chem_class": "Polar sin carga (amida)"},
    "cluster_aspartico": {"name_es": "Ácido Aspártico", "name_en": "Aspartic Acid", "iupac_3": "Asp", "iupac_1": "D", "codons": ["GAU", "GAC"], "chem_class": "Ácido con carga negativa"},
    "cluster_asparagina": {"name_es": "Asparagina", "name_en": "Asparagine", "iupac_3": "Asn", "iupac_1": "N", "codons": ["AAU", "AAC"], "chem_class": "Polar sin carga (amida)"},
    "cluster_glutamico": {"name_es": "Ácido Glutámico", "name_en": "Glutamic Acid", "iupac_3": "Glu", "iupac_1": "E", "codons": ["GAA", "GAG"], "chem_class": "Ácido con carga negativa"},
    "cluster_fenilalanina": {"name_es": "Fenilalanina", "name_en": "Phenylalanine", "iupac_3": "Phe", "iupac_1": "F", "codons": ["UUU", "UUC"], "chem_class": "Aromático hidrofóbico no polar"},
    "cluster_valina": {"name_es": "Valina", "name_en": "Valine", "iupac_3": "Val", "iupac_1": "V", "codons": ["GUU", "GUC", "GUA", "GUG"], "chem_class": "Alifático no polar ramificado"},
    "cluster_isoleucina": {"name_es": "Isoleucina", "name_en": "Isoleucine", "iupac_3": "Ile", "iupac_1": "I", "codons": ["AUU", "AUC", "AUA"], "chem_class": "Alifático no polar ramificado"},
    "cluster_leucina": {"name_es": "Leucina", "name_en": "Leucine", "iupac_3": "Leu", "iupac_1": "L", "codons": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], "chem_class": "Alifático no polar ramificado"},
    "cluster_prolina": {"name_es": "Prolina", "name_en": "Proline", "iupac_3": "Pro", "iupac_1": "P", "codons": ["CCU", "CCC", "CCA", "CCG"], "chem_class": "Iminoácido cíclico rígido"},
    "cluster_treonina": {"name_es": "Treonina", "name_en": "Threonine", "iupac_3": "Thr", "iupac_1": "T", "codons": ["ACU", "ACC", "ACA", "ACG"], "chem_class": "Polar neutro hidroxilado"},
    "cluster_serina": {"name_es": "Serina", "name_en": "Serine", "iupac_3": "Ser", "iupac_1": "S", "codons": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "chem_class": "Polar neutro hidroxilado"},
    "cluster_glicina": {"name_es": "Glicina", "name_en": "Glycine", "iupac_3": "Gly", "iupac_1": "G", "codons": ["GGU", "GGC", "GGA", "GGG"], "chem_class": "Alifático flexible no quiral"},
    "cluster_alanina_a": {"name_es": "Alanina (Materia / Estructura)", "name_en": "Alanine A", "iupac_3": "Ala", "iupac_1": "A", "codons": ["GCU", "GCC"], "chem_class": "Alifático pequeño no polar"},
    "cluster_alanina_b": {"name_es": "Alanina (Polaridad / Forma)", "name_en": "Alanine B", "iupac_3": "Ala", "iupac_1": "A", "codons": ["GCA", "GCG"], "chem_class": "Alifático pequeño no polar"},
    "cluster_arginina": {"name_es": "Arginina", "name_en": "Arginine", "iupac_3": "Arg", "iupac_1": "R", "codons": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], "chem_class": "Básico básico con carga positiva"},
    "cluster_cistina": {"name_es": "Cisteína / Cistina", "name_en": "Cysteine", "iupac_3": "Cys", "iupac_1": "C", "codons": ["UGU", "UGC"], "chem_class": "Polar azufrado (puentes disulfuro)"},
    "cluster_lisina": {"name_es": "Lisina", "name_en": "Lysine", "iupac_3": "Lys", "iupac_1": "K", "codons": ["AAA", "AAG"], "chem_class": "Básico con carga positiva"},
    "cluster_choque": {"name_es": "Codones de Choque (Revolución)", "name_en": "Shock Codons", "iupac_3": "Shk", "iupac_1": "!", "codons": ["UGA", "CUG"], "chem_class": "Polaridad de mutación rápida"},
    "cluster_sinonimo": {"name_es": "Codón Sinónimo (Sinarquía)", "name_en": "Synonymous Codon", "iupac_3": "Syn", "iupac_1": "=", "codons": ["GUG", "UUG"], "chem_class": "Modulación de traducción peptídica"}
}


# ══════════════════════════════════════════════════════════════════════════════
# UTILIDADES DE PARSEO Y FORMATEO
# ══════════════════════════════════════════════════════════════════════════════

def _parse_datetime(dt_str: str) -> datetime:
    """
    Parsea cadenas de fecha y hora en diversos formatos comunes.
    Fix C: Maneja con precisión tanto objetos naive como aware con timezone offset.
    """
    dt_str = dt_str.strip()
    if dt_str.endswith("Z"):
        dt_str = dt_str[:-1] + "+00:00"
    
    # Intentar primero fromisoformat (soporta +02:00, -03:00, etc.)
    try:
        return datetime.fromisoformat(dt_str)
    except Exception:
        pass

    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(dt_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha inválido '{dt_str}'. Use 'YYYY-MM-DD HH:MM:SS' o ISO-8601.")


def _resolve_natal_and_utc_datetimes(birth_datetime: str, utc_offset_hours: float) -> Tuple[datetime, datetime]:
    """
    Resuelve deterministamente el datetime local y el datetime UTC sin dobles offsets.
    """
    dt = _parse_datetime(birth_datetime)
    if dt.tzinfo is not None:
        # Cadena aware: usar su propio timezone offset
        dt_utc = dt.astimezone(timezone.utc)
        dt_local = dt.replace(tzinfo=None)
    else:
        # Cadena naive: aplicar utc_offset_hours
        dt_local = dt
        dt_utc = (dt_local - timedelta(hours=utc_offset_hours)).replace(tzinfo=timezone.utc)
    return dt_local, dt_utc


def _enrich_sphere(sphere_name: str, s_data: Dict[str, Any]) -> Dict[str, Any]:
    """Enriquece una esfera con metadatos del catálogo CORE64."""
    key_num = s_data.get("key", 0)
    k_cat = hm.CORE64_CATALOG.get(key_num, {})
    bits = k_cat.get("bits", "000000")
    trigram = hm.DiscreteParticleEngine.get_trigram_breakdown(bits)
    
    enriched = dict(s_data)
    enriched.update({
        "sphere_name": sphere_name,
        "vortex_id": key_num,
        "bits": bits,
        "entropy": k_cat.get("entropia", ""),
        "coherence": k_cat.get("coherencia", ""),
        "resonance": k_cat.get("resonancia", ""),
        "pair_antipode_id": k_cat.get("pair", 0),
        "cluster_name": hm.resolve_cluster_name(k_cat.get("ring", "")),
        "lower_trigram": {
            "bits": trigram["lower_bits"],
            "name": trigram["lower_desc"],
            "role": trigram["lower_role"]
        },
        "upper_trigram": {
            "bits": trigram["upper_bits"],
            "name": trigram["upper_desc"],
            "role": trigram["upper_role"]
        },
        "firmware": k_cat.get("firmware", "")
    })
    return enriched


# ══════════════════════════════════════════════════════════════════════════════
# HERRAMIENTAS MCP (TOOLS)
# ══════════════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_vortex_info(vortex_id: int) -> Dict[str, Any]:
    """
    Obtiene la morfología cuántico-discreta y ontológica completa de un Vórtice Resonante (1 a 64).
    
    Devuelve la palabra booleana de 6 bits, desglose de trigramas (inferior bio-somático y superior
    ambiental), antípoda lógica inversa (NOT / DH=6), clúster bioquímico de codones (anillo de aminoácidos),
    frecuencias ontológicas (Entropía/Sombra, Coherencia/Don, Resonancia/Siddhi), firmware operativo
    y los 6 vecinos a distancia de Hamming DH=1 (mutación de 1 bit).
    """
    if vortex_id < 1 or vortex_id > 64:
        return {"error": f"vortex_id debe estar entre 1 y 64, recibido: {vortex_id}"}
    
    k_data = hm.CORE64_CATALOG.get(vortex_id, {})
    bits = k_data.get("bits", "000000")
    trigram = hm.DiscreteParticleEngine.get_trigram_breakdown(bits)
    pair_id = k_data.get("pair", 0)
    pair_bits = hm.CORE64_CATALOG.get(pair_id, {}).get("bits", "")
    
    dh1_neighbors = []
    for other_id, other_data in hm.CORE64_CATALOG.items():
        if other_id == vortex_id:
            continue
        other_bits = other_data.get("bits", "")
        if hm.DiscreteParticleEngine.calculate_hamming_distance(bits, other_bits) == 1:
            dh1_neighbors.append({
                "vortex_id": other_id,
                "bits": other_bits,
                "coherence": other_data.get("coherencia", ""),
                "resonance": other_data.get("resonancia", "")
            })
    
    ring_key = k_data.get("ring", "")
    bio_info = AMINO_ACID_MAP.get(ring_key, {})
    
    return {
        "vortex_id": vortex_id,
        "bits": bits,
        "trigrams": {
            "lower": {
                "bits": trigram["lower_bits"],
                "name": trigram["lower_desc"],
                "role": trigram["lower_role"]
            },
            "upper": {
                "bits": trigram["upper_bits"],
                "name": trigram["upper_desc"],
                "role": trigram["upper_role"]
            }
        },
        "antipode_not_pair": {
            "vortex_id": pair_id,
            "bits": pair_bits,
            "coherence": hm.CORE64_CATALOG.get(pair_id, {}).get("coherencia", ""),
            "hamming_distance": 6
        },
        "cluster": {
            "code": ring_key,
            "name": hm.resolve_cluster_name(ring_key),
            "amino_acid": bio_info.get("name_es", ""),
            "iupac_3": bio_info.get("iupac_3", "")
        },
        "ontological_frequencies": {
            "entropy": k_data.get("entropia", ""),
            "coherence": k_data.get("coherencia", ""),
            "resonance": k_data.get("resonancia", "")
        },
        "firmware": k_data.get("firmware", ""),
        "dh1_mutation_neighbors": dh1_neighbors
    }


@mcp.tool()
def search_vortices(query: str, search_type: str = "all") -> List[Dict[str, Any]]:
    """
    Busca vórtices resonantes en el catálogo CORE-64 según palabras clave o criterios algebraicos.
    
    Args:
        query: Término de búsqueda (ej. 'Liderazgo', 'Miedo', 'leucina', '110010', 'Agua', 'Fuego').
        search_type: 'all', 'keyword', 'cluster', 'bits', o 'trigram'.
    """
    q_lower = query.strip().lower()
    results = []
    
    for v_id, data in hm.CORE64_CATALOG.items():
        bits = data.get("bits", "")
        entropy = data.get("entropia", "")
        coherence = data.get("coherencia", "")
        resonance = data.get("resonancia", "")
        firmware = data.get("firmware", "")
        ring_name = hm.resolve_cluster_name(data.get("ring", ""))
        
        match = False
        matched_in = []
        
        if search_type in ("all", "keyword"):
            for field_name, val in [("entropy", entropy), ("coherence", coherence), ("resonance", resonance), ("firmware", firmware)]:
                if q_lower in val.lower():
                    match = True
                    matched_in.append(field_name)
                    
        if search_type in ("all", "cluster"):
            if q_lower in ring_name.lower() or q_lower in data.get("ring", "").lower():
                match = True
                matched_in.append("cluster")
                
        if search_type in ("all", "bits"):
            if q_lower in bits:
                match = True
                matched_in.append("bits")
                
        if search_type in ("all", "trigram"):
            lower_name = hm.TRIGRAM_NAMES.get(bits[:3], "")
            upper_name = hm.TRIGRAM_NAMES.get(bits[3:], "")
            if q_lower in lower_name.lower() or q_lower in upper_name.lower():
                match = True
                matched_in.append("trigram")
        
        if match:
            results.append({
                "vortex_id": v_id,
                "bits": bits,
                "entropy": entropy,
                "coherence": coherence,
                "resonance": resonance,
                "cluster": ring_name,
                "matched_fields": matched_in
            })
            
    return results


@mcp.tool()
def calculate_hologenetic_profile(
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    use_topocentric: bool = True,
    matrix_mode: str = "cosmic_26"
) -> Dict[str, Any]:
    """
    Calcula la Matriz Hologénetica Natal y Prenatal (Diseño) con precisión determinista de efemérides.
    
    Ejecuta el solver Newton-Raphson para resolver el instante exacto del arco solar prenatal de 88°,
    aplica corrección de paralaje lunar topocéntrico a la Esfera de la Atracción y proyecta las
    posiciones planetarias sobre la rueda de 64 vórtices y 6 líneas.
    """
    dt_local, dt_utc = _resolve_natal_and_utc_datetimes(birth_datetime, utc_offset_hours)
    
    raw_profile = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_utc,
        lat_deg=latitude,
        lon_deg=longitude,
        use_topocentric=use_topocentric,
        matrix_mode=matrix_mode
    )
    
    raw_spheres = raw_profile.get("spheres", {})
    enriched_spheres = {}
    for s_name, s_info in raw_spheres.items():
        enriched_spheres[s_name] = _enrich_sphere(s_name, s_info)
        
    return {
        "calculation_metadata": {
            "local_datetime": dt_local.strftime("%Y-%m-%d %H:%M:%S"),
            "utc_natal": raw_profile.get("utc_natal"),
            "utc_prenatal_design": raw_profile.get("utc_prenatal"),
            "kepler_days_prior": raw_profile.get("kepler_days_prior"),
            "solver_iterations": raw_profile.get("kepler_solver_iterations"),
            "sun_natal_longitude": raw_profile.get("sol_natal_lon"),
            "sun_design_longitude": raw_profile.get("sol_design_lon"),
            "coordinates": {"latitude": latitude, "longitude": longitude},
            "use_topocentric": use_topocentric,
            "matrix_mode": matrix_mode,
            "total_spheres": len(enriched_spheres)
        },
        "spheres": enriched_spheres
    }


@mcp.tool()
def calculate_thermodynamic_yield(
    entropy: float,
    coherence: float,
    resonance: float,
    epsilon: float = 0.05
) -> Dict[str, Any]:
    """
    Evalúa la Ecuación de Estado Cotidiana (Termodinámica de Sistemas Abiertos no lineales).
    
    Calcula el Rendimiento Biológico: Y = (C * R) / (E + epsilon), diagnosticando el régimen
    operativo del sistema biológico y emitiendo una prescripción somática de calibración.
    """
    yield_val, regimen, prescripcion = hm.CelestialMechanicsEngine.calculate_biological_yield(
        e=entropy, c=coherence, r=resonance, epsilon=epsilon
    )
    
    return {
        "state_vector": {
            "entropy_E": max(0.0, min(1.0, entropy)),
            "coherence_C": max(0.0, min(1.0, coherence)),
            "resonance_R": max(0.0, min(1.0, resonance))
        },
        "biological_yield_Y": yield_val,
        "operating_regime": regimen,
        "somatic_prescription": prescripcion
    }


@mcp.tool()
def analyze_vortex_bridge(vortex_a: int, vortex_b: int) -> Dict[str, Any]:
    """
    Diagnostica el enlace bio-electromagnético y la dinámica de interferencia entre dos Vórtices Resonantes.
    """
    if vortex_a < 1 or vortex_a > 64 or vortex_b < 1 or vortex_b > 64:
        return {"error": "Ambos vórtices deben estar comprendidos entre 1 y 64."}
        
    bridge = hm.DiscreteParticleEngine.analyze_bridge(vortex_a, vortex_b)
    data_a = hm.CORE64_CATALOG.get(vortex_a, {})
    data_b = hm.CORE64_CATALOG.get(vortex_b, {})
    
    is_canonical = False
    channel_name = ""
    for k1, k2, c_name in hm.NetworkSynastryEngine.CANONICAL_HARMONIC_CHANNELS:
        if (k1 == vortex_a and k2 == vortex_b) or (k1 == vortex_b and k2 == vortex_a):
            is_canonical = True
            channel_name = c_name
            break
            
    return {
        "vortex_a": {
            "id": vortex_a,
            "bits": data_a.get("bits", ""),
            "coherence": data_a.get("coherencia", ""),
            "cluster": hm.resolve_cluster_name(data_a.get("ring", ""))
        },
        "vortex_b": {
            "id": vortex_b,
            "bits": data_b.get("bits", ""),
            "coherence": data_b.get("coherencia", ""),
            "cluster": hm.resolve_cluster_name(data_b.get("ring", ""))
        },
        "hamming_distance": bridge.get("hamming_distance"),
        "coupling_type": bridge.get("coupling_type"),
        "is_canonical_harmonic_channel": is_canonical,
        "canonical_channel_name": channel_name if is_canonical else None,
        "flow_dynamics": bridge.get("flow_dynamics"),
        "collapse_risk": bridge.get("collapse_risk"),
        "calibration_remedy": bridge.get("calibration_remedy")
    }


@mcp.tool()
def analyze_network_synastry(
    birth_datetime_a: str,
    birth_datetime_b: str,
    utc_offset_a: float = 0.0,
    utc_offset_b: float = 0.0,
    lat_a: float = 40.4168,
    lon_a: float = -3.7038,
    lat_b: float = 40.4168,
    lon_b: float = -3.7038,
    name_a: str = "Sujeto Alfa",
    name_b: str = "Sujeto Beta",
    matrix_mode: str = "canonical"
) -> Dict[str, Any]:
    """
    Calcula la sinastría biofísica y acoplamiento electromagnético entre dos operadores o matrices.
    """
    _, dt_a_utc = _resolve_natal_and_utc_datetimes(birth_datetime_a, utc_offset_a)
    _, dt_b_utc = _resolve_natal_and_utc_datetimes(birth_datetime_b, utc_offset_b)
    
    mat_a = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_a_utc, lat_deg=lat_a, lon_deg=lon_a, matrix_mode=matrix_mode
    )
    mat_b = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_b_utc, lat_deg=lat_b, lon_deg=lon_b, matrix_mode=matrix_mode
    )
    
    return hm.NetworkSynastryEngine.analyze_coupling(
        matrix_a=mat_a, matrix_b=mat_b, name_a=name_a, name_b=name_b
    )


@mcp.tool()
def get_planetary_transits(
    datetime_iso: Optional[str] = None,
    offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    use_topocentric: bool = True
) -> Dict[str, Any]:
    """
    Calcula los tránsitos planetarios en tiempo real proyectados sobre la rueda de 64 vórtices.
    """
    if datetime_iso:
        dt_base = _parse_datetime(datetime_iso)
        if dt_base.tzinfo is None:
            dt_base = dt_base.replace(tzinfo=timezone.utc)
        else:
            dt_base = dt_base.astimezone(timezone.utc)
    else:
        dt_base = datetime.now(timezone.utc)
        
    dt_calc = dt_base + timedelta(hours=offset_hours)
    
    transits = hm.RealTimeTransitEngine.calculate_transits(
        dt_utc=dt_calc, lat_deg=latitude, lon_deg=longitude, use_topocentric=use_topocentric
    )
    
    enriched_positions = {}
    positions = transits.get("positions", {})
    for body_name, b_info in positions.items():
        k_num = b_info.get("key", 0)
        k_data = hm.CORE64_CATALOG.get(k_num, {})
        enriched_positions[body_name] = {
            "longitude_deg": b_info.get("longitude", 0.0),
            "vortex_id": k_num,
            "line": b_info.get("line", 1),
            "bits": k_data.get("bits", "000000"),
            "entropy": k_data.get("entropia", ""),
            "coherence": k_data.get("coherencia", ""),
            "resonance": k_data.get("resonancia", ""),
            "cluster": hm.resolve_cluster_name(k_data.get("ring", ""))
        }
        
    return {
        "timestamp_utc": dt_calc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "offset_hours_applied": offset_hours,
        "positions": enriched_positions
    }


@mcp.tool()
def evaluate_transit_interference(
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    transit_datetime_iso: Optional[str] = None,
    transit_offset_hours: float = 0.0
) -> Dict[str, Any]:
    """
    Evalúa la interferencia cuántica y activación de canales entre una Carta Natal y los Tránsitos actuales.
    """
    _, dt_utc = _resolve_natal_and_utc_datetimes(birth_datetime, utc_offset_hours)
    
    natal_matrix = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_utc, lat_deg=latitude, lon_deg=longitude, matrix_mode="cosmic_26"
    )
    
    if transit_datetime_iso:
        dt_tr = _parse_datetime(transit_datetime_iso)
        if dt_tr.tzinfo is None:
            dt_tr = dt_tr.replace(tzinfo=timezone.utc)
        else:
            dt_tr = dt_tr.astimezone(timezone.utc)
    else:
        dt_tr = datetime.now(timezone.utc)
    dt_tr = dt_tr + timedelta(hours=transit_offset_hours)
    
    transits = hm.RealTimeTransitEngine.calculate_transits(
        dt_utc=dt_tr, lat_deg=latitude, lon_deg=longitude
    )
    
    return hm.RealTimeTransitEngine.evaluate_transit_interference(
        natal_matrix=natal_matrix,
        transits_dict=transits.get("positions", {}),
        dt_utc=dt_tr
    )


# ── Expansión 1: Escáner Predictivo de Ventanas de Tránsitos ──
@mcp.tool()
def scan_transit_windows(
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    start_datetime_iso: Optional[str] = None,
    days_ahead: int = 30,
    step_hours: int = 12
) -> Dict[str, Any]:
    """
    Escanea un horizonte temporal hacia adelante detectando las ventanas exactas donde
    los tránsitos planetarios cierran canales electromagnéticos armónicos o activan antípodas NOT (DH=6)
    sobre la matriz natal del operador.
    
    Utiliza las claves reales del motor: 'live_activated_channels', 'direct_ignitions' y 'transit_antipodes'.
    """
    _, dt_natal_utc = _resolve_natal_and_utc_datetimes(birth_datetime, utc_offset_hours)
    
    natal_matrix = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_natal_utc, lat_deg=latitude, lon_deg=longitude, matrix_mode="cosmic_26"
    )
    
    if start_datetime_iso:
        dt_start = _parse_datetime(start_datetime_iso)
        if dt_start.tzinfo is None:
            dt_start = dt_start.replace(tzinfo=timezone.utc)
        else:
            dt_start = dt_start.astimezone(timezone.utc)
    else:
        dt_start = datetime.now(timezone.utc)

    days_ahead = max(1, min(180, days_ahead))
    step_hours = max(1, min(48, step_hours))
    total_steps = int((days_ahead * 24) // step_hours)

    windows = []
    for step in range(total_steps + 1):
        dt_cur = dt_start + timedelta(hours=step * step_hours)
        transits = hm.RealTimeTransitEngine.calculate_transits(
            dt_utc=dt_cur, lat_deg=latitude, lon_deg=longitude
        )
        interf = hm.RealTimeTransitEngine.evaluate_transit_interference(
            natal_matrix=natal_matrix,
            transits_dict=transits.get("positions", {}),
            dt_utc=dt_cur
        )
        ignitions = interf.get("direct_ignitions", [])
        channels = interf.get("live_activated_channels", [])
        antipodes = interf.get("transit_antipodes", [])

        if channels or antipodes or ignitions:
            windows.append({
                "timestamp_utc": dt_cur.strftime("%Y-%m-%d %H:%M UTC"),
                "direct_ignitions_count": len(ignitions),
                "live_channels_count": len(channels),
                "antipodes_count": len(antipodes),
                "live_activated_channels": channels,
                "transit_antipodes": antipodes,
                "direct_ignitions": [
                    {"vortex": ig.get("key"), "bodies": ig.get("transit_bodies"), "spheres": ig.get("natal_spheres")}
                    for ig in ignitions
                ],
                "weather_summary": interf.get("weather_summary")
            })

    return {
        "scan_range_days": days_ahead,
        "step_hours": step_hours,
        "total_active_windows": len(windows),
        "active_windows": windows[:50]
    }


# ── Expansión 2: Sinastría Multicuerpo / Topología de Grupo (Penta / WA) ──
@mcp.tool()
def analyze_group_topology(
    profile_names: Optional[List[str]] = None,
    custom_members: Optional[List[Dict[str, Any]]] = None,
    matrix_mode: str = "canonical"
) -> Dict[str, Any]:
    """
    Analiza la sinastría de equipo / multicuerpo (Penta / Grupo de 3 a 6 operadores):
      • Cobertura colectiva de los 64 vórtices (porcentaje y puntos ciegos sin cubrir).
      • Canales electromagnéticos completados por la sinergia colectiva del equipo.
      • Vórtices redundantes (activados por múltiples miembros).
      • Anillos de codones / clústeres bioquímicos dominantes en el grupo.
      
    Args:
        profile_names: Lista opcional de nombres de perfiles almacenados en profiles_vault.json.
        custom_members: Lista opcional de miembros arbitrarios con:
                        [{"name": str, "birth_datetime": str, "utc_offset": float, "lat": float, "lon": float}]
        matrix_mode: 'canonical' (11 esferas) o 'cosmic_26' (26 esferas).
    """
    members_data = []

    # 1. Cargar perfiles desde bóveda si se especifican nombres o si no hay miembros custom
    if profile_names or not custom_members:
        vault = hm.ProfilesVaultManager.load_vault()
        vault_by_name = {p.get("name", "").strip().lower(): p for p in vault}
        if profile_names:
            for p_name in profile_names:
                p_obj = vault_by_name.get(p_name.strip().lower())
                if p_obj:
                    members_data.append(p_obj)
        else:
            members_data.extend(vault)

    # 2. Agregar miembros custom si existen
    if custom_members:
        for cm in custom_members:
            members_data.append({
                "name": cm.get("name", "Operador"),
                "dt_str": cm.get("birth_datetime", "1990-05-21 14:30:00"),
                "utc_offset": cm.get("utc_offset", 0.0),
                "lat": cm.get("lat", 40.4168),
                "lon": cm.get("lon", -3.7038)
            })

    if len(members_data) < 2:
        return {"error": "Se requieren al menos 2 miembros para evaluar la topología de grupo."}

    # 3. Calcular matrices para cada miembro
    calculated_members = []
    collective_keys_map: Dict[int, List[str]] = {}

    for mem in members_data:
        m_name = mem.get("name", "Operador")
        dt_str = mem.get("dt_str", "")
        tz = float(mem.get("utc_offset", 0.0))
        lat = float(mem.get("lat", 40.4168))
        lon = float(mem.get("lon", -3.7038))

        _, dt_utc = _resolve_natal_and_utc_datetimes(dt_str, tz)
        mat = hm.CelestialMechanicsEngine.calculate_activation_matrix(
            dt_utc=dt_utc, lat_deg=lat, lon_deg=lon, matrix_mode=matrix_mode
        )
        active_keys = set()
        for s_name, s_data in mat.get("spheres", {}).items():
            k = s_data.get("key", 0)
            if k > 0:
                active_keys.add(k)
                collective_keys_map.setdefault(k, []).append(f"{m_name} ({s_name})")

        calculated_members.append({
            "name": m_name,
            "active_vortices": sorted(list(active_keys)),
            "vortices_count": len(active_keys)
        })

    all_active_keys = set(collective_keys_map.keys())
    all_64_keys = set(range(1, 65))
    blind_spots = sorted(list(all_64_keys - all_active_keys))

    # 4. Canales electromagnéticos completados por el equipo
    group_closed_channels = []
    for ka, kb, c_name in hm.NetworkSynastryEngine.CANONICAL_HARMONIC_CHANNELS:
        if ka in all_active_keys and kb in all_active_keys:
            group_closed_channels.append({
                "channel": c_name,
                "vortex_a": ka,
                "vortex_b": kb,
                "contributors_a": collective_keys_map[ka],
                "contributors_b": collective_keys_map[kb]
            })

    # 5. Vórtices redundantes (activados por 2 o más miembros)
    shared_vortices = [
        {"vortex_id": k, "bits": hm.CORE64_CATALOG.get(k, {}).get("bits", ""), "contributors": holders}
        for k, holders in collective_keys_map.items() if len(holders) > 1
    ]

    coverage_pct = round((len(all_active_keys) / 64.0) * 100.0, 1)

    return {
        "total_team_members": len(calculated_members),
        "members": calculated_members,
        "collective_coverage": {
            "active_vortices_count": len(all_active_keys),
            "coverage_percentage": coverage_pct,
            "active_vortices": sorted(list(all_active_keys)),
            "blind_spots_count": len(blind_spots),
            "blind_spots": blind_spots
        },
        "completed_group_channels_count": len(group_closed_channels),
        "completed_group_channels": group_closed_channels,
        "shared_vortices_redundancy": shared_vortices
    }


# ── Expansión 3: Puente Biomolecular de Codones de ARN y Aminoácidos IUPAC ──
@mcp.tool()
def get_amino_acid_bridge(vortex_id: int) -> Dict[str, Any]:
    """
    Mapea de forma determinista un Vórtice Resonante (1 a 64) con la biología molecular estándar:
      • Nombre y abreviatura IUPAC estándar (3 letras y 1 letra) del aminoácido.
      • Tripletes de codones de ARN mensajero asociados.
      • Propiedades fisicoquímicas del residuo.
      • Clúster genómico / Anillo de aminoácidos en la biosfera.
      • Vórtices socios que integran el mismo anillo biológico.
    """
    if vortex_id < 1 or vortex_id > 64:
        return {"error": "vortex_id debe estar entre 1 y 64."}

    v_data = hm.CORE64_CATALOG.get(vortex_id, {})
    ring_code = v_data.get("ring", "")
    bio = AMINO_ACID_MAP.get(ring_code, {
        "name_es": "Desconocido", "name_en": "Unknown", "iupac_3": "???", "iupac_1": "?", "codons": [], "chem_class": "No clasificado"
    })

    # Socios en el mismo anillo de codones
    partners = [k for k, v in hm.CORE64_CATALOG.items() if v.get("ring") == ring_code and k != vortex_id]

    return {
        "vortex_id": vortex_id,
        "bits": v_data.get("bits", "000000"),
        "cluster_code": ring_code,
        "cluster_name": hm.resolve_cluster_name(ring_code),
        "amino_acid": {
            "name_es": bio["name_es"],
            "name_en": bio["name_en"],
            "iupac_3letter": bio["iupac_3"],
            "iupac_1letter": bio["iupac_1"],
            "rna_codons": bio["codons"],
            "chemical_classification": bio["chem_class"]
        },
        "codon_ring_partner_vortices": partners
    }


@mcp.tool()
def get_hypercube_topology(vortex_id: int) -> Dict[str, Any]:
    """
    Calcula la topología de distancias de Hamming completa del Hipercubo Booleano 6D (2^6 = 64)
    partiendo del Vórtice Resonante indicado como centro de coordenadas.
    """
    if vortex_id < 1 or vortex_id > 64:
        return {"error": "vortex_id debe estar entre 1 y 64."}
        
    base_data = hm.CORE64_CATALOG.get(vortex_id, {})
    base_bits = base_data.get("bits", "000000")
    
    buckets: Dict[int, List[Dict[str, Any]]] = {i: [] for i in range(7)}
    
    for k_num, k_data in hm.CORE64_CATALOG.items():
        k_bits = k_data.get("bits", "000000")
        dh = hm.DiscreteParticleEngine.calculate_hamming_distance(base_bits, k_bits)
        buckets[dh].append({
            "vortex_id": k_num,
            "bits": k_bits,
            "coherence": k_data.get("coherencia", ""),
            "cluster": hm.resolve_cluster_name(k_data.get("ring", ""))
        })
        
    return {
        "center_vortex": {
            "id": vortex_id,
            "bits": base_bits,
            "coherence": base_data.get("coherencia", "")
        },
        "hamming_distribution": {
            f"DH_{i}": {
                "count": len(buckets[i]),
                "nodes": buckets[i]
            } for i in range(7)
        }
    }


@mcp.tool()
def list_vault_profiles() -> List[Dict[str, Any]]:
    """Obtiene la lista completa de perfiles guardados en la Bóveda Persistente (profiles_vault.json)."""
    return hm.ProfilesVaultManager.load_vault()


@mcp.tool()
def save_vault_profile(
    name: str,
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    country: str = "España",
    city: str = "Madrid",
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    topocentric: bool = True
) -> Dict[str, Any]:
    """Guarda o actualiza un perfil natal en la Bóveda Persistente (profiles_vault.json)."""
    dt_local = _parse_datetime(birth_datetime).replace(tzinfo=None)
    profile_data = {
        "name": name.strip(),
        "dt_str": dt_local.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": utc_offset_hours,
        "country": country,
        "city": city,
        "lat": latitude,
        "lon": longitude,
        "topocentric": topocentric
    }
    updated_list = hm.ProfilesVaultManager.save_profile(profile_data)
    return {
        "status": "success",
        "saved_profile": profile_data,
        "total_profiles_in_vault": len(updated_list)
    }


@mcp.tool()
def delete_vault_profile(name: str) -> Dict[str, Any]:
    """Elimina un perfil de la Bóveda Persistente (profiles_vault.json) por su nombre exacto."""
    updated_list = hm.ProfilesVaultManager.delete_profile(name)
    return {
        "status": "success",
        "deleted_profile": name,
        "remaining_profiles": len(updated_list)
    }


@mcp.tool()
def export_dossier_html(
    name: str,
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    entropy: float = 0.20,
    coherence: float = 0.85,
    resonance: float = 0.90,
    save_path: Optional[str] = None,
    return_raw_html: bool = False
) -> Dict[str, Any]:
    """
    Genera un Dossier Ejecutivo Soberano completo en formato HTML Bio-SciFi autocontenido.
    
    Por defecto guarda el archivo en disco (evitando consumir tokens de contexto al agente) y
    retorna un resumen ejecutivo. Si se requiere el HTML crudo, activar `return_raw_html=True`.
    """
    dt_local, dt_utc = _resolve_natal_and_utc_datetimes(birth_datetime, utc_offset_hours)
    
    cosmic_26 = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_utc,
        lat_deg=latitude,
        lon_deg=longitude,
        use_topocentric=True,
        matrix_mode="cosmic_26"
    )
    spheres = cosmic_26.get("spheres", {})
    bio_yield, regimen, prescripcion = hm.CelestialMechanicsEngine.calculate_biological_yield(
        entropy, coherence, resonance
    )
    
    safe_name = html.escape(name)
    
    table_rows = []
    for s_name, s_data in spheres.items():
        k_num = s_data.get("key", 0)
        line = s_data.get("line", 1)
        k_cat = hm.CORE64_CATALOG.get(k_num, {})
        bits = k_cat.get("bits", "000000")
        
        # Fix B: Clasificación determinista usando el campo estructurado 'origen'
        orig = s_data.get("origen", "")
        is_conscious = ("Natal" in orig or "Consciente" in orig) and ("Pre-natal" not in orig and "NOT" not in orig)
        tag_col = "#00f0ff" if is_conscious else "#f472b6"
        tag_txt = "CONSCIENTE (NATAL)" if is_conscious else "INCONSCIENTE (DESIGN)"
        
        table_rows.append(f"""
        <tr>
            <td style="font-weight: bold; color: {tag_col};">{html.escape(s_name)}</td>
            <td><span style="font-size: 10px; padding: 2px 6px; border-radius: 4px; background: rgba(255,255,255,0.06); color: {tag_col};">{tag_txt}</span></td>
            <td style="font-family: Consolas; font-weight: bold; color: #fbbf24;">V{k_num}.{line}</td>
            <td style="font-family: Consolas; color: #94a3b8;">{bits}</td>
            <td style="color: #ef4444;">{html.escape(k_cat.get('entropia', ''))}</td>
            <td style="color: #00f0ff; font-weight: bold;">{html.escape(k_cat.get('coherencia', ''))}</td>
            <td style="color: #a78bfa;">{html.escape(k_cat.get('resonancia', ''))}</td>
            <td style="color: #34d399; font-size: 11px;">{html.escape(hm.resolve_cluster_name(k_cat.get('ring', '')))}</td>
        </tr>
        """)
        
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>HEXA-MATRIX CORE-64 • Dossier Ejecutivo Soberano • {safe_name}</title>
<style>
  body {{
    background: #060a14;
    color: #e2e8f0;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    margin: 0;
    padding: 30px;
    line-height: 1.5;
  }}
  .container {{ max-width: 1100px; margin: 0 auto; }}
  .header {{
    border-bottom: 2px solid #00f0ff;
    padding-bottom: 18px;
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  h1 {{ margin: 0; font-size: 24px; color: #00f0ff; letter-spacing: 1px; }}
  .subtitle {{ color: #94a3b8; font-size: 13px; margin-top: 4px; }}
  .meta-box {{
    background: #0b1324;
    border: 1px solid rgba(0, 240, 255, 0.2);
    border-radius: 8px;
    padding: 18px;
    margin-bottom: 25px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 15px;
  }}
  .meta-item b {{ color: #00f0ff; font-size: 11px; text-transform: uppercase; display: block; }}
  .meta-item span {{ font-size: 14px; color: #f8fafc; font-family: Consolas, monospace; }}
  .card {{
    background: #0b1324;
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 25px;
  }}
  h2 {{ margin-top: 0; font-size: 16px; color: #fbbf24; border-bottom: 1px solid rgba(251, 191, 36, 0.2); padding-bottom: 8px; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 12px; }}
  th {{ background: #0f1c38; color: #93c5fd; padding: 10px 8px; text-align: left; font-weight: 600; border-bottom: 2px solid rgba(0,240,255,0.3); }}
  td {{ padding: 8px; border-bottom: 1px solid rgba(148, 163, 184, 0.1); }}
  tr:hover {{ background: rgba(0, 240, 255, 0.04); }}
  .footer {{ text-align: center; color: #64748b; font-size: 11px; margin-top: 40px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.08); }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div>
      <h1>⚡ HEXA-MATRIX CORE-64 • DOSSIER EJECUTIVO SOBERANO</h1>
      <div class="subtitle">Arquitectura Cuántica Bio-Informacional y Topología de 26 Nodos Cósmicos</div>
    </div>
    <div style="text-align: right; font-family: Consolas; color: #38bdf8; font-size: 12px;">
      OPERADOR: {safe_name.upper()}<br>
      VERSIÓN DIRECTIVA v3.0 SOBERANA
    </div>
  </div>

  <div class="meta-box">
    <div class="meta-item">
      <b>Fecha y Hora Natal (Local)</b>
      <span>{dt_local.strftime("%Y-%m-%d %H:%M:%S")} (UTC{'+' if utc_offset_hours >= 0 else ''}{utc_offset_hours:g})</span>
    </div>
    <div class="meta-item">
      <b>Instante Natal (UTC)</b>
      <span>{cosmic_26.get('utc_natal', '')}</span>
    </div>
    <div class="meta-item">
      <b>Solver Prenatal 88° (Diseño Inconsciente)</b>
      <span>{cosmic_26.get('utc_prenatal', '')} ({cosmic_26.get('kepler_days_prior', 0)} días antes)</span>
    </div>
    <div class="meta-item">
      <b>Coordenadas Geográficas</b>
      <span>Lat: {latitude:.4f}°, Lon: {longitude:.4f}°</span>
    </div>
  </div>

  <div class="card">
    <h2>🧪 VECTOR DE ESTADO TERMODINÁMICO COTIDIANO [E, C, R]</h2>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 15px; text-align: center;">
      <div style="background: rgba(239,68,68,0.1); border: 1px solid #ef4444; border-radius: 6px; padding: 10px;">
        <span style="font-size: 11px; color: #fca5a5;">ENTROPÍA (E)</span><br>
        <span style="font-size: 20px; font-weight: bold; color: #ef4444; font-family: Consolas;">{entropy:.2f}</span>
      </div>
      <div style="background: rgba(0,240,255,0.1); border: 1px solid #00f0ff; border-radius: 6px; padding: 10px;">
        <span style="font-size: 11px; color: #7dd3fc;">COHERENCIA (C)</span><br>
        <span style="font-size: 20px; font-weight: bold; color: #00f0ff; font-family: Consolas;">{coherence:.2f}</span>
      </div>
      <div style="background: rgba(167,139,250,0.1); border: 1px solid #a78bfa; border-radius: 6px; padding: 10px;">
        <span style="font-size: 11px; color: #ddd6fe;">RESONANCIA (R)</span><br>
        <span style="font-size: 20px; font-weight: bold; color: #a78bfa; font-family: Consolas;">{resonance:.2f}</span>
      </div>
      <div style="background: rgba(16,185,129,0.1); border: 1px solid #10b981; border-radius: 6px; padding: 10px;">
        <span style="font-size: 11px; color: #6ee7b7;">RENDIMIENTO BIOLÓGICO (Y)</span><br>
        <span style="font-size: 20px; font-weight: bold; color: #10b981; font-family: Consolas;">{bio_yield:.2f}</span>
      </div>
    </div>
    <p><b>Régimen Operativo:</b> <span style="color: #00f0ff;">{html.escape(regimen)}</span></p>
    <p><b>Prescripción Somática:</b> <em>{html.escape(prescripcion)}</em></p>
  </div>

  <div class="card">
    <h2>🌌 MATRIZ CÓSMICA TOTAL: 26 NODOS ACTIVOS (CONSCIENTE E INCONSCIENTE)</h2>
    <table>
      <thead>
        <tr>
          <th>Esfera / Nodo</th>
          <th>Plano</th>
          <th>Vórtice & Línea</th>
          <th>Palabra 6-Bit</th>
          <th>Entropía (Sombra)</th>
          <th>Coherencia (Don)</th>
          <th>Resonancia (Siddhi)</th>
          <th>Clúster Bioquímico</th>
        </tr>
      </thead>
      <tbody>
        {''.join(table_rows)}
      </tbody>
    </table>
  </div>

  <div class="footer">
    Hexa-Matrix Core-64 Fases AI • Ingeniería Cuántica y Efemérides Deterministas VSOP87 / Meeus • No Cloud Dependency
  </div>
</div>
</body>
</html>"""

    # Determinar ruta de guardado segura
    if not save_path:
        clean_filename = "".join(c for c in name if c.isalnum() or c in ("-", "_")).strip() or "operador"
        save_path = os.path.join(SCRIPT_DIR, f"dossier_{clean_filename}.html")
    
    target_path = os.path.abspath(save_path)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    resp = {
        "status": "success",
        "file_saved": target_path,
        "file_size_bytes": os.path.getsize(target_path),
        "subject": name,
        "total_spheres": len(spheres),
        "biological_yield_Y": bio_yield,
        "operating_regime": regimen
    }
    if return_raw_html:
        resp["html_content"] = html_content
    return resp


@mcp.tool()
def export_dossier_pdf(
    name: str,
    birth_datetime: str,
    utc_offset_hours: float = 0.0,
    latitude: float = 40.4168,
    longitude: float = -3.7038,
    entropy: float = 0.20,
    coherence: float = 0.85,
    resonance: float = 0.90,
    save_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Genera un Dossier Ejecutivo Soberano completo en formato PDF nativo utilizando ReportLab.
    
    Incluye tabla formateada de los 26 Nodos Cósmicos, vectores de estado termodinámico
    y síntesis ontológica.
    """
    if not REPORTLAB_AVAILABLE:
        return {"error": "ReportLab no está disponible en este entorno. Instalar con: pip install reportlab"}

    dt_local, dt_utc = _resolve_natal_and_utc_datetimes(birth_datetime, utc_offset_hours)
    
    cosmic_26 = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_utc,
        lat_deg=latitude,
        lon_deg=longitude,
        use_topocentric=True,
        matrix_mode="cosmic_26"
    )
    spheres = cosmic_26.get("spheres", {})
    bio_yield, regimen, prescripcion = hm.CelestialMechanicsEngine.calculate_biological_yield(
        entropy, coherence, resonance
    )

    if not save_path:
        clean_filename = "".join(c for c in name if c.isalnum() or c in ("-", "_")).strip() or "operador"
        save_path = os.path.join(SCRIPT_DIR, f"dossier_{clean_filename}.pdf")
    target_path = os.path.abspath(save_path)

    doc = SimpleDocTemplate(
        target_path,
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )
    styles = getSampleStyleSheet()
    
    st_title = ParagraphStyle("BioTitle", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, textColor=rl_colors.HexColor("#00f0ff"), spaceAfter=3)
    st_sub = ParagraphStyle("BioSub", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, textColor=rl_colors.HexColor("#94a3b8"), spaceAfter=8)
    st_h2 = ParagraphStyle("BioH2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, textColor=rl_colors.HexColor("#fbbf24"), spaceBefore=6, spaceAfter=4)
    st_body = ParagraphStyle("BioBody", parent=styles["Normal"], fontName="Helvetica", fontSize=8, leading=10.5, textColor=rl_colors.HexColor("#e2e8f0"))
    st_th = ParagraphStyle("BioTH", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=7.5, leading=9, textColor=rl_colors.HexColor("#93c5fd"))
    st_td = ParagraphStyle("BioTD", parent=styles["Normal"], fontName="Helvetica", fontSize=7, leading=8.5, textColor=rl_colors.HexColor("#e2e8f0"))

    elements = [
        Paragraph(f"⚡ HEXA-MATRIX CORE-64 • DOSSIER EJECUTIVO • {html.escape(name).upper()}", st_title),
        Paragraph("Arquitectura Cuántica Bio-Informacional y Topología de 26 Nodos Cósmicos", st_sub),
        Spacer(1, 4),
        Paragraph(f"<b>Instante Natal:</b> {dt_local.strftime('%Y-%m-%d %H:%M:%S')} (UTC{'+' if utc_offset_hours>=0 else ''}{utc_offset_hours:g}) | <b>Prenatal 88°:</b> {cosmic_26.get('utc_prenatal')} | <b>Lat:</b> {latitude:.4f}° <b>Lon:</b> {longitude:.4f}°", st_body),
        Spacer(1, 6),
        Paragraph(f"<b>Vector de Estado:</b> E={entropy:.2f} | C={coherence:.2f} | R={resonance:.2f} | <b>Rendimiento Biológico (Y):</b> {bio_yield:.2f}", st_h2),
        Paragraph(f"<b>Régimen Operativo:</b> {html.escape(regimen)}", st_body),
        Paragraph(f"<b>Prescripción Somática:</b> {html.escape(prescripcion)}", st_body),
        Spacer(1, 8),
        Paragraph("🌌 MATRIZ CÓSMICA TOTAL (26 NODOS ACTIVOS)", st_h2)
    ]

    table_data = [
        [
            Paragraph("<b>Esfera</b>", st_th),
            Paragraph("<b>Plano</b>", st_th),
            Paragraph("<b>Vórtice</b>", st_th),
            Paragraph("<b>Bits</b>", st_th),
            Paragraph("<b>Coherencia (Don)</b>", st_th),
            Paragraph("<b>Resonancia (Siddhi)</b>", st_th),
            Paragraph("<b>Clúster</b>", st_th)
        ]
    ]

    for s_name, s_data in spheres.items():
        k_num = s_data.get("key", 0)
        line = s_data.get("line", 1)
        k_cat = hm.CORE64_CATALOG.get(k_num, {})
        orig = s_data.get("origen", "")
        is_conscious = ("Natal" in orig or "Consciente" in orig) and ("Pre-natal" not in orig and "NOT" not in orig)
        plane_str = "Natal" if is_conscious else "Design"

        table_data.append([
            Paragraph(html.escape(s_name), st_td),
            Paragraph(plane_str, st_td),
            Paragraph(f"V{k_num}.{line}", st_td),
            Paragraph(k_cat.get("bits", ""), st_td),
            Paragraph(html.escape(k_cat.get("coherencia", "")), st_td),
            Paragraph(html.escape(k_cat.get("resonancia", "")), st_td),
            Paragraph(html.escape(hm.resolve_cluster_name(k_cat.get("ring", ""))), st_td)
        ])

    table = Table(table_data, colWidths=[42 * mm, 16 * mm, 16 * mm, 16 * mm, 32 * mm, 32 * mm, 32 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), rl_colors.HexColor("#0f1c38")),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("GRID", (0, 0), (-1, -1), 0.5, rl_colors.HexColor("#334155"))
    ]))
    elements.append(table)

    doc.build(elements)

    return {
        "status": "success",
        "pdf_saved": target_path,
        "file_size_bytes": os.path.getsize(target_path),
        "subject": name,
        "total_spheres": len(spheres),
        "biological_yield_Y": bio_yield
    }


# ══════════════════════════════════════════════════════════════════════════════
# RECURSOS MCP (RESOURCES)
# ══════════════════════════════════════════════════════════════════════════════

@mcp.resource("hexamatrix://vortices/catalog")
def resource_catalog() -> str:
    """Catálogo completo de los 64 Vórtices Resonantes en formato JSON."""
    return json.dumps(hm.CORE64_CATALOG, indent=2, ensure_ascii=False)


@mcp.resource("hexamatrix://channels/canonical")
def resource_canonical_channels() -> str:
    """Los 36 canales de resonancia electromagnética canónicos del sistema."""
    channels = [
        {"vortex_a": k1, "vortex_b": k2, "name": name}
        for k1, k2, name in hm.NetworkSynastryEngine.CANONICAL_HARMONIC_CHANNELS
    ]
    return json.dumps(channels, indent=2, ensure_ascii=False)


@mcp.resource("hexamatrix://vault/profiles")
def resource_vault_profiles() -> str:
    """Lista activa de perfiles natales persistidos en profiles_vault.json."""
    return json.dumps(hm.ProfilesVaultManager.load_vault(), indent=2, ensure_ascii=False)


@mcp.resource("hexamatrix://theory/manifesto")
def resource_theory_manifesto() -> str:
    """El manifiesto 'Espíritu, Algoritmo y Coherencia: El Punto Medio de Hexa-Matrix Core-64'."""
    doc_path = os.path.join(SCRIPT_DIR, "ESPIRITU_ALGORITMO_Y_COHERENCIA.md")
    if os.path.exists(doc_path):
        with open(doc_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Documento ESPIRITU_ALGORITMO_Y_COHERENCIA.md no localizado en el directorio raíz."


# ══════════════════════════════════════════════════════════════════════════════
# PROMPTS MCP
# ══════════════════════════════════════════════════════════════════════════════

@mcp.prompt()
def analyze_natal_matrix_prompt(subject_name: str, birth_datetime: str, utc_offset_hours: float) -> str:
    """
    Prompt estructurado para realizar una lectura ontológica y biofísica exhaustiva de la carta natal.
    """
    return f"""Eres Antigravity Hexa-Matrix Copilot, el asistente cuántico bio-informacional especializado en Hexa-Matrix Core-64.

Por favor, utiliza la herramienta `calculate_hologenetic_profile` para el sujeto:
• Nombre: {subject_name}
• Fecha y hora local: {birth_datetime}
• Huso horario: UTC{'+' if utc_offset_hours >= 0 else ''}{utc_offset_hours:g}
• matrix_mode: 'cosmic_26'

A partir de los datos calculados:
1. Analiza el Eje Cuántico Primario: Trabajo de Vida (Sol Natal) y Evolución (Tierra Natal).
2. Analiza el Diseño Inconsciente (88° solar arc): Resplandor y Propósito.
3. Evalúa la Esfera de la Atracción y su paralaje lunar topocéntrico.
4. Identifica los clústeres de codones (anillos de aminoácidos) predominantes con `get_amino_acid_bridge`.
5. Emite un protocolo de calibración somática basado en las frecuencias de Don (Coherencia) y Siddhi (Resonancia)."""


@mcp.prompt()
def synastry_coupling_prompt(name_a: str, birth_a: str, tz_a: float, name_b: str, birth_b: str, tz_b: float) -> str:
    """
    Prompt estructurado para auditar el acoplamiento bio-electromagnético y sinastría entre dos personas.
    """
    return f"""Eres Antigravity Hexa-Matrix Copilot.

Por favor, ejecuta la herramienta `analyze_network_synastry` con los siguientes datos:
• Sujeto A: {name_a} ({birth_a}, UTC{'+' if tz_a >= 0 else ''}{tz_a:g})
• Sujeto B: {name_b} ({birth_b}, UTC{'+' if tz_b >= 0 else ''}{tz_b:g})

Sintetiza:
1. El Índice de Resonancia Relacional (η_red).
2. Los Canales Electromagnéticos cerrados conjuntamente (chispas electromagnéticas activas).
3. Los Nodos de Compañerismo (vórtices idénticos activados).
4. Los Cruces Antípodas (inversión lógica NOT bit a bit, DH=6) y su manejo constructivo.
5. Recomendación práctica para optimizar la sinergia de equipo o pareja."""


@mcp.prompt()
def thermodynamic_calibration_prompt(entropy: float, coherence: float, resonance: float) -> str:
    """
    Prompt para diagnosticar el vector de estado cotidiano [E, C, R] y emitir prescripciones somáticas.
    """
    return f"""Eres Antigravity Hexa-Matrix Copilot.

Por favor, ejecuta la herramienta `calculate_thermodynamic_yield` con el vector de estado actual:
• Entropía (E): {entropy}
• Coherencia (C): {coherence}
• Resonancia (R): {resonance}

A partir del Rendimiento Biológico resultante (Y) y el régimen operativo diagnosticado:
1. Explica la dinámica de fluidos de energía y atención que está experimentando el operador.
2. Detalla el riesgo somático específico de este estado si se prolonga en el tiempo.
3. Proporciona una rutina concreta de micro-calibración en 3 pasos (respiración, anclaje somático y acción material inmediata)."""


# ══════════════════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ══════════════════════════════════════════════════════════════════════════════

def main():
    """Inicia el servidor MCP sobre transporte estándar stdio."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
