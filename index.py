from flask import Flask,request,send_from_directory,Response
from pathlib import Path
import response

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name=None):
    return ""

################################################################ -- product -- ################################################################

@app.route('/product',methods = ['PUT','GET','POST','DELETE'])
def product():
    if(request.method=='GET'):
        limit = request.args.get('limit')
        page = request.args.get('page')
        return response.product_list_response(limit,page)
    elif(request.method=='PUT'):
        return response.product_create(request.data)
    elif(request.method=='POST'):
        return response.product_update(request.data)
    elif(request.method=='DELETE'):
        return response.product_delete(request.data)
    else:
        return response.method_not_found()

@app.route('/product/<param>',methods = ['GET'])
def productSub(param):
    if(request.method=='GET'):
        if(param=='id'):
            id = request.args.get('id')
            return response.product_by_id_response(id)
        elif(param=='uid'):
            uid = request.args.get('uid')
            return response.product_by_id_response(uid,True)
        else:
            return response.method_not_found()
    else:
        return response.method_not_found()

################################################################################################################################################

################################################################ -- priceType -- ################################################################

@app.route('/priceType',methods = ['PUT','GET','POST','DELETE'])
def priceType():
    if(request.method=='GET'):
        limit = request.args.get('limit')
        page = request.args.get('page')
        return response.pricetype_list_response(limit,page)
    elif(request.method=='PUT'):
        return response.pricetype_create(request.data)
    elif(request.method=='POST'):
        return response.pricetype_update(request.data)
    elif(request.method=='DELETE'):
        return response.pricetype_delete(request.data)
    else:
        return response.method_not_found()

@app.route('/priceType/<param>',methods = ['GET'])
def priceTypeSub(param):
    if(request.method=='GET'):
        if(param=='id'):
            id = request.args.get('id')
            return response.pricetype_by_id_response(id)
        elif(param=='uid'):
            uid = request.args.get('uid')
            return response.pricetype_by_id_response(uid,True)
        else:
            return response.method_not_found()
    else:
        return response.method_not_found()

################################################################################################################################################

################################################################ -- product price -- ################################################################

@app.route('/productPrice/<param>',methods = ['GET'])
def productPrice(param):
    if param == 'priceType':
        id = request.args.get('id')
        return response.product_price(id)
    if param == 'product':
        id = request.args.get('id')
        return response.product_price(id,False)
    else:
        return response.method_not_found()

@app.route('/productPrice',methods = ['PUT','GET','POST'])
def priceTypeList():
    if(request.method=='GET'):
        limit = request.args.get('limit')
        page = request.args.get('page')
        return response.product_price_list(limit,page)
    elif(request.method=='PUT'):
        return response.product_price_create(request.data)
    else:
        return response.method_not_found()

################################################################################################################################################

@app.route("/files/<file_name>")
def serve_file(file_name):
    """Set up a dynamic routes for directory items at /files/"""
    dir_path = Path("photo")
    return send_from_directory(dir_path, file_name)