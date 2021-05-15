##
##from flask import Flask
##from flask_restful import Resource, Api, reqparse
##import pandas as pd
##import ast
##app = Flask(__name__)
##api = Api(app)
##data={1:'pratik',2:'hii'}
##
##class Users(Resource):
##    def get(self):
##        return {'data': data}, 200  # return data and 200 OK
##
##    def post(self):
##        parser = reqparse.RequestParser()  # initialize
##        parser.add_argument('Id', required=True)  # add args
##        args = parser.parse_args()  # parse arguments to dictionary
##
##        if args['Id'] in list(data['userId']):
##            return {
##                'message': f"'{args['userId']}' already exists."
##            }, 409
##        else:
##            # create new dataframe containing new values
##            new_data = pd.DataFrame({'Id': [args['Id']],})
##            # add the newly provided values
##            data = data.append(new_data, ignore_index=True)
##            return {'data': data.to_dict()}, 200  # return data with 200 OK
##    
##api.add_resource(Users, '/users')  # '/users' is our entry point for Users
###api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations
##
##if __name__ == '__main__':
##    app.run()  # run our Flask app


from flask import Flask, render_template
app = Flask(__name__,template_folder='../../')

@app.route('/')
def home():
   return render_template('p.html')
if __name__ == '__main__':
   app.run()
