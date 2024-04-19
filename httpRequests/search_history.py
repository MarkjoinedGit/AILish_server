from flask import request,jsonify
from utils.config import app
from services import search_history_service

searchHistoryService = search_history_service.SearchHistoryService()

