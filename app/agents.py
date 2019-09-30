from app import db
from app.models import Agent

names = ['magnesium', 'chlorine', 'scandium', 'flerovium', 'tin']

def new_agent():
    agent = Agent()
    db.session.add(agent)
    db.session.commit()
    agent.name = names[agent.id-1]
    db.session.commit()
    return agent
