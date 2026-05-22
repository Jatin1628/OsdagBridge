from osdagbridge.core.utils.common import (
    KEY_SPAN,
    KEY_SKEW_ANGLE,
    KEY_GIRDER,
    KEY_CROSS_BRACING,
    KEY_END_DIAPHRAGM,
    KEY_DECK_CONCRETE_GRADE_BASIC,
    KEY_TS_OVERALL_WIDTH,
    KEY_TS_NO_OF_GIRDERS,
    KEY_TS_GIRDER_SPACING,
    KEY_TS_DECK_OVERHANG,
    KEY_TS_DECK_THICKNESS,
    KEY_GIRDER_DEPTH,
    KEY_GIRDER_TOP_FLANGE_WIDTH,
    KEY_GIRDER_TOP_FLANGE_THICKNESS,
    KEY_GIRDER_BOTTOM_FLANGE_WIDTH,
    KEY_GIRDER_BOTTOM_FLANGE_THICKNESS,
    KEY_GIRDER_WEB_THICKNESS,
    KEY_GIRDER_SECTIONAL_AREA,
    KEY_GIRDER_SECTIONAL_IZ,
    KEY_CROSS_BRACING_TYPE,
    KEY_CROSS_BRACING_SECTION,
    KEY_CROSS_BRACING_SPACING,
    KEY_END_DIAPHRAGM_TYPE,
    KEY_END_DIAPHRAGM_BRACING_SECTION_DESIGNATION,
    KEY_DS_STUD_DIAMETER,
    KEY_DS_STUD_HEIGHT,
    KEY_DS_STUD_ULTIMATE_STRENGTH,
    KEY_DS_STUD_YIELD_STRENGTH,
    KEY_DS_STUD_COUNT,
    KEY_DS_REINF_MATERIAL,
    KEY_DS_REINF_BOUNDS,
    KEY_DS_TOP_CLEAR_COVER,
    KEY_DS_BOTTOM_CLEAR_COVER,
)

# ── Empty value sentinel ──────────────────────────────────────────────────────

EMPTY = "-"


# ── Formatting helpers ────────────────────────────────────────────────────────

def _mpa(value):
    """Convert Pa → MPa, rounded to 2 dp. Returns EMPTY on any failure."""
    try:
        return round(float(value) / 1e6, 2)
    except Exception:
        return EMPTY


def _num(value, decimals=2):
    """Round a numeric value. Returns EMPTY on any failure."""
    try:
        return round(float(value), decimals)
    except Exception:
        return EMPTY


def _mm(value, decimals=1):
    """Convert metres → mm, rounded. Returns EMPTY on any failure."""
    try:
        return round(float(value) * 1e3, decimals)
    except Exception:
        return EMPTY


def _mm2(value, decimals=1):
    """Convert m² → mm², rounded. Returns EMPTY on any failure."""
    try:
        return round(float(value) * 1e6, decimals)
    except Exception:
        return EMPTY


def _mm4(value):
    """Convert m⁴ → mm⁴ in scientific notation string. Returns EMPTY on any failure."""
    try:
        v = float(value) * 1e12
        return round(v, 3)
    except Exception:
        return EMPTY


def _val(value):
    """Return value as-is, or EMPTY if missing/blank."""
    return value if value not in (None, "", [], {}) else EMPTY


def _has(*values):
    """Return True only if every value is present (not None / blank)."""
    return all(v not in (None, "", [], {}) for v in values)


# ── Resolver registry ─────────────────────────────────────────────────────────
# Populated at the bottom of this file after all resolver functions are defined.
# Maps table schema id → callable(input_dict, bridge) → dict | None

RESOLVER_MAP: dict[str, callable] = {}


def resolve_table(table_id: str, input_dict: dict, bridge) -> dict | None:
    """
    Look up and call the resolver for table_id.
    Returns None if no resolver exists or if the resolver itself returns None
    (meaning required keys were absent).
    """
    fn = RESOLVER_MAP.get(table_id)
    return fn(input_dict, bridge) if fn else None


# ── Resolvers — Bridge Configuration ─────────────────────────────────────────

def resolve_bridge_config_summary(input_dict: dict, bridge=None) -> dict | None:
    overall_width  = input_dict.get(KEY_TS_OVERALL_WIDTH)
    span           = input_dict.get(KEY_SPAN)
    no_of_girders  = input_dict.get(KEY_TS_NO_OF_GIRDERS)
    girder_spacing = input_dict.get(KEY_TS_GIRDER_SPACING)
    deck_overhang  = input_dict.get(KEY_TS_DECK_OVERHANG)
    skew_angle     = input_dict.get(KEY_SKEW_ANGLE, 0)

    if not _has(overall_width, span, no_of_girders, girder_spacing, deck_overhang):
        return None

    return {
        "id":    "bridge_configuration_summary",
        "label": "Bridge Configuration Summary",
        "columns": [
            "Overall Width (m)",
            "Span (m)",
            "No. of Girders",
            "Girder Spacing (m)",
            "Deck Overhang (m)",
            "Skew Angle (deg)",
        ],
        "rows": [[
            _num(overall_width),
            _num(span),
            _val(no_of_girders),
            _num(girder_spacing),
            _num(deck_overhang),
            _num(skew_angle),
        ]],
    }


def resolve_material_properties_steel(input_dict: dict, bridge=None) -> dict | None:
    girder_grade   = input_dict.get(KEY_GIRDER)
    bracing_grade  = input_dict.get(KEY_CROSS_BRACING)
    diaphragm_grade = input_dict.get(KEY_END_DIAPHRAGM)

    if not _has(girder_grade):
        return None

    # Pull steel properties from bridge DB lookup if bridge is available
    try:
        steel = bridge._build_material_props().steel_prop
        fu = _mpa(steel.Fu)
        fy = _mpa(steel.Fy)
        e  = _mpa(steel.E)
        g  = _mpa(steel.E / (2 * (1 + steel.v)))
        v  = _num(steel.v)
    except Exception:
        fu = fy = e = g = v = EMPTY

    def _row(component, grade):
        return [
            component,
            _val(grade),
            fu, fy, e, g, v,
            11.7,
        ]

    return {
        "id":    "material_properties_steel",
        "label": "Material Properties - Steel",
        "columns": [
            "Component",
            "Grade",
            "Ultimate Tensile Strength, Fᵤ (MPa)",
            "Yield Strength, Fᵧ (MPa)",
            "Modulus of Elasticity, E (MPa)",
            "Modulus of Rigidity, G (MPa)",
            "Poisson's Ratio, ν",
            "Thermal Expansion Coefficient (×10⁻⁶/°C)",
        ],
        "rows": [
            _row("Girder",        girder_grade),
            _row("Cross Bracing", bracing_grade),
            _row("End Diaphragm", diaphragm_grade),
        ],
    }


def resolve_material_properties_concrete(input_dict: dict, bridge=None) -> dict | None:
    concrete_grade = input_dict.get(KEY_DECK_CONCRETE_GRADE_BASIC)

    if not _has(concrete_grade):
        return None

    try:
        mat   = bridge._build_material_props()
        cp    = mat.concrete_prop
        fck   = _num(cp.fck)
        fctm  = _num(cp.fctm)
        ecm   = _num(cp.Ecm)
        # Modular ratio: E_steel / E_concrete (both in MPa)
        steel_e_mpa   = _mpa(mat.steel_prop.E)
        modular_ratio = (
            round(float(steel_e_mpa) / float(ecm), 2)
            if isinstance(steel_e_mpa, (int, float))
            and isinstance(ecm, (int, float))
            and float(ecm) > 0
            else EMPTY
        )
    except Exception:
        fck = fctm = ecm = modular_ratio = EMPTY

    # Density and Poisson's ratio are material constants for normal concrete
    density       = 25.0   # kN/m³
    poissons_ratio = 0.20

    def _row(component):
        return [
            component,
            _val(concrete_grade),
            fck,
            fctm,
            ecm,
            modular_ratio,
            density,
            poissons_ratio,
        ]

    return {
        "id":    "material_properties_concrete",
        "label": "Material Properties - Concrete",
        "columns": [
            "Component",
            "Grade",
            "Characteristic Compressive Strength, fₖ (MPa)",
            "Mean Tensile Strength, fₜₘ (MPa)",
            "Secant Modulus of Elasticity, Eₘ (MPa)",
            "Modular Ratio",
            "Density (kN/m³)",
            "Poisson's Ratio, ν",
        ],
        "rows": [
            _row("Deck Slab"),
        ],
    }


# ── Resolvers — Member Definitions ───────────────────────────────────────────

def resolve_girder_section_properties(input_dict: dict, bridge=None) -> dict | None:
    depth     = input_dict.get(KEY_GIRDER_DEPTH)
    bf_top    = input_dict.get(KEY_GIRDER_TOP_FLANGE_WIDTH)
    tf_top    = input_dict.get(KEY_GIRDER_TOP_FLANGE_THICKNESS)
    bf_bot    = input_dict.get(KEY_GIRDER_BOTTOM_FLANGE_WIDTH)
    tf_bot    = input_dict.get(KEY_GIRDER_BOTTOM_FLANGE_THICKNESS)
    tw        = input_dict.get(KEY_GIRDER_WEB_THICKNESS)
    area      = input_dict.get(KEY_GIRDER_SECTIONAL_AREA)
    iz        = input_dict.get(KEY_GIRDER_SECTIONAL_IZ)
    n_girders = input_dict.get(KEY_TS_NO_OF_GIRDERS)

    if not _has(depth, bf_top, tf_top, bf_bot, tf_bot, tw, area, iz, n_girders):
        return None

    try:
        n = int(n_girders)
    except Exception:
        return None

    row = [
        EMPTY,                  # Girder label — filled per-row below
        _mm(depth),
        _mm(bf_top),
        _mm(bf_bot),
        _mm(tf_top),
        _mm(tf_bot),
        _mm(tw),
        _mm2(area),
        _mm4(iz),
        EMPTY,                  # Cross-section class — not yet resolved from inputs
    ]

    rows = []
    for i in range(1, n + 1):
        r = list(row)
        r[0] = f"Girder {i}"
        rows.append(r)

    return {
        "id":    "girder_section_properties",
        "label": "Girder Section Properties",
        "columns": [
            "Girder",
            "Depth, d (mm)",
            "Top Flange Width, bfₜₒₚ (mm)",
            "Bottom Flange Width, bfᵦₒₜ (mm)",
            "Top Flange Thickness, tfₜₒₚ (mm)",
            "Bottom Flange Thickness, tfᵦₒₜ (mm)",
            "Web Thickness, tᵤ (mm)",
            "Cross-sectional Area, A (mm²)",
            "Second Moment of Area (z-axis), Iᵤ (mm⁴)",
            "Cross-section Class",
        ],
        "rows": rows,
    }


def resolve_cross_bracing_section_properties(input_dict: dict, bridge=None) -> dict | None:
    cb_type    = input_dict.get(KEY_CROSS_BRACING_TYPE)
    cb_section = input_dict.get(KEY_CROSS_BRACING_SECTION)
    cb_spacing = input_dict.get(KEY_CROSS_BRACING_SPACING)

    if not _has(cb_type, cb_spacing):
        return None

    return {
        "id":    "cross_bracing_section_properties",
        "label": "Cross Bracing Section Properties",
        "columns": [
            "Type",
            "Section",
            "Spacing (m)",
        ],
        "rows": [[
            _val(cb_type),
            _val(cb_section),
            _num(cb_spacing),
        ]],
    }


def resolve_end_diaphragm_section_properties(input_dict: dict, bridge=None) -> dict | None:
    ed_type    = input_dict.get(KEY_END_DIAPHRAGM_TYPE)
    ed_section = input_dict.get(KEY_END_DIAPHRAGM_BRACING_SECTION_DESIGNATION)

    if not _has(ed_type):
        return None

    return {
        "id":    "end_diaphragm_section_properties",
        "label": "End Diaphragm Section Properties",
        "columns": [
            "Type",
            "Section",
        ],
        "rows": [[
            _val(ed_type),
            _val(ed_section),
        ]],
    }


def resolve_shear_stud_properties(input_dict: dict, bridge=None) -> dict | None:
    diameter  = input_dict.get(KEY_DS_STUD_DIAMETER)
    height    = input_dict.get(KEY_DS_STUD_HEIGHT)
    fu        = input_dict.get(KEY_DS_STUD_ULTIMATE_STRENGTH)
    fy        = input_dict.get(KEY_DS_STUD_YIELD_STRENGTH)
    count     = input_dict.get(KEY_DS_STUD_COUNT)

    if not _has(diameter, height, fu, fy, count):
        return None

    return {
        "id":    "shear_stud_properties",
        "label": "Shear Stud Properties",
        "columns": [
            "Diameter (mm)",
            "Height (mm)",
            "Ultimate Tensile Strength, Fᵤ (MPa)",
            "Yield Strength, Fᵧ (MPa)",
            "Number per Section",
        ],
        "rows": [[
            _num(diameter),
            _num(height),
            _num(fu),
            _num(fy),
            _val(count),
        ]],
    }


def resolve_deck_slab_properties(input_dict: dict, bridge=None) -> dict | None:
    thickness    = input_dict.get(KEY_TS_DECK_THICKNESS)
    reinf_size   = input_dict.get(KEY_DS_REINF_BOUNDS)
    reinf_mat    = input_dict.get(KEY_DS_REINF_MATERIAL)
    top_cover    = input_dict.get(KEY_DS_TOP_CLEAR_COVER)
    bot_cover    = input_dict.get(KEY_DS_BOTTOM_CLEAR_COVER)

    if not _has(thickness):
        return None

    # Format reinforcement label as "Grade @ spacing" when both are available,
    # otherwise show whichever part is present.
    def _reinf_label(size, mat):
        if _has(size) and _has(mat):
            return f"{mat} — {size}mm"
        return _val(size or mat)

    return {
        "id":    "deck_slab_properties",
        "label": "Deck Slab Properties",
        "columns": [
            "Thickness (mm)",
            "Reinforcement Material",
            "Reinforcement Size (mm)",
            "Top Cover (mm)",
            "Bottom Cover (mm)",
        ],
        "rows": [[
            _mm(thickness),
            _val(reinf_mat),
            _val(reinf_size),
            _num(top_cover),
            _num(bot_cover),
        ]],
    }


# ── Registry — must be after all resolver definitions ────────────────────────

RESOLVER_MAP: dict[str, callable] = {
    "bridge_configuration_summary":       resolve_bridge_config_summary,
    "material_properties_steel":          resolve_material_properties_steel,
    "material_properties_concrete":       resolve_material_properties_concrete,
    "girder_section_properties":          resolve_girder_section_properties,
    "cross_bracing_section_properties":   resolve_cross_bracing_section_properties,
    "end_diaphragm_section_properties":   resolve_end_diaphragm_section_properties,
    "shear_stud_properties":              resolve_shear_stud_properties,
    "deck_slab_properties":               resolve_deck_slab_properties,
}