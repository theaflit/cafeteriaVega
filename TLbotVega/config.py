from dataclasses import dataclass

@dataclass
class Config:
    token: str = 'YOUR_TOKEN'
    pay_token: str = ''
    admin_id: int = 00000000