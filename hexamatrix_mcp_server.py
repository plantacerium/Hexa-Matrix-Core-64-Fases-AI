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
  • Bóveda persistente de perfiles natales (profiles_vault.json).
  • Generación y exportación de Dossiers Ejecutivos Bio-SciFi (HTML y PDF).
══════════════════════════════════════════════════════════════════════════════
"""

import sys
import os
import json
import base64
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Union

# Asegurar que el directorio de este script esté en sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

# Importar el núcleo matemático y de datos de HexaMatrix
try:
    import hexa_matrix_core_64_fases_ai as hm
except ImportError as e:
    sys.stderr.write(f"Error importando hexa_matrix_core_64_fases_ai: {e}\n")
    raise

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
# UTILIDADES DE PARSEO Y FORMATEO
# ══════════════════════════════════════════════════════════════════════════════

def _parse_datetime(dt_str: str) -> datetime:
    """Parsea cadenas de fecha y hora en diversos formatos comunes."""
    dt_str = dt_str.strip()
    if dt_str.endswith("Z"):
        dt_str = dt_str[:-1]
    
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
    try:
        return datetime.fromisoformat(dt_str)
    except Exception as e:
        raise ValueError(f"Formato de fecha inválido '{dt_str}'. Use 'YYYY-MM-DD HH:MM:SS' o ISO-8601: {e}")


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
    
    # Calcular los 6 vecinos a distancia de Hamming DH = 1
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
            "code": k_data.get("ring", ""),
            "name": hm.resolve_cluster_name(k_data.get("ring", ""))
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
    
    Args:
        birth_datetime: Fecha y hora local de nacimiento (ej. '1990-05-21 14:30:00' o ISO-8601).
        utc_offset_hours: Huso horario local con respecto a UTC (ej. 2.0 para España CEST, -3.0 para Argentina).
        latitude: Latitud geográfica en grados decimales (por defecto Madrid: 40.4168).
        longitude: Longitud geográfica en grados decimales (por defecto Madrid: -3.7038).
        use_topocentric: Activar corrección de paralaje topocéntrico para la Luna (recomendado: True).
        matrix_mode: 'canonical' (11 esferas), 'nodes' (15 esferas), 'polar_not' (22 esferas),
                     o 'cosmic_26' (26 esferas: Matriz Cósmica Total Consciente + Inconsciente).
    """
    dt_local = _parse_datetime(birth_datetime)
    dt_utc = dt_local - timedelta(hours=utc_offset_hours)
    dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    
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
    
    Args:
        entropy: Coeficiente de Entropía/Sombra/Fricción somática E en rango [0.0, 1.0].
        coherence: Coeficiente de Coherencia/Don/Estructuración C en rango [0.0, 1.0].
        resonance: Coeficiente de Resonancia/Siddhi/Apertura de campo R en rango [0.0, 1.0].
        epsilon: Constante de amortiguación para evitar singularidad por división por cero (defecto: 0.05).
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
    
    Calcula la distancia de Hamming exacta (0 a 6 bits) y clasifica el acoplamiento en:
      • Antípoda (Inversión Lógica NOT, DH=6): Tensión bipolar máxima y eje de calibración.
      • Clúster Bioquímico Homólogo: Resonancia por simpatía biológica del anillo de aminoácidos.
      • En Paralelo (DH <= 2): Coexistencia simultánea de alta frecuencia.
      • En Serie (DH > 2): Pipeline de flujo de cascada.
    Indica riesgos de colapso entrópico y protocolos de remediación armónica.
    """
    if vortex_a < 1 or vortex_a > 64 or vortex_b < 1 or vortex_b > 64:
        return {"error": "Ambos vórtices deben estar comprendidos entre 1 y 64."}
        
    bridge = hm.DiscreteParticleEngine.analyze_bridge(vortex_a, vortex_b)
    
    data_a = hm.CORE64_CATALOG.get(vortex_a, {})
    data_b = hm.CORE64_CATALOG.get(vortex_b, {})
    
    # Comprobar si forman un canal canónico armónico cerrado
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
    
    Identifica:
      • Canales electromagnéticos cerrados conjuntamente (pares armónicos complementarios).
      • Nodos de compañerismo (activaciones en el mismo vórtice por ambos sujetos).
      • Cruces antípodas (inversión lógica NOT bit a bit, polaridad máxima).
      • Clústeres bioquímicos compartidos.
      • Índice de Resonancia Relacional de Red (η_red).
    """
    dt_a = _parse_datetime(birth_datetime_a) - timedelta(hours=utc_offset_a)
    dt_b = _parse_datetime(birth_datetime_b) - timedelta(hours=utc_offset_b)
    dt_a = dt_a.replace(tzinfo=timezone.utc)
    dt_b = dt_b.replace(tzinfo=timezone.utc)
    
    mat_a = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_a, lat_deg=lat_a, lon_deg=lon_a, matrix_mode=matrix_mode
    )
    mat_b = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_b, lat_deg=lat_b, lon_deg=lon_b, matrix_mode=matrix_mode
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
    
    Permite time-scrubbing temporal sumando o restando horas (offset_hours) respecto al instante actual o especificado.
    """
    if datetime_iso:
        dt_base = _parse_datetime(datetime_iso)
        if dt_base.tzinfo is None:
            dt_base = dt_base.replace(tzinfo=timezone.utc)
    else:
        dt_base = datetime.now(timezone.utc)
        
    dt_calc = dt_base + timedelta(hours=offset_hours)
    
    transits = hm.RealTimeTransitEngine.calculate_transits(
        dt_utc=dt_calc, lat_deg=latitude, lon_deg=longitude, use_topocentric=use_topocentric
    )
    
    # Enriquecer cada cuerpo en tránsito con metadatos de vórtice
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
    
    Detecta canales electromagnéticos completados por los planetas en tránsito y activación de
    antípodas NOT (disparadores de polaridad y tensión creativa).
    """
    dt_local = _parse_datetime(birth_datetime)
    dt_utc = dt_local - timedelta(hours=utc_offset_hours)
    dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    
    natal_matrix = hm.CelestialMechanicsEngine.calculate_activation_matrix(
        dt_utc=dt_utc, lat_deg=latitude, lon_deg=longitude, matrix_mode="cosmic_26"
    )
    
    if transit_datetime_iso:
        dt_tr = _parse_datetime(transit_datetime_iso)
        if dt_tr.tzinfo is None:
            dt_tr = dt_tr.replace(tzinfo=timezone.utc)
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


@mcp.tool()
def get_hypercube_topology(vortex_id: int) -> Dict[str, Any]:
    """
    Calcula la topología de distancias de Hamming completa del Hipercubo Booleano 6D (2^6 = 64)
    partiendo del Vórtice Resonante indicado como centro de coordenadas.
    
    Clasifica los 64 vórtices por su distancia de Hamming DH = 0..6:
      • DH = 0: El vórtice mismo (1 nodo).
      • DH = 1: Vecinos directos de mutación de 1 bit (6 nodos).
      • DH = 2: Vecinos a 2 bits (15 nodos).
      • DH = 3: Zona ecuatorial / ortogonal de máxima tensión (20 nodos).
      • DH = 4: Complementarios secundarios (15 nodos).
      • DH = 5: Pre-antípodas a 1 bit de inversión total (6 nodos).
      • DH = 6: Antípoda lógica NOT bit a bit (1 nodo).
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
    """
    Guarda o actualiza un perfil natal en la Bóveda Persistente (profiles_vault.json).
    """
    dt_local = _parse_datetime(birth_datetime)
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
    save_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Genera un Dossier Ejecutivo Soberano completo en formato HTML Bio-SciFi autocontenido.
    
    Incluye los 26 Nodos Cósmicos, vectores de estado termodinámico, síntesis ontológica
    de Espíritu ⟷ Algoritmo e instrucciones somáticas.
    """
    dt_local = _parse_datetime(birth_datetime)
    dt_utc = dt_local - timedelta(hours=utc_offset_hours)
    dt_utc = dt_utc.replace(tzinfo=timezone.utc)
    
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
    
    # Filas de la tabla de 26 nodos
    table_rows = []
    for s_name, s_data in spheres.items():
        k_num = s_data.get("key", 0)
        line = s_data.get("line", 1)
        k_cat = hm.CORE64_CATALOG.get(k_num, {})
        bits = k_cat.get("bits", "000000")
        is_conscious = "Design" not in s_name and "design" not in s_name and "Inconsciente" not in s_name and "Resplandor" not in s_name and "Propósito" not in s_name and "Atracción" not in s_name and "Abundancia" not in s_name
        tag_col = "#00f0ff" if is_conscious else "#f472b6"
        tag_txt = "CONSCIENTE (NATAL)" if is_conscious else "INCONSCIENTE (DESIGN)"
        
        table_rows.append(f"""
        <tr>
            <td style="font-weight: bold; color: {tag_col};">{s_name}</td>
            <td><span style="font-size: 10px; padding: 2px 6px; border-radius: 4px; background: rgba(255,255,255,0.06); color: {tag_col};">{tag_txt}</span></td>
            <td style="font-family: Consolas; font-weight: bold; color: #fbbf24;">V{k_num}.{line}</td>
            <td style="font-family: Consolas; color: #94a3b8;">{bits}</td>
            <td style="color: #ef4444;">{k_cat.get('entropia', '')}</td>
            <td style="color: #00f0ff; font-weight: bold;">{k_cat.get('coherencia', '')}</td>
            <td style="color: #a78bfa;">{k_cat.get('resonancia', '')}</td>
            <td style="color: #34d399; font-size: 11px;">{hm.resolve_cluster_name(k_cat.get('ring', ''))}</td>
        </tr>
        """)
        
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>HEXA-MATRIX CORE-64 • Dossier Ejecutivo Soberano • {name}</title>
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
      OPERADOR: {name.upper()}<br>
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
    <p><b>Régimen Operativo:</b> <span style="color: #00f0ff;">{regimen}</span></p>
    <p><b>Prescripción Somática:</b> <em>{prescripcion}</em></p>
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

    if save_path:
        target_path = os.path.abspath(save_path)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return {
            "status": "success",
            "file_saved": target_path,
            "bytes": len(html_content.encode("utf-8"))
        }
        
    return {
        "status": "success",
        "html_content": html_content,
        "bytes": len(html_content.encode("utf-8"))
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
4. Identifica los clústeres de codones (anillos de aminoácidos) predominantes.
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
