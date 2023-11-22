from flask import Flask, render_template, url_for
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


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
    return render_template('home.html')

@app.route("/stats")

def stats():
    
    teams = [
    { "id": 1, "name": "Nice", "logo": "Nice.png" },
    { "id": 2, "name": "PSG", "logo": "PSG.png" },
    { "id": 3, "name": "Monaco", "logo": "Monaco.png" },
    { "id": 4, "name": "Reims", "logo": "Reims.png" },
    { "id": 5, "name": "Lille", "logo": "Lille.png" },
    { "id": 6, "name": "Brest", "logo": "Brest.png" },
    { "id": 7, "name": "LeHavre", "logo": "LeHavre.png" },
    { "id": 8, "name": "Nantes", "logo": "Nantes.png" },
    { "id": 9, "name": "Marseille", "logo": "Marseille.png" },
    { "id": 10, "name": "Lens", "logo": "Lens.png" },
    { "id": 11, "name": "Rennes", "logo": "Rennes.png" },
    { "id": 12, "name": "Strasbourg", "logo": "Strasbourg.png" },
    { "id": 13, "name": "Montpellier", "logo": "Montpellier.png" },
    { "id": 14, "name": "Toulouse", "logo": "Toulouse.png" },
    { "id": 15, "name": "Lorient", "logo": "Lorient.png" },
    { "id": 16, "name": "Metz", "logo": "Metz.png" },
    { "id": 17, "name": "Clermont", "logo": "Clermont.png" },
    { "id": 18, "name": "Lyon", "logo": "Lyon.png" },
]

    # Triez les équipes par ordre alphabétique
    teams.sort(key=lambda x: x["name"])
    
    selected_team = " "

    fig = generate_pie_chart(selected_team)

    pie_chart_html = fig.to_html(full_html=False)

    return render_template('stats.html', teams=teams, selected_team=selected_team, players_shots=players_shots, Situations = Situations, pie_chart_data=pie_chart_html)

if __name__ == '__main__':
    app.run(debug= True)