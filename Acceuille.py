import streamlit as st
import subprocess

def main():
    # Centrer le titre avec une balise div et une classe CSS
    st.markdown("<div style='text-align: center;'><h1>Bienvenue sur CODY+</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><p>Critical Optimizer for Decision Yielding</p></div>", unsafe_allow_html=True)
    
    
    # Centrer la description avec une balise div et une classe CSS
    st.markdown("<div style='text-align: center;'><p>CODY+ est une application développée par 3F1R consulting.</p></div>", unsafe_allow_html=True)
    
    # Ajouter une image ou un logo représentatif de votre projet
    st.image("cody_plus_logo.png", use_column_width=True)
    
    st.markdown("<div style='text-align: center;'><p>Qui vous aide à trouver le meilleur endroit où vivre en France en fonction de différents critères, tels que la sécurité, la présence de zones vertes, la densité de population, etc.</p></div>", unsafe_allow_html=True)
    
    # Ajouter des sections ou des points saillants pour mettre en avant les fonctionnalités clés de votre application
    st.write("fonctionnalité principale :")
    st.write("- Trouver la meilleur ville où vivre.")

    if st.button("Cody +", key="redirect_button"):
        st.markdown("<a href='https://3f1rcodyplus.streamlit.app' target='_blank'>Redirection vers l'application visuelle</a>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
