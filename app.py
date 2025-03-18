import streamlit as st
import re

def check_code_criteria(code, criteria):
    """Prüft den Code anhand einer Checkliste von Kriterien."""
    results = {}
    for criterion, regex in criteria.items():
        match = re.search(regex, code)
        results[criterion] = bool(match)
    return results

# HTML-Kriterien (Regex-Patterns für die Überprüfung)
html_criteria = {
    "Verwendung eines <h1>-Tags": r"<h1>.*?</h1>",
    "Verwendung eines <img>-Tags": r"<img\s+.*?>",
    "Verwendung eines <a>-Tags mit href": r"<a\s+href=",
    "Verwendung einer <p>-Tags": r"<p>.*?</p>",
    "Verwendung einer <p>-Tags": r"<p>.*?</p>",
}

# CSS-Kriterien (Regex-Patterns für die Überprüfung)
css_criteria = {
    "Verwendung einer Klasse (.class)": r"\.\w+\s*{",
    "Verwendung einer ID (#id)": r"#\w+\s*{",
    "Festlegen einer Farbe (color:)": r"color:\s*#[0-9a-fA-F]{3,6}|color:\s*\w+;",
    "Verwendung eines Flexbox-Layouts": r"display:\s*flex;",
    "Verwendung einer Media Query": r"@media\s*\(.*?\)\s*{",
}

# Streamlit Web-App
st.title("Code-Validierungsmaschine")
st.write("Fügen Sie Ihren Code unten ein und klicken Sie auf 'Validieren'.")

# Auswahl, ob HTML oder CSS geprüft werden soll
type_of_code = st.selectbox("Wählen Sie die Code-Art:", ["HTML", "CSS"])

user_code = st.text_area("Code eingeben:")
if st.button("Validieren"):
    if user_code.strip():
        # Die richtige Kriterienliste basierend auf der Auswahl laden
        selected_criteria = html_criteria if type_of_code == "HTML" else css_criteria
        results = check_code_criteria(user_code, selected_criteria)
        
        st.subheader("Ergebnisse")
        for criterion, met in results.items():
            st.write(f"✅ {criterion}" if met else f"❌ {criterion}")
    else:
        st.warning("Bitte geben Sie einen Code ein.")
