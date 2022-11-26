FROM python:3-buster
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE=1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED=1
# tz_dataのインストール時の操作をスキップするために設定
ENV DEBIAN_FRONTEND=noninteractive

# Poetryの仮想環境を無効化する設定
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Poetryのパスを通す
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /usr/src/app
RUN pip3 install -U pip
RUN wget --quiet -O - https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock $WORK_DIR
RUN poetry install --no-interaction
COPY development /usr/src/app
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "entrypoint.sh" ]
# DEBUG=falseの場合の実行コマンド
CMD daphne -b 0.0.0.0 -p 8000 development.asgi:application
