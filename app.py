import plotly.express as px
from shiny.express import input, ui
from shiny import reactive, render
from shinywidgets import render_plotly
import seaborn as sns
import pandas as pd 
from shinyswatch import theme 
from faicons import icon_svg


#Load the dataset
titanic_df = sns.load_dataset("titanic")

#Title 
ui.page_opts(title="Cera's Titanic Dashboard", fillable=True)

#Add a theme 
theme.superhero()

#Create the sidebar
with ui.sidebar(open="open"):
    with ui.accordion():
        with ui.accordion_panel("Survival"):
            ui.input_selectize("alive", "Did They Survive?", 
                               list(titanic_df['alive'].unique()))
        with ui.accordion_panel("Gender"):
            ui.input_selectize("sex", "Sex of the Passenger", list(titanic_df["sex"].unique()))
        with ui.accordion_panel("Class"):
            ui.input_selectize("selected_class", "Class of the Passenger", list(titanic_df['class'].unique()))


def filtered_df():
    survival = input.alive() 
    sex = input.sex()  
    selected_class = input.selected_class()  
    
    # Filter the dataframe based on the input values
    filtered_df = titanic_df[
        (titanic_df['alive'] == survival) &
        (titanic_df['sex'] == sex) &
        (titanic_df['class'] == selected_class)
    ]
    
    return filtered_df

with ui.card():
        ui.card_header("Titanic Data")
        @render.data_frame  
        def titanic1_df():
            return render.DataGrid(titanic_df) 

@render.plot(alt="A Seaborn histogram on penguin body mass in grams.")  
def plot():  
    ax = sns.histplot(data=titanic_df, x="class", y="age")  
    ax.set_title("Passenger Class vs. Age")
    ax.set_xlabel("Class")
    ax.set_ylabel("Age")
    return ax  

