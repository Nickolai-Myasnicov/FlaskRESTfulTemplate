from api import Resource, reqparse, db
from api.models.user import UserModel
from api.schemas.user import user_schema, users_schema


class UserResource(Resource):
    def get(self, id):
        user = UserModel.query.get(id)
        if user:
            return user_schema.dump(user), 200
        return {"Error": f"User with id={id} not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True)
        parser.add_argument("password", required=True)
        user_data = parser.parse_args()
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201