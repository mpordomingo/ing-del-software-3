Minimun viable product for Software Engineering III course at UCA. 2020.

Due to some issues install psycopg2, trying this in the env might help:
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
