"""
Configuration file for CryptoDashboard
Centralizes settings and provides validation for required environment variables.
"""

import os
from typing import Optional

class Config:
    """Configuration class for the CryptoDashboard application."""
    
    # Binance API Configuration
    BINANCE_API_KEY: Optional[str] = os.environ.get('binance_api')
    BINANCE_API_SECRET: Optional[str] = os.environ.get('binance_secret')
    BINANCE_API_URL: str = 'https://api.binance.us/api'
    
    # Dashboard Configuration
    DASH_REFRESH_INTERVAL: int = 1000  # milliseconds
    DASH_PORT: int = 8050
    DASH_HOST: str = '0.0.0.0'
    DASH_DEBUG: bool = True
    
    # WebSocket Configuration
    WEBSOCKET_TIMEOUT: int = 5  # seconds
    
    # Data Configuration
    HISTORICAL_DATA_LIMIT: int = 1000
    DEFAULT_TIMEFRAME: str = '1d'
    
    @classmethod
    def validate_api_keys(cls) -> bool:
        """
        Validate that required API keys are present.
        
        Returns:
            bool: True if both API key and secret are present, False otherwise
        """
        if not cls.BINANCE_API_KEY or not cls.BINANCE_API_SECRET:
            return False
        return True
    
    @classmethod
    def get_api_credentials(cls) -> tuple:
        """
        Get API credentials with validation.
        
        Returns:
            tuple: (api_key, api_secret)
            
        Raises:
            ValueError: If API credentials are missing
        """
        if not cls.validate_api_keys():
            raise ValueError(
                "Binance API credentials are required. "
                "Please set the following environment variables:\n"
                "  - binance_api: Your Binance API key\n"
                "  - binance_secret: Your Binance API secret"
            )
        return cls.BINANCE_API_KEY, cls.BINANCE_API_SECRET
    
    @classmethod
    def get_binance_client_config(cls) -> dict:
        """
        Get configuration for Binance client.
        
        Returns:
            dict: Configuration dictionary for Binance client
        """
        return {
            'api_key': cls.BINANCE_API_KEY,
            'api_secret': cls.BINANCE_API_SECRET,
            'api_url': cls.BINANCE_API_URL
        }

# Convenience functions
def get_api_key() -> str:
    """Get the Binance API key."""
    return Config.BINANCE_API_KEY

def get_api_secret() -> str:
    """Get the Binance API secret."""
    return Config.BINANCE_API_SECRET

def get_api_url() -> str:
    """Get the Binance API URL."""
    return Config.BINANCE_API_URL

def validate_credentials() -> bool:
    """Validate API credentials are present."""
    return Config.validate_api_keys() 