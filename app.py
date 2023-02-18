import streamlit as st

import utils.display as udisp

import src.pages.home
import src.pages.aboutkm
import src.pages.youtube
import src.pages.articles




MENU = {
    "Home" : src.pages.home,
    "About" : src.pages.aboutkm,
    #"Contact" : src.pages.ads,
    "Articles" : src.pages.articles,
    "YouTube Videos" : src.pages.youtube,
    #"Black History Month Projects" : src.pages.games,
    #"Facebook Chatbots" : src.pages.follow,
    #"Instagram Filters" : src.pages.friends,
    }

def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("Pick an option...", list(MENU.keys()))

    menu = MENU[menu_selection]

    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)
    st.sidebar.title("")
    st.sidebar.title("Contact Me")
    st.sidebar.info(
        "[LinkedIn](https://www.linkedin.com/in/emmanuel-acheampong/)"
        +"\n"+
        "\n"+
        "[Github](https://github.com/acheamponge)"
        +"\n"+
        "\n"+
        "[Twitter](https://twitter.com/achampiong)"
         +"\n"+
        "\n"+
        "[Medium](https://medium.com/@achampion.emma/)"
    )
if __name__ == "__main__":
    main()