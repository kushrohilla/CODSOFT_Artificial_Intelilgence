mkdir -p ~/.streamlit/


echo "\
[server]\n\
port = $port\n\n
enableCORS = false\n\
headless = true\n\
\n\
"> ~/.streamlit/config.toml