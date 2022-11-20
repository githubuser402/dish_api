from flask import Blueprint, send_from_directory
from config.config import Config

document_routes = Blueprint("document_routes", __name__)


@document_routes.route("/<filename>", methods=["GET"])
def get_document(filename):
    return send_from_directory(Config.MEDIAFILES_FOLDER, filename)