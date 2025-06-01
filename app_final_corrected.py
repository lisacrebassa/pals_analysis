import streamlit as st
st.set_page_config(page_title="Analyse des Pals - Palworld", layout="wide")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des fichiers nettoyés
@st.cache_data
def load_data():
    combat_df = pd.read_csv("Cleaned_Combat_Attribute_Table.csv")
    job_df = pd.read_csv("Cleaned_Job_Skills_Table.csv")
    hidden_df = pd.read_csv("hidden_pallu_attributes_cleaned.csv")
    refresh_df = pd.read_csv("Cleaned_Pal_Refresh_Levels.csv")
    tower_df = pd.read_csv("Cleaned_Tower_BOSS_Attributes.csv")
    ordinary_df = pd.read_csv("pals_with_inferred_boss_stats.csv")
    return combat_df, job_df, hidden_df, refresh_df, tower_df, ordinary_df

combat_df, job_df, hidden_df, refresh_df, tower_df, ordinary_df = load_data()

st.title("📊 Analyse stratégique de Palworld")
st.markdown("Optimisez vos combats et votre production grâce à cette interface interactive.")

# Onglets principaux
menu = st.sidebar.radio("Navigation", ["Stratégie de Combat", "Gestion du Campement", "Zones & Boss"])

if menu == "Stratégie de Combat":
    st.header("⚔️ Optimisation des Stratégies de Combat")

    combat_df['total_combat'] = combat_df[['hp', 'melee_attack', 'remote_attack', 'defense']].sum(axis=1)
    top_pals = combat_df.sort_values("total_combat", ascending=False).head(10)

    st.subheader("Top 10 des Pals les plus puissants")
    st.dataframe(top_pals[['name', 'total_combat']])

    st.subheader("Corrélations entre attributs de combat")
    fig, ax = plt.subplots()
    sns.heatmap(combat_df[['hp', 'melee_attack', 'remote_attack', 'defense']].corr(), annot=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Taille vs Puissance de combat")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=combat_df, x="volume_size", y="total_combat", ax=ax2)
    st.pyplot(fig2)

elif menu == "Gestion du Campement":
    st.header("🏕️ Optimisation de la Production au Campement")

    numeric_skills = job_df.select_dtypes(include='number').drop(columns=['handling_speed', 'rarity'], errors='ignore')
    job_df['nb_skills'] = (numeric_skills > 0).sum(axis=1)
    job_df['composite'] = job_df['handling_speed'] * job_df['nb_skills']

    top_workers = job_df.sort_values("composite", ascending=False).head(10)
    st.subheader("Top 10 des Pals les plus efficaces pour le travail")
    st.dataframe(top_workers[['english_name', 'handling_speed', 'nb_skills']])

    # Produits utiles au campement via pasture
    st.subheader("Pals produisant des ressources utiles (ranch)")
    prod_pals = hidden_df[hidden_df['pasture'] > 0]
    st.dataframe(prod_pals[['tribe', 'pasture']])

    # Pals actifs la nuit
    st.subheader("Pals actifs la nuit")
    nocturnes = hidden_df[hidden_df['nocturnal'] == 1]
    st.write(f"Nombre de Pals nocturnes : {len(nocturnes)}")
    st.dataframe(nocturnes[['tribe', 'rarity', 'foodamount']])

elif menu == "Zones & Boss":
    st.header("🌍 Zones d'apparition & Boss")

    st.subheader("Distribution des niveaux d'apparition")
    fig3, ax3 = plt.subplots()
    sns.histplot(refresh_df['min_level'], bins=20, ax=ax3)
    st.pyplot(fig3)

    st.subheader("Top 10 zones d'apparition")
    top_zones = refresh_df['refresh_area'].value_counts().head(10).index
    refresh_df['zone_grouped'] = refresh_df['refresh_area'].apply(lambda z: z if z in top_zones else 'Autres')
    fig4, ax4 = plt.subplots()
    sns.countplot(data=refresh_df, y='zone_grouped', order=refresh_df['zone_grouped'].value_counts().index, ax=ax4)
    st.pyplot(fig4)

    # Bosses
    st.subheader("Boss les plus puissants")
    tower_df['total_power'] = tower_df[['hp', 'melee_attack', 'remote_attack', 'defense', 'support']].sum(axis=1)
    cols = ['hp', 'melee_attack', 'remote_attack', 'defense', 'support']
    available_cols = [col for col in cols if col in ordinary_df.columns]
    ordinary_df['total_power'] = ordinary_df[available_cols].sum(axis=1)

    top_tower = tower_df.sort_values("total_power", ascending=False).head(1)
    top_ordinary = ordinary_df.sort_values("total_power", ascending=False).head(1)

    st.write("**Tower Boss le plus puissant :**", top_tower.iloc[0]['name'])
    st.write("**Ordinary Boss le plus puissant :**", top_ordinary.iloc[0]['name'])
