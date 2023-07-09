from flask import request
from lib.learn_list_generator import search_ddg_for_relevant_episodes




def select_relevant_episodes_from_search():
    q = request.args.get('q')
    if q is None:
        q = request.args.get('search_term')

    engine = request.args.get('engine', 'difflib')
    print(f'q {q}')
    return search_ddg_for_relevant_episodes(q, engine)
