from flask import Flask, render_template, url_for
import pandas as pd
import plotly.express as px

app = Flask(__name__)

players_shots = pd.read_csv('players_shots.csv')
Situations = pd.read_csv('situations.csv')

# Fonction pour générer le pie chart pour une équipe spécifique

def generate_pie_chart(selected_team):
    team_data = Situations[Situations['Team'] == selected_team]

    fig = px.pie(
        team_data,
        names='Situation',
        values='Shots',
        title=f'Répartitions des Occasions - {selected_team}',
        labels={'Situation': 'Shot Situation'},
        hover_data=['Goals', 'xG'],
    )

    return fig


@app.route("/")

def home():
    
    teams = [
        { "id": 1, "name": "Nice" },
        { "id": 2, "name": "PSG" },
        { "id": 3, "name": "Monaco" },
        { "id": 4, "name": "Reims" },
        { "id": 5, "name": "Lille" },
        { "id": 6, "name": "Brest" },
        { "id": 7, "name": "LeHavre" },
        { "id": 8, "name": "Nantes" },
        { "id": 9, "name": "Marseille" },
        { "id": 10, "name": "Lens" },
        { "id": 11, "name": "Rennes" },
        { "id": 12, "name": "Strasbourg" },
        { "id": 13, "name": "Montpellier" },
        { "id": 14, "name": "Toulouse" },
        { "id": 15, "name": "Lorient" },
        { "id": 16, "name": "Metz" },
        { "id": 17, "name": "Clermont" },
        { "id": 18, "name": "Lyon" },
    ]

    # Triez les équipes par ordre alphabétique
    teams.sort(key=lambda x: x["name"])
    
    selected_team = "PSG"

    fig = generate_pie_chart(selected_team)

    pie_chart_html = fig.to_html(full_html=False)

    return render_template('home.html', teams=teams, selected_team=selected_team, players_shots=players_shots, Situations = Situations, pie_chart_data=pie_chart_html)

if __name__ == '__main__':
    app.run(debug= True)