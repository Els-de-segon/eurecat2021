import flask
from flask import request, jsonify, make_response

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# Endpoint per posar noves dades dels sensors
@app.route("/api/measurements/add", methods=["POST"])
def create_collection():
    args = request.args
    
    # Mirem que ens donin 3 arguments
    if args.__len__() != 3: return make_response("ERROR: 3 Arguments needed", 400)
    
    values = {
        "aigua": args.get("aigua"),
        "aire":  args.get("aire"),
        "amoniac": args.get("amoniac")}
    
    for key in args:
        elem = args[key]
        if not __isValid(elem): return make_response(f"ERROR: bad argument -> {key}", 400)
    
    resultat = str(False)## Canviar per el metode de ml

    res = make_response(resultat, 201)
    return res

# Pasat un element comprova si es un float major de 0
def __isValid(element):
    try:
        value = float(element)
        return value >= 0
    except:
        return False


if __name__ == "__main__":
    app.run()
    
