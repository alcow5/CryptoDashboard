"""
Utility functions for CryptoDashboard
Provides error handling, logging, and common utilities.
"""

import logging
import time
from typing import Any, Dict, List, Optional
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def handle_api_error(func):
    """
    Decorator to handle API errors gracefully.
    
    Args:
        func: Function to wrap with error handling
        
    Returns:
        Wrapped function with error handling
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"API Error in {func.__name__}: {str(e)}")
            return None
    return wrapper

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry functions on failure.
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        Decorated function with retry logic
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        logger.error(f"Function {func.__name__} failed after {max_retries} attempts: {str(e)}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {str(e)}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def validate_balance_data(balance_data: Dict[str, Any]) -> bool:
    """
    Validate balance data from Binance API.
    
    Args:
        balance_data: Balance data from Binance API
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    if not isinstance(balance_data, dict):
        logger.error("Balance data is not a dictionary")
        return False
    
    if 'balances' not in balance_data:
        logger.error("Balance data missing 'balances' key")
        return False
    
    if not isinstance(balance_data['balances'], list):
        logger.error("Balances is not a list")
        return False
    
    return True

def filter_non_zero_balances(balances: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filter out zero balances from balance list.
    
    Args:
        balances: List of balance dictionaries
        
    Returns:
        List of non-zero balances
    """
    non_zero_balances = []
    for balance in balances:
        try:
            free_amount = float(balance.get('free', '0'))
            if free_amount > 0:
                non_zero_balances.append(balance)
        except (ValueError, TypeError):
            logger.warning(f"Invalid balance data: {balance}")
            continue
    
    return non_zero_balances

def format_currency(amount: float, currency: str = 'USD', decimals: int = 2) -> str:
    """
    Format currency amount with proper formatting.
    
    Args:
        amount: Amount to format
        currency: Currency code
        decimals: Number of decimal places
        
    Returns:
        Formatted currency string
    """
    try:
        if currency == 'USD':
            return f"${amount:,.{decimals}f}"
        elif currency == 'BTC':
            return f"{amount:.8f} BTC"
        else:
            return f"{amount:.{decimals}f} {currency}"
    except (ValueError, TypeError):
        return f"{amount} {currency}"

def calculate_portfolio_value(balances: List[Dict[str, Any]], prices: Dict[str, float]) -> float:
    """
    Calculate total portfolio value in USD.
    
    Args:
        balances: List of balance dictionaries
        prices: Dictionary of asset prices in USD
        
    Returns:
        Total portfolio value in USD
    """
    total_value = 0.0
    
    for balance in balances:
        asset = balance.get('asset', '')
        free_amount = float(balance.get('free', '0'))
        
        if asset == 'USDT':
            total_value += free_amount
        elif asset in prices:
            total_value += free_amount * prices[asset]
        else:
            logger.warning(f"No price data for asset: {asset}")
    
    return total_value

def safe_float_conversion(value: Any, default: float = 0.0) -> float:
    """
    Safely convert value to float with error handling.
    
    Args:
        value: Value to convert
        default: Default value if conversion fails
        
    Returns:
        Converted float value
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        logger.warning(f"Could not convert {value} to float, using default {default}")
        return default

def log_api_request(endpoint: str, params: Optional[Dict] = None):
    """
    Log API request for debugging.
    
    Args:
        endpoint: API endpoint being called
        params: Request parameters (optional)
    """
    logger.info(f"API Request: {endpoint}")
    if params:
        logger.debug(f"Parameters: {params}")

def log_api_response(endpoint: str, status: str, data_size: Optional[int] = None):
    """
    Log API response for debugging.
    
    Args:
        endpoint: API endpoint that was called
        status: Response status
        data_size: Size of response data (optional)
    """
    logger.info(f"API Response: {endpoint} - {status}")
    if data_size:
        logger.debug(f"Response size: {data_size} bytes")

class DataValidator:
    """Class for validating various data types."""
    
    @staticmethod
    def is_valid_symbol(symbol: str) -> bool:
        """
        Validate trading symbol format.
        
        Args:
            symbol: Trading symbol to validate
            
        Returns:
            bool: True if symbol is valid
        """
        if not isinstance(symbol, str):
            return False
        
        # Basic symbol validation (can be enhanced)
        if len(symbol) < 3 or len(symbol) > 20:
            return False
        
        # Check for common patterns
        if not symbol.isalnum():
            return False
        
        return True
    
    @staticmethod
    def is_valid_timeframe(timeframe: str) -> bool:
        """
        Validate timeframe format.
        
        Args:
            timeframe: Timeframe to validate
            
        Returns:
            bool: True if timeframe is valid
        """
        valid_timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
        return timeframe in valid_timeframes
    
    @staticmethod
    def is_valid_limit(limit: int) -> bool:
        """
        Validate limit parameter.
        
        Args:
            limit: Limit value to validate
            
        Returns:
            bool: True if limit is valid
        """
        return isinstance(limit, int) and 1 <= limit <= 1000 