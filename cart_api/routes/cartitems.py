import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem
from cart_api.database import DatabaseProducts



# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    # def on_get(self, req, resp, cartitem_id):
    #     cartitem = DatabaseProducts.get(id=cartitem_id)
    #     resp.status = falcon.HTTP_200
    #     resp.media = model_to_dict(cartitem)
    def on_get(self, req, resp, cartitem_id):
        cartitem = DatabaseProducts.get(id=cartitem_id)
        resp.media = model_to_dict(cartitem)
        print(req.media)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp, cartitem_id):
        cartitem = DatabaseProducts.post(id=cartitem_id)
        obj = req.get_media()
        cartitem_id.save()
        resp.media = model_to_dict(cartitem_id)
        resp.status = falcon.HTTP_201
        print(resp.media)


class CartItem:
    def on_get(self, req, resp, cartitem_id):
        cartitem = DatabaseProducts.get(id=cartitem_id)
        resp.status = falcon.HTTP_200
        resp.media = model_to_dict(cartitem)

    def on_delete(self, req, resp, cartitem_id):
        DatabaseProducts.delete_by_id(cartitem_id)
        resp.status = falcon.HTTP_204


