"""
Default data schema for Generate Results Table dialog.

Purpose:
Centralized source of table structure (columns) for all result tables.
Rows are intentionally empty — resolvers in generate_results_values_builder.py
populate them with live values when the user has entered the required inputs.
"""

EMPTY = "-"

GENERATE_RESULTS_DEFAULTS = {

    "model_definition": {
        "id": "model_definition",
        "label": "Model Definition",

        "bridge_configuration": {
            "id": "bridge_configuration",
            "label": "Bridge Configuration",

            "bridge_configuration_summary": {
                "id": "bridge_configuration_summary",
                "label": "Bridge Configuration Summary",
                "columns": [
                    "Overall Width (m)",
                    "Span (m)",
                    "No. of Girders",
                    "Girder Spacing (m)",
                    "Deck Overhang (m)",
                    "Skew Angle (deg)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "material_properties_steel": {
                "id": "material_properties_steel",
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
                    ["Girder",        EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                    ["Cross Bracing", EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                    ["End Diaphragm", EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "material_properties_concrete": {
                "id": "material_properties_concrete",
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
                    ["Deck Slab", EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "load_definitions": {
            "id": "load_definitions",
            "label": "Load Definitions",

            "permanent_load_summary": {
                "id": "permanent_load_summary",
                "label": "Permanent Load Summary",
                "columns": [
                    "Dead Load, DL (kN/m)",
                    "Wearing Surface Load, DW (kN/m)",
                    "Secondary Impact Dead Load, SIDL (kN/m)",
                    "Total Load (kN/m)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "live_load_definitions": {
                "id": "live_load_definitions",
                "label": "Live Load Definitions",
                "columns": [
                    "Vehicle Class",
                    "Impact Factor",
                ],
                "rows": [
                    [EMPTY, EMPTY],
                ],
            },

            "wind_load_parameters": {
                "id": "wind_load_parameters",
                "label": "Wind Load Parameters",
                "columns": [
                    "Basic Wind Speed, Vᵦ (m/s)",
                    "Design Wind Speed at Height z, Vᵤ (m/s)",
                    "Design Wind Pressure at Height z, Pᵤ (N/m²)",
                    "Drag Coefficient, Cᴅ",
                    "Lift Coefficient, Cᴸ",
                    "Gust Factor, G",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "seismic_load_parameters": {
                "id": "seismic_load_parameters",
                "label": "Seismic Load Parameters",
                "columns": [
                    "Zone",
                    "Seismic Zone Factor, Z",
                    "Importance Factor, I",
                    "Spectral Acceleration / g, Sₐ/g",
                    "Horizontal Acceleration Coefficient, Aₕ",
                    "Vertical Acceleration Coefficient, Aᵥ",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "temperature_load_parameters": {
                "id": "temperature_load_parameters",
                "label": "Temperature Load Parameters",
                "columns": [
                    "Maximum Temperature (°C)",
                    "Minimum Temperature (°C)",
                    "Temperature Rise Change, ΔTᵣᵢₛₑ (°C)",
                    "Temperature Fall Change, ΔTfₐₗₗ (°C)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "load_combinations": {
                "id": "load_combinations",
                "label": "Load Combinations",
                "columns": [
                    "Combination",
                    "Expression",
                ],
                "rows": [
                    [EMPTY, EMPTY],
                ],
            },
        },

        "member_definitions": {
            "id": "member_definitions",
            "label": "Member Definitions",

            "girder_section_properties": {
                "id": "girder_section_properties",
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
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "cross_bracing_section_properties": {
                "id": "cross_bracing_section_properties",
                "label": "Cross Bracing Section Properties",
                "columns": [
                    "Type",
                    "Section",
                    "Spacing (m)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY],
                ],
            },

            "end_diaphragm_section_properties": {
                "id": "end_diaphragm_section_properties",
                "label": "End Diaphragm Section Properties",
                "columns": [
                    "Type",
                    "Section",
                ],
                "rows": [
                    [EMPTY, EMPTY],
                ],
            },

            "shear_stud_properties": {
                "id": "shear_stud_properties",
                "label": "Shear Stud Properties",
                "columns": [
                    "Diameter (mm)",
                    "Height (mm)",
                    "Ultimate Tensile Strength, Fᵤ (MPa)",
                    "Yield Strength, Fᵧ (MPa)",
                    "Number per Section",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "deck_slab_properties": {
                "id": "deck_slab_properties",
                "label": "Deck Slab Properties",
                "columns": [
                    "Thickness (mm)",
                    "Top Reinforcement",
                    "Bottom Reinforcement",
                    "Top Cover (mm)",
                    "Bottom Cover (mm)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },
    },

    "analysis_results": {
        "id": "analysis_results",
        "label": "Analysis Results",

        "load_effects_girder": {
            "id": "load_effects_girder",
            "label": "Load Effects - Girder",

            "bending_moment_envelope": {
                "id": "bending_moment_envelope",
                "label": "Bending Moment Diagram - Envelope",
                "columns": [
                    "Girder",
                    "Maximum Bending Moment, Mₘₐₓ (kNm)",
                    "Minimum Bending Moment, Mₘᵢₙ (kNm)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY],
                ],
            },

            "shear_force_envelope": {
                "id": "shear_force_envelope",
                "label": "Shear Force Diagram - Envelope",
                "columns": [
                    "Girder",
                    "Maximum Shear Force, Vₘₐₓ (kN)",
                    "Minimum Shear Force, Vₘᵢₙ (kN)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY],
                ],
            },

            "bending_moment_by_load_case": {
                "id": "bending_moment_by_load_case",
                "label": "Bending Moment - By Load Case",
                "columns": [
                    "Girder",
                    "Dead Load, DL (kNm)",
                    "Wearing Surface, DW (kNm)",
                    "Secondary Impact Dead Load, SIDL (kNm)",
                    "Live Load, LL (kNm)",
                    "Earthquake Load, EL (kNm)",
                    "Wind Load, WL (kNm)",
                    "Temperature Load, TL (kNm)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "shear_force_by_load_case": {
                "id": "shear_force_by_load_case",
                "label": "Shear Force - By Load Case",
                "columns": [
                    "Girder",
                    "Dead Load, DL (kN)",
                    "Wearing Surface, DW (kN)",
                    "Secondary Impact Dead Load, SIDL (kN)",
                    "Live Load, LL (kN)",
                    "Earthquake Load, EL (kN)",
                    "Wind Load, WL (kN)",
                    "Temperature Load, TL (kN)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "deflections": {
            "id": "deflections",
            "label": "Deflections",

            "deflection_live_load": {
                "id": "deflection_live_load",
                "label": "Deflection - Live Load",
                "columns": [
                    "Girder",
                    "Deflection due to Live Load, δ_ₗᵢᵥₑ (mm)",
                    "Permissible Limit",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "deflection_total_load": {
                "id": "deflection_total_load",
                "label": "Deflection - Total Load",
                "columns": [
                    "Girder",
                    "Total Deflection, δₜₒₜₐₗ (mm)",
                    "Permissible Limit",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "stress_results": {
            "id": "stress_results",
            "label": "Stress Results",

            "stress_steel_service": {
                "id": "stress_steel_service",
                "label": "Stress in Structural Steel - Service",
                "columns": [
                    "Girder",
                    "Compression (MPa)",
                    "Tension (MPa)",
                    "Shear (MPa)",
                    "Allowable",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "stress_concrete_service": {
                "id": "stress_concrete_service",
                "label": "Stress in Concrete Deck - Service",
                "columns": [
                    "Girder",
                    "Stress in Concrete, σc (MPa)",
                    "Allowable Stress (MPa)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY],
                ],
            },

            "stress_reinf_service": {
                "id": "stress_reinf_service",
                "label": "Stress in Reinforcement - Service",
                "columns": [
                    "Girder",
                    "Stress in Reinforcement, σᵣₑᵢₙf (MPa)",
                    "Allowable Stress (MPa)",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY],
                ],
            },
        },
    },

    "design_results": {
        "id": "design_results",
        "label": "Design Results",

        "uls_checks": {
            "id": "uls_checks",
            "label": "ULS Checks",

            "flexural_resistance_check": {
                "id": "flexural_resistance_check",
                "label": "Flexural Resistance Check",
                "columns": [
                    "Girder",
                    "Ultimate Bending Moment, Mᵤ (kNm)",
                    "Design Bending Moment, Mᵈ (kNm)",
                    "Demand to Capacity Ratio, DCR",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "shear_resistance_check": {
                "id": "shear_resistance_check",
                "label": "Shear Resistance Check",
                "columns": [
                    "Girder",
                    "Ultimate Shear Force, Vᵤ (kN)",
                    "Design Shear Force, Vᵈ (kN)",
                    "Demand to Capacity Ratio, DCR",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "bending_shear_interaction_check": {
                "id": "bending_shear_interaction_check",
                "label": "Bending-Shear Interaction Check",
                "columns": [
                    "Girder",
                    "Ultimate Bending Moment, Mᵤ (kNm)",
                    "Reduced Design Bending Resistance, Mᵈᵥ (kNm)",
                    "Demand to Capacity Ratio, DCR",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "lateral_torsional_buckling_check": {
                "id": "lateral_torsional_buckling_check",
                "label": "Lateral Torsional Buckling Check - Construction Stage",
                "columns": [
                    "Girder",
                    "Ultimate Bending Moment, Mᵤ (kNm)",
                    "LTB Design Buckling Resistance, Mᵦ (kNm)",
                    "LTB Reduction Factor, χ_LT",
                    "Non-Dimensional Slenderness, λ̄_LT",
                    "Demand to Capacity Ratio, DCR",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "sls_checks": {
            "id": "sls_checks",
            "label": "SLS Checks",

            "deflection_control_live": {
                "id": "deflection_control_live",
                "label": "Deflection Control - Live Load",
                "columns": [
                    "Girder",
                    "Deflection due to Live Load, δ_ₗᵢᵥₑ (mm)",
                    "Permissible Limit",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "deflection_control_total": {
                "id": "deflection_control_total",
                "label": "Deflection Control - Total Load",
                "columns": [
                    "Girder",
                    "Total Deflection, δₜₒₜₐₗ (mm)",
                    "Span, L (mm)",
                    "Permissible Limit, L/600 (mm)",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "max_stress_steel": {
                "id": "max_stress_steel",
                "label": "Maximum Stress Limitation - Steel",
                "columns": [
                    "Girder",
                    "Stress in Steel, σₛ (MPa)",
                    "Yield Strength, fyk (MPa)",
                    "Allowable Stress, 0.9·fyk (MPa)",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    ["Girder 1", 180, 350, 315, "IRC 22 Cl. 604.3.1", "PASS"],
                    ["Girder 2", 176, 350, 315, "IRC 22 Cl. 604.3.1", "PASS"],
                    ["Girder 3", 176, 350, 315, "IRC 22 Cl. 604.3.1", "PASS"],
                    ["Girder 4", 180, 350, 315, "IRC 22 Cl. 604.3.1", "PASS"],
                ],
            },

            "max_stress_concrete": {
                "id": "max_stress_concrete",
                "label": "Maximum Stress Limitation - Concrete",
                "columns": [
                    "Girder",
                    "Stress in Concrete, σc (MPa)",
                    "Characteristic Compressive Strength, fck (MPa)",
                    "Allowable Stress, 0.48·fck (MPa)",
                    "Status",
                ],
                "rows": [
                    ["Girder 1", 12.5, 40, 19.2, "PASS"],
                    ["Girder 2", 12.1, 40, 19.2, "PASS"],
                    ["Girder 3", 12.1, 40, 19.2, "PASS"],
                    ["Girder 4", 12.5, 40, 19.2, "PASS"],
                ],
            },

            "max_stress_reinforcement": {
                "id": "max_stress_reinforcement",
                "label": "Maximum Stress Limitation - Reinforcement",
                "columns": [
                    "Girder",
                    "Stress in Reinforcement, σᵣₑᵢₙf (MPa)",
                    "Characteristic Yield Strength, fyk (MPa)",
                    "Allowable Stress, 0.8·fyk (MPa)",
                    "Status",
                ],
                "rows": [
                    ["Girder 1", 220, 500, 400, "PASS"],
                    ["Girder 2", 215, 500, 400, "PASS"],
                    ["Girder 3", 215, 500, 400, "PASS"],
                    ["Girder 4", 220, 500, 400, "PASS"],
                ],
            },
        },

        "fatigue_checks": {
            "id": "fatigue_checks",
            "label": "Fatigue Checks",

            "fatigue_assessment_girder": {
                "id": "fatigue_assessment_girder",
                "label": "Fatigue Assessment - Girder",
                "columns": [
                    "Girder",
                    "Stress Range, Δσ (MPa)",
                    "Fatigue Limit, ffd (MPa)",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "fatigue_assessment_shear_connectors": {
                "id": "fatigue_assessment_shear_connectors",
                "label": "Fatigue Assessment - Shear Connectors",
                "columns": [
                    "Stud Group",
                    "Shear Stress Range, Δτ (MPa)",
                    "Fatigue Limit for Shear, τfd (MPa)",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "shear_connector_design": {
            "id": "shear_connector_design",
            "label": "Shear Connector Design",

            "shear_connector_capacity": {
                "id": "shear_connector_capacity",
                "label": "Shear Connector Capacity",
                "columns": [
                    "Girder",
                    "Stud Diameter, d (mm)",
                    "Stud Height, h (mm)",
                    "Ultimate Tensile Strength of Stud, fu (MPa)",
                    "Characteristic Compressive Strength, fck (MPa)",
                    "Modulus of Elasticity of Concrete, Ec (MPa)",
                    "Nominal Capacity per Stud, Qu (kN)",
                    "Design Capacity per Stud, Qd (kN)",
                    "No. of Studs per Section",
                    "Total Design Capacity, ΣQd (kN)",
                    "Clause Reference",
                ],
                "rows": [
                    ["Girder 1", 20, 100, 495, 40, 34000, 98.5, 83.7, 2, 167.4, "IRC 22 Cl. 606.3.1"],
                    ["Girder 2", 20, 100, 495, 40, 34000, 98.5, 83.7, 2, 167.4, "IRC 22 Cl. 606.3.1"],
                    ["Girder 3", 20, 100, 495, 40, 34000, 98.5, 83.7, 2, 167.4, "IRC 22 Cl. 606.3.1"],
                    ["Girder 4", 20, 100, 495, 40, 34000, 98.5, 83.7, 2, 167.4, "IRC 22 Cl. 606.3.1"],
                ],
            },

            "shear_connector_spacing_uls": {
                "id": "shear_connector_spacing_uls",
                "label": "Shear Connector Spacing - ULS Strength",
                "columns": [
                    "Girder",
                    "Design Vertical Shear, VL (kN)",
                    "Total Stud Capacity, ΣQd (kN)",
                    "Spacing from Vertical Shear, SL1 (mm)",
                    "Full Shear Connection Force, H (kN)",
                    "Spacing from Full Shear Force, SL2 (mm)",
                    "Governing ULS Spacing, min(SL1, SL2) (mm)",
                    "Clause Reference",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "shear_connector_spacing_fatigue": {
                "id": "shear_connector_spacing_fatigue",
                "label": "Shear Connector Spacing - Fatigue",
                "columns": [
                    "Girder",
                    "Fatigue Shear Range, Vr (kN)",
                    "Fatigue Capacity per Stud, Qr (kN)",
                    "No. of Studs per Section",
                    "Fatigue Governing Spacing, SR (mm)",
                    "Clause Reference",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "governing_shear_connector_spacing": {
                "id": "governing_shear_connector_spacing",
                "label": "Governing Shear Connector Spacing",
                "columns": [
                    "Girder",
                    "ULS Spacing, SL (mm)",
                    "Fatigue Spacing, SR (mm)",
                    "Governing Spacing, min(SL, SR) (mm)",
                    "Max Permissible — 600 mm",
                    "Max Permissible — 3·t_slab (mm)",
                    "Max Permissible — 4·h_stud (mm)",
                    "Adopted Permissible Limit (mm)",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },

            "shear_connector_detailing_checks": {
                "id": "shear_connector_detailing_checks",
                "label": "Shear Connector Detailing Checks",
                "columns": [
                    "Girder",
                    "Stud Diameter, d (mm)",
                    "Flange Thickness, tf (mm)",
                    "d ≤ 2·tf Check (mm)",
                    "Stud Height, h (mm)",
                    "h ≥ 4·d Check (mm)",
                    "Longitudinal Edge Distance (mm)",
                    "Min. Edge Distance Required (mm)",
                    "Slab Embedment Above Stud (mm)",
                    "Min. Embedment Required (mm)",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "transverse_and_crack_checks": {
            "id": "transverse_and_crack_checks",
            "label": "Transverse And Crack Checks",

            "transverse_shear_check": {
                "id": "transverse_shear_check",
                "label": "Transverse Shear Check in Concrete Slab",
                "columns": [
                    "Girder",
                    "Design Longitudinal Shear per Unit Length, VL (kN/m)",
                    "Concrete Shear Resistance, 0.9·L·√fck (kN/m)",
                    "Reinforcement Shear Resistance, 0.8·fyk·Ast (kN/m)",
                    "Total Shear Resistance, VRd (kN/m)",
                    "Demand to Capacity Ratio, DCR",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    ["Girder 1", 285, 198, 245, 443, 0.64, "IRC 22 Cl. 606.10", "PASS"],
                    ["Girder 2", 278, 198, 245, 443, 0.63, "IRC 22 Cl. 606.10", "PASS"],
                    ["Girder 3", 278, 198, 245, 443, 0.63, "IRC 22 Cl. 606.10", "PASS"],
                    ["Girder 4", 285, 198, 245, 443, 0.64, "IRC 22 Cl. 606.10", "PASS"],
                ],
            },

            "crack_width_check": {
                "id": "crack_width_check",
                "label": "Crack Width Check",
                "columns": [
                    "Girder",
                    "Calculated Crack Width, wₖ (mm)",
                    "Permissible Crack Width Limit (mm)",
                    "Minimum Reinforcement Area, As,min (mm²)",
                    "Reinforcement Area Provided, As,prov (mm²)",
                    "Bar Diameter, φ (mm)",
                    "Bar Spacing, s (mm)",
                    "Clause Reference",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },

        "design_summary": {
            "id": "design_summary",
            "label": "Design Summary",

            "design_results_summary": {
                "id": "design_results_summary",
                "label": "Design Results Summary",
                "columns": [
                    "Member",
                    "Check Name",
                    "Demand (Units as applicable)",
                    "Capacity (Units as applicable)",
                    "Demand to Capacity Ratio, DCR",
                    "Status",
                ],
                "rows": [
                    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                ],
            },
        },
    },
}