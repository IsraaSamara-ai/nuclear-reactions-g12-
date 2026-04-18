import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(
    page_title="التفاعلات النووية التفاعلية",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# قراءة ملف HTML
with open("nuclear_reactions.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# عرض التطبيق بكامل الشاشة
components.html(
    html_content,
    height=950,
    scrolling=True
)