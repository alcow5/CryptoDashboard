#!/usr/bin/env python3
"""
Setup script for CryptoDashboard
Helps users install dependencies and validate their environment.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python 3.7+ is required. Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_node_version():
    """Check if Node.js is installed."""
    print("📦 Checking Node.js...")
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"✅ Node.js {version} is installed")
        return True
    except FileNotFoundError:
        print("❌ Node.js is not installed. Please install Node.js 14+ from https://nodejs.org/")
        return False

def install_python_dependencies():
    """Install Python dependencies."""
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python dependencies"
    )

def install_node_dependencies():
    """Install Node.js dependencies."""
    if not Path("package.json").exists():
        print("❌ package.json not found")
        return False
    
    return run_command(
        "npm install",
        "Installing Node.js dependencies"
    )

def check_environment_variables():
    """Check if required environment variables are set."""
    print("🔑 Checking environment variables...")
    
    api_key = os.environ.get('binance_api')
    api_secret = os.environ.get('binance_secret')
    
    if not api_key:
        print("⚠️  binance_api environment variable is not set")
    else:
        print("✅ binance_api environment variable is set")
    
    if not api_secret:
        print("⚠️  binance_secret environment variable is not set")
    else:
        print("✅ binance_secret environment variable is set")
    
    if not api_key or not api_secret:
        print("\n📝 To set environment variables:")
        print("   Linux/Mac: export binance_api='your_api_key' && export binance_secret='your_api_secret'")
        print("   Windows: set binance_api=your_api_key && set binance_secret=your_api_secret")
        print("   Or create a .env file with these variables")
        return False
    
    return True

def create_env_template():
    """Create a .env template file."""
    env_template = """# Binance API Configuration
# Get your API keys from: https://www.binance.us/en/usercenter/settings/api-management
binance_api=your_binance_api_key_here
binance_secret=your_binance_secret_key_here

# Dashboard Configuration (optional)
DASH_PORT=8050
DASH_HOST=0.0.0.0
DASH_DEBUG=true
"""
    
    if not Path(".env").exists():
        with open(".env", "w") as f:
            f.write(env_template)
        print("📄 Created .env template file")
        print("   Please edit .env with your actual API credentials")
    else:
        print("📄 .env file already exists")

def main():
    """Main setup function."""
    print("🚀 CryptoDashboard Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check Node.js
    if not check_node_version():
        sys.exit(1)
    
    # Install Python dependencies
    if not install_python_dependencies():
        print("❌ Failed to install Python dependencies")
        sys.exit(1)
    
    # Install Node.js dependencies
    if not install_node_dependencies():
        print("❌ Failed to install Node.js dependencies")
        sys.exit(1)
    
    # Create .env template
    create_env_template()
    
    # Check environment variables
    check_environment_variables()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your Binance API credentials")
    print("2. Run the Python dashboard: python binanceDashboard.py")
    print("3. Run the Next.js frontend: npm run dev")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 