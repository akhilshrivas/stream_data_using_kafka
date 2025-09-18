**stream_data_using_kafka**

--

A project to stream and process data using Kafka. Producer sends data, consumer receives, with dashboards/logging to monitor flow.

--

**Table of Contents**

1.Overview
2.Features
3.Repository Structure
4.Prerequisites
5.Setup Instructions
6.How to Run
7.Usage
8.Troubleshooting / Common Issues
9.Future Improvements
10.License

--

**Overview**
This project demonstrates how to stream data using Apache Kafka. It includes:
A producer component to send data
A consumer component to receive and possibly process data
Dashboard-style monitoring via notebooks
IPython / Jupyter notebooks for exploring results

--

**Features**

Real-time data streaming with Kafka

Data visualization / exploration with Jupyter notebooks

Modular producer / consumer codes

Sample datasets included for testing

--

**Repository Structure**
File / Folder	Purpose
producer.py	sends data into Kafka topic(s)
consumer.py	reads data from topic(s) & handles processing
dashboard_consumer.py	consumer + dashboard/reporting view
cons.ipynb	notebook exploring data from consumer
prod.ipynb	notebook exploring data from producer or full pipeline
IT Salary Survey EU 2020.csv	sample dataset used by producer (if applicable)

--

**Prerequisites**
Python 3.x installed
Apache Kafka setup (local or remote)
pip for installing dependencies
Jupyter Notebook (for notebooks)

--

**Setup Instructions**
Clone the repo
git clone https://github.com/akhilshrivas/stream_data_using_kafka.git
cd stream_data_using_kafka

Create and activate virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate     # on Linux/macOS
venv\Scripts\activate        # on Windows

Install dependencies

pip install -r requirements.txt

If you don’t yet have a requirements.txt, create one listing needed libraries (e.g. kafka-python, pandas, etc.)

Ensure Kafka is running

Start Zookeeper (if needed)

Start Kafka broker(s)

Create topic(s) if required

--

**How to Run**
Run producer to send data:
python producer.py
Run consumer to receive data:
python consumer.py

For dashboards / notebooks:

jupyter notebook

Then open cons.ipynb or prod.ipynb as needed to explore or visualize.

--

**Usage**
You can adapt producer to send different datasets by modifying the CSV or source.
Use consumer or dashboard script to transform / filter / summarize streamed data.
The notebooks help in exploratory data analysis and understanding latency, throughput, etc.

--

**Troubleshooting / Common Issues**
Problem	Possible Solution
Kafka not reachable / connection refused	Check broker address, ports; ensure Kafka service is running
Topic doesn’t exist	Create topic manually or via script before producing or consuming
Version / dependency mismatch	Use virtual env; upgrade / reinstall dependencies
Line endings warnings (LF vs CRLF)	Configure Git: git config core.autocrlf true

--

**Future Improvements**
Add Docker setup for Kafka + services for easier environment setup
Add more robust error handling in producer/consumer
Add schema validation (e.g., Avro, JSON Schema)
Add automated tests
Add monitoring or alerting (e.g., using Prometheus + Grafana)
--
**License**
This project is under the MIT License — see LICENSE file for details.
