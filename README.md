# CryptoDashboard

A real-time cryptocurrency portfolio tracking dashboard built with Python (Dash) and Next.js, designed to monitor Binance account balances and crypto holdings.

## 🚀 Features

- **Real-time Portfolio Tracking**: Live monitoring of cryptocurrency balances from Binance
- **Multi-currency Support**: Track portfolio values in USDT and BTC
- **Interactive Dashboards**: Built with Dash (Python) and Next.js (React)
- **WebSocket Integration**: Real-time price updates via Binance WebSocket API
- **Historical Data**: CSV export of historical price data
- **Responsive Design**: Modern UI with Tailwind CSS

## 📁 Project Structure

```
CryptoDashboard/
├── Python Backend/
│   ├── binanceDashboard.py      # Main Dash application with real-time dashboard
│   ├── binanceAPI.py           # Binance API integration and historical data
│   ├── binanceBal.py           # Balance calculation utilities
│   ├── binanceWEBSOCKETS.py    # WebSocket connection for real-time data
│   └── eth_candle.csv          # Historical ETH price data
│
├── Next.js Frontend/
│   ├── pages/
│   │   ├── _app.js             # Next.js app configuration
│   │   └── index.js            # Main dashboard page
│   ├── components/
│   │   └── layout.js           # Layout component with Bootstrap
│   ├── styles/
│   │   └── index.css           # Tailwind CSS configuration
│   ├── public/                 # Static assets (crypto icons)
│   └── package.json            # Node.js dependencies
│
├── Legacy Files/
│   ├── frontendtesting.html    # Static HTML dashboard
│   ├── fronendtesting.css      # Legacy CSS styles
│   ├── fronendtesting.js       # Legacy JavaScript
│   ├── testingdash.js          # Minified dashboard code
│   └── scratch.js              # Development scratch file
│
└── Configuration/
    ├── tailwind.config.js      # Tailwind CSS configuration
    ├── postcss.config.js       # PostCSS configuration
    └── .gitignore              # Git ignore rules
```

## 🛠️ Technology Stack

### Backend (Python)
- **Dash**: Interactive web application framework
- **Plotly**: Data visualization library
- **python-binance**: Binance API client
- **pandas**: Data manipulation and analysis
- **dash-bootstrap-components**: Bootstrap styling for Dash

### Frontend (Next.js)
- **Next.js**: React framework
- **React**: UI library
- **Tailwind CSS**: Utility-first CSS framework
- **Recharts**: Chart library for React
- **node-binance-api**: Binance API for Node.js

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.7+
- Node.js 14+
- Binance account with API keys

### Environment Variables
Set up the following environment variables:
```bash
export binance_api="your_binance_api_key"
export binance_secret="your_binance_secret_key"
```

### Backend Setup (Python)
1. Install Python dependencies:
```bash
pip install dash dash-core-components dash-html-components dash-bootstrap-components plotly python-binance pandas
```

2. Run the main dashboard:
```bash
python binanceDashboard.py
```

3. Run individual components:
```bash
# Get historical data
python binanceAPI.py

# Calculate balances
python binanceBal.py

# Test WebSocket connection
python binanceWEBSOCKETS.py
```

### Frontend Setup (Next.js)
1. Install Node.js dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
npm start
```

## 🔧 Configuration

### Tailwind CSS
The project uses Tailwind CSS for styling. Configuration is in `tailwind.config.js`.

### Binance API
- Uses Binance.US API endpoint
- Requires API key and secret for authenticated requests
- Supports both REST API and WebSocket connections

## 📊 Dashboard Features

### Real-time Metrics
- Portfolio value in USDT and BTC
- Individual token prices (e.g., BNB/USDT)
- Portfolio distribution pie chart
- Live price updates via WebSocket

### Data Visualization
- Interactive charts with Plotly
- Real-time data updates
- Responsive design for mobile and desktop

### Historical Data
- CSV export of historical price data
- Configurable time intervals
- Data analysis capabilities

## 🚨 Issues Identified

### 1. Security Issues
- **API Keys in Environment Variables**: While using environment variables is good, ensure they're not committed to version control
- **Missing API Key Validation**: No validation for missing or invalid API keys

### 2. Code Quality Issues
- **Inconsistent Naming**: Files like `fronendtesting.js` have typos
- **Large Minified Files**: `testingdash.js` (91KB) should be in `.gitignore`
- **Missing Error Handling**: Limited error handling in API calls
- **Hardcoded Values**: Some hardcoded values that should be configurable

### 3. Architecture Issues
- **Mixed Technologies**: Both Python (Dash) and Next.js implementations exist
- **Duplicate Functionality**: Multiple dashboard implementations
- **Missing Documentation**: Limited inline code documentation

### 4. Dependencies Issues
- **Outdated Dependencies**: Some packages may be outdated
- **Missing Requirements File**: No `requirements.txt` for Python dependencies

## 🔧 Recommended Fixes

### 1. Security Improvements
```python
# Add API key validation
if not api_key or not api_secret:
    raise ValueError("Binance API credentials are required")
```

### 2. Code Organization
- Create a `requirements.txt` file for Python dependencies
- Add proper error handling and logging
- Implement configuration management
- Clean up legacy files

### 3. Documentation
- Add inline code comments
- Create API documentation
- Add deployment instructions

### 4. Testing
- Add unit tests for core functionality
- Implement integration tests for API calls
- Add error scenario testing

## 🚀 Deployment

### Local Development
1. Set up environment variables
2. Run Python backend: `python binanceDashboard.py`
3. Run Next.js frontend: `npm run dev`

### Production Deployment
1. Build the Next.js application: `npm run build`
2. Deploy Python backend to a cloud service (Heroku, AWS, etc.)
3. Configure environment variables on the deployment platform
4. Set up proper SSL certificates for secure API communication

## 📝 License

This project was created as a college assignment. Please ensure compliance with Binance API terms of service and applicable regulations.

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome. Please ensure any changes maintain the existing functionality and add proper error handling.

## ⚠️ Disclaimer

This application interacts with cryptocurrency exchanges and handles real financial data. Use at your own risk and ensure compliance with local regulations regarding cryptocurrency trading and data handling. 