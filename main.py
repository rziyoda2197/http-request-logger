import datetime
import jwt

class SessionManager:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_token(self, user_id, expiry_minutes):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiry_minutes)
        }
        return jwt.encode(payload, self.secret_key, algorithm='HS256')

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

# Misol
session_manager = SessionManager('sekret_kluch')

user_id = 1
expiry_minutes = 30

token = session_manager.generate_token(user_id, expiry_minutes)
print(token)

verified_user_id = session_manager.verify_token(token)
print(verified_user_id)

# Tokenni keyinroq so'ralganida
verified_user_id = session_manager.verify_token(token)
print(verified_user_id)
```

Kodda quyidagilar mavjud:

- `SessionManager` klassi yaratildi, u `secret_key` ni saqlaydi.
- `generate_token` metodida token yaratiladi, u `user_id` va `expiry_minutes` ni o'z ichiga oladi.
- `verify_token` metodida tokenni tekshiradi, agar token muddati tugagan bo'lsa, `None` qaytaradi.
- Misolni ko'rsatib, `SessionManager` klassi va uning metodlari ishlatiladi.
