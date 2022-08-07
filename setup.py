from distutils.core import setup

setup(
    name="broker_api",
    version="0.22",
    description="Interface for submitting and managing purchases across multiple crypto brokers",
    author="Chris Fernando",
    author_email="chris.t.fernando@gmail.com",
    url="https://github.com/chris-t-fernando/broker-api",
    packages=["broker_api"],
    install_requires=[
        "alpaca_trade_api",
        "pandas",
        "yfinance",
        "pyswyft",
        "boto3",
        "bta-lib",
        "yfinance",
    ],
)
