import streamlit as st
import re

def check_code_criteria(code, criteria):
    """Prüft den Code anhand einer Checkliste von Kriterien."""
    results = {}
    for criterion, regex in criteria.items():
        match = re.search(regex, code, re.DOTALL)
        results[criterion] = bool(match)
    return results

# HTML-Kriterien (Regex-Patterns für die Überprüfung)
html_criteria = {
    "Korrekte Grundstruktur (doctype, html, head, body)": r"<!DOCTYPE html>.*?<html>.*?<head>.*?</head>.*?<body>.*?</body>.*?</html>",
    "Verlinkung CSS-Stylesheet": r"<link\s+rel=[\'\"]stylesheet[\'\"]\s+href=[\'\"].*?stylesheet.css[\'\"]",
    "Paragraph (<p>)": r"<p[^>]*>.*?</p>",
    "Tab-Titel (<title>)": r"<title>.*?</title>",
    "Überschrift(en) (<h1> - <h6>)": r"<h[1-6]>.*?</h[1-6]>",
    "Bild (<img>)": r"<img\s+.*?>",
    "Link (<a href>)": r"<a\s+href=",
    "Link öffnet neues Fenster (target=_blank)": r"<a\s+[^>]*target=[\'\"]_blank[\'\"]",
    "Bild oder Icon als anklickbarer Link": r"<a\s+[^>]*>(\s*<img\s+.*?>\s*)+</a>",
    "Class-Attribut verwendet": r"class=[\'\"].*?[\'\"]",
    "ID-Attribut verwendet": r"id=[\'\"].*?[\'\"]"
}

# CSS-Kriterien (Regex-Patterns für die Überprüfung)
css_criteria = {
    "Schriftgröße (font-size)": r"font-size:\s*[^;]+;",
    "Schriftart (font-family)": r"font-family:\s*[^;]+;",
    "Farbe (color)": r"color:\s*[^;]+;",
    "Hintergrundfarbe (background-color)": r"background-color:\s*[^;]+;",
    "Breite (width)": r"width:\s*[^;]+;",
    "Höhe (height)": r"height:\s*[^;]+;",
    "Text-Ausrichtung (text-align)": r"text-align:\s*[^;]+;",
    "Abgerundete Ecken (border-radius)": r"border-radius:\s*[^;]+;",
    "Box-Schatten (box-shadow)": r"box-shadow:\s*[^;]+;",
    "Verlauf (linear-gradient)": r"linear-gradient\(",
    "Padding": r"padding(-[a-z]+)?:\s*[^;]+;",
    "Margin": r"margin(-[a-z]+)?:\s*[^;]+;",
    "Flexbox (display: flex)": r"display:\s*flex;",
    "Ausrichtung mit justify-content": r"justify-content:\s*[^;]+;",
    "Ausrichtung mit align-items": r"align-items:\s*[^;]+;"
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
