import json
from datetime import datetime

class AuditTrail:
    def __init__(self, audit_log_file='audit_log.json'):
        self.audit_log_file = audit_log_file

    def log_action(self, action, user_id, details):
        with open(self.audit_log_file, 'a') as file:
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'action': action,
                'user_id': user_id,
                'details': details
            }
            file.write(json.dumps(log_entry) + '\\n')
