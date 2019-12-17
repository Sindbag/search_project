from flask import Flask, render_template, request
from search.search import retrieve, score_documents, prepare_serp
from search.indexer import build_index
from search.query import Query
from time import time

app = Flask(__name__, template_folder='.')
build_index()


@app.route('/', methods=['GET'])
def index():
    start_time = time()

    query = Query(request.args.get('query'))

    # первичный список кандидатов
    documents = retrieve(query)
    # отсортированный список кандидатов
    scored_documents = score_documents(query, documents)

    results = prepare_serp(query, scored_documents)
    return render_template(
        'index.html',
        time="%.2f" % (time()-start_time),
        query=query.get_text(),
        search_engine_name='Yandex',
        results=results
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)



