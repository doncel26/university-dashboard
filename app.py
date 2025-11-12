import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="University Dashboard", layout="wide")
st.title("🎓 University Dashboard - Data Visualization")
st.markdown("Explora los datos académicos y visualiza métricas clave del proyecto universitario.")

st.sidebar.header("📁 Cargar datos")
uploaded_file = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Datos cargados correctamente.")
    st.write("Vista previa de los datos:")
    st.dataframe(df.head())
else:
    st.info("Sube un archivo CSV para comenzar.")
    st.stop()

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
if len(numeric_cols) < 2:
    st.warning("Necesitas al menos dos columnas numéricas para graficar.")
    st.stop()

x_col = st.selectbox("Selecciona la variable del eje X", numeric_cols)
y_col = st.selectbox("Selecciona la variable del eje Y", numeric_cols)

st.subheader("📊 Gráfico estático (Matplotlib)")
fig, ax = plt.subplots()
ax.scatter(df[x_col], df[y_col], color="teal", alpha=0.7)
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_title("Relación entre variables (Matplotlib)")
st.pyplot(fig)

st.subheader("🧩 Gráfico interactivo (Plotly)")
fig_plotly = px.scatter(df, x=x_col, y=y_col, color=y_col,
                        title="Visualización Interactiva (Plotly)",
                        template="plotly_dark")
st.plotly_chart(fig_plotly, use_container_width=True)

st.subheader("📈 Estadísticas descriptivas")
st.dataframe(df.describe())

st.markdown("---")
st.markdown("Desarrollado por **Melanny Doncel** 🦋 | Dashboard Universitario 2025")
