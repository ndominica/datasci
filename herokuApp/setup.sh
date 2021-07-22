mkdir -p ~/.streamlit/

echo"\
[server]\n\
headless = truen\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml