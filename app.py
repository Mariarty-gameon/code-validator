import streamlit as st
import re

def check_code_criteria(code, criteria):
    """Prüft den Code anhand einer Checkliste von Kriterien."""
    results = {}
    for criterion, regex in criteria.items():
        match = re.search(regex, code)
        results[criterion] = bool(match)
    return results

# Checkliste der Code-Kriterien (Regex-Patterns für die Überprüfung)
criteria = {
    "Verwendung einer for-Schleife": r"\bfor\b",
    "Verwendung einer if-Bedingung": r"\bif\b",
    "Definieren einer Funktion": r"\bdef\s+\w+\s*\(",
    "Verwendung einer Liste": r"\[.*\]",
    "Import einer Bibliothek": r"\bimport\s+\w+",
}

# Streamlit Web-App
st.title("Code-Validierungsmaschine")
st.write("Fügen Sie Ihren Code unten ein und klicken Sie auf 'Validieren'.")

user_code = st.text_area("Code eingeben:")
if st.button("Validieren"):
    if user_code.strip():
        results = check_code_criteria(user_code, criteria)
        st.subheader("Ergebnisse")
        for criterion, met in results.items():
            st.write(f"✅ {criterion}" if met else f"❌ {criterion}")
    else:
        st.warning("Bitte geben Sie einen Code ein.")
