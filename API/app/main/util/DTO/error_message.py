from flask_restplus import fields

from main.util.api import api


error_message = api.model("Error Message", {
    "message": fields.String(description="Error Message, additional info about error")
})
