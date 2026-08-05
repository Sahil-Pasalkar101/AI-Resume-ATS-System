import logging 
import httpx
import json
from datetime import datetime,timezone
from typing import List ,Dict, Optional

logger = logging.getLogger("ats_resume_scorer")

#from backend.core.config import 