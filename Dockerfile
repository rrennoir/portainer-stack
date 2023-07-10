FROM python:3-slim AS builder
ADD . /build
WORKDIR /build
RUN pip install --target=/app requests

FROM gcr.io/distroless/python3-debian11
COPY --from=builder /build /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/src/main.py"]
