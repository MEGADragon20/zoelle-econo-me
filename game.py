from flask import Blueprint, render_template, request
import redis, json, uuid

class Country:
    def __init__(self, name):
        self.name = name
        self.gdp = 0
        self.population = 0
        self.emoji = ""
        self.tarifs = 0.05

    def asign_attributes(self):
        if self.name == 'Deutschland':
            self.gdp = 4000
            self.population = 80
            self.emoji = "🇩🇪"
        elif self.name == 'USA':
            self.gdp = 21000
            self.population = 331
            self.emoji = "🇺🇸"
        elif self.name == 'China':
            self.gdp = 14000
            self.population = 1439
            self.emoji = "🇨🇳"
        elif self.name == "Schweiz":
            self.gdp = 15
            self.population = 3
            self.emoji = "🇨🇭"
        elif self.name == "Japan":
            self.gdp = 350
            self.population = 113
            self.emoji = "🇯🇵"
        elif self.name == "VAE":
            self.gdp = 400
            self.emoji = "🇦🇪"
            self.population = 9

    @classmethod
    def create_country(cls, name):
        country = cls(name)
        country.asign_attributes()
        return country

game_bp = Blueprint('game', __name__, template_folder='templates')

REDIS_URL = 'redis://localhost:6379/0'

def save_redis(data):
    r = redis.from_url(REDIS_URL)
    r.set('game_data', json.dumps(data))

def load_redis():
    r = redis.from_url(REDIS_URL)
    data = r.get('game_data')
    return json.loads(data) if data else None

@game_bp.route('/choose_country')
def choose_country():
    return render_template('choose_country.html')

@game_bp.route('/start', methods=['POST'])
def play():
    state = load_redis()
    id = str(uuid.uuid4())
    country = request.form
    state[id] = {'country': country}
    save_redis(state)
    return render_template('play.html')