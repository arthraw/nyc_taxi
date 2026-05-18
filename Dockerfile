FROM astrocrpublic.azurecr.io/runtime:3.2-4
USER astro
COPY requirements.txt .
COPY ./ingestion .
RUN pip install --no-cache-dir -r requirements.txt