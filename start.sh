#!/bin/sh
echo ****** Starting Server ********
exec gunicorn -b 0.0.0.0:5000 ml_server:app
exec streamlit run webApp.py