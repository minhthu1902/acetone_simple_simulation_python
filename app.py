# Acetone Production Simulation (Simplified Python Demo)
# Goal: Estimate required raw materials for 10,000 kg/year acetone via isopropanol dehydrogenation

import streamlit as st

# Constants and basic assumptions
ACETONE_YIELD = 0.85  # 85% yield efficiency
MW_ACETONE = 58.08  # g/mol
MW_ISOPROPANOL = 60.10  # g/mol

# Input form
st.title("🧪 Acetone Production Estimator")
st.markdown("Estimate raw material requirements for acetone production (based on simplified stoichiometry).")

acetone_kg = st.number_input("Target Acetone Production (kg/year):", min_value=1000, value=10000, step=1000)

# Basic stoichiometry: 
# C3H8O (isopropanol) → C3H6O (acetone) + H2

# Convert to mol and back-calculate isopropanol
acetone_mol = (acetone_kg * 1000) / MW_ACETONE
isopropanol_mol_needed = acetone_mol / ACETONE_YIELD
isopropanol_kg_needed = isopropanol_mol_needed * MW_ISOPROPANOL / 1000

# Output results
st.subheader("📊 Required Inputs")
st.write(f"**Isopropanol Required:** {isopropanol_kg_needed:,.2f} kg/year")
st.write("Assumes single-step dehydrogenation reaction with 85% yield.")

# Simple PFD (text-based, could be linked with SVG in frontend)
st.subheader("🧩 Simplified Process Flow Diagram (PFD)")
st.markdown("""
```
[Isopropanol Tank] → [Dehydrogenation Reactor] → [Separator] → [Acetone Product Tank]
                                                ↓
                                            [H2 Byproduct]
```
""")
